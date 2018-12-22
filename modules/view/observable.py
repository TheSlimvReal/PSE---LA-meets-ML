from typing import List

from modules.view.subscriber import Subscriber


##  Class for creating updating strings
#
#   Can be used if you want to create an string in the view, that will be updated with new values
class Observable:

    subscribers: List[Subscriber] = []

    ##  Method to trigger an update on all subscribers
    #
    #   @param update the new value
    def next(self, update: str) -> None:
        for subscriber in self.subscribers:
            subscriber.update(update)

    ##  A subscriber can be added with this function
    #
    #   @param subscriber the subscriber that wants to receive status updates
    def add_subscriber(self, subscriber: Subscriber) -> None:
        self.subscribers.append(subscriber)

    ##  A subscriber can be removed with this function
    #
    #   @param subscriber the subscriber who wants to be removed from receiving status updates
    def remove_subscriber(self, subscriber: Subscriber) -> None:
        self.subscribers.remove(subscriber)
