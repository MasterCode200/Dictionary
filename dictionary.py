
import json

from difflib import get_close_matches
dict = json.load(open("C:/Users/Aarav/Downloads/dictionary.json"))
def translate(w):
    w = w.lower()

    if w in dict :
        return dict[w]
    elif len(get_close_matches(w,dict.keys()))>0:
        yn = input("Did you mean %s instead? enter Y if yes or N is no  "%get_close_matches(w,dict.keys())[0])
        yn = yn.lower()
        if yn=="y":
            return dict[get_close_matches(w,dict.keys())[0]]
        elif yn=="n":
            return "The word does not exist. Please double check it."
        else:
            return "We did not understand your entry"
    else:
        return "The word does not exist. Please double check it."

w = input("Enter the word ")
output = translate(w)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
input("Press ENTER to exit")
