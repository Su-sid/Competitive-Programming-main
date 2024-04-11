class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        line_sweep_arr = [0] * (len(s)+1)       
        for start,end,direction in shifts:
            if direction==0:
                direction = -1
            line_sweep_arr[start] += direction
            line_sweep_arr[end+1] -= direction  # Shift back for the one following the end of the shift interval
        
        accumulated = 0                         # Accumulated number for increase/decrease
        res = []
        for i in range(len(s)):
            accumulated += line_sweep_arr[i]    # Accumulate
            chr_num = ord(s[i])-ord('a')        # Get the unicode of this chr 
            chr_num = (chr_num+accumulated)%26  # %26 to wrapping around
            res.append(chr(chr_num+ord('a')))   # Add the shifted chr to the result
        return ''.join(res)