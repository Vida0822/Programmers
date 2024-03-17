import java.util.*;

class Solution {
    public static int n, m;

    public boolean solution(int[][] key, int[][] lock) {
        n = lock.length;
        m = key.length;

        // 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
        int[][] newLock = new int[n * 3][n * 3];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                newLock[i + n][j + n] = lock[i][j];
            }
        }

        for (int i = 0; i < 4; i++) {
            // 회전
            key = rotation(key);

            // 이동
            for (int j = 0; j < n * 2; j++) {
                for (int k = 0; k < n * 2; k++) {
                    int[][] keyAt = move(j, k, key);
                    if (check(keyAt, newLock))
                        return true;
                }
            }
        }
        return false;
    }

    public int[][] rotation(int[][] key) {
        int[][] newKey = new int[m][m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                newKey[j][m - 1 - i] = key[i][j];
            }
        }
        return newKey;
    }

    public int[][] move(int nx, int ny, int[][] key) {
        int[][] keyAt = new int[n * 3][n * 3];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                keyAt[nx + i][ny + j] = key[i][j];
            }
        }
        return keyAt;
    }

    public boolean check(int[][] keyAt, int[][] lock) {
        for (int i = n; i < n * 2; i++) {
            for (int j = n; j < n * 2; j++) {
                if (lock[i][j] + keyAt[i][j] != 1)
                    return false;
            }
        }
        return true;
    }
}
