# Dropbox Tools

## Install

1. install with pip
```bash
pip install "git+https://github.com/lithiumice/Dropbox-tools"
```

or install from local clone
```bash
pip install -e .
```

2. install with poetry
```bash
poetry add "git+https://github.com/lithiumice/Dropbox-tools"
```

or install from local clone

```bash
# poetry init
poetry install
```

## How to use / Usage

```bash
# set dropbox api token to environment
# add this to your ~/.bashrc or run on current terminal
export DBX_TOKEN=xxxx

# python dbx.py -i /path/to/local/file
dbx up -l /path/to/local/file [-r /remote/folder]
```

## License

WTFPL. Check [LICENSE](LICENSE)

Reference
- https://github.com/shadiakiki1986/dbxcli-extras

## Issues
- pkg_resources.extern.packaging.requirements.InvalidRequirement: .* suffix can only be used with `==` or `!=` operators  
refer to https://github.com/pypa/pipx/issues/998
    - pip install pip==23.2.1