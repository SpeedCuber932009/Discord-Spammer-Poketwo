from webserver import keep_alive
import requests

channelID = 915464352667140106
headers = {
    "authorization":
    "889717787021422622"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
