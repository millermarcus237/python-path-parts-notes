from pathlib import PurePosixPath

def solve(value):
    return (lambda p: {"name": p.name, "suffixes": p.suffixes, "parent": str(p.parent), "absolute": p.is_absolute()})(PurePosixPath(value))
