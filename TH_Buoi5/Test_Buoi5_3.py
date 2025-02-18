with open ('./TH_Buoi5/P1_data.txt', 'r') as f:
    sentence = f.read()
    print(sentence)

words = sentence.split()
words = [word.lower() for word in words]

counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
print(counter)