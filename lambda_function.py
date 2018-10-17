import json

def lambda_handler(event, context):
    # TODO implement
    reply=""
    if event["message"] == "hi":
        reply = 'Hi there! How can I help you today?'

    elif event["message"] == "hey":
        reply = "Hey there! How can I help today?"

    elif event["message"] == "hello":
        reply = "Hello there! How can I help today?"
        
    elif event["message"] == "how is the weather outside?":
        reply = "Please turn on your location services"
        
    elif event["message"] == "what is your name?":
        reply = "Hi, I am Chatbot !"
        
    else:
        reply = "wait for it! under maintainance :)"
        
    return reply