import pronouncing
from collections import Counter
import random
import sys


pronounciations_list = []

def text_pronounciation(text):
    words = text.split()
    for word in words:
        word_phones = pronouncing.phones_for_word(word) ## splits an array
        print word_phones
        for phone in word_phones:
            pronounciations_list.append(phone)
    return pronounciations_list



for line in sys.stdin:
    line = line.strip()
    pro_list = text_pronounciation(line)
    print pro_list
