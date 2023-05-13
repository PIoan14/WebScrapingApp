from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import smtplib
from email.message import EmailMessage
import schedule
import time

def scrapingApp():

    # --tools---
    try:
        url = "https://www.orange.ro/info/film/cinema/14"

        path = r'C:\Users\User\OneDrive\Documente\chromedriver\chromedriver.exe'

        service = Service(path)
        driver = webdriver.Chrome(service=service)
        driver.get(url)

        with open('FilmData.txt', 'w') as file:
            file.write("HELLO! WELCOME TO TODAY'S RAPORT\nHere I send you best rated films from almost all malls from Bucharest\n\n")

        def convert(lista):
            aux = list()
            # print(lista)
            termen = list()
            for item in lista:
                try:
                    termen.append(item[:3])
                except Exception:
                    termen.append('0.0')
            termen.remove(termen[-1])
            for item in termen:
                aux.append(float(item))
            lista = list()
            for item in aux:
                lista.append(item)

            return lista

        winner = dict()
        # ----AFI------------

        dateAfi = dict()
        lt = driver.find_elements(by='xpath', value='//div[@class="col-md-5 col-sm-9 txt-xs"]')
        listaTitluriAfi = list()
        for i in lt:
            titlu = i.find_element(by='xpath', value='./h3/a').text
            listaTitluriAfi.append(titlu)

        # print(listaTitluriAfi)

        lg = driver.find_elements(by='xpath', value='//div[@class="col-md-5 col-sm-9 txt-xs"]')
        listaGenuri = list()

        lr = driver.find_elements(by='xpath', value='//div[@class="col-md-5 col-sm-9 txt-xs"]')
        listaRatinguriAfi = list()
        for i in lr:
            try:
                a = i.find_element(by='xpath',
                                   value='./div[@class= "row row-spaced20"]/div[@class="col-xs-12 movieRating"]/span[@class="txt-lg bold"]')
            except Exception:
                a = None
            finally:
                try:
                    rating = a.text
                except Exception:
                    rating = None
                finally:
                    listaRatinguriAfi.append(rating)

        # print(listaRatinguriAfi)
        rating_filme_afi = convert(listaRatinguriAfi)
        # print(rating_filme_afi)
        for i in range(0, len(rating_filme_afi)):
            dateAfi.update({listaTitluriAfi[i]: rating_filme_afi[i]})

        # print(dateAfi)
        x = max(dateAfi.values())
        second = dict()
        #print(dateAfi)
        for k, v in dateAfi.items():
            #print("flag")
            if v == x:
                with open("FilmData.txt", 'a') as file:
                    file.write(f"Today's best rated from AFI COTROCENI MALL : <<{k}>> with {v}/10 rating points\n"
                               f"---------------------------------------------------------------------\n")
                    winner.update({k: v})

        # ---Mega mall--------

        url2 = "https://www.orange.ro/info/film/cinema/16"
        driver.get(url2)

        lt2 = driver.find_elements(by='xpath', value='//div[@class="col-md-5 col-sm-9 txt-xs"]')
        lista_titluriMegamall = list()
        dateMega = dict()

        for i in lt2:
            titlu = i.find_element(by='xpath', value="./h3/a").text
            lista_titluriMegamall.append(titlu)

        # print(lista_titluriMegamall)

        lr2 = driver.find_elements(by='xpath', value='//div[@class="col-md-5 col-sm-9 txt-xs"]')
        listaRatinguriMegamall = list()

        for i in lr2:
            try:
                a = i.find_element(by='xpath',
                                   value='./div[@class="row row-spaced20"]/div[@class="col-xs-12 movieRating"]/span[@class="txt-lg bold"]')
            except Exception:
                a = None
            finally:
                try:
                    rating = a.text
                except Exception:
                    rating = None
                finally:
                    listaRatinguriMegamall.append(rating)
        # print(listaRatinguriMegamall)
        rating_filme_MegaMall = convert(listaRatinguriMegamall)

        for i in range(0, len(rating_filme_MegaMall)):
            dateMega.update({lista_titluriMegamall[i]: rating_filme_MegaMall[i]})
        x = max(dateMega.values())

        for k, v in dateMega.items():
            if v == x:
                with open("FilmData.txt", 'a') as file:
                    file.write(f"Today's best rated from MEGA MALL : <<{k}>> with {v}/10 rating points\n"
                               f"---------------------------------------------------------------------\n")
                    winner.update({k: v})

        # ----Park lake-------

        url3 = "https://www.orange.ro/info/film/cinema/17"
        driver.get(url3)
        dateParkLake = dict()

        lt3 = driver.find_elements(by='xpath', value='//div[@class="col-md-5 col-sm-9 txt-xs"]')
        listaTitluriParkLake = list()
        for i in lt3:
            titlu = i.find_element(by='xpath', value='./h3/a').text
            listaTitluriParkLake.append(titlu)
        # print(listaTitluriParkLake)

        lr3 = driver.find_elements(by='xpath', value='//div[@class="col-md-5 col-sm-9 txt-xs"]')
        lista_ratinguriParkLake = list()

        for i in lr3:
            try:
                a = i.find_element(by='xpath',
                                   value='./div[@class="row row-spaced20"]/div[@class="col-xs-12 movieRating"]/span[@class="txt-lg bold"]')
            except Exception:
                a = None
            finally:
                try:
                    rating = a.text
                except Exception:
                    rating = None
                finally:
                    lista_ratinguriParkLake.append(rating)
        # print(lista_ratinguriParkLake)
        rating_filme_Lake = convert(lista_ratinguriParkLake)

        for i in range(0, len(rating_filme_Lake)):
            dateParkLake.update({listaTitluriParkLake[i]: rating_filme_Lake[i]})

        x = max(dateParkLake.values())
        for k, v in dateParkLake.items():
            if v == x:
                with open("FilmData.txt", 'a') as file:
                    file.write(f"Today's best rated from PARK LAKE MALL : <<{k}>> with {v}/10 rating points\n"
                               f"---------------------------------------------------------------------\n")
                    winner.update({k: v})
        # ---Vitan------

        url4 = 'https://www.orange.ro/info/film/cinema/29'

        driver.get(url4)

        lt4 = driver.find_elements(by='xpath', value='//div[@class="col-md-5 col-sm-9 txt-xs"]')
        lista_titluriVitan = list()
        dateVitan = dict()
        for i in lt4:
            titlu = i.find_element(by='xpath', value='./h3/a').text
            lista_titluriVitan.append(titlu)

        # print(lista_titluriVitan)

        lr4 = driver.find_elements(by='xpath', value='//div[@class="col-md-5 col-sm-9 txt-xs"]')
        listaRatinguriVitan = list()

        for i in lr4:
            try:
                a = i.find_element(by='xpath',
                                   value='./div[@class="row row-spaced20"]/div[@class="col-xs-12 movieRating"]/span[@class="txt-lg bold"]')
            except Exception:
                a = None
            finally:
                try:
                    rating = a.text
                except:
                    rating = None
                finally:
                    listaRatinguriVitan.append(rating)
        rating_filme_Vitan = convert(listaRatinguriVitan)

        for i in range(0, len(rating_filme_Vitan)):
            dateVitan.update({lista_titluriVitan[i]: rating_filme_Vitan[i]})

        x = max(dateVitan.values())

        for k, v in dateVitan.items():
            if v == x:
                with open("FilmData.txt", 'a') as file:
                    file.write(f"Today's best rated from VITAN MALL: <<{k}>> with {v}/10 rating points \n"
                               f"---------------------------------------------------------------------\n\n")
                    winner.update({k: v})

        # ------final step-------------------!!!!!!!!!!
        x = max(winner.values())
        counter = 0
        for k, v in winner.items():
            if v == x:
                counter += 1

        for k, v in winner.items():
            if v == x:
                with open("FilmData.txt", 'a') as file:
                    file.write(f"Today's BIG WINNER : <<{k}>> with {v} rating points!!\n\n")

        with open("FilmData.txt", 'a') as file:
            file.write("HAVE A NICE DAY ! ;-))")

        # ------------emailSending--------------------

        sender = 'autoprogramemails@gmail.com'
        receiver = 'pnicola100@gmail.com'
        subject = 'Daily Movie Ratings'
        parola = 'qskmlgqvmaezluly'

        email = EmailMessage()
        email['From'] = sender
        email['To'] = receiver
        email['Subject'] = subject

        with open("FilmData.txt", 'r') as file:
            body = file.read()

        email.set_content(body)

        try:
            with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(sender, parola)
                smtp.send_message(email)
        except Exception:
            print("Nu s-a trimite email-ul!")

    except Exception:
       return None

scrapingApp()
#schedule.every().day.at('02:14').do(scrapingApp)

#while 1:
    #schedule.run_pending()
    #time.sleep(1)