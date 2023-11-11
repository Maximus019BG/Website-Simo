from bs4 import BeautifulSoup
import requests
import mysql.connector

# List of URLs to scrape
urls = [
    {
        "url": "https://www.moew.government.bg/bg/kampanii/ekokalendar/page/1/",
        "tag": "h3",
        "class": "document-title"
    },
    {
        "url": "https://www.moew.government.bg/bg/kampanii/ekokalendar/page/2/",
        "tag": "h3",
        "class": "document-title"
    },
    {
        "url": "https://www.moew.government.bg/bg/kampanii/ekokalendar/page/3/",
        "tag": "h3",
        "class": "document-title"
    }
]

try:
    # Connection to the database
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="pesho",
        password="parola",
        database="WebScrape"
    )

    cursor = db.cursor()

    for url_data in urls:
        url = url_data["url"]
        tag = url_data["tag"]
        class_name = url_data["class"]

        page = requests.get(url)

        if page.status_code == 200:
            # Locating all elements with the specified tag and class
            soup = BeautifulSoup(page.text, 'html.parser')
            elements = soup.find_all( tag, class_=class_name)

            if elements:
                for element in elements:
                    # Extracting the text content of each element
                    element_value = element.text.strip()  # Use .strip() to remove leading/trailing white spaces

                    # Displaying the element value
                    print(element_value)

                    # Check if the name already exists in the database
                    select_query = "SELECT name FROM help WHERE name = %s"
                    cursor.execute(select_query, (element_value,))
                    existing_name = cursor.fetchone()

                    if not existing_name:
                        # Name doesn't exist; insert it
                        insert_query = "INSERT INTO help (name) VALUES (%s)"
                        cursor.execute(insert_query, (element_value,))
                        print(f"Inserted: {element_value}")
                    else:
                        print(f"Name already exists: {element_value}")

                # Commit the changes to the database after processing each URL
                db.commit()
            else:
                print(f"Elements not found on the web page: {url}")
        else:
            print(f"Failed to retrieve the web page: {url}")

    cursor.close()
    db.close()

except mysql.connector.Error as e:
    print(f"Database Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
