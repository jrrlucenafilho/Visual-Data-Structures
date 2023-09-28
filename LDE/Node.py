class Node:
    def __init__(self):
        self.content = 0
        self.previous = None
        self.next = None

    def get_content(self):
        return self.content

    def get_previous(self):
        return self.previous

    def get_next(self):
        return self.next

    def set_content(self, new_content):
        self.content = new_content

    def set_previous(self, new_previous):
        self.previous = new_previous

    def set_next(self, new_next):
        self.next = new_next