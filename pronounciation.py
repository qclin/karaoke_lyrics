import pronouncing
from collections import Counter
import random

text = 'april is the cruelest month breeding lilacs out of the dead'
def get_rhymes():
    chick_rhythm = pronouncing.rhymes('roses')
    print chick_rhythm

def word_pronounciations():
    # pronounciation in ARPAbet symbols
    # http://www.speech.cs.cmu.edu/cgi-bin/cmudict#phones
    ### list of possible pronounciations
    phones_per = pronouncing.phones_for_word('permit')
    print phones_per

def word_pronounciations_count():
    count = Counter()
    words = text.split()
    for word in words:
        pronounciation_list = pronouncing.phones_for_word(word)
        if len(pronounciation_list) > 0:
            count.update(pronounciation_list[0].split(" "))

    print count.most_common(5)

def search_match_by_regex():
    phones_sigh = pronouncing.phones_for_word("jest")[0]
    print phones_sigh
    print pronouncing.search(phones_sigh)[:5]
    #finds all of the words that end in -iddle
    phone_iddle = pronouncing.search("IH1 D AH0 L$")
    print phone_iddle



def replace_rand():
    # re-writes a text by taking each word and replacing it with a random word that begin with the same first two phone
    out = list()
    for word in text.split():
        phones = pronouncing.phones_for_word(word)[0]
        first2 = phones.split()[:2]
        out.append(random.choice(pronouncing.search("^" + " ".join(first2))))

        print ' '.join(out)
        # apex isotoner themselves crenshaw muzzy bruso lyons outhouse oven them deciliter


def count_syllables():
    pronounciation_list = pronouncing.phones_for_word('programming')
    pronouncing.syllable_count(pronounciation_list[0])
    # for text
    phones =[pronouncing.phones_for_word(p)[0] for p in text.split()]
    print sum([pronouncing.syllable_count(p) for p in phones])

# count_syllables()

def stress_pattern():
    phones_list = pronouncing.phones_for_word("snappiest")
    meter = pronouncing.stresses(phones_list[0])
    print meter # 102
    # 1 : primary stress, 2: secondary stress , 0: unstressed
    ## search by stress pattern
    stress_first = pronouncing.search_stresses('100100')
    stress_either = pronouncing.search_stresses('^00[12]00[12]$') ## either 1 or 2 in the []
    print stress_first
    print stress_either
# stress_pattern()
