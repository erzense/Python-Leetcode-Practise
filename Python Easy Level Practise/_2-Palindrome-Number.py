def isPalindrome(number):
    palindrome = False
    number = str(number)
    control = number[::-1]
    if number == control:
        palindrome = True
        print("Your number is palindrome")
        
    else:
        palindrome = False
        print("Your number is not palindrome")
        
    print(palindrome)

number = input("Number:")
isPalindrome(number)


