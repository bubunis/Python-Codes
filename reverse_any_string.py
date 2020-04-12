value = input("Insert Your String: ")
value = str(value)
#print(len(value))

def reverse(s):
	c = ""
	for x in range(len(s), 0, -1):
		c += s[x-1]
	return (c)

print(reverse(value))

### Output ###
#Insert Your String: 12345 Test
#tseT 54321     
