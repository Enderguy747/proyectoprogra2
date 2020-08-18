import os

class Execute():

    def EjecutarSpider(self):
        comand = 'cd C:/Users/Daniel/Desktop/Proyecto 2/pruebas/virtual/Scripts & activate.bat & cd / & cd C:/Users/Daniel/Desktop/Proyecto 2/pruebas/tutorial & scrapy crawl quotes2'
        os.system(command=comand)
#ex = Execute()
#ex.EjecutarSpider()