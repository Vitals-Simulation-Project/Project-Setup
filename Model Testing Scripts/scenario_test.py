import requests
import json
import time
from pull_model import pull_model


# pull the model
if pull_model("llava:7b") == "success":
    print("Model successfully pulled.")
else:
    print("Model pull failed.")
    exit()


URL = "http://localhost:11434/api/chat" 
MODEL = "llava:7b"


# send one request to get the model loaded
data = {
    "model": MODEL,
    "messages": [
        {
            "role": "user",
            "content": "Hello"
        }
    ],
    "stream": False
}

response = requests.post(URL, json=data)
response_json = json.loads(response.text)
print(response_json["message"]["content"])


# wait a few seconds to make sure the model is loaded
time.sleep(5)
print("\n")
input("Ensure all other software is closed. Press Enter to start the test.")




context_history = [
    {
        "role": "user",
        "content": "Hello."
    },
    {
        "role": "assistant",
        "content": "Hi there! How can I help you today?"
    },
    {
        "role": "user",
        "content": "Tell me about the state I'm in"
    },
    {
        "role": "assistant",
        "content": "Sure! What state are you in?"
    },
    {
        "role": "user",
        "content": "I am in Florida"
    }
]

data = {
    "model": MODEL,
    "messages": context_history,
    "stream": False
}

start_time = time.time()

response = requests.post(URL, json=data)
response_json = json.loads(response.text)

end_time = time.time()

time_taken = end_time - start_time


reply = response_json["message"]["content"]



print("Question: ", context_history[-1]["content"])
print("Answer: ", reply)
print("Time taken: ", time_taken)
print("\n\n")


# wait 3 seconds
time.sleep(3)


context_history = [
    {
        "role": "user",
        "content": "Are you Mario?"
    },
]


data = {
    "model": MODEL,
    "messages": context_history,
    "stream": False
}


start_time = time.time()

response = requests.post(URL, json=data)
response_json = json.loads(response.text)

end_time = time.time()

time_taken = end_time - start_time


reply = response_json["message"]["content"]



print("Question: ", context_history[-1]["content"])
print("Answer: ", reply)
print("Time taken: ", time_taken)
print("\n\n")