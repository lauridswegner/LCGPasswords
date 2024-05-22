from lcg import LCGPseudoRandomizer

class PasswordGenerator:

    def __init__(self):
        self.chars: str = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers: str = "0123456789"
        self.specialChars: str = "!$%&"

        self.randomizer = LCGPseudoRandomizer()

    def generate_password(self, password_length:int, charsCheck=True, numbersCheck=True, specialCharsCheck=True):
        self.combination = []
        self.output = ""

        if charsCheck:
            self.combination.append(self.chars)
        if numbersCheck:
            self.combination.append(self.numbers)
        if specialCharsCheck:
            self.combination.append(self.specialChars)

        print(self.combination)

        for i in range(password_length):
            choice = self.randomizer.randomint(0, len(self.combination))
            self.output += self.randomizer.randomchoice(self.combination[choice])
        
        return self.output

#passgen = PasswordGenerator()
#test = passgen.generate_password(10, charsCheck=True, numbersCheck=True, specialCharsCheck=True)
#print(test)