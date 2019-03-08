

##  interface class than can be registered to an observable
from modules.exception.exceptions import NotImplementedException


class Subscriber:

    ##  Will be triggered when new values arrive
    #
    #   @param value the new value that was passed to the observable
    def update(self, value: str) -> None:
        raise NotImplementedException("Method UPDATE not implemented in class SUBSCRIBER")

    ##  Will be called when the observable is done
    def finished(self) -> None:
        raise NotImplementedException("Method FINISHED not implemented in class SUBSCRIBER")
