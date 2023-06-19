# 9개의 서로 다른 자연수
numList = []

for i in range(9):
    num = int(input())
    numList.append(num)
    
# 이들 중 최댓값 찾기
print(max(numList))
# 최댓값 몇 번째 수인지 찾기
print(numList.index(max(numList)) + 1)