package ys.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
    2240 자두나무
 */
public class Boj2240 {

    static int T;
    static int W;
    static int[][][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        dp = new int[T + 1][W + 2][3];

        for (int i = 1; i <= T; i++) {
            int tree = Integer.parseInt(br.readLine());
            for (int j = 1; j <= W + 1; j++) {
                if (tree == 1) {
                    dp[i][j][1] = Math.max(dp[i - 1][j][1], dp[i - 1][j - 1][2]) + 1;
                    dp[i][j][2] = Math.max(dp[i - 1][j][2], dp[i - 1][j - 1][1]);
                } else {
                    if (i == 1 && j == 1) continue;
                    dp[i][j][1] = Math.max(dp[i - 1][j][1], dp[i - 1][j - 1][2]);
                    dp[i][j][2] = Math.max(dp[i - 1][j][2], dp[i - 1][j - 1][1]) + 1;
                }
            }
        }

        int result = 0;
        for (int i = 1; i <= W + 1; i++) {
            result = Math.max(result, Math.max(dp[T][i][1], dp[T][i][2]));
        }
        System.out.println(result);
    }
}
