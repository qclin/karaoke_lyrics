import markovify
import re

with open('./text/imagine.txt') as file:

    lyrics = file.read()

    markov_lyrics = markovify.Text(lyrics)
    print markov_lyrics

def generateSentence():
    lyrics_sentences = ""
    vowels = list('aeiou')
    for i in range(20):
        markov_sentence = markov_lyrics.make_sentence()
        if markov_sentence is not None:
            lyrics_sentences += markov_sentence +'\n'
            # cut = re.findall(r'[aeiouAEIOU]*', lyrics_sentences)
            cut = re.sub(r'[aeiouAEIOU]*', '', lyrics_sentences)
            with open("text/sub_vowel.txt", "w") as text_file:
                text_file.write(cut)
                print cut
            # re.split(r'[ ](?=[A-Z]+\b)', input)

    print lyrics_sentences

generateSentence()
