def roman_to_int(s):
    total = 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(s)):
        if i > 0 and roman_values[s[i]] > roman_values[s[i - 1]]:
            total += roman_values[s[i]] - 2 * roman_values[s[i - 1]]
        else:
            total += roman_values[s[i]]

    return total

# Example usage:
roman = input("Enter a Roman numeral: ")
print("The integer value is:", roman_to_int(roman))
