package ys.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
    점화식을 찾지 못해서 블로그 참고..
 */
public class Boj2156 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // init
        int n = Integer.parseInt(br.readLine());
        int[] wines = new int[n+1];

        // 포도주를 안마시는 경우, 1번 연속 마신 경우 , 2번 연속 마신 경우 나눠서 2차원 배열 생성
        int[][] dp = new int[n+1][3];

        for (int i = 1; i < wines.length; i++) {
            wines[i] = Integer.parseInt(br.readLine());
        }

        int max = wines[1];

        dp[1][0] = 0;
        dp[1][1] = wines[1];
        dp[1][2] = 0;

        if (n > 1) {
            dp[2][0] = dp[1][1];
            dp[2][1] = wines[2];
            dp[2][2] = dp[1][1] + wines[2];

            max = dp[2][2];
        }

        for (int i = 3; i < dp.length; i++) {

            dp[i][0] = Math.max(dp[i - 1][1], dp[i - 1][2]);
            dp[i][1] = Math.max(Math.max(dp[i - 2][1], dp[i - 2][2]), dp[i - 2][0]) + wines[i];
            dp[i][2] = dp[i - 1][1] + wines[i];

            if (max < dp[i][0]) {
                max = dp[i][0];
            }
            if (max < dp[i][1]) {
                max = dp[i][1];
            }
            if (max < dp[i][2]) {
                max = dp[i][2];
            }
        }

        System.out.println(max);

    }
}
