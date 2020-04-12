import sys
import os

def str_lst(s):
    nums = list(s.split(" "))
    for j in range(0, len(nums)):
        nums[j] = int(nums[j])
    return nums

val = input('Enter a list numbers or elements separated with space: ')

act_list = str_lst(val)
print('The Largest number in List: ', max(act_list))
larg = max(act_list)

count = 0
for x in range(0, len(act_list)):
    if larg == act_list[x]:
        count += 1

print('Total no of occurance: ', count)

#=== output ====

#Enter a list numbers or elements separated with space: 3 4 22 11 3 22
#The Largest number in List:  22
#Total no of occurance:  2
