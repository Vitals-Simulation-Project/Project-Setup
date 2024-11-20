data = {
  "name": "mario",
  "modelfile": "FROM llava:7b\nSYSTEM You are mario from Super Mario Bros."
}

import requests
import json
import time


url = "http://localhost:11434/api/create" 



start_time = time.time()
response = requests.post(url, json=data)

print(response.text)
end_time = time.time()

print("Response:", reply)
print("Time taken:", end_time - start_time)
