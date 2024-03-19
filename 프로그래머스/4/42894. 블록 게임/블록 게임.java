class Solution {
    private int n;
    private int[][] board;

    public int solution(int[][] board) {
        this.board = board;
        n = board.length;
        int answer = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0) continue;

                if (isA(i, j)) {
                    if (drop(i + 1, j + 1, board[i][j]) && drop(i + 1, j + 2, board[i][j])) {
                        remove(i, j, i + 1, j, i + 1, j + 1, i + 1, j + 2);
                        j = -1;
                        answer++;
                    }
                } else if (isB(i, j)) {
                    if (drop(i + 2, j - 1, board[i][j])) {
                        remove(i, j, i + 1, j, i + 2, j, i + 2, j - 1);
                        j = -1;
                        answer++;
                    }
                } else if (isC(i, j)) {
                    if (drop(i + 2, j + 1, board[i][j])) {
                        remove(i, j, i + 1, j, i + 2, j, i + 2, j + 1);
                        j = -1;
                        answer++;
                    }
                } else if (isD(i, j)) {
                    if (drop(i + 1, j - 1, board[i][j]) && drop(i + 1, j - 2, board[i][j])) {
                        remove(i, j, i + 1, j, i + 1, j - 1, i + 1, j - 2);
                        j = -1;
                        answer++;
                    }
                } else if (isE(i, j)) {
                    if (drop(i + 1, j - 1, board[i][j]) && drop(i + 1, j + 1, board[i][j])) {
                        remove(i, j, i + 1, j, i + 1, j - 1, i + 1, j + 1);
                        j = -1;
                        answer++;
                    }
                }
            }
        }
        return answer;
    }

    private void remove(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
        board[x1][y1] = 0;
        board[x2][y2] = 0;
        board[x3][y3] = 0;
        board[x4][y4] = 0;
    }

    private boolean drop(int x, int y, int value) {
        for (int i = 0; i < x; i++) {
            if (board[i][y] == 0) continue;
            if (board[i][y] != value) return false;
        }
        return true;
    }

    private boolean isA(int x, int y) {
        int num = board[x][y];
        if (y + 2 >= n || x + 1 >= n) return false;
        return board[x + 1][y] == num && board[x + 1][y + 1] == num && board[x + 1][y + 2] == num;
    }

    private boolean isB(int x, int y) {
        int num = board[x][y];
        if (x + 2 >= n || y - 1 < 0) return false;
        return board[x + 1][y] == num && board[x + 2][y] == num && board[x + 2][y - 1] == num;
    }

    private boolean isC(int x, int y) {
        int num = board[x][y];
        if (x + 2 >= n || y + 1 >= n) return false;
        return board[x + 1][y] == num && board[x + 2][y] == num && board[x + 2][y + 1] == num;
    }

    private boolean isD(int x, int y) {
        int num = board[x][y];
        if (x + 1 >= n || y - 2 < 0) return false;
        return board[x + 1][y] == num && board[x + 1][y - 1] == num && board[x + 1][y - 2] == num;
    }

    private boolean isE(int x, int y) {
        int num = board[x][y];
        if (x + 1 >= n || y - 1 < 0 || y + 1 >= n) return false;
        return board[x + 1][y] == num && board[x + 1][y + 1] == num && board[x + 1][y - 1] == num;
    }
}
