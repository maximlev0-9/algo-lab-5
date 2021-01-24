class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_max_length = 0
        max_length = 0
        current_chars = []
        for i in s:
            print(current_chars)
            if i in current_chars:
                max_length = max(max_length, current_max_length)
                del current_chars[0:current_chars.index(i)+1]
                current_chars.append(i)
                current_max_length = len(current_chars)
            else:
                current_chars.append(i)
                current_max_length+=1
        
        max_length = max(max_length, current_max_length)
        print(current_chars)
        return max_length


print(Solution().lengthOfLongestSubstring("aabaab!bb"))

