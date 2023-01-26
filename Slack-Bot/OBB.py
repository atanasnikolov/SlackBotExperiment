import os
from dotenv import load_dotenv
from pathlib import Path
import slack


#Things that need to be changed if another device is used deotenv_path/ slack_bot_token/ Client.conversations_invite (users to groups (if possible))

dotenv_path = Path('C:\\Users\\Tanio\\Desktop\\VS Code\\Slack-Bot\\.env')
load_dotenv(dotenv_path=dotenv_path)

slack_bot_token = os.getenv('SLACK_BOT_TOKEN')
client = slack.WebClient(token=slack_bot_token)

channel_name = "new-users-channel"
if __name__ == "__main__":
    result = client.conversations_create(name=channel_name)

    channel_id1 = result["channel"]["id"]
    #since I have no money (thank you for the promotion btw) I am using users since groups are for the paid version 
    response = client.conversations_invite(channel=channel_id1, users=["U04K643Q8UF", "U04LA6EA1GS"])
    add_topic = client.conversations_setTopic(channel=channel_id1, topic="This is the Topic of the channel")
    add_bookmark = client.bookmarks_add(channel_id=channel_id1, title="tubata", type="link", link="insert link here")
    welcome_message = client.chat_postMessage(channel=channel_id1, text='This is the welcome message from the BOT')
    #add_description = client.admin_teams_settings_setDescription(team_id=channel_id1, description="Remove comment if you have the enterprise version so you can use this function")





