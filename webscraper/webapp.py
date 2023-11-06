from bs4 import BeautifulSoup
import requests
import mysql.connector

try:
    # Connection to the database
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="pesho",
        password="parola",
        database="WebScrape"
    )


    # Link to the web page
    url = "https://www.speedcomputers.biz/palit-rtx-4060-dual-8gb-gddr6-video-karta/"
    page = requests.get(url)
    cursor = db.cursor()

    if page.status_code == 200:
        # Locating the price tag
        soup = BeautifulSoup(page.text, 'html.parser')
        price = soup.find("span", class_="price uk-price")

        if price:
            # Extracting the text content of the price element
            price_value = price.text.strip()  # Use .strip() to remove leading/trailing white spaces

            # Displaying the price
            print(price_value)

            # Inserting the price into the database
            insert_query = "INSERT INTO hardware (price) VALUES (%s)"
            cursor.execute(insert_query, (price_value,))

            # Commit the changes to the database
            db.commit()

            cursor.close()
            db.close()
        else:
            print("Price not found on the web page.")
    else:
        print("Failed to retrieve the web page.")

except mysql.connector.Error as e:
    print(f"Database Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
