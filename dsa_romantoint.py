#Given a roman numeral, convert it to an integer.

class Solution:  
    def romanToInt(self, s: str) -> int:  
        
        roman_numerals = {  
            'I': 1,  
            'V': 5,  
            'X': 10,  
            'L': 50,  
            'C': 100,  
            'D': 500,  
            'M': 1000  
        }  
        
        total = 0  
        length = len(s)  
        
        for i in range(length):  
            
            if i < length - 1 and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:  
                total -= roman_numerals[s[i]]  
            else:  
                total += roman_numerals[s[i]]  
        
        return total  