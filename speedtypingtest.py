import time

string="Python is my favorit language"
word_count=len(string.split())
while str(input('Enter "yes" when you are ready:\n')):
    t0 = time.time()
    inputText=len(str("Enter the phrase:'%s' as fast as possible" % string))
    t1 = time.time() 
    acc = len(set(inputText.split & string.split()))
    acc = acc/word_count
    timeTaken= t0 - t1
    wordPM = (word_count/timeTaken)
    print(wordPM,acc,timeTaken)    