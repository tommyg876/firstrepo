import unicodedata

punctuation = {}
total_words = []

for sentence in open('x.txt'):
    for char in sentence:
        if unicodedata.category(char).startswith('P'):
            punctuation[char] = 1

all_punctuation = ' '.join(punctuation)
with open ('x.txt') as f:
    for sentence in f:
        clean_sentence = sentence.strip().replace("—", " ")
        for word in clean_sentence.split():
            word = word.strip(all_punctuation).lower()
            total_words.append(word)

trigram_counter = {}

for i in range(len(total_words)-2):
    trigram = (total_words[i], total_words[i+1], total_words[i+2])
    if trigram in trigram_counter: 
        trigram_counter [trigram] += 1
    else:
        trigram_counter[trigram] = 1
    
  
print (trigram_counter)