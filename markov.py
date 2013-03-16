#!/usr/bin/env python
import random
from sys import argv

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    global lyrics
    lyrics = {}
    words = input_text.split()

    counter = 0
    #create chain
    
    for index,word in enumerate(words):
        #counter must end before the end of the len to avoid out of range
        while counter < len(words) - 3:
            #check if word pair value exists
            if (words[counter], words[counter+1]) not in lyrics:
                lyrics[words[counter], words[counter+1]] = [words[counter+2]]
            else:
                #if true, add to list
                #get the list from the dictionary and append the value
                lyrics[words[counter], words[counter+1]].append(words[counter+2])
            counter += 1


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""


    tupled_list = lyrics.items()
    #get random dictionary key pair
    dict_length = len(tupled_list)
    starter_keypair = random.randint(0,dict_length)
    starter_tuple = tupled_list[starter_keypair]
    #print starter_tuple
    i = 0
    starter_key1 = starter_tuple[0][0]
    #print starter_key1
    starter_key2 = starter_tuple[0][1]
    #print starter_key2

    new_lyric = [starter_key1, starter_key2]

    while i < 5:
        
        #key - tuple(0)
        #lyric_key = key[1]
            #key - tuple(1)

            #get random value
        
        num_value = len(lyrics[starter_key1, starter_key2]) - 1
        random_value = random.randint(0, num_value)
        lyric_value = lyrics[starter_key1, starter_key2][random_value]
            #find the next value based on lyric_key,lyric_value tuple
            #nextword = lyrics[(lyric_key,lyric_value)][1]
        #print starter_key1, starter_key2, lyric_value
        new_lyric.append(lyric_value)
        #new_starter = key[1], lyric_value
        i += 1
        starter_key1 = starter_key2
        starter_key2 = lyric_value
    new_lyric_txt =  " ".join(new_lyric)
    print new_lyric_txt
    
    #for key,value in lyrics.items():
        #start the chain with key:value pair
        #print key,value
        # while i < 5:
        #     starter = key,value
        #     #key - tuple(0)
        #     lyric_key = key[1]
        #     #key - tuple(1)

        #     #get random value
        #     num_value = len(lyrics[key[0], key[1]]) - 1
        #     random_value = random.randint(0, num_value)
        #     print num_value,random_value
        #     lyric_value = lyrics[key[0], key[1]][random_value]
        #     #find the next value based on lyric_key,lyric_value tuple
        #     #nextword = lyrics[(lyric_key,lyric_value)][1]
        #     print key[0],key[1], lyric_value
        #     starter = key[1], lyric_value
        #     i += 1

        
    #return nextword

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
    random_text = make_text(chain_dict)
    # print random_text

main()

#if __name__ == "__main__":
 #   main()
