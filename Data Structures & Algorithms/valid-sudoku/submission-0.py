class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                b = (r // 3) * 3 + (c // 3)   # which box (0-8)

                # your turn: check rows[r], cols[c], boxes[b]

                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)
                # if val is already in any → invalid
                # otherwise → add it to all three

        return True