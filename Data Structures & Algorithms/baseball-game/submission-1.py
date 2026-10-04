from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum = 0
        for op in operations:
            if op not in ["+", "C", "D"]:
                op = int(op)
                record.append(op)
                sum = sum + op
            elif op == "+":
                sum += (record[-1] + record[-2])
                record.append(record[-1] + record[-2])
            elif op == "C":
                sum -= record[-1]
                record.pop()
            elif op == "D":
                sum += 2 * record[-1]
                record.append(2 * record[-1])

        return sum