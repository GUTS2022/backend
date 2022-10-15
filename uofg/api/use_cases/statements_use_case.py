from ..models.statement import Statement
from typing import List

class StatementsUseCase:
    def __init__(self):
        self.statements: List[Statement] = []
        self.load_statements()

    def load_statements(self):
        text = ""
        with open("./uofg/assets/data/student_statements.txt", 'r') as txt:
            text = txt.read()

        text = text.split("\n")

        ids = []
        names = []
        tests = []
        for i in range(len(text)):
            if i%5 == 1:
                ids.append(text[i][16:])
            elif i%5 == 2:
                names.append(text[i][6:])
            elif i%5 == 3:
                tests.append(text[i][11:])

        for i in range(len(ids)):
            statement = Statement(
                ids[i],
                names[i],
                tests[i]
            )
            self.statements.append(statement)

    def get_statement_by_id(self, student_id):
        for statement in self.statements:
            print(statement)
            if statement.student_id == student_id:
                return statement

        return "Statement not found"