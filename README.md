# Dropbox Tools

Dropbox utilities(sync, upload, etc) based on offical Dropbox API

## TODO
- [ ] add progress bar when uploading. refer https://github.com/dropbox/dropbox-sdk-python/blob/c5ea3f8e900512222a234b9f353f0abcbf9f865a/dropbox/base.py#L3172

Bugs
- [ ] will fail to upload large file

Related:
- https://github.com/dropbox/dbxcli/
- https://rclone.org/


## Install

1. install with pip
```bash
pip uninstall dropbox-tools
pip install -U "git+https://github.com/lithiumice/Dropbox-tools"
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

Utillities from https://github.com/shadiakiki1986/dbxcli-extras.git
```bash
# syncronize a local directory with a remote directory in dropbox
dbxcli_extras sync [--verbosity={0,1,2}] [--start-from=<path>] <localdir> <dbxdir>

# recursive get
dbxcli_extras getr [--verbosity={0,1,2}] [--verify] <dbxdir> <localdir>
```

For examples, see [this jupyter notebook](https://gist.github.com/shadiakiki1986/7c478d451a4221d464d7bcfd5fc6a914)


## License

WTFPL. Check [LICENSE](LICENSE)

Reference
- https://github.com/shadiakiki1986/dbxcli-extras

