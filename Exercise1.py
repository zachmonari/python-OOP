class Book:
    def borrow(self):
        return "Borrowing a general book."
class EBook(Book):
    def borrow(self):
        return "Downloading the eBook."

class AudioBook(Book):
    def borrow(self):
        return "Streaming the audiobook."
def process_borrow(item: Book):
    print(item.borrow())

process_borrow(EBook())
process_borrow(AudioBook())