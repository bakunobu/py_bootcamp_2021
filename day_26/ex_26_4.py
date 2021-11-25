def phrase_to_dict(phrase:str) -> dict:
    len_dict = {word:len(word) for word in phrase.split(" ")}
    return(len_dict)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
phrase_to_dict = phrase_to_dict(sentence)
for k, v in phrase_to_dict.items():
    print(f'"{k}": {v}')