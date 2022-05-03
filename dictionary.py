import json #import json
from difflib import get_close_matches # import function from difflib library

data = json.load(open("example\file\pathway")) #assign file in json format to var

#create function
def translate(w):
    w = w.lower() # Caps input will be converted to lower
    if w in data:
        return data[w]
    elif w.upper():
        return data[w.upper()]
    elif w.title(): #The title() function in python is the Python String Method which is used to convert the first character in each word to Uppercase and remaining characters to Lowercase in the string and returns a new string.
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0: 
        yn = input("Did you mean %s instead? Enter Y for yes or N for no: " % get_close_matches(w, data.keys())[0]) #pulling first value from closest match
        if yn == "Y": #testing incorrect intput to see if suggested word is the correct answer
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist, please check your entry"
        else: 
            return "We didn't understand your entry"
    else:
       return "This word does not exist. Please enter a different word."
   
   
    
    
        

word = input("Please enter the search term: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
