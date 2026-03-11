#Sentence = [Determiner] + [noun] + [verb] + .
#Single past, single present, single future, plural past, plural present, plural future

import random

determiners_single = [ "one", "a single", "an alone",]
determiners_plural = [ "Many", "A few", "A couple", "Sixty nine"]
single_nouns = ["cat", "dog", "turtle", "kid", "pencil"]
verbs_past = ["thought", "died", "ate", "balled up", "nae-naed", "skrrted"]
verbs_present = ["thinking", "running", "dying", "eating"]
verbs_future = ["will think", "will run", "will die", "will be eating"]
prep_phrases = ["on the game", "during his class", "in the fridge", "down the well", "on the court"]

def main():
    print(f"{make_sentence(1, 0, 0, 0, 0, 0)}")
    print(f"{make_sentence(0, 1, 0, 0, 0, 0)}")
    print(f"{make_sentence(0, 0, 1, 0, 0, 0)}")
    print(f"{make_sentence(0, 0, 0, 1, 0, 0)}")
    print(f"{make_sentence(0, 0, 0, 0, 1, 0)}")
    print(f"{make_sentence(0, 0, 0, 0, 0, 1)}")

def get_determiner():
    determiner = random.choice(determiners_single)
    return determiner
def get_determiner_plural():
    determiner = random.choice(determiners_plural)
    return determiner
def get_noun():
    noun = (f"{random.choice(single_nouns)}")
    return noun
def get_noun_plural():
    noun = (f"{random.choice(single_nouns)}s")
    return noun
def get_past_verb():
    verb = random.choice(verbs_past)
    return verb
def get_present_verb():
    verb = random.choice(verbs_present)
    return verb
def get_future_verb():
    verb = random.choice(verbs_future)
    return verb
def get_prep_phrase():
    prep = random.choice(prep_phrases)
    return prep

def make_sentence(single_past, single_present, single_future, plural_past, plural_present, plural_future):
    if single_past == True :
        sentence = (f"{get_determiner()} {get_noun()} {get_past_verb()} {get_prep_phrase()}.")  
        return sentence
    if single_present == True:
        sentence = (f"{get_determiner()} {get_noun()} is {get_present_verb()} {get_prep_phrase()}.")  
        return sentence
    if single_future == True:
        sentence = (f"{get_determiner()} {get_noun()} {get_future_verb()} {get_prep_phrase()}.")  
        return sentence
    if plural_past == True:
        sentence = (f"{get_determiner_plural()} {get_noun_plural()} {get_past_verb()} {get_prep_phrase()}.")  
        return sentence
    if plural_present == True:
        sentence = (f"{get_determiner_plural()} {get_noun_plural()} are {get_present_verb()} {get_prep_phrase()}.")  
        return sentence
    if plural_future == True:
        sentence = (f"{get_determiner_plural()} {get_noun_plural()} {get_future_verb()} {get_prep_phrase()}.")  
        return sentence

main()