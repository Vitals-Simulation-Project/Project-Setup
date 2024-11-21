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

NUM_TRIALS = 10 # number of questions in list to test
MODEL = "llava:7b"

TEXT_ONLY_QUESTIONS = [
    "What are the main differences between machine learning and deep learning?",
    "Can you explain the concept of entropy in physics and information theory?",
    "How do neural networks process and classify images?",
    "What are some real-world applications of reinforcement learning?",
    "Can you write a Python function to reverse a string?",
    "Explain how blockchain technology works in a simple way.",
    "What is the historical significance of the Silk Road in global trade?",
    "What are the benefits of meditation for mental health?",
    "What is the meaning of life according to different philosophies?",
    "Can you create a short poem about the universe?"
]

time_taken_for_each_question  = []
replies = []

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




for i in range(NUM_TRIALS):    
    question = TEXT_ONLY_QUESTIONS[i]
    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": False
    }
    start_time = time.time()

    response = requests.post(URL, json=data)
    response_json = json.loads(response.text)

    end_time = time.time()

    time_taken_for_each_question.append(end_time - start_time)


    replies.append(response_json["message"]["content"])

    print("Trial ", i + 1, " completed.")


for i in range(NUM_TRIALS):
    print("Question: ", TEXT_ONLY_QUESTIONS[i])
    print("Answer: ", replies[i])
    print("Time taken: ", time_taken_for_each_question[i])
    print("\n\n")

print("Average time taken per text question: ", sum(time_taken_for_each_question) / NUM_TRIALS)

# write all the data to a file
with open("textonly_performance_results.txt", "w") as f:
    for i in range(NUM_TRIALS):
        f.write("Question: " + TEXT_ONLY_QUESTIONS[i] + "\n")
        f.write("Answer: " + replies[i] + "\n")
        f.write("Time taken: " + str(time_taken_for_each_question[i]) + "\n\n\n")
    f.write("Average time taken per text question: " + str(sum(time_taken_for_each_question) / NUM_TRIALS) + "\n")