# Maximum Total Subarray Value 

nums = [2,5,8]
k = 2

max_numb = nums[0]
min_numb = nums[0]

for i in nums:
    if i > max_numb:
        max_numb = i
    if i < min_numb:
        min_numb = i 
    value = (max_numb - min_numb )*k

print(value)

###################################################################################

# 1732 Find the Highest Altitue

gain = [-5,1,0,5,-7]

cur = 0
maximum = 0

for i in gain :
    cur = cur + i
    if cur > maximum:
        maximum = cur
print(maximum) 

#######################################################################################