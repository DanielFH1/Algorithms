import sys 

arr = [sys.stdin.readline().strip() for _ in range(3)]
target_n = 0

for i in range(3):
    if arr[i] not in ['Fizz','Buzz','FizzBuzz']: # 숫자라는 뜻뜻
        target_n = int(arr[i]) + (3-i)
        break 
    
if target_n% 15==0:
    print("FizzBuzz")
elif target_n % 3 ==0:
    print("Fizz")
elif target_n % 5 ==0:
    print("Buzz")
else:
    print(target_n)