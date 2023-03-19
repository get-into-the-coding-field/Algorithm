package ys.programmers;

public class Prog12947 {
    public boolean solution(int x) {
        boolean answer = false;
        int n = x;
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x = x / 10;
        }

        if (n % sum == 0) {
            answer = true;
        }

        return answer;
    }
}
