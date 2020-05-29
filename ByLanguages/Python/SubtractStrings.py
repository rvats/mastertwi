# Given two strings str1 and str2 where str2 is a subset of str1
# write code to subtract str2 from str1 which should return string with characters in same order as that were in string 1 and are not present in str2
# e.g. if str1 = "Hello World" and str2 = "Helo Wrd" then the result will be "lol"
# Additional Notes Remember Strings are immutable in Python, which means you cannot change an existing string. Review Memory Impact

str1 = "Hello World"
str2 = "Helo Wrd"

def subtract_string(str1, str2):
    result = str1
    for char1 in str2:
        idx = result.index(char1)
        print(char1 + " " + str(idx))
        result = result[:idx] +  result[idx+1:] 
    return result

print(subtract_string(str1, str2))