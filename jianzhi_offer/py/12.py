class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        self.board = board
        self.m, self.n = m, n

        for i in range(m):
            for j in range(n):
                if self.search(i, j, [], word):
                    return True
        
        return False

    def search(self, i, j, seen, word):
        if word == "":
            return True
        elif i<0 or i>=self.m or j<0 or j>=self.n or word[0] != self.board[i][j] or (i, j) in seen:
            return False
        else:
            return self.search(i-1, j, seen+[(i,j)], word[1:]) or self.search(i+1, j, seen+[(i,j)], word[1:]) or self.search(i, j-1, seen+[(i,j)], word[1:]) or self.search(i, j+1, seen+[(i,j)], word[1:])