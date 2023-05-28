import requests

def download_file(file_url, username, password):
    try:
        # Set the SharePoint file URL
        file_url = file_url.replace(" ", "%20")

        # Set the request headers with authentication credentials
        headers = {'User-Agent': 'Mozilla/5.0'}
        auth = (username, password)

        # Send a GET request to download the file
        response = requests.get(file_url, headers=headers, auth=auth)
        print(response.status_code)
        if response.status_code == 200:
            # Extract the file name from the URL
            file_name = file_url.split("/")[-1]

            # Write the file content to disk
            with open(file_name, 'wb') as file:
                file.write(response.content)

            print("File downloaded successfully.")
        else:
            print("Failed to download the file. Status Code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Provide the SharePoint file URL, username, and password
file_url = "https://<company-name>.sharepoint.com/Shared%20Documents/sharepoint/powerpoint"
username = "username"
password = "password"


# Call the download_file function
download_file(file_url, username, password)
