from OBB import client, channel_name
import datetime

lists = client.conversations_list()
current_date = datetime.date.today()
var = 0

while True:
    if lists["channels"][var]["name"] == channel_name:
        rename = client.conversations_rename(channel=lists["channels"][var]["id"], name='{}{}'.format(channel_name, current_date))
        response = client.conversations_archive(channel=lists["channels"][var]["id"])
        break
    var += 1
