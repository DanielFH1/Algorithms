import sys
N = int(sys.stdin.readline())

words = set()
for i in range(N):
    words.add(sys.stdin.readline().strip())
    
words_list = list(words)
words_list.sort(key=lambda x: (len(x),x)) # 일회용 함수 : x가 들어오면 (길이,x)를 뱉어라

for word in words_list:
    print(word)