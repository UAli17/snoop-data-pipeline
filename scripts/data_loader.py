import json
import os


def load_json_data(folder_path):
    data = []
    for file in os.listdir(folder_path):
        if file.endswith('.json'):
            with open(os.path.join(folder_path, file), 'r') as f:
                json_data = json.load(f)
                data.extend(json_data['transactions'])
    return data
