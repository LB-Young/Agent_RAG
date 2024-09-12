from agent_rag.the3rd_packages.document_split.layout_analyzer.types.docx_layout import DocxLayout
from agent_rag.the3rd_packages.document_split.layout_analyzer.types.pdf_layout import PDFLayout

class Layout_Factory:
    def get_layout_processor(ext):
        if ext == "docx":
            return DocxLayout()
        elif ext == "pdf":
            return PDFLayout()