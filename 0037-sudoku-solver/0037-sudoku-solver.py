class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def backtrack():

            best_cell = None
            best_options = None

            # Find the empty cell with the fewest choices
            for r in range(9):
                for c in range(9):

                    if board[r][c] != '.':
                        continue

                    box = (r // 3) * 3 + (c // 3)

                    options = []

                    for num in "123456789":
                        if (num not in rows[r] and
                            num not in cols[c] and
                            num not in boxes[box]):
                            options.append(num)

                    # No possible number -> dead end
                    if not options:
                        return False

                    # Choose the cell with minimum options
                    if best_options is None or len(options) < len(best_options):
                        best_options = options
                        best_cell = (r, c)

                        # Can't get better than one option
                        if len(options) == 1:
                            break

                if best_options is not None and len(best_options) == 1:
                    break

            # No empty cells -> solved
            if best_cell is None:
                return True

            r, c = best_cell
            box = (r // 3) * 3 + (c // 3)

            for num in best_options:

                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if backtrack():
                    return True

                # Undo
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            return False

        backtrack()