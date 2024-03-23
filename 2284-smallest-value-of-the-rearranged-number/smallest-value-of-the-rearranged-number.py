class Solution:
    def smallestNumber(self, num: int) -> int:
        # Convert the integer to a list of digits
        num_str = str(num)
        num_list = list(num_str)
        if num==0: 
            return 0

        # Check if the number is negative
        if num_list[0] == '-':
            # Sort the digits in ascending order (excluding the negative sign)
            sorted_digits = sorted(num_list[1::],reverse=True)
            # Reconstruct the smallest number
            result = "-" + "".join(sorted_digits)
        else:
            # Sort the digits in descending order
            sorted_digits = sorted(num_list)
            i=1
            while (sorted_digits[0]=='0'):  
                
                sorted_digits[0]=sorted_digits[i] 
                sorted_digits[i]=0
                i+=1
            # Reconstruct the smallest number
            result = "".join(map(str,sorted_digits))

        return int(result)