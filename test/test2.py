
import collections

text = input("Введите текст: ")
words = text.split()
counter = collections.Counter(words)
most_common = counter.most_common()[0]
print(most_common)












