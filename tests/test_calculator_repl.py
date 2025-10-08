from app.calculator_repl import main


def test_calculator_repl_non_interactive():
    commands = [
        ("3", "+", "5"),
        ("10", "-", "4"),
        ("2", "*", "3"),
        ("8", "/", "2"),
        ("a", "+", "3"),       # invalid number
        ("5", "x", "2"),       # invalid operation
        ("5", "/", "0"),       # divide by zero
    ]
    results = main(interactive=False, commands=commands)

    assert results[0] == 8.0
    assert results[1] == 6.0
    assert results[2] == 6.0
    assert results[3] == 4.0
    assert "Invalid number" in results[4]
    assert "Invalid operation" in results[5]
    assert "division by zero" in results[6]
