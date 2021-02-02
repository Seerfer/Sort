class Error(Exception):
    def __init__(self, messege):
        self.messege = messege

    def __str__(self):
        return self.messege
