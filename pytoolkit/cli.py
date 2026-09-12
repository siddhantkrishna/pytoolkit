import click
from tools.organizer import organize_folder
from tools.renamer import rename_files
from tools.duplicate_finder import find_duplicates, delete_duplicates
from tools.pdf_merger import merge_pdfs, split_pdf

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

@main.command()
@click.argument('folder')
@click.option('--delete', is_flag=True, help="Delete duplicate files, keeping first copy.")
def duplicates(folder, delete):
    """Find duplicate files in FOLDER."""
    dupes = find_duplicates(folder)
    if not dupes:
        print("No duplicates found.")
        return
    for file_hash, paths in dupes.items():
        print(f"Duplicate group: {paths}")
    if delete:
        delete_duplicates(dupes)

@main.command()
@click.argument('files', nargs=-1, required=True)
@click.option('--output', default="merged.pdf", help="Output file path.")
def merge(files, output):
    """Merge multiple PDF FILES into one."""
    merge_pdfs(list(files), output)

if __name__ == "__main__":
    main()
