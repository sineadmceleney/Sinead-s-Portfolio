#Name: Mallory Grider
#Modified by:
#Date: July 27, 2017
"""Purpose: starter code for Caesar Shift Cipher program. The program both
	encrypts and decrypts plaintext."""
"""History:
	The caesar cipher is a symmetric key cipher that operates on the premise that
you rotate the alphabet a set number of characters creating a key. For
instance:
    A == Z
    B == A
    C == B
    ...
    Z == Y
The cipher is very insecure as when you find the offset you have found the
key. Running it through 26 variations will crack it easily. It also can be
cracked by letter frequencies.

The cipher was invented by Julius Caesar to encrypt military messages. Caesar used a
shift of 3.

It was secure most likely when Julius Caesar invented it but never again
(note that most of Julius Caesar's enemies were illerate).

QUICK CODE NOTE:
		YOU WILL NEED THE FOLLOWING BUILT-IN FUNCTIONS:
			1. ord(): returns the ASCII value of a character
			2. chr(): takes in an ASCII value and returns the character
			3. isalpha(): detects if input is a character in the alphabet
			4. find(): """

#A function to encode plain text
def encode(str, int):
	#This takes the letters of the word and puts them into a list
	plainlist = list(plainText)
	#This defines the cipherText variable
	cipherText = ""
	#A for loop that loops through the letters in the word
	for letter in plainlist:
		#Converts the letter to an ASC value, then adds the shift number to that ASC value, then translates it back to a letter
		ASCvalue = ord(letter)
		ASCvalue = ASCvalue + shift_num
		cipherLetter = chr(ASCvalue)
		#adds the newly encoded letter to a string called cipherText
		cipherText = cipherText + cipherLetter
	#prints the cipherText
	print("Your ciphertext is: ")
	print(cipherText)



#Brute force method; checks against every possible shift (does not have access to a key)
def decode(cipherText):
	#makes a list of the letters in the cipher
	cipherList = list(cipherText)
	for shiftAttempt in (0, 26):
		plainText = ""
		for cipherLetter in cipherList:
			ASCvalue = ord(cipherLetter)
			ASCvalue = ASCvalue + shiftAttempt
			plainLetter = chr(ASCvalue)
			plainText = plainText + plainLetter
		print("Shift " + str(shiftAttempt) + ":")
		print(plainText)


	#Your code

user_input = str(input("Would you like to encode or decode a message?"))
plainText = ""
shift_num = 0
ASCvalue = 0



if (user_input == "encode"):
	plainText = input("What is your message?")
	shift_num = int(input("What would you like to shift the message by?"))
	encode(plainText, shift_num)
elif (user_input == "decode"):
	cipherText = input("What is your ciphertext?")
	decode(cipherText)
else:
	print("Please input 'encode' or 'decode'")
