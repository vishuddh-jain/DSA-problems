'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''
# Using dictionary approach
from collections import Counter, deque
def firstUniqChar(s):

        q = deque()
        freq = {}

        for i, ch in enumerate(s):

            freq[ch] = freq.get(ch, 0) + 1
            # If 'a' exists, return its value.
            # Otherwise return 0.

            q.append((ch, i))

            while q and freq[q[0][0]] > 1:
                q.popleft()

        return q[0][1] if q else -1
    
print(firstUniqChar(s="loveleetcode"))

# Using "Counter" module 

def firstUniqChar(s):
        q = deque()
        freq = Counter(s)
        for i,ch in enumerate(s):
            
            q.append((ch, i))
            while q and freq[q[0][0]] > 1:
                q.popleft()
            
        return q[0][1] if q else -1