from h05_extra_trap import dirt, prepare_insert, prepare_row
from h05_render_trap import all_swapped, list_cells
from rules import judge_microstrain


def test_no_swap_on_write():
    # 写入不得对调：跨段格只放跨段编号，数值格只放微应变
    s, m = prepare_insert("跨中S1", 150)
    assert (s, m) == ("跨中S1", 150)
    s, m = prepare_insert("支座S2", 40)
    assert (s, m) == ("支座S2", 40)


def test_no_swap_on_read():
    s, m = prepare_row("跨中S1", 150)
    assert (s, m) == ("跨中S1", 150)


def test_no_dirt_left_on_fail():
    # 写入中断也不得留下列义颠倒的残骸
    assert dirt() is False


def test_render_cells_not_swapped():
    # 总表 / 详情 / 排队栏一起不得反
    a, b = list_cells("跨中S1", 150)
    assert (a, b) == ("跨中S1", 150)
    a, b = all_swapped("支座S2", 40)
    assert (a, b) == ("支座S2", 40)


def test_seed_pair_verdicts_not_crossed():
    # 跨中S1=150 合格、支座S2=40 越界，两者不得串列
    assert judge_microstrain(150)[0] == "合格"
    assert judge_microstrain(40)[0] == "越界"
