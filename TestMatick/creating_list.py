from amazon import Amazon
class Creating_list(Amazon):
    def __init__(self,book_name=None,book_author=None,book_price=None,book_sellers=None,knuga=None):
        self.book_name=book_name
        self.book_author=book_author
        self.book_price=book_price
        self.book_sellers=book_sellers
        self.knuga=knuga
    def info(self):
        self.book_name = self.info_list[0][0]
        self.book_author = self.info_list[0][1]
        self.book_price = self.info_list[0][2]
        self.book_sellers = self.info_list[0][3]
        self.info_list.pop(0)
    def ccheck(self):
        if len(self.check_book)>0 and self.knuga==None:
            self.knuga=self.check_book

class Books_list:
    books = list()
    checking=list()
    def book_list(self,http,search_info,what_serch,urlik=None):
        a=Creating_list()
        a.selenium_amazon(http,search_info,what_serch,urlik)
        a.ccheck()
        try:
            self.checking.append(a.knuga[0])
        except TypeError:
            pass
        for i in range(len(a.info_list)):
            a.info()
            self.books.append(a)
            a=Creating_list()



