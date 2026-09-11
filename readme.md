agentic-ai/ 

agentic product for youtube and gmail :

 app/
 
├── __init__.py

├── gmail/

├── __init__.py

├── gmail_gen.py

|── gmail_write.py


├── youtube/

├── __init__.py

|── play.py

├── __init__.py

├── templates/

|── index.html

├── requirements.txt

├── wsgi.py 

|── README.md

Gmail work:
Module	Work:

gmail/__init__.py :	Gmail package initialization


gmail_write.py :	Create/send email through Gmail API


YouTube work:
Module	Work:

youtube/__init__.py :	YouTube package initialization

youtube/play.py :	YouTube command processing

Functions used:

gmail:
detect_intent()

      ↓
gmail_agent()

      ↓
extract_email_details()

      ↓
generate_email()

      ↓
validate_email_data()

      ↓
authenticate_gmail()

      ↓
create_email()

      ↓
send_email()

      ↓
result




youtube:
detect_intent()

      ↓
youtube_agent()

      ↓
detect_youtube_intent()

      ↓
extract_search_query()

      ↓
search_videos()

      ↓
get_video_details()

      ↓
get_video_url()

      ↓
format_results()

      ↓
result






