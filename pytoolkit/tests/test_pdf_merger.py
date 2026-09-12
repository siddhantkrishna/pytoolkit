import os
from pypdf import PdfWriter
from tools.pdf_merger import merge_pdfs

def create_dummy_pdf(path):
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    with open(path, 'wb') as f:
        writer.write(f)

def test_merge_pdfs_creates_output(tmp_path):
    pdf1 = tmp_path / "a.pdf"
    pdf2 = tmp_path / "b.pdf"
    create_dummy_pdf(str(pdf1))
    create_dummy_pdf(str(pdf2))
    output = tmp_path / "merged.pdf"
    merge_pdfs([str(pdf1), str(pdf2)], str(output))
    assert output.exists()
