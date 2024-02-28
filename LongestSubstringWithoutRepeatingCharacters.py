class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        longest = [1]
        for i in range(1, length):
            tempString = s[i]
            for j in range(i - 1, -1, -1):
                if s[j] not in tempString:
                    tempString += s[j]
                else:
                    break
            longest.append(max(len(tempString), longest[i - 1]))

        return longest[-1]
