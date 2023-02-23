package ys.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj15486 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] times = new int[n+2];
        int[] prices = new int[n+2];

        for (int i = 1; i < n+1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            times[i] = Integer.parseInt(st.nextToken());
            prices[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n+2];
        int max = 0;
        for (int i = 1; i <= n+1; i++) {
            max = Math.max(max, dp[i]);
            if (i + times[i] <= n+1) {
                dp[i + times[i]] = Math.max(dp[i+times[i]], max + prices[i]);
            }
        }
        System.out.println(max);
    }
}
