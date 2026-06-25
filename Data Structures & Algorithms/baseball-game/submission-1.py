class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == "+":
                if record :
                    num = record[-1] + record[-2]
                    record.append(num)
            elif operations[i] == 'D':
                if record :
                    num = 2*record[-1]
                    record.append(num)
            elif operations[i] == "C":
                if record :
                    record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)

