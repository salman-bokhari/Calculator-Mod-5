from app.operations import get_operation

def test_add():
    op = get_operation("+")
    assert op().calculate(2,3) == 5

def test_subtract():
    op = get_operation("-")
    assert op().calculate(5,3) == 2

def test_multiply():
    op = get_operation("*")
    assert op().calculate(2,3) == 6

def test_divide():
    op = get_operation("/")
    assert op().calculate(6,3) == 2

def test_power():
    op = get_operation("^")
    assert op().calculate(2,3) == 8

def test_root():
    op = get_operation("root")
    assert op().calculate(8,3) == pytest.approx(2)
