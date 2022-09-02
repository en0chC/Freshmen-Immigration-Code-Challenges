# This function reverses a string given as an array of characters
def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Go through each element from the beginning to middle of the list
        for i in range(len(s) // 2):
            # Swap the current element with element at the reversed index
            temp = s[len(s) - (i + 1)]
            s[len(s) - (i + 1)] = s[i]
            s[i] = temp