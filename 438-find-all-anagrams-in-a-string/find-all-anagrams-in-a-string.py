class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Frequency dictionary for p and for the current window in s
        p_freq = Counter(p)
        window_freq = Counter(s[:len(p)-1])
        
        # List to store the starting indices of anagrams of p in s
        result = []
        
        # Iterate through s with a window of size len(p)
        for i in range(len(p) - 1, len(s)):
            # Add the new character to the window
            window_freq[s[i]] += 1
            
            # Check if the window frequency matches p's frequency
            if window_freq == p_freq:
                result.append(i - len(p) + 1)
            
            # Remove the oldest character from the window
            window_freq[s[i - len(p) + 1]] -= 1
            if window_freq[s[i - len(p) + 1]] == 0:
                del window_freq[s[i - len(p) + 1]]
        
        return result


# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         k= len(p) #length p
#         n= len(s) #length of s ---- 10
#         p_dict= {}
#         # win_dict= {}
#         for i in p:
#             if i in p_dict:
#                 p_dict[i]+=1
#             else:
#                 p_dict[i]=1
#         # print(p_dict)
#         total=list()
#         for i in range(k-1,n):  #---i== 3 e, 4 b, 5 a, 6 b, 7 a, 8 c,  9 d,
#             start= i-k   #s[i-k]
#             # window_size=s[start+1:i+1]
#             window_size=s[start+1:i+1]
#             print(window_size) #window_size=s[:i+1]
#             win_dict= {}
#             for i in window_size:
#                 if i in win_dict:
#                     win_dict[i]+=1
#                 else:
#                     win_dict[i]=1

#             if p_dict== win_dict:
#                 total.append(start+1)
#         return total
# from collections import Counter
