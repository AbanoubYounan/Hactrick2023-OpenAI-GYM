import numpy as np
import requests
import json

maze = np.load('hackathon_sample.npy')
agent_id = "Tc1sS4FzG8" # Add your agent id here

### the ip below should be modified by you according to the server IP communicated with you
#### students track --> 16.170.85.45
#### working professionals track --> 13.49.133.141
response = requests.post('http://16.170.85.45:5000/submitMaze', json={"agentId": agent_id, "submittedMaze": json.dumps(maze.tolist())})
print(response.text, response.status_code)