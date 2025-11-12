import json

def reverse_str(word:str):
    return { "original": word, "reversed_text": word[::-1] }

def to_upper(word:str):
    return { "original": word, "uppercased_text": word.upper() }

def remove_vowels(text):
    to_remove = 'aeiouAEIOU'
    newitem:str = ''
    for singl in text:
        if singl not in to_remove: 
            newitem += singl
    return { "original": text, "without_vowels": newitem }

def remove_every_third(text):
    newitem:str = ''
    for singl in range(len(text)):
        print (singl)
        print (text[singl])
        if (singl+1) % 3 != 0: 
            newitem += text[singl]
    return { "original": text, "without_every_third": newitem }

def letter_counts_map(text):
    text = text.lower()
    letter_counts = {}
    for singl in text:
        letter_counts[singl] = text.count(singl)
    with open("data/letter_counts.json", 'w') as d:
        letter_counts_json = json.dumps(letter_counts, indent=2)
        d.write(letter_counts_json)
    with open("data/letter_counts.json", 'r') as l:
        r = l.read()
        letter_counts_load = json.loads(r)
    return letter_counts_load



          
# print(letter_counts('elimelech'))