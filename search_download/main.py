from sharepoint_downloader import SharePointDownloader


def main():
    # Configure SharePoint credentials and search query
    username = "surya@datahungrylabs.onmicrosoft.com"
    password = "Deloitte1"
    search_query = "https://datahungrylabs.sharepoint.com/Shared%20Documents/sharepoint/new1/powerpoint/sahi.pptx"

    # Create an instance of SharePointDownloader
    downloader = SharePointDownloader(username, password)

    # Search and download matched documents
    downloader.download_documents(search_query)


if __name__ == "__main__":
    main()