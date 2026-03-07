#Sentence = [Determiner] + [noun] + [verb] + .
import random

determiners = [ "Some", "Many", "A few", "A couple", "Sixty nine"]
nouns = ["cats", "dogs", "turtles", "kids", "pencils"]
verbs = ["thought", "died", "ate", "balled up", "will get rizzed up", "nae-naed", "skrrted"]
prep_phrases = ["on the game", "during his class", "in the fridge", "down the well", "on the court"]

def main():
    print(f"{make_sentence()}")

def get_determiner():
    determiner = random.choice(determiners)
    return determiner

def get_noun():
    noun = random.choice(nouns)
    return noun
def get_verb():
    verb = random.choice(verbs)
    return verb
def get_prep_phrase():
    prep = random.choice(prep_phrases)
    return prep

def make_sentence():
    sentence = (f"{get_determiner()} {get_noun()} {get_verb()} {get_prep_phrase()}.")  
    return sentence

main()