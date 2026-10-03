"""列义守护：跨段格只放跨段文本，数值格只放有限数值。

两列绝不对调：提交内容在入库前先过这里的校验，任一列不合规即整体拒绝，
不产生任何半写入的残骸。纯标准库实现，方便无外部依赖下单测。
"""

import math

# 跨段编号至少含一个字母（含汉字），纯数字串视为“数值串列”，拒绝。
def _has_label_char(text: str) -> bool:
    return any(ch.isalpha() for ch in text)


def validate_reading(span_code, microstrain):
    """返回净化后的 (span_code: str, microstrain: float)，不合规抛 ValueError。"""
    if not isinstance(span_code, str):
        raise ValueError("跨段编号必须是文本")
    span = span_code.strip()
    if not span:
        raise ValueError("跨段编号不能为空")
    if not _has_label_char(span):
        raise ValueError("跨段格只许填写跨段编号，不能填写数值")

    # bool 是 int 的子类，先排除；只接受 JSON 数字（int/float），拒绝字符串。
    if isinstance(microstrain, bool):
        raise ValueError("微应变必须是数字")
    if isinstance(microstrain, int):
        ms = float(microstrain)
    elif isinstance(microstrain, float):
        ms = microstrain
    else:
        raise ValueError("微应变必须是数字")
    if not math.isfinite(ms):
        raise ValueError("微应变必须是有限数字")

    return span, ms
