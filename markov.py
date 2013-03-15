#!/usr/bin/env python

from sys import argv

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    global lyrics
    lyrics = {}
    words = input_text.split()

    counter = 0

    while counter < len(words) - 2:

        for index,word in enumerate(words): 
            lyrics[words[counter], words[counter+1]] = words[counter+2]
        counter += 1

    print lyrics


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    for key,value in lyrics.items():
        #start the chain with key:value pair
        starter = key,value
        #key - tuple(0)
        lyric_key = key[1]
        #key - tuple(1)
        lyric_value = value
        #find the next value based on lyric_key,lyric_value tuple
        nextword = lyrics[(lyric_key,lyric_value)]
        print key[0],key[1], value, nextword
        
    return nextword

def main():

    script, filename = argv

    # args = sys.argv

    # Change this to read input_text from a file
    f = open(filename)
    global input_text
    input_text = f.read()
    # print input_text
    f.close()

    chain_dict = make_chains(input_text)
    #random_text = make_text(chain_dict)
    # print random_text

main()

#if __name__ == "__main__":
 #   main()
