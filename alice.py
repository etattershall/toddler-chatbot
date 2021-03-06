'''
                  ___
                /-|||-\ 
               /| . . |\
              // \ c / \\
             >o<  | |  >o<
             
                 ALICE
                 
Welcome to the Toddler Chatbot

Created on 10/07/2017
@author: Emma Tattershall
'''
from __future__ import print_function
import sys
import random
import re

def reply(fulltext):
    '''
        Function takes a text string and calculates an appropriate reply
    '''
    # 5% chance of responding with an insult (toddlers are horrible)
    if random.random() > 0.95:
        return 'You smell!'
    
    # Make the text lowercase so that capital letters (and the lack therof)
    # don't confuse the program    
    text = fulltext.lower()
    # Get the characters before the first space.
    first_token = text.split(' ')[0]
    # Now find all the actual letters before the first piece of punctuation.
    try:
        first_word = re.findall('^\w+', first_token)[0]
    except:
        first_word = ''

    # Respond appropriately to emoticons
    emoticons = re.findall("[:;]'?-?[\Wpo0xsb]", text)
    if len(emoticons) > 0:
        return ':-D'
    
    # If the user has not put in any text input (e.g. they have submitted a 
    # emoty string or punctuation only), prompt them for input again.
    if text == '' or first_word == '':
        return "I'm bored"

    # Make polite conversation
    if text.startswith('hello') or text.startswith('hi'):
        return 'Hi'

    for question in ["whats your name",
                     "what's your name",
                     "who are you",
                     "what are you called"]:
        if question in text:
            return 'Alice'

    for question in ["how old are you",
                     "what's your age",
                     "whats your age"]:
        if question in text:
            return 'Three and one quarter'

    # If asked for other information...
    if first_word in ['who', 'what', 'where', 'why', 'when', 'how', 'which']:
        # Repeat the question back
        if text[-1] == '?':
            return fulltext[0].upper() + fulltext[1:-1] + ', sillypants'
        else:
            return fulltext[0].upper() + fulltext[1:] + ', sillypants'
        
    # If asked to do something...
    elif first_word in ['can', 'will', 'should', 'would', 'does', 'is', 'was'] and 'you' in text:
        # Say no
        return 'No'

    # And finally, if it's a statement...
    else:
        # Ask why
        return 'Why?'
    

print(
r'''
                  ___
                /-|||-\ 
               /| . . |\
              // \ c / \\
             >o<  | |  >o<
             
                 ALICE

Say something!
''')
try:
    while True:
        # Prompt for user input
        # Note: Python 2 and 3 deal with user input slightly differently. The lines below make
        # sure that the code runs the same on both versions.
        if sys.version.startswith('2'):
            fulltext = raw_input('')
        else:
            fulltext = input('')
        # Calculate the reply and print it in the terminal
        print('>>> ' + reply(fulltext) + '\n')
except KeyboardInterrupt:
    print('>>> Bye bye!\n')
