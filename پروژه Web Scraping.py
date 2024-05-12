import requests
from bs4 import BeautifulSoup
import mysql.connector

user_input = input('what car are you looking for? ')

re = requests.get('https://www.truecar.com/used-cars-for-sale/listings')
soup = BeautifulSoup(re.text ,'html.parser')
ads = soup.find_all('div', attrs={'data-test':'usedListing'})

carlist = []

for ad in ads:
    ad_title = ad.find('div', attrs={'data-test':'vehicleCardConditionYearMake'})
    car_name = ad.find('div', attrs={'data-test':'vehicleCardTrim'})
    car_price = ad.find('span', attrs={'data-test':'vehicleCardPriceLabelAmount'})
    car_info = ad.find('div', attrs={'data-test':'vehicleMileage'})

    ad_title = ad_title.text.strip()
    car_name = car_name.text.strip()
    car_price = car_price.text.strip()
    car_info = car_info.text.strip()

    cartuple = [ad_title,car_name,car_price,car_info]
    carlist.append(tuple(cartuple))

matchedlist = []
for i in range(0, len(carlist)):
    if user_input in carlist[i][1]:
        matchfounded = carlist[i]
        matchedlist.append(matchfounded)
n=2
while len(matchedlist) < 20:
    re = requests.get('https://www.truecar.com/used-cars-for-sale/listings/?page=%d' %(n))
    n += 1
    soup = BeautifulSoup(re.text ,'html.parser')
    ads = soup.find_all('div', attrs={'data-test':'usedListing'})

    carlist = []

    for ad in ads:
        ad_title = ad.find('div', attrs={'data-test':'vehicleCardConditionYearMake'})
        car_name = ad.find('div', attrs={'data-test':'vehicleCardTrim'})
        car_price = ad.find('span', attrs={'data-test':'vehicleCardPriceLabelAmount'})
        car_info = ad.find('div', attrs={'data-test':'vehicleMileage'})

        ad_title = ad_title.text.strip()
        car_name = car_name.text.strip()
        car_price = car_price.text.strip()
        car_info = car_info.text.strip()

        cartuple = [ad_title,car_name,car_price,car_info]
        carlist.append(tuple(cartuple))

    for i in range(0, len(carlist)):
        if user_input in carlist[i][1]:
            matchfounded = carlist[i]
            matchedlist.append(matchfounded)
    
db_selection = input("Do you have an existing database?[yes/no] ")
if db_selection == 'yes':
    db_select = input("Please enter the name of your database: ")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pzthekabir",
        database= str(db_select)
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE cars (price VARCHAR(255), mileage VARCHAR(255))")
    for j in range(0,len(matchedlist)):
        mycursor.execute("INSERT INTO cars (price, mileage) VALUES (%s, %s)", (matchedlist[j][2], matchedlist[j][3]))
        mydb.commit()
    mydb.close()
elif db_selection == 'no':
    db_create = input("Please enter a name for your database to be created: ")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pzthekabir"
        )
    mycursor = mydb.cursor()
    mycursor.execute(f"CREATE DATABASE {db_create}")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pzthekabir",
        database= str(db_create)
        )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE cars (price VARCHAR(255), mileage VARCHAR(255))")
    for j in range(0,len(matchedlist)):
        mycursor.execute("INSERT INTO cars (price, mileage) VALUES (%s, %s)", (matchedlist[j][2], matchedlist[j][3]))
        mydb.commit()
    mydb.close()