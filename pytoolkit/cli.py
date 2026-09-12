import click
from tools.organizer import organize_folder

@click.group()
def main():
    """PyToolkit: A collection of automation tools."""
    pass

@main.command()
@click.argument('folder')
def organize(folder):
    """Organize files in FOLDER by extension."""
    organize_folder(folder)

if __name__ == "__main__":
    main()
