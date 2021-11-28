def count_char(text,char):
    count=0
    for letter in text:
        if letter == char:
            count = count + 1
            return count
filename=input('Enter a filename: ')
with open (filename) as f:
    word = f.read()
    for char in "abcdefghijklmnopqrstuvwxyz":
        perc = 100* count_char(word,char)/len(word)
        print("{} - {} %".format(char,round(perc,2)))