package 윤.w11;

/*
    프로그래머스 3단계 43162 : 네트워크
*/

import java.util.ArrayList;
import java.util.List;

public class ChangeWord {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        String[] words = {"hot", "dot", "dog", "lot", "log", "cog"};
        System.out.println("======================================");
        System.out.println("my answer : " + solution.solution("hit", "cog", words)); // 4
        System.out.println("======================================");
    }
}

class Solution {
    static boolean[] visited;
    static int answer = 0;

    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        dfs(begin, target, words, 0);
        return answer;
    }

    public static void dfs(String begin, String target, String[] words, int cnt) {
        if (begin.equals(target)) {
            answer = cnt;
            return;
        }

        for (int i = 0; i < words.length; i++) {
            if (visited[i]) {
                continue;
            }

            int k = 0;    // 같은 스펠링 몇개인지 세기
            for (int j = 0; j < begin.length(); j++) {
                if (begin.charAt(j) == words[i].charAt(j)) {
                    k++;
                }
            }

            if (k == begin.length() - 1) {  // 한글자 빼고 모두 같은 경우
                visited[i] = true;
                dfs(words[i], target, words, cnt + 1);
                visited[i] = false;
            }
        }
    }
}