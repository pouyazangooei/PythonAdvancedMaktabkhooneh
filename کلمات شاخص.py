paraghraph = str(input())
paraghraph = list(paraghraph)
for i in range(0,len(paraghraph)):
    if paraghraph[i] == ',':
        paraghraph[i] = ''
paraghraph = "".join(paraghraph)
sentences = paraghraph.split('.')
result = []
wordcount = 1
for sentence in sentences:
    words = sentence.split()
    for word in words:
        if word[0].isupper() and word != words[0]:
            result.append((word,wordcount))
        wordcount += 1

if len(result) > 0:
    for word, index in result:
        print(f"{index}:{word}")
else:
    print('None')