from problem import Problem
from datetime import datetime, timedelta


class CountingSundays(Problem, name="Counting Sundays", expected=171):
    @Problem.solution()
    def with_datetime(self):
        """
        We just loop through each day using datetime and check if its a sunday and the first of the month
        """
        start = datetime(day=1, month=1, year=1901)
        end = datetime(day=1, month=1, year=2001)
        sundays = 0
        while start != end:
            if start.weekday() == 6 and start.day == 1:
                sundays += 1
            start = start + timedelta(days=1)

        return sundays
