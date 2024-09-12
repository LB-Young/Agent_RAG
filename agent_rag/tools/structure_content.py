from agent_rag.the3rd_packages.document_split.document_extractor import DocumentExtractor


def document_extract_tool(file_path):
    extractor = DocumentExtractor(file_path, False, "test", db_type="local")
    response_slices = extractor.do_extract()
    return response_slices
