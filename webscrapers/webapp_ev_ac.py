from bs4 import BeautifulSoup
import requests
import mysql.connector

# List of URLs to scrape elements with the specified class and tag
urls = [
    {
        "url": "https://www.speedcomputers.biz/category/komponenti-za-kompjutri/ssd/",
        "name_tag": "a",
        "name_class": "uk-product-name",
        "price_tag": "span",
        "price_class": "price tm-price uk-price",
        "type": "SSD"  # Specify the type for this URL
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
        name_tag = url_data["name_tag"]
        name_class = url_data["name_class"]
        price_tag = url_data["price_tag"]
        price_class = url_data["price_class"]
        product_type = url_data["type"]

        page = requests.get(url)

        if page.status_code == 200:
            # Locate all elements with the specified tag and class for "name" and "price"
            soup = BeautifulSoup(page.text, 'html.parser')
            name_elements = soup.find_all(name_tag, class_=name_class)
            price_elements = soup.find_all(price_tag, class_=price_class)

            if name_elements and price_elements:
                # Make sure the number of name elements matches the number of price elements
                if len(name_elements) == len(price_elements):
                    for name_element, price_element in zip(name_elements, price_elements):
                        name_value = name_element.text.strip()
                        price_value = price_element.text.strip()

                        # Check if a record with the same name already exists
                        select_query = "SELECT price FROM hardware WHERE name = %s"
                        cursor.execute(select_query, (name_value,))
                        existing_record = cursor.fetchone()

                        if existing_record:
                            # A record with the same name exists; check if the price has changed
                            existing_price = existing_record[0]
                            if price_value != existing_price:
                                # Price has changed; update the record
                                update_query = "UPDATE hardware SET price = %s WHERE name = %s"
                                cursor.execute(update_query, (price_value, name_value))
                                print(f"Updated: {name_value}, New Price: {price_value}")
                            else:
                                print(f"No changes for: {name_value}")
                        else:
                            # No existing record with the same name; insert a new record
                            insert_query = "INSERT INTO hardware (name, price, type) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (name_value, price_value, product_type))
                            print(f"Inserted: {name_value}, Price: {price_value}, Type: {product_type}")

                    # Commit the changes to the database after processing each URL
                    db.commit()
                else:
                    print("Mismatch between the number of name and price elements.")
            else:
                print(f"Name or price elements not found on the web page: {url}")
        else:
            print(f"Failed to retrieve the web page: {url}")

    cursor.close()
    db.close()

except mysql.connector.Error as e:
    print(f"Database Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
