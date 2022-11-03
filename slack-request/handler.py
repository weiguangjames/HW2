import json
def handle(req):
    data ={
    "text":"Serverless Message",
    "attachments":[{
        "title": "The course of COEN 241 Cloud Computing!",
        "fields":[{
            "title":"Satisfaction",
            "value":"100",
            "short": True,
        }],
        "author_name": "weiguangjames",
        "author_icon": "https://avatars.githubsercontent.com/u/116145145?s=40&v=4",
        "image_url":"https://www.scu.edu/media/offices/umc/scu-brand-guildelines/visual-identity-amp-photography/visual-identity-toolkit/logos-amp-seals/Mission-Dont3.png"
    },
    {
        "title": "About COEN 241",
        "text": "Sean Choi is the best professor!."
    },
    {
        "fallback": "Would you recommend COEN 241 to your friends?",
        "title": "Would you recommend COEN 241 to your friends?",
        "callback_id": "response123",
        "color": "#3AA3E3",
        "attachment_type":"default",
        "actions": [
            {
                "name": "recommend",
                "text": "Of Course!",
                "type": "button",
                "value": "recommend"
            },
            {
                "name": "Take it again",
                "text": "One more time",
                "type": "button",
                "value": "Take it again"
            }
        ]
    }]
}

    return json.dumps(data)
