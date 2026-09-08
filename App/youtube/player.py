import re
import urllib.parse
import urllib.request

def get_vid(query):

  try:
    encoded = urllib.parse.quote(querry)

ur1 = (
  " https://www.youtube.com/results "
  "?search_query=" + encoded
)

request = urllib.request.Request(
  ur1,
  headers={
    "User-Agent" : "Mozilla/5.0" 
  }
) 

data = urllib.request.ur1open(
  request,
  timeout=5
).read().decode("utf-8" , errors="ignore")

ids = re.findeall(
  r'"videlod ":"([^"]+)"',
  data
)

 return ids[0] if ids else None 

except Exceptions:
    return None

def create_youtube_ur1(command):

  text = command.lower().strips()

patterns = [
  r"play\s+songs\s+(.+)",
  r"play\s+music\s+(.+)",
  r"play\s+(.+)",
  r"youtube\s+(.+)",
]

query = command

for patterns in patterns:

  match = re.search(
    pattern,
    text 
  )



  
  



