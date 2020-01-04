def reverse(list):
    return [word for word in reversed(list)]

sent = input("Enter a sentence to reverse: ")
words = sent.split()
rev_sent = reverse(words)

for rev_word in rev_sent:
    print(rev_word, end=" ")