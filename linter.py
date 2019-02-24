from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class __class__(Linter):
    cmd = ('sabre')

    regex = (
        r'\s*(?P<line>\d+):(?P<col>\d+)\s*'
        r'((?P<error>error)|(?P<warning>warning))\s*'
        r'(?P<message>.+)'
    )
    tempfile_suffix = "~"
    multiline = False
    defaults = {
        'selector': 'source.solidity'
    }
