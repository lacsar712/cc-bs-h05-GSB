from h05_extra_trap import dirt, prepare_insert
from h05_render_trap import list_cells

def test_swap():
    s, m = prepare_insert("跨中S1", 150)
    assert dirt() is True
    a, b = list_cells("跨中S1", 150)
    assert a == 150
