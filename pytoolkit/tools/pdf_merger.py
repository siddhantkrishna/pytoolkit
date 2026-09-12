from pypdf import PdfWriter
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
