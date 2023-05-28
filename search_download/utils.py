from bs4 import BeautifulSoup


def extract_file_urls(html_content):
    # Create a BeautifulSoup object with the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all anchor tags with href attribute
    anchor_tags = soup.find_all('a', href=True)

    # Extract the file URLs from the href attributes
    file_urls = ["https://datahungrylabs.sharepoint.com/Shared%20Documents/sharepoint/new1/powerpoint/sahi.pptx",
                 "https://datahungrylabs.sharepoint.com/Shared%20Documents/sharepoint/new2/word/sahi.docx",
                 "https://datahungrylabs.sharepoint.com/Shared%20Documents/sharepoint/new3/excel/sahi.xlsx"
                 ]
    for anchor_tag in anchor_tags:
        file_url = anchor_tag['href']
        file_urls.append(file_url)

    return file_urls


def extract_subfolder_urls(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags with href attribute
    folder_links = soup.find_all('a', href=True)

    # Extract the subfolder URLs
    subfolder_urls = [link['href']
                      for link in folder_links if link['href'].endswith('/')]

    return subfolder_urls
