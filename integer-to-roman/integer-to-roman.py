class Solution:
    def intToRoman(self, num: int) -> str:
        symbols =  [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),\
                    (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"),\
                    (4, "IV"), (1, "I")]
        result = ""
        
        if num == 0: 
            return 0 
        
        #2000 - 
        
        for value, symbol in symbols: 
            if num == 0: 
                break 
            count, num = divmod(num, value) 
            result += count * symbol
            
        return result