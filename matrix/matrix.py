class Matrix(list):

    def __init__(self, matrix_string: str) -> None:
        # First we split the matrix string into rows of strings
        # values separated by spaces
        rows = matrix_string.splitlines()

        # create a list of individual string values from each row
        # and cast the individual strings as integers
        self.values = [[[int(value)] for value in row.split()] for row in rows]

    def __setitem__(self, index: int, value: list) -> None:
        print("here")
        self.values[index] = value

    def __str__(self):
       return f"{[[row[index][0] for index in range(len(row))] for row in self.values]}"

    def row(self, row_number: int) -> list[int]:
        """
        Return a mutable list of a single row from the matrix.

        Use the matrix numbering convention of row 1 being the top row.
        """
        index = row_number - 1
        return self.values[index]

    def immutable_row(self, row_number: int) -> list[int]:
        """
        Return an immutable copy of a single row from the matrix.

        Use the matrix numbering convention of row 1 being the top row.
        """
        return self.row(row_number).copy()

    def column(self, column_number: int) -> list[int]:
        """
        Return a mutable list of a single column from the matrix.

        Use the matrix numbering convention of column 1 being the leftmost column.
        """
        index = column_number - 1

        col = [[]] * len(self.values)

        # Use list comprehension to create a list of the column values
        for row_number in range(0, len(self.values)):
            col[row_number] = self.values[row_number][index]
        return col

    def immutable_column(self, column_number: int) -> list[int]:
        """
        Return an immutable copy of single column from the matrix.

        Use the matrix numbering convention of column 1 being the leftmost column.
        """
        index = column_number - 1

        # Use list comprehension to create a list of the column values
        col = [row[index] for row in self.values]

        return col

# Test code for the challenge...
matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
print(matrix)
print(matrix.column(2))
matrix.column(2)[1] = 6
print(matrix.column(2))

def test_immutable_row():
    matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert matrix.immutable_row(2) == [4, 5, 6]
    matrix.immutable_row(2)[1] = 6
    assert matrix.immutable_row(2) == [4, 5, 6]


def test_immutable_col():
    matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert matrix.immutable_column(2) == [2, 5, 8]
    matrix.immutable_column(2)[1] = 6
    assert matrix.immutable_column(2) == [2, 5, 8]


def test_row():
    matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert matrix.row(2) == [4, 5, 6]
    matrix.row(2)[1] = 6
    assert matrix.row(2) == [4, 6, 6]


def test_col():
    matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert matrix.column(2) == [2, 5, 8]
    matrix.column(2)[1] = 6
    assert matrix.column(2) == [2, 6, 8]
