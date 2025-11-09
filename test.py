s = input("Enter a string: ")

diff = ord('a') - ord('A')

first = chr(ord(s[0])-diff)
middle = s[len(s)//2]
last = chr(ord(s[-1])-diff)

result = first + middle + last
print(result)

