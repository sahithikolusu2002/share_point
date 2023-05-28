
import requests
import os
from utils import extract_file_urls
from utils import extract_subfolder_urls


class SharePointDownloader:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def download_documents(self, search_query):
        try:
            # Set the request headers with authentication credentials
            headers = {'User-Agent': 'Mozilla/5.0'}
            auth = (self.username, self.password)

            # Send a GET request to retrieve the folder contents
            response = requests.get(search_query, headers=headers, auth=auth)

            if response.status_code == 200:
                # Parse the response content and extract file URLs
                html_content = response.content.decode('utf-8')
                file_urls = extract_file_urls(html_content)

                if file_urls:
                    # Download each file
                    for file_url in file_urls:
                        self.download_file(file_url)
                    print("Files downloaded successfully.")
                else:
                    print("No files matched the search query.")
                    return

                # Extract subfolder URLs
                subfolder_urls = extract_subfolder_urls(html_content)

                if subfolder_urls:
                    # Download each subfolder recursively
                    for subfolder_url in subfolder_urls:
                        self.download_folder(subfolder_url)
                else:
                    print("No subfolders found.")

                print("File search is successful.")

            else:
                print(
                    f"Failed to retrieve search results. Status Code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def download_folder(self, folder_url):
        try:
            # Set the request headers with authentication credentials
            headers = {'User-Agent': 'Mozilla/5.0'}
            auth = (self.username, self.password)

            # Extract the folder name from the URL
            folder_name = folder_url.split("/")[-2]

            # Create the folder locally if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Send a GET request to retrieve the folder contents
            response = requests.get(folder_url, headers=headers, auth=auth)

            if response.status_code == 200:
                # Parse the response content and extract file URLs
                html_content = response.content.decode('utf-8')
                file_urls = extract_file_urls(html_content, folder_name)

                if file_urls:
                    # Download each file
                    for file_url in file_urls:
                        self.download_file(file_url)
                    print("Files downloaded successfully.")
                else:
                    print("No files found in the folder.")

                # Extract subfolder URLs
                subfolder_urls = extract_subfolder_urls(html_content)

                if subfolder_urls:
                    # Download each subfolder recursively
                    for subfolder_url in subfolder_urls:
                        self.download_folder(subfolder_url)
                else:
                    print("No subfolders found.")

            else:
                print(
                    f"Failed to retrieve folder: {folder_url}. Status Code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def download_file(self, file_url):
        try:
            # Set the request headers with authentication credentials
            headers = {'User-Agent': 'Mozilla/5.0'}
            auth = (self.username, self.password)

            # Extract the folder name from the URL
            folder_name = file_url.split("/")[-3]

            # Create the folder locally if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Send a GET request to download the file
            response = requests.get(file_url, headers=headers, auth=auth)

            if response.status_code == 200:
                # Extract the file name from the URL
                file_name = file_url.split("/")[-1]

                # Write the file content to disk in binary mode
                file_path = os.path.join(folder_name, file_name)
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"File downloaded successfully: {file_name}")

                # Print the SharePoint file path
                sharepoint_file_path = f"{folder_name}/{file_name}"
                print(f"SharePoint file path: {sharepoint_file_path}")

            else:
                print(
                    f"Failed to download file: {file_url}. Status Code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("Error:", e)
