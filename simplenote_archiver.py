import os
import sys
import datetime
import simplenote

username = os.environ["SIMPLENOTE_USERNAME"]
password = os.environ["SIMPLENOTE_PASSWORD"]
updated_tags = os.environ["SIMPLENOTE_UPDATED_TAG"]
archive_tags = os.environ["SIMPLENOTE_ARCHIVE_TAG"]

if not (username and password and updated_tags and archive_tags):
    print("Environment variables not found: SIMPLENOTE_USERNAME, SIMPLENOTE_PASSWORD, SIMPLENOTE_UPDATED_TAG, SIMPLENOTE_ARCHIVE_TAG")
    sys.exit(1)

sn = simplenote.Simplenote(username, password)

notes, status = sn.get_note_list(tags = [updated_tags])

if status:
    print("Note retrieval failed")
    sys.exit(1)

print(notes)

date_str = str(datetime.datetime.now().date())

for note in notes:
   sn.add_note({'content': date_str + " " + note['content'], 'tags': [archive_tags]})
