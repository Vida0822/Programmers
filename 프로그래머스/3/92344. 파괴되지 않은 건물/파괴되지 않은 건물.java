class Solution {
    public int solution(int[][] board, int[][] skill) {
        int row = board.length;
        int col = board[0].length;
        int[][] damage = new int[row+1][col+1]; // 공격 좌표 저장
        // skill 계산
        for (int[] ints : skill) {
            int power = ints[5];
            if (ints[0] == 1) {
                power = -power;
            }
            //skill[i][1]:x1, skill[i][2]:y1, skill[i][3]:x2, skill[i][4]:y2
            damage[ints[1]][ints[2]] += power;
            damage[ints[1]][ints[4] + 1] -= power;
            damage[ints[3] + 1][ints[2]] -= power;
            damage[ints[3] + 1][ints[4] + 1] += power;
        }

        // 누적합 계산
        int[][] sum = new int[row+1][col+1];
        // 가로로
        for(int i=0; i<row+1; i++) {
            sum[i][0] = damage[i][0];
            for(int j=1; j<col+1; j++) {
                sum[i][j] = damage[i][j] + sum[i][j - 1];
            }
        }
        // 세로로
        for(int j=0; j<col+1; j++) {
            for(int i=1; i<row+1; i++){
                sum[i][j] += sum[i-1][j];
            }
        }

        // 누적합(총 데미지)과 원래 상태 더하기
        int answer = 0;
        for(int i=0; i<row; i++) {
            for (int j=0; j<col; j++) {
                if(board[i][j] + sum[i][j] > 0) {
                    answer++;
                }
            }
        }
        return answer;
    }
}