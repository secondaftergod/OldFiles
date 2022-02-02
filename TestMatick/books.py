from creating_list import Books_list
class Books(Books_list):
    def __init__(self):
        self.books=self.books
        self.checking=self.checking
    def __str__(self):
        for i in self.books:
            if i.book_name==self.checking[0]:
                print('This link book in ours object list')




books=Books()
check='https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/ref=sr_1_5?crid=3V2N7ELZXA99K&keywords=Python&qid=1643196807&s=books&sprefix=python%2Cstripbooks-intl-ship%2C143&sr=1-5'
books.book_list('https://www.amazon.com/','//*[@id="searchDropdownBox"]/option[6]','python')
