import click
from tools.organizer import organize_folder
from tools.renamer import rename_files

@click.group()
def main():
    """PyToolkit: A collection of automation tools."""
    pass

@main.command()
@click.argument('folder')
def organize(folder):
    """Organize files in FOLDER by extension."""
    organize_folder(folder)

@main.command()
@click.argument('folder')
@click.option('--prefix', default="", help="Prefix to add to filenames.")
@click.option('--suffix', default="", help="Suffix to add to filenames.")
@click.option('--ext', default=None, help="Only rename files with this extension.")
@click.option('--dry-run', is_flag=True, help="Preview changes without renaming.")
def rename(folder, prefix, suffix, ext, dry_run):
    """Bulk rename files in FOLDER."""
    rename_files(folder, prefix, suffix, ext, dry_run)

if __name__ == "__main__":
    main()
