from modular_steering.interface import ModuleInterface

class TemperatureModule(ModuleInterface):
    """Extract text from a PDF."""
    def onmsgrecv(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def onstop(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass
    
    def onstart(self):
        print("start temperaturemodule")

