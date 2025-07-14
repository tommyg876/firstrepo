input_path = 'words.txt'
reader = open('words.txt', 'r')

def check_word (word):
    for line in reader:
        line = line.strip()
        if len(line) != 5:
            return False
        if 'e' not in word:
            return False
        if line[3]!= 'e':
            return False
        if 'T' in word or 'I' in word or 'D' in word:
            return False
        if 'R' not in word:
            return False
        return True

count = 0 
for line in reader:
    word = line.strip()
    if check_word(word):
        count += 1


print ("matching words: ", count)

    #have to have e be in the fourth letter
    #TID are not in the word
    #R is in the word
