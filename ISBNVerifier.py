def parseISBN(isbn):
    digits = ""

    for character in isbn:
        if character != '-':
            if character == "X":
                digits += "10"
            else:
                digits += character

    return digits

def isISBN(digits):
    if len(digits) < 10 or len(digits) > 11:
        return False
    elif len(digits) == 11:
        if digits[len(digits)-2:len(digits)] != "10":
            return False

    if (int(digits[0]) * 10 + int(digits[1]) * 9 + int(digits[2]) * 8 + int(digits[3]) * 7 + int(digits[4]) * 6 + int(digits[5]) * 5 + int(digits[6]) * 4 + int(digits[7]) * 3 + int(digits[8]) * 2 + int(digits[9:len(digits)]) * 1) % 11 == 0:
        return True
    return False


def main():  # define main function
    print(isISBN(parseISBN('3-598-21508-8')))


if __name__ == '__main__':
    main()  # call main() function
