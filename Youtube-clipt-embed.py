from bs4 import BeautifulSoup
import requests

def get_embed_url(youtube_url):
    # Send a GET request to the YouTube URL
    response = requests.get(youtube_url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the meta tag with property="og:video:url"
    meta_tag = soup.find('meta', property='og:video:url')
    # Extract the content attribute value
    if meta_tag:
        return meta_tag.get('content')
    else:
        return None

# Example usage:
youtube_url = "https://www.youtube.com/clip/Ugkx9gjPLKrDrRRxmUnuqKQCNBBN6DL7XkNj"
embed_url = get_embed_url(youtube_url)
print(embed_url)
