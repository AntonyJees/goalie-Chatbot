import json
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to the project root
project_root = os.path.dirname(script_dir)

# Path to teams.json in project root
teams_json_path = os.path.join(project_root, 'teams.json')
# Path to output teams.txt in data folder
teams_txt_path = os.path.join(script_dir, 'teams.txt')

print(f"Looking for: {teams_json_path}")

with open(teams_json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    teams = data['teams']

with open(teams_txt_path, 'w', encoding='utf-8') as f:
    for team in teams:
        f.write(team + '\n')

print(f"✓ Successfully created {teams_txt_path} with {len(teams)} teams!")
