# introductory messages
print("Greetings. This is a GPA calculator for the University of Texas.")
print("Having your transcript with you is highly recommended.")
print("Tip: The first number of a class is how many credit hours the class is worth!\n"
      "For example: CS 312 has a 3 in front, so it is worth 3 credit hours.")


# saves the credit hours used for input. is in bounds (above 0 & and an integer)
def ch_in_bounds():
    while True:
        try:
            credit_hours = int(input("How many credit hours is this class worth?\n"))
        except ValueError:
            # if it is NOT a int, then we need to get input again through continue and let user know
            print("\nValue must be an integer. Please try again.")
            continue
        # found value that is integer
        if credit_hours <= 0:
            print("\nA class cannot be worth 0 or negative credit hours. Please try again.")
        else:
            # print("credit hours saved:", credit_hours)
            return credit_hours


# asks for letter grade from user, then returns weighted grade points
def grade_point_interpreter():
    while True:
        grade = input("What grade did you earn in this class? Enter in format like this: D-.\n")
        # if it is a String, then it must be a valid letter
        grade = grade.upper()
        if 'A' == grade:
            return 4
        elif 'A-' == grade:
            return 3.67
        elif 'B+' == grade:
            return 3.33
        elif 'B' == grade:
            return 3
        elif 'B-' == grade:
            return 2.67
        elif 'C+' == grade:
            return 2.33
        elif 'C' == grade:
            return 2
        elif 'C-' == grade:
            return 1.67
        elif 'D+' == grade:
            return 1.33
        elif 'D' == grade:
            return 1
        elif 'D-' == grade:
            return 0.67
        elif 'F' == grade:
            return 0
        # if none of these, then invalid
        print("This input is invalid. Enter your letter grade for this class like this: B- or F")


def gather_info():
    data = [ch_in_bounds(), grade_point_interpreter()]
    qp = data[0] * data[1]
    print(data)
    print(qp)
    while True:
        decision = input("Would you like to add another class? Type any key for yes. N for no.")
        # if n then no, and we will stop adding classes and calculate
        if decision == 'N' or decision == 'n':
            # final calculation goes here
            gpa = round(qp / data[0], 4)
            print("\n\nYour GPA at UT is: ", gpa)
            break
        # anything else, we keep gathering information. we add it into this array
        ch_temp = ch_in_bounds()
        gp_temp = grade_point_interpreter()
        data[0] += ch_temp  # credit hour total
        data[1] += gp_temp  # actual grade points earned
        qp += ch_temp * gp_temp
        print(qp)
        print(data)


gather_info()


