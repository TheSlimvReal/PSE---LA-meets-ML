
##  Class for creating updating strings
#
#   Can be used if you want to create an string in the view, that will be updated with new values
from modules.view.subscriber import Subscriber


class Observable:

    ##  Method to trigger an update on all subscribers
    #
    #   @param update the new value
    def next(self, update: str) -> None:
        pass

    ##  A subscriber can be added with this function
    #
    #   @param subscriber the subscriber that wants to receive status updates
    def add_subscriber(self, subscriber: Subscriber) -> None:
        pass

    ##  A subscriber can be removed with this function
    #
    #   @param subscriber the subscriber who wants to be removed from receiving status updates
    def remove_subscriber(self, subscriber: Subscriber) -> None:
        pass
