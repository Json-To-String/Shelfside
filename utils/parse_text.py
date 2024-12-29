# import re
# # (?<=§).*?(?=;)
#
# persona = 'Clear'
# strengths = []
# weaknesses = []
# quotes = []
# with open('personas_strength_weak_quotes.txt', 'r') as txt:
#     for ind, element in enumerate(txt.read().split('\n')):
#         print(ind, element)

import json

with open('personas.json', 'r') as f:
    data = json.load(f)
    print(data['Blue']['Strengths'])
