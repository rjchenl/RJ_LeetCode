# Given an array of integers nums and an integer target, return indices of the t
# wo numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 104
#  -109 <= nums[i] <= 109
#  -109 <= target <= 109
#  Only one valid answer exists. 
#  
# 
#  
# Follow-up: Can you come up with an algorithm that is less than O(n2) time comp
# lexity? Related Topics Array Hash Table 
#  👍 23627 👎 788


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # print('====== test start =======')
        if 2 <= len(nums) <= 10000 and -10 ** 9 <= target <= 10 ** 9:

            i = 0
            ans_list = []
            for index, number in enumerate(nums):
                i = index + 1
                while i < len(nums):
                    if -10 ** 9 <= nums[i] <= 10 ** 9:
                        result = nums[index] + nums[i]
                        # print(f'index : {index},i:{i}, result:{result}')
                        if result == target:
                            ans_list.append(index)
                            ans_list.append(i)
                        i = i + 1
                        # print(ans_list)
            return ans_list
            # print('====== test end =======')


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
ans = solution.twoSum([3,2,4], 6)
print(f'ans:{ans}')
