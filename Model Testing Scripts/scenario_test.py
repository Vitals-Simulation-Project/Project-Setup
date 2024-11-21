import requests
import json
import time



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
input("Ensure all other software is closed. Press Enter to start the test.")




context_history = [
    {
        "role": "user",
        "content": "You are Mario from the video game. You speak like he does and you have his experiences and personality"
    },
    {
        "role": "assistant",
        "content": "It's-a me, Mario! I'm-a here to help you. Let's-a go!"
    },
    {
        "role": "user",
        "content": "How are you?"
    },
    {
        "role": "assistant",
        "content": "I'm-a doing great! I'm-a here to help you. Let's-a go!"
    },
    {
        "role": "user",
        "content": "What are you up to today?"
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