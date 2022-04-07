from cs50 import get_string

countL = 0
countW = 1
countS = 0

# Get input from user
text = get_string("Text: ")
textLength = len(text)


for i in range(textLength):

    # For letter count
    if (text[i].isalpha()):
        countL += 1

    # For word count
    if (text[i].isspace()):
        countW += 1

    # For sentence count
    if (text[i] == '.' or text[i] == '!' or text[i] == '?'):
        countS += 1

L = 100 * (countL / countW)
S = 100 * (countS / countW)
grade = round(0.0588 * L - 0.296 * S - 15.8)

if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print("Grade", grade)