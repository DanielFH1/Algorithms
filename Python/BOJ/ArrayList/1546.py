n = int(input()) # 과목갯수 n에 
mylist = list(map(int, input().split()))# my_list 에 성적
myMax = max(mylist)# myMax 에 최댓값
sum = sum(mylist)# sum에 총합
print(sum * 100 / myMax / n)# 새 평균(수학으로 간소화)