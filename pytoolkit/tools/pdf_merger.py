from pypdf import PdfWriter, PdfReader
import os

def merge_pdfs(file_paths, output_path):
    writer = PdfWriter()
    for path in file_paths:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue
        writer.append(path)
    with open(output_path, 'wb') as f:
        writer.write(f)
    print(f"Merged {len^(file_paths^)} files into {output_path}")

def split_pdf(file_path, start_page, end_page, output_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    reader = PdfReader(file_path)
    writer = PdfWriter()
    for i in range(start_page - 1, min(end_page, len(reader.pages))):
        writer.add_page(reader.pages[i])
    with open(output_path, 'wb') as f:
        writer.write(f)
    print(f"Split pages {start_page}-{end_page} into {output_path}")
