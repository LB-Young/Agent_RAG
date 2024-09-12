import os


from agent_rag.the3rd_packages.document_split.extractor.extractor_factory import Extractor_Factory
from agent_rag.the3rd_packages.document_split.layout_analyzer.layout_factory import Layout_Factory

class ExtractorHandler:
    def __init__(self, file_path, ext):
        self.file_path = file_path
        self.extractor_processor = Extractor_Factory.get_extractor_processor(ext)
        self.layout_analyzer = Layout_Factory.get_layout_processor(ext)

    def do_extract(self):
        extractor_slices = self.extractor_processor.extract(self.file_path)
        layout_slices = self.layout_analyzer.analize(extractor_slices)
        return layout_slices