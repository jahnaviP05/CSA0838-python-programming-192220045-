class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))  
        unique_nums.sort(reverse=True)  
        if len(unique_nums) >= 3:
            return unique_nums[2]  
        else:
            return unique_nums[0]  
solution = Solution()
print(solution.thirdMax([3, 2, 1]))  
print(solution.thirdMax([1, 2]))     
print(solution.thirdMax([2, 2, 3, 1]))
