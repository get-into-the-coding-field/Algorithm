package 윤.w3.ballgame;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
    프로그래머스 120843번 : 공 던지기
*/

public class BallGame {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        int[] numbers = {1, 2, 3, 4, 5, 6};
        System.out.println(solution.solution(numbers, 5));
    }
}

/*
내가 쓴 답
*/

class Solution {
    public int solution(int[] numbers, int k) {

        int count = 1;
        int answer = 1;
        int lastNum = numbers[numbers.length - 1];

        while (count < k) {
            count++;
            answer += 2;

            if (answer > lastNum) {
                answer -= lastNum;
            }
        }
        return answer;
    }
}

/*
다른 사람이 쓴 답
*/

class Solution1 {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        answer = numbers[((1 + ((k - 1) * 2)) % numbers.length) - 1];
        return answer;
    }
}

class Solution2 {
    public int solution(int[] numbers, int k) {
        return (k - 1) * 2 % numbers.length + 1;
    }
}

class Solution3 {
    public int solution(int[] numbers, int k) {
        return IntStream.range(1, k).mapToObj(i -> numbers).flatMapToInt(IntStream::of).toArray()[2 * k - 2];
        // IntStream.range(1,k) : 1부터 k까지 for문 돌기
        // mapToObj() : 원시스트림(IntStream)을 객체스트림으로 바꾸기
        // flatMapToInt(IntStream::of) : 쪼개기
    }
}