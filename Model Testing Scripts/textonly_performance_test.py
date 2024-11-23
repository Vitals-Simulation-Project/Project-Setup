import requests
import json
import time
from pull_model import pull_model
import os
import statistics

# This script tests the performance of a LLM model from Ollama on text-based questions.
# The script sends a list of text-based questions to the model and records the time taken for each question.
# The script writes the questions, responses, and time taken to a file called textonly_performance_results.txt.

# INSTRUCTIONS
# 1. Go to https://ollama.com/download and install Ollama
# 2. Open a regular powershell terminal and run "ollama serve"
#    a. If you get an error, Ollama is already running and you're good to go
# 3. Close all other applications to ensure the test is accurate
# 4. Run this script
# 5. The results will be written to textonly_performance_results.txt in the test_results directory


NUM_TRIALS = 10    # number of questions in list to test
MODEL = "llava:7b" # model from Ollama
URL = "http://localhost:11434/api/chat" 

dir_path = os.path.dirname(__file__)
relative_path = "test_results/textonly_performance_results.txt"
file_path = os.path.join(dir_path, relative_path)



# pull the model
if pull_model(MODEL) == "success":
    print("Model successfully pulled.")
else:
    print("Model pull failed.")
    exit()




# list of text-only questions to test, num_trials should be less than or equal to the number of questions in the list 
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
with open(file_path, "w") as f:
    f.write("Model: " + MODEL + "\n")
    f.write("Number of questions tested: " + str(NUM_TRIALS) + "\n\n\n")

    for i in range(NUM_TRIALS):
        f.write("Question: " + TEXT_ONLY_QUESTIONS[i] + "\n")
        f.write("Answer: " + replies[i] + "\n")
        f.write("Time taken: " + str(time_taken_for_each_question[i]) + "\n\n\n")

    f.write("Average time taken per text question: " + str(sum(time_taken_for_each_question) / NUM_TRIALS) + "\n")
    f.write("Minimum time taken: " + str(min(time_taken_for_each_question)) + "\n")
    f.write("Maximum time taken: " + str(max(time_taken_for_each_question)) + "\n")
    f.write("Standard deviation: " + str(statistics.stdev(time_taken_for_each_question)) + "\n")
    f.close()
    
