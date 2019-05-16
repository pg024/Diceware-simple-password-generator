from sys import argv
import random
import linecache

#receives the wordlist as argument
script, filename = argv


#the function takes an empty list, randomly chooses 'ele' words from the wordlist
def generator(filename, ele, lines):
	psw = []
	for i in range(0, ele):
		seed = random.randint(1, lines)
		word = linecache.getline(filename, seed).rstrip('\n')
		psw.append(word)
	return psw
	
		
print("\n")
print("Hello! This is a psw generator\n")


print("How many elements? The minimum reccomended is 6.")
ele = int(input("> "))

#counting filename's lines
with open(filename) as foo:
    lines = len(foo.readlines())

#generating passphrase function
psw = generator(filename, ele, lines)


entropy = 12.9 * ele
print("\n")
print(f"The passphrase has an entropy of roughly {entropy} bits.")

if entropy < 28:
	print("It is very weak, it is strongly suggested to enforce it.")
elif entropy > 28 and entropy < 58:
	print("It is somehow weak to medium, better to enforce it.")
elif entropy > 59 and entropy < 127:
	print("It is strong.")
else:
	print("It's very strong, strong enough until 2050.")

print("\n")
print("The new generated passphrase therefor is:\n")	
print('\x1b[1;37;42m' +  ' '.join(str(y) for y in psw) + '\x1b[0m')
print("\n")


