import requests
import os

class DownloadFolder:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def download_folder(self, file_url):
        try:
            # Set the request headers with authentication credentials
            headers = {'User-Agent': 'Mozilla/5.0'}
            auth = (self.username, self.password)

            # Extract the folder name from the URL
            folder_name = file_url.split("/")[-2]

            # Create the folder locally if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

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

                # Print the SharePoint file path
                sharepoint_file_path = f"{folder_name}/{file_name}"
                print(f"SharePoint file path: {sharepoint_file_path}")
            else:
                print(f"Failed to download file: {file_url}. Status Code: {file_response.status_code}")

        except requests.exceptions.RequestException as e:
            print("Error:", e)


# Provide the SharePoint file URL, username, and password
file_url = "https://datahungrylabs.sharepoint.com/Shared%20Documents/share_visual/word/helo.docx"
username = "surya@datahungrylabs.onmicrosoft.com"
password = "Deloitte1"

# Create an instance of DownloadFolder
downloader = DownloadFolder(username, password)

# Call the download_folder method
downloader.download_folder(file_url)
