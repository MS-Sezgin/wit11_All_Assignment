"""

✅ Project 3: Word Analysis Tool
Practice string methods, loops, conditions, lists, and sets.

Ask the user for a sentence.

Analyze:

Character count (excluding spaces)
Word count
Unique words (set)
Longest word
👉 Hint: Use split(), len(), set().

"""
##1
sentences = input("give me a sentence\n")
characterCounter = len(sentences.replace(" ", ""))
print(f"{characterCounter}")

##2
wordCounterList = sentences.split()
wordCounter=len(wordCounterList)
print(f"\n{wordCounter}")

##3
uniqeWordList=set(wordCounterList)
print(f"\n{uniqeWordList}")

##4
longestWord = ""
for i in wordCounterList:
    longestWord = i if len(longestWord) < len(i) else longestWord

print(f"\n{longestWord}")