import pycodestyle


def test_style():
    """
    Test PEP 8 style conventions

    E501 - Line too long (82 > 79 characters)
    W504 - Line break occurred after a binary operator
    """

    style = pycodestyle.StyleGuide(ignore=['E501', 'W504'])
    result = style.check_files([
        'tests/',
        'src/',
    ])
    assert not result.total_errors
