# This function finds the first occurence of needle string in haystack
def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Go through each index in haystack
        for i in range(len(haystack)):
            if (haystack[i : i + len(needle)] == needle):
                return i
        return -1