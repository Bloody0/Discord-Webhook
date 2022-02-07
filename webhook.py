import requests
from time import sleep

examplembed = { 
    'title': 'Microsoft Announcement',
    'description': 'Please consider using Visual Studio Code! Thanks!',
    "url": "https://code.visualstudio.com/",
    'color': '16711680'
}

payload = {
    'content': '<@905807266098339870>',
    'username': "Microsoft",
    'avatar_url': "https://th.bing.com/th/id/OIP.wk7Vhon0stlJtBAWUBE0DgHaJH?pid=ImgDet&rs=1",
    'embeds': [examplembed]
}

while(True):
    requests.post(url='https://discordapp.com/api/webhooks/939912770613289031/PduP48qwO8N5nw1a6E7UnKE1rVhJqDEWQkapk89J0wwGwUCyezwKb9FC_LiRBHDc7jo9',
    json=payload)
    sleep(1)