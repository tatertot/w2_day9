#!/usr/bin/env python
import random
from sys import argv

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    global lyrics
    lyrics = {}
    words = input_text.split()
    count = 0
    counter = 0
    num_words = 0
    #create chain
    num_words = 4 #get input for number of starter words
    key_count = 0 #keeps track of the index of the word in the words list)
    key_builder = 0 

    while count < (len(words) - num_words):
        
        #counter must end before the end of the len to avoid out of range

        #construct the key with Variable number of words
        #want variable to equal words[counter+0], words[counter+1], words[counter+2], etc
        print key_count,key_builder,count,counter
        counter = 0
        #this counter won't reset will stop after first sentence - need to find a way to reset the counter
        while counter < len(words) - (num_words+1):
            key_construct = [] #list that will hold the words to be used as key
            #check if word pair value exists
            while key_builder < num_words:
                key_construct.append(words[key_count]) #create a list of the words to be as the set of keys in the dict
                #print words[key_count-1]
                key_construct_text = '('+",".join(key_construct)+')' #print out the string of words from the array
                print key_construct_text
                if key_construct_text not in lyrics:
                    lyrics[key_construct_text] = words[key_count]
                    print lyrics[key_construct_text]
                else:
                    #if true, add to list
                    #get the list from the dictionary and append the value
                    key_construct.append(words[key_count])
                key_count += 1
                key_builder += 1
                print key_count
            counter += 1
        key_count += 1
        key_builder += 1
        count += 1
        


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""


    tupled_list = lyrics.items()
    print lyrics
    #get random dictionary key pair
    dict_length = len(tupled_list)
    print dict_length
    starter_keypair = random.randint(0,dict_length)
    starter_tuple = tupled_list[starter_keypair]
    #print starter_tuple
    i = 0
    starter_key1 = starter_tuple[0][0]
    #print starter_key1
    starter_key2 = starter_tuple[0][1]
    #print starter_key2

    new_lyric = [starter_key1, starter_key2]

    while i < 5: #number of words
        
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

main()

#if __name__ == "__main__":
 #   main()
