

##  abstract class than can be registered to an observable
class Subscriber:

    ##  Will be triggered when new values arrive
    #
    #   @param value the new value that was passed to the observable
    def update(self, value: str) -> None:
        pass

    ##  Will be called when the observable is done
    def finished(self) -> None:
        pass
