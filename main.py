import datetime
import os
import sys

import simplenote

username = os.environ["SIMPLENOTE_USERNAME"]
password = os.environ["SIMPLENOTE_PASSWORD"]
updated_tag = os.environ["SIMPLENOTE_UPDATED_TAG"]
archive_tag = os.environ["SIMPLENOTE_ARCHIVE_TAG"]

if not (username and password and updated_tag and archive_tag):
    print(
        "Environment variables not found: SIMPLENOTE_USERNAME, SIMPLENOTE_PASSWORD, SIMPLENOTE_UPDATED_TAG, SIMPLENOTE_ARCHIVE_TAG")
    sys.exit(1)

sn = simplenote.Simplenote(username, password)


def simplenote_archiver(request=None):
    notes, status = sn.get_note_list(tags=[updated_tag])
    notes = filter(lambda x: not x["deleted"], notes)

    if status:
        print("Note retrieval failed")
        sys.exit(1)

    date_str = str(datetime.datetime.now().date())

    for note in notes:
        sn.add_note({'content': date_str + " " + note['content'], 'tags': [archive_tag]})


if __name__ == '__main__':
    simplenote_archiver()
