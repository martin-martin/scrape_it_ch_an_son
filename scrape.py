import requests
from bs4 import BeautifulSoup

song_title = "Traicionera"
artist_name = "Sebastian Yatra"

def linify(a_string):
  """Replaces whitespace chars in a string for dashes."""
  linified = a_string.replace(" ", "-")
  return linified

def scrape(artist_name, song_title):
  """Scrapes the lyrics of a specified song from the Genius website.

  :param artist_name: name of the artist
  :type artist_name: str
  :param song_title: title of the song
  :type song_title: str
  :return: lyrics for the given song
  :rtype: str (including newline chars)
  """
  # the URL uses dashes to separate words
  # and is built in the format 'baseURL/artist-song-lyrics'
  path = linify(artist_name) + "-" + linify(song_title) + "-lyrics"
  page_url = "http://genius.com/" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  # remove script tags that they put in the middle of the lyrics
  [h.extract() for h in html('script')]
  # Genius has a tag called 'lyrics'!
  lyrics = html.find("lyrics").get_text()
  return lyrics

print scrape(artist_name, song_title)