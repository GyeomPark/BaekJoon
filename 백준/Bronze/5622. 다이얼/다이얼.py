
word = input()
call = list(['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'])
time = 0

for i in range(len(word)):
    for t in range(len(call)):
        if (word[i] in call[t]) == True:
            time += (t + 3)

print(time)