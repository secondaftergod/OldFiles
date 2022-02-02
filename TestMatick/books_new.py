class Books:
    books_list = list()

    def __init__(self,book_name=None,book_author=None,book_price=None,book_sellers=None,knuga=None):

        self.book_name=book_name
        self.book_author=book_author
        self.book_price=book_price
        self.book_sellers=book_sellers
        self.knuga=knuga

    def __call__(self, *args, **kwargs):
        if self.book_name!=None:
            self.books_list.append(self)

a=Books('Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming')
