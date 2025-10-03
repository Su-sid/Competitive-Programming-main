class Solution:
    def average(self, salary: List[int]) -> float:
        # sub_salary = sorted (salary)
        salary.sort()

        sub_salary = salary[1:-1]

        return sum(sub_salary)/len(sub_salary)