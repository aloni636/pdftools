from pypdf import PdfWriter
from typing import List

def concat(src_paths:List[str], dst_path:str):
    merger = PdfWriter()
    for path in src_paths:
        merger.append(path)
    merger.write(dst_path)
    merger.close()
