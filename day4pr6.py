def delchar(s, c):
    if len(c) == 1:
        result = ''.join(char for char in s if char != c)
        return result
    else:
        return s
input_string = input("Enter the string: ")
char_to_delete = input("Enter a character to be deleted: ")

result = delchar(input_string, char_to_delete)

print("String after the character is removed:", result)
