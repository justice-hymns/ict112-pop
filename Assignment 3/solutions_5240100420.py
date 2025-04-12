#QUESTION 1
s = "Programming"
reversed_s = s[::-1]
print("Reversed string:", reversed_s)

#QUESTION 2
full_name = input("Enter your full name: ")
initials = ".".join(word[0].upper() for word in full_name.split())
print("Initials:", initials + ".")

#QUESTION 3
s = input("Enter a string: ")
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#QUESTION 4
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)

#QUESTION 5
text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print("Modified string:", modified_text)