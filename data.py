# import json

# jsonContent = [
#   {"id": 1, "name": "apple", "price": 15.90},
#   {"id": 2, "name": "banana", "price": 12.90},
#   {"id": 3, "name": "carrot", "price": 5.90},
#   {"id": 4, "name": "cucumber", "price": 7.90},
#   {"id": 5, "name": "eggplant", "price": 10.90},
#   {"id": 6, "name": "mango", "price": 12.9},
#   {"id": 7, "name": "onion", "price": 5.90},
# ]

# # initialize mixed stories file for google colab (students should have it in their working dir)
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(jsonContent, f, indent=4)


def return_in_reversr(word:str):
    return { "original": word, "reversed_text": word[::-1] }

def return_in_uppercase(word:str):
    return { "original": word, "uppercased_text": word.upper() }
    
    
    
