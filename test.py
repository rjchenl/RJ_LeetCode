# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
print('====== test start =======')
nums = [3, 2, 4]
target = 6
i = 0
ans_list = []
for index, number in enumerate(nums):
    i = index + 1
    while i < len(nums):
        result = nums[index] + nums[i]
        print(f'index : {index},i:{i}, result:{result}')
        if result == target:
            ans_list.append(index)
            ans_list.append(i)
        i = i + 1
print(ans_list)

print('====== test end =======')
