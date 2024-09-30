
   def roman_to_integer(s: str) -> int:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)

    for i in range(n):
        value = roman_values[s[i]]

        if i + 1 < n and roman_values[s[i + 1]] > value:
            total -= value
        else:
            total += value
    
    return total

print(roman_to_integer("III"))      
print(roman_to_integer("LVIII"))    
print(roman_to_integer("MCMXCIV"))  


