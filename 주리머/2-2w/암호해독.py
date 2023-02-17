key = list(input().strip())
word = input().strip()
wordArr = []


for i in range(len(key)):
    wordArr.append(word[i * (len(word) // len(key)):(i + 1) * (len(word) // len(key))])

newWordArr = []

for i in range(len(wordArr[0])):
    chr = ""
    for j in range(len(wordArr)):
        chr += wordArr[j][i]
    newWordArr.append(chr)

sortedKey = sorted(key)

answerArr = []
for i in range(len(key)):
    idx = sortedKey.index(key[i])
    answer = ""
    
    for j in range(len(newWordArr)):
        answer += newWordArr[j][idx]
    
    sortedKey[idx] = "0"

    answerArr.append(answer)

result = ""
for i in range(len(answerArr[0])):
    for j in range(len(answerArr)):
        result += answerArr[j][i]
        
print(result)

'''
HUMDING
EIAAHEBXOIFWEHRXONNAALRSUMNREDEXCTLFTVEXPEDARTAXNAARYIEX

ONCEUPONATIMEINALANDFARFARAWAYTHERELIVEDTHREEBEARSXXXXXX

BATBOY
EYDEMBLRTHANMEKTETOEEOTH

MEETMEBYTHEOLDOAKTREENTH
'''

