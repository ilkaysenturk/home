from datetime import date
class Insert():

    def __init__(self,header_text):
        self.header_text=header_text
    def seperator_line():
        print('--------------------------------------------------------------------')

    def line_space():
        print()

    def footer():
        print('Created by IS, ''Created on',"{:%m-%d-%Y}".format(date.today()))

    def header(self):
        hdr=self.header_text
        cnt=hdr.center(68,'-')
        print(cnt)
