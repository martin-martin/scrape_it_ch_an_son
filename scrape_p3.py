# ported to python 3.x
import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint

## fetch more lyrics at once
song_dict = {
  "Traicionera" : "Sebastian Yatra",
  "Adentro" : "Calle 13",
  "Me Gustas Tu" : "Manu Chao"
}

## do the user input
# artist_name = input("Enter artist name: ")
# song_title = input("Enter song name: ")

## hardcoded
# song_title = "Traicionera"
# artist_name = "Sebastian Yatra"

class AppURLopener(urllib.request.FancyURLopener):
  """Mimics a different user agent to avoid blocking the request."""
  version = "Mozilla/5.0"

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
  # using the version spoofing to circumvent the 403 error
  opener = AppURLopener()
  res = opener.open(page_url)
  # the roundabout approach returns a 'byte' object
  # and needs to be converted to 'str'
  page = res.read().decode('utf-8')
  # the input is already a 'str', so no need for '.text'
  html = BeautifulSoup(page, "html.parser")
  # remove script tags that they put in the middle of the lyrics
  [h.extract() for h in html('script')]
  # Genius has a tag called 'lyrics'!
  lyrics = html.find("lyrics").get_text()
  return lyrics


##### make it run requests ######

# weld a bucket to catch 'em all
lyrics_dict = dict()

for song, artist in song_dict.items():
  lyrics = scrape(artist, song)
  # create a dict that has a tuple of (artist, song) as key
  # and the fitting lyrics as value
  lyrics_dict[(artist, song)] = lyrics

#pprint(lyrics_dict)