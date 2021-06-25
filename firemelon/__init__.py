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
        return choice([Generator.adjective(), Generator.noun()])

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
    def sep(seps=None):
        return choice(seps or separators)

    def generate(self, complexity=4, sep=None, use_number=True):
        pattern = self.choose_pattern(complexity, use_number)
        password = []
        seps = None
        if isinstance(sep, (list, tuple)):
            seps = sep
        for i in range(complexity):
            password.extend([
                sep or self.sep(seps),
                pattern[i]
            ])
        return "".join(password[:-1])

    def variance(self, complexity=4, sep=None, use_number=True):
        word_variance = len(nouns) + len(adjectives)
        seps = [sep] if isinstance(sep, str) else (sep or separators)
        sep_variance = len(seps)
        if use_number and complexity > 2:
            number_variance = sum(10 ** x for x in range(3, complexity + 1))
            return (word_variance * sep_variance) ** (complexity - 1) * number_variance * complexity
        
        return sep_variance ** (complexity - 1) * word_variance ** complexity

    def choose_pattern(self, complexity, use_number):
        if complexity < 3:
            return [self.word(), self.noun()][:complexity]

        pattern = [self.word() for _ in range(complexity - 1)]
        pattern.insert(
            choice(range(complexity)),
            self.number(
                choice(range(3, complexity + 1))
            ) if use_number else self.word()
        )
        return pattern


passgen = Generator().generate