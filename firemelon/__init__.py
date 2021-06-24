from random import choice, choices

from .nouns import nouns
from .adjectives import adjectives

separators = "; _,.:-!@#$%^&*=+'"

class Generator:
    @staticmethod
    def noun():
        return choice(nouns)

    @staticmethod
    def adjective():
        return choice(adjectives)

    @staticmethod
    def word():
        return choice([self.adjective(), self.noun()])

    @staticmethod
    def number(length=3):
        return "".join(
            map(
                str, 
                choices(
                    range(10), 
                    k=length
                )
            )
        )

    @staticmethod
    def sep():
        return choice(separators)

    def generate(self, complexity=4, sep=None, use_number=True):
        pattern = self.choose_pattern(complexity, use_number)
        password = []
        for i in range(complexity):
            password.extend([
                sep or self.sep(),
                pattern[i]
            ])
        return "".join(password[:-1])

    def choose_pattern(self, complexity, use_number):
        if complexity < 3:
            return [self.word(), self.noun]

        pattern = [self.word() for _ in range(self.complexity - 1)]
        pattern.insert(
            choice(range(complexity)),
            self.number(
                choice(range(3, complexity + 1))
            ) if use_number else self.word()
        )
        return pattern


passgen = Generator().generate