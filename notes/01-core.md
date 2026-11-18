# Inspect a POSIX path without I/O: implementation

## What the example does

PurePosixPath manipulates path syntax without touching the filesystem. It does not resolve symlinks or establish that a path stays inside a trusted directory.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"/data/archive.tar.gz"
```

Expected result:

```json
{
  "name": "archive.tar.gz",
  "suffixes": [
    ".tar",
    ".gz"
  ],
  "parent": "/data",
  "absolute": true
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
