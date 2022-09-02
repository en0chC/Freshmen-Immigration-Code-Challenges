# This function returns indeces of two numbers that add up to variable target
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Go through each possible combination of elements in the list by
        # taking each element from start to second last element
        for i in range(len(nums) - 1):
            # Then taking each element from one after current to last element
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]