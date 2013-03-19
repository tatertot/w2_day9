#!/usr/bin/env python
# http://thysmichels.com/2012/02/06/twitter-python-api-tutorial/
#https://twitter.com/VamptwitPotter

from sys import argv
from random import randint
import twitter


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    my_dict = {}

    counter = 0

    for index,word in enumerate(corpus):
        # counter -3 because the last 3 will be a tuple
        while counter < len(corpus) - 3:

            # creates key,value pairings. keys are tuples.
            if (corpus[counter], corpus[counter+1]) not in my_dict:
                my_dict[corpus[counter], corpus[counter+1]] = [corpus[counter+2]]
            else:
                my_dict[corpus[counter], corpus[counter+1]].append(corpus[counter+2]) 
            counter += 1
    return my_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    #create tuple list of dictionary items (each key,value pair now a single item in list)
    tups = chains.items()
    #len of tups is 152
    length = len(tups)
    #select random index in tups list

    tweet = []

    count = 0

    while count < 2:
        rand_index = randint(0,length)
    #return value of rand_index - the actual words
        rand_set = tups[rand_index - 1]
    #access key using rand_set to return the FIRST word of the tuple
        first_word = rand_set[0][0]
    #access key using rand_set to return the SECOND word of tuple
        second_word = rand_set[0][1]
    #separate second tuple from selected list key,value pairs
        second_tup = rand_set[1]
    #select a random number to return a value to be chosen from second tuple
        rand_picker = len(second_tup)
    #return value using rand_pick number to access value
        rand_value = second_tup[rand_picker - 1]
    #3 word pair (key and random value)    
        tweet_phrase = first_word + " " + second_word + " " + rand_value + " "
        tweet.append(tweet_phrase)
        count += 1
    final_tweet =  " ".join(tweet)
    return final_tweet


def main():

    script, filename = argv

    # Change this to read input_text from a file
    f = open(filename)
    input_text = f.read()
    f.close()

    #split on the spaces from input_text
    input_text = input_text.split()

    #strip punctuation
    for word in input_text:
        word.strip('(,."-)')  

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    api = twitter.Api(consumer_key='ubKXrQeqqmFKCTmCPklgwg', consumer_secret='rFLjdKZMw4z82ENwr6zhthR5pd88eM6JF4XVqEV0', access_token_key='1279111003-Cdxog5qLSumAJasSTfFpoLGLLJRIoo3doO6keOq', access_token_secret='nrG0wyAsiA8ro0wzAvMQPaMC9L8EVbAJ94BLOdTSRo')

    status = api.PostUpdates(random_text)

main()
if __name__ == "__main__":
    main()
