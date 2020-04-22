from problem import Problem
import os.path as path


class NameScores(Problem, name="Names Scores", expected=871198282):
    """
    NOTE: I did some regex replace to convert the names file so each name is on its own line
    """
    @classmethod
    def load_names(cls, file=path.join(path.dirname(__file__), '../files/p022_names.txt')):
        with open(file) as r:
            return sorted(map(str.strip, r.readlines()))

    @classmethod
    def calculate_name_score(cls, name):
        return sum(ord(n) - 64 for n in name)

    @Problem.solution()
    def solution(self):
        names = self.load_names()

        return sum((i+1) * self.calculate_name_score(name) for i, name in enumerate(names))


