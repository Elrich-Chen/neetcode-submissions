class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r_idx, row in enumerate(board):
            for c_idx, col in enumerate(row):
                if col == '.':
                    continue
                elif col in rows[r_idx] or col in cols[c_idx] or col in square[3*(r_idx//3) + c_idx//3]:
                    return False
                else:
                    rows[r_idx].add(col)
                    cols[c_idx].add(col)
                    square[3*(r_idx//3) + c_idx//3].add(col)
        
        return True