
text = input("Enter a string: ")

# Forward direction
print("\nCharacters in Forward Direction:")
i = 0
while i < len(text):
    print(text[i], end='__')
    i += 1

# Backward direction
print("\nCharacters in Backward Direction:")
i = len(text) - 1
while i >= 0:
    print(text[i], end='__')
    i -= 1
