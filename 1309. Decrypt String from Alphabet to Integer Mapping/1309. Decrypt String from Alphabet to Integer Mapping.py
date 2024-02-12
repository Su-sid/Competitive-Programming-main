class Solution:
    def freqAlphabets(self, s='') -> str:
        mapping = {
            '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
            '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r',
            '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'
        }

        my_string = s[::-1]
        empty = ''
        i = 0

        while i < len(my_string):
            if my_string[i] == '#':
                # Extract the two characters before '#' and reverse them to match the mapping
                result = my_string[i+2] + my_string[i+1]
                empty += mapping.get(result)
                i += 3  # Skip the next two characters after '#'
            else:
                empty += mapping.get(my_string[i], "")
                i += 1

        return empty[::-1]  # Reverse the result string to maintain original order
