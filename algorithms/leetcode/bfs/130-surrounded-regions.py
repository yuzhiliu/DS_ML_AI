class Solution(object):
    # BFS
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        if m <= 2 or n <= 2:
            return
        queue = collections.deque()
        queue.extend((i, 0) for i in range(m))
        queue.extend((i, n - 1) for i in range(m))
        queue.extend((0, j) for j in range(n))
        queue.extend((m - 1, j) for j in range(n))
        while queue:
            i, j = queue.popleft()
            if i >= 0 and i < m and j >= 0 and j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                queue.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
    # UF
