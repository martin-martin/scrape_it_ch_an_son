# implemented in Ruby
require 'open-uri'
require 'Nokogiri'

# define the necessary methods
def linify(a_string)
  """Replaces whitespace chars in a string for dashes."""
  linified = a_string.gsub(" ", "-")
  return linified
end

def scrape(artist_name, song_title)
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
  page_url = "https://genius.com/" << linify(artist_name).chomp + "-" + linify(song_title).chomp + "-lyrics"
  # catch unsuccessful query attemtps
  begin
    page = Nokogiri::HTML(open(page_url, "User-Agent" => "Mozilla/5.0"))
    # Genius has a tag called 'lyrics'!
    lyrics = page.at_css("lyrics")
    return lyrics.content
  rescue
    error_msg = "No lyrics found. Please try again."
    return error_msg
  end
end

# getting the input from the user
puts "Enter artist name: "
artist_name = gets
puts "Enter song name: "
song_title = gets

# calling one shot
print scrape(artist_name, song_title)