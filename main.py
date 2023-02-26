import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Replace the URL with the web page you want to scrape
url = "https://www.classcentral.com/report/free-certificates"

# Scrape the web page and extract the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the text in the HTML content
text_list = [element.text for element in soup.find_all()]

# Translate the text to Hindi using Google Translate API
translator = Translator()
hindi_text_list = [translator.translate(text, dest="hi").text for text in text_list]

# Replace the original text with the translated text in the HTML content
for i, element in enumerate(soup.find_all()):
    element.string = hindi_text_list[i]

# Save the translated HTML content to a file
with open("translated_page.html", "w", encoding="utf-8") as f:
    f.write(str(soup))


# Upload the translated HTML content to a free web server
# Follow the instructions provided by the web server to upload the HTML content
