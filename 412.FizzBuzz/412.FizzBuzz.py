class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        finalAnswer = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                finalAnswer.append("FizzBuzz")
                continue
            if i % 3 == 0:
                finalAnswer.append("Fizz")
                continue
            if i % 5 == 0:
                finalAnswer.append("Buzz")
                continue
            else:
                finalAnswer.append(str(i))

        return finalAnswer
