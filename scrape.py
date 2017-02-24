import requests
from bs4 import BeautifulSoup

base_url = "http://api.genius.com"

song_title = "Lake Song"
artist_name = "The Decemberists"

def linify(a_string):
  linified = a_string.replace(" ", "-")
  return linified

def scrape(artist_name, song_title):
  # getting the URL right
  path = linify(artist_name) + "-" + linify(song_title) + "-lyrics"
  page_url = "http://genius.com" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  # remove script tags that they put in the middle of the lyrics
  [h.extract() for h in html('script')]
  # at least Genius is nice and has a tag called 'lyrics'!
  lyrics = html.find("lyrics").get_text
  return lyrics

print scrape(artist_name, song_title)