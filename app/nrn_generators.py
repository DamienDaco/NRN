"""
National Register Number generator code for Belgium.
"""
import random


class NrnBelgiumGenerateFromDate:
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender
        self.yearLast2Digits = self.year[2:]
        self.numberOfBirth = '1'

        """ Generate a random number of birth.
        This number helps distinguish people born the same day.
        Male = odd numbers between 1 and 997.
        Female = even numbers between 2 and 998.
        """
        if self.gender.lower() == 'male':
            self.numberOfBirth = random.randrange(1, 999, 2)

        elif self.gender.lower() == 'female':
            self.numberOfBirth = random.randrange(2, 1000, 2)

        self.firstBlock = self.yearLast2Digits + self.month + self.day + str(self.numberOfBirth)

        # If born after 2000, prepend number 2:
        if int(self.year) >= 2000:
            self.firstBlock = '2' + self.firstBlock

        # Control number: Modulo firstblock with 97. Substract result from 97:
        self.controlNumberToString = str(97 - (int(self.firstBlock) % 97))
        # Ensure control number is always 2 digits long by using an f-string with 00 mask (Prepend zeroes if necessary)
        self.controlNumberToString = f"{int(self.controlNumberToString):02d}"

        # Ensure number of birth is always 3 digits long by using an f-string with 000 mask (Prepend zeroes if necessary)
        self.numberOfBirth = f"{int(self.numberOfBirth):03d}"

        self.nrn = self.yearLast2Digits + '.' + self.month + '.' +  self.day + '-' + str(self.numberOfBirth) + '.' + self.controlNumberToString


class NrnBelgiumValidator:
    def __init__(self, string):

        self.rawNumber = string
        # Remove . and - characters using a list comprehension:
        self.cleanNumber = "".join([x for x in self.rawNumber if x != '.' if x != '-'])

        if len(self.cleanNumber) == 11:

            self.firstBlock = self.cleanNumber[:9]
            self.lastBlock = self.cleanNumber[9:11]
            self.computeControlNumber = 97 - (int(self.firstBlock) % 97)

            if self.computeControlNumber == int(self.lastBlock):
                print("Number passed validation test.")
                self.isValid = True
            else:
                print("Number failed validation test.")
                self.isValid = False

        else:
            print("Invalid number length.")
            self.isValid = False
