import json
import os

home = os.path.expanduser('~')
settings_file = os.path.join(home,'mathdeck_settings.json')

with open(settings_file) as file:
    settings = json.load(file)

problem_libs = settings['problem libraries']
