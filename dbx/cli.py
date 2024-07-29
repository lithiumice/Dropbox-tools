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
    
    upload(dbx, full_name=local_file, folder=remote_folder, subfolder="", name=Path(local_file).name)
    print(f"[INFO] Uploaded {local_file} to {remote_folder}")
    
    
cli.add_command(up)


if __name__ == "__main__":
    cli()