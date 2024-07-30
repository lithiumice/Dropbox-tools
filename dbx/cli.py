import click
import dropbox
import os

from pathlib import Path

from .dbx import list_folder, download, upload


@click.group()
def cli():
    pass


def get_dbx_instance():
    if not "DBX_TOKEN" in os.environ:
        raise EnvironmentError(f"You should set `DBX_TOKEN` variable in shell before using this script.")

    token = os.environ["DBX_TOKEN"]
    dbx = dropbox.Dropbox(token)
    return dbx

@click.command()
@click.option('-l', '--local_file', type=click.Path(exists=True))
@click.option('-r', '--remote_folder', type=str, default="/")
def up(local_file, remote_folder="/"):
    """
    Args:
        local_file: full path to the file
        remote_folder: remote folder, default is "/", the root of dropbox account.
    """
    # get full path
    local_file = os.path.abspath(local_file)
    
    dbx = get_dbx_instance()
    
    upload(dbx, fullname=local_file, folder=remote_folder, subfolder="", name=Path(local_file).name)
    print(f"[INFO] Uploaded {local_file} to {remote_folder}")
    
    
cli.add_command(up)




from .sync import DbxcliSync
from .getr import DbxcliGetr


@click.command()
@click.argument('localdir', type=click.Path(exists=True))
@click.argument('dbxdir', type=str)
@click.option('--verbosity', default=0, help="Verbosity level: 0, 1, 2")
@click.option('--start-from', default="", help="Files are sorted before sync. Use this field to start from a particular file instead of from the beginning.")
def sync(localdir, dbxdir, verbosity, start_from):
    """
    sync local folder with remote dropbox folder
    Solves https://github.com/dropbox/dbxcli/issues/53
    """
    dcs = DbxcliSync(localdir, dbxdir, verbosity)
    dcs.sync_dir(start_from)


@click.command()
@click.argument('dbxdir', type=str)
@click.argument('localdir', type=click.Path(exists=True))
@click.option('--verify', is_flag=True, default=False, help="Verify downloads (download it several times)")
@click.option('--verbosity', default=0, help="Verbosity level: 0, 1, 2")
def getr(dbxdir, localdir, verify, verbosity):
    """
    Recursive get
    Solves https://github.com/dropbox/dbxcli/issues/60
    """
    dcg = DbxcliGetr(verify, verbosity)
    dcg.getr(dbxdir, localdir)



cli.add_command(sync)
cli.add_command(getr)


if __name__ == "__main__":
    cli()