class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = dict() # We store the compliments needed and the index of the number who has that compliment

        for i in range(len(nums)):
            compliment =  target - nums[i]
            if nums[i] in compliments.keys():
                return [compliments[nums[i]], i]
            
            compliments[compliment] = i
        
        return []