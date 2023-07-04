words = input().upper()
wordslist = list(set(words))
li = []
for i in wordslist:
    cnt = words.count(i)
    li.append(cnt)
if li.count(max(li)) > 1:
    print("?")
else:
    max_index = li.index(max(li))
    print(wordslist[max_index])