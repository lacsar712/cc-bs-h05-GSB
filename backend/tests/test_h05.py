import pathlib

import pytest

from columns import validate_reading
from rules import judge_microstrain

BACKEND = pathlib.Path(__file__).resolve().parents[1]
FRONTEND_APP = BACKEND.parent / "frontend" / "src" / "app.js"


# ---------- 列义：跨段格只放跨段，数值格只放数值 ----------

def test_normal_pair_kept_in_column_order():
    span, ms = validate_reading("跨中S1", 150)
    assert span == "跨中S1"
    assert ms == 150.0
    assert isinstance(ms, float)


def test_span_must_be_label_not_bare_number():
    # 跨段格收到纯数字（对调的典型残骸）必须拒绝
    for bad in ["150", " 40 ", "12.5", "-3", ""]:
        with pytest.raises(ValueError):
            validate_reading(bad, 150)


def test_microstrain_must_be_numeric_not_label():
    # 数值格收到跨段文本（对调的另一侧）必须拒绝
    for bad in ["跨中S1", "150abc", None, [150], {}]:
        with pytest.raises(ValueError):
            validate_reading("跨中S1", bad)


def test_rejects_non_finite_and_bool():
    for bad in [float("nan"), float("inf"), float("-inf"), True, False]:
        with pytest.raises(ValueError):
            validate_reading("跨中S1", bad)


# ---------- 种子数据：跨中150、支座40 不得串列 ----------

def test_seed_pairs_do_not_cross():
    text = (BACKEND / "db.py").read_text(encoding="utf-8")
    assert '("跨中S1", 150.0)' in text
    assert '("支座S2", 40.0)' in text
    assert judge_microstrain(150.0)[0] == "合格"
    assert judge_microstrain(40.0)[0] == "越界"


# ---------- 陷阱模块必须彻底移除 ----------

def test_swap_trap_modules_removed():
    for name in ("span_strain_swap.py", "h05_extra_trap.py", "h05_render_trap.py"):
        assert not (BACKEND / name).exists(), f"{name} 必须删除"
    app_src = (BACKEND / "api" / "app.py").read_text(encoding="utf-8")
    assert "prepare_insert" not in app_src
    assert "swap" not in app_src.lower()


# ---------- 总表/排队栏列序：跨段列在微应变列之前 ----------

def test_frontend_table_columns_not_swapped():
    src = FRONTEND_APP.read_text(encoding="utf-8")
    assert "h05-trap-cols" not in src
    span_pos = src.index('m("td", r.span_code)')
    ms_pos = src.index('m("td", r.microstrain)')
    assert span_pos < ms_pos


# ---------- 复核岗只读 ----------

def test_reviewer_remains_read_only():
    app_src = (BACKEND / "api" / "app.py").read_text(encoding="utf-8")
    # 唯一的写接口仍按 writer 角色拦截
    assert 'user["role"] != "writer"' in app_src
