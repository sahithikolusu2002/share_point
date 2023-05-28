import requests
import os
from bs4 import BeautifulSoup

def download_folder(folder_url, username, password):
    try:
        # Set the request headers with authentication credentials
        headers = {'User-Agent': 'Mozilla/5.0'}
        auth = (username, password)

        # Send a GET request to retrieve the folder contents
        response = requests.get(folder_url, headers=headers, auth=auth)

        if response.status_code == 200:
            # Extract the folder name from the URL
            folder_name = folder_url.split("/")[-1]

            # Create the folder locally if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Parse the response content as HTML
            html_content = response.content.decode('utf-8')

            # Extract the file URLs from the HTML content
            file_urls = extract_file_urls(html_content)

            # Download each file within the folder
            for file_url in file_urls:
                # Send a GET request to download the file
                file_response = requests.get(file_url, headers=headers, auth=auth)

                if file_response.status_code == 200:
                    # Extract the file name from the URL
                    file_name = file_url.split("/")[-1]

                    # Write the file content to disk in binary mode
                    file_path = os.path.join(folder_name, file_name)
                    with open(file_path, 'wb') as file:
                        file.write(file_response.content)
                    print(f"File downloaded successfully: {file_name}")
                else:
                    print(f"Failed to download file: {file_url}. Status Code: {file_response.status_code}")
        else:
            print(f"Failed to retrieve folder contents. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Helper function to extract file URLs from HTML content using BeautifulSoup
def extract_file_urls(html_content):
    # Create a BeautifulSoup object with the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all anchor tags with href attribute
    anchor_tags = soup.find_all('a', href=True)

    # Extract the file URLs from the href attributes
    file_urls = ["https://<company-name>.sharepoint.com/Shared%20Documents/sharepoint/powerpoint/PRESENTATION TITLE.pptx",
                "https://<company-name>.sharepoint.com/Shared%20Documents/sharepoint/excel/Book1.xlsx",
                 "https://<company-name>.sharepoint.com/Shared%20Documents/sharepoint/word/ZURAIDE ELORRIAGA.docx"
                ]
    for anchor_tag in anchor_tags:
        file_url = anchor_tag['href']
        file_urls.append(file_url)

    return file_urls

# Provide the SharePoint folder URL, username, and password
file_url = "https://<company-name>.sharepoint.com/Shared%20Documents/sharepoint"
username = "username"
password = "password"

# Call the download_folder function
download_folder(file_url, username, password)
