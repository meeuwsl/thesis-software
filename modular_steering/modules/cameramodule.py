from modular_steering.interface import ModuleInterface

class CameraModule:
    """Extract text from a PDF."""
    def onmsgrecv(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def onstop(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

    def onstart(self):
        print("start cameramodule")
