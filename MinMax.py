//5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate m essage and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

great = None
oh_no = None
while True:
    num = input("Enter a number: ")
    if num == "21": break
    try:
        num = int(num)
        if great is None or great < num: great = num
        if oh_no is None or oh_no > num: oh_no = num
    except:
        print("Invalid input")
        continue
print ("Maximum is", great);
print ("Minimum is", oh_no);

//lab id : https://www.py4e.com/tools/pythonauto/?PHPSESSID=2230f42900e05037dfcc281ca9df7cb2
