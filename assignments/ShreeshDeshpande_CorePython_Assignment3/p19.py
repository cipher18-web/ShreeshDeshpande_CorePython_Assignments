#check how many times every word appears

sentence = input("Enter sentence: ").split()
word_count = {}
for word in sentence:
  word_count[word] = word_count.get(word, 0) + 1
print(word_count)