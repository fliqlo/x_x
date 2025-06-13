def atbash(text):
    result = ''
    for char in text:
        if char.isalpha():
            # Convert to uppercase and find the corresponding Atbash character
            offset = ord(char.upper()) - ord('A')
            result += chr(ord('Z') - offset)
        else:
            result += char
    return result

# Example usage
print(atbash("igit"))  # Output: zkkov
