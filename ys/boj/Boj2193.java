package ys.boj;

import java.util.Scanner;

public class Boj2193 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        long[] dp = new long[n];

        dp[0] = 1L;

        if (n > 1) {
            dp[1] = 1L;
            for (int i = 2; i < n; i++) {
                dp[i] = dp[i - 2] + dp[i - 1];
            }
        }
        System.out.println(dp[n-1]);
    }
}
