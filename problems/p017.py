from problem import Problem


class NumberLetterCount(Problem, name="Number letter counts", expected=21124):

    num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                 90: 'Ninety', 100: 'Hundred', 1000: "Thousand"}

    @classmethod
    def number_to_words(cls, n):
        words = ""

        # if the number is contained in our mapping then we return it
        # We only do this for numbers under 100 or else we would get 100 = hundred instead of one hundred
        if n in cls.num2words and n < 100:
            return cls.num2words[n]

        # we look at the 1000th and 100th place
        for step in [1000, 100]:
            d, r = divmod(n, step)

            # if the number is not divisible by step we just continue
            if d == 0:
                continue

            # otherwise we add the words to our output and discard that place from the number
            else:
                words += cls.num2words[d] + cls.num2words[step]
                n = r

        # if there is still anything left after dealing with 100s and 1000s then we must deal with 10s and 1s
        if n != 0:
            # if we have already added anything to our output then we need and
            if len(words) != 0:
                words += "and"

            # if the number is already mapped we just add that
            if n in cls.num2words:
                words += cls.num2words[n]
            else:
                d, r = divmod(n, 10)
                # converts a number from 99 - 20 to words
                words += cls.num2words[d*10] + cls.num2words[r]

        return words

    @Problem.solution()
    def mapping(self):
        return sum(map(len, (self.number_to_words(n) for n in range(1, 1001))))


