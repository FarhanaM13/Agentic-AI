import re
import urllib.parse
import urllib.request

def get_vid(query):
try:
encoded = urllib.parse.quote(query)

```
    url = (
        "https://www.youtube.com/results"
        "?search_query=" + encoded
    )

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            )
        }
    )

    with urllib.request.urlopen(
        req,
        timeout=10
    ) as response:

        data = response.read().decode(
            "utf-8",
            errors="ignore"
        )

    ids = re.findall(
        r'"videoId":"([^"]+)"',
        data
    )

    return ids[0] if ids else None

except Exception:
    return None
```

def create_youtube_url(command):

```
text = command.strip()

patterns = [
    r"^\s*play\s+song\s+(.+?)\s*$",
    r"^\s*play\s+music\s+(.+?)\s*$",
    r"^\s*play\s+(.+?)\s*$",
    r"^\s*youtube\s+(.+?)\s*$"
]

query = text

for pattern in patterns:

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:
        query = match.group(1).strip()
        break

if not query:
    return None

video_id = get_vid(query)

if not video_id:
    return None

return (
    "https://www.youtube.com/embed/"
    + video_id
    + "?autoplay=1&mute=0"
)
```
