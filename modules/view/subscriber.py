

##  Class than can be registered to an observable
class Subscriber:

    ##  will be triggered when new values arrive
    #
    #   @param value the new value that was passed to the observable
    def update(self, value: str) -> None:
        pass
