from modular_steering.interface import ModuleInterface

class CameraModule:
    def __init__(self):
        super().__init__()
        print("cameramodule initialised")


    """Extract text from a PDF."""
    def onmsgrecv((self, message, payload)):
        pass

    def onstop(self):
        print("stop cameramodule")
        pass

    def onstart(self):
        print("start cameramodule")
        pass