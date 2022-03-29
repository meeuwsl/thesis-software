import abc 

class ModuleInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'onmsgrecv') and 
                callable(subclass.onmsgrecv) and 
                hasattr(subclass, 'onstop') and 
                callable(subclass.onstop) and 
                hasattr(subclass, 'onstart') and 
                callable(subclass.onstart) or 
                NotImplemented
        )
    
    @abc.abstractmethod
    def onmsgrecv(self):
        raise NotImplementedError

    @abc.abstractmethod
    def onstop(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def onstart(self):
        raise NotImplementedError








