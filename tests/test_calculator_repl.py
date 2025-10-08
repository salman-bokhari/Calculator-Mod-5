from app.calculator_repl import HELP_TEXT
def test_help_contains_commands():
    assert 'help' in HELP_TEXT
