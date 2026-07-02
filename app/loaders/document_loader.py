from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:

    def load_pdf(self, file_path: str):
        """
        Load a PDF document and return its pages.
        """

        loader = PyPDFLoader(file_path)

        documents = loader.load()

        return documents