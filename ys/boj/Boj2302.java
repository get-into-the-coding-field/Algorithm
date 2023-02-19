package ys.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
    극장좌석 (실버1)
    https://www.acmicpc.net/problem/2302
    점화식 풀이 보기
 */
public class Boj2302 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int vipCnt = Integer.parseInt(br.readLine());

        int[] dp = new int[n + 1];
        int[] vips = new int[n + 1];

        for (int i = 0; i < vipCnt; i++) {
            vips[Integer.parseInt(br.readLine())] = 1;
        }

        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < dp.length; i++) {
            if (vips[i] == 1 || vips[i - 1] == 1) {
                dp[i] = dp[i - 1];
            } else {
                dp[i] = dp[i - 2] + dp[i - 1];
            }
        }
        System.out.println(dp[n]);
    }
}
