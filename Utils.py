from LinkedList import LinkedList


class Utils:
    def __init__(self, items):
        self.items = items
        self.linked_list = LinkedList()
        self.create_linked_list()

    def get_linked_list(self):
        return self.linked_list

    def create_linked_list(self):
        for item in self.items:
            self.linked_list.append(item)
