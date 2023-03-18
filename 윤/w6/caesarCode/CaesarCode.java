package 윤.w6.caesarCode;

/*
    프로그래머스 1단계 12926 : 시저암호
*/


public class CaesarCode {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        System.out.println(solution.solution("z", 1)); // "e F d"
    }
}

/*
내가 쓴 답
*/

class Solution {
    public String solution(String s, int n) {
        String answer = "";
        char[] charArr = s.toCharArray();

        for (char c : charArr) {
            int code = c + n;
            if (Character.isUpperCase(c)) {
                answer += code > 'Z' ? Character.toString(code - 26) : Character.toString(code);
            } else if (Character.isLowerCase(c)) {
                answer += code > 'z' ? Character.toString(code - 26) : Character.toString(code);
            } else {
                answer += c;
            }
        }
        return answer;
    }
}


/*
다른 사람이 쓴 답
*/


class Solution2 {
    public String solution(String s, int n) {
        String result = "";
        n = n % 26;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (Character.isLowerCase(ch)) {
                ch = (char) ((ch - 'a' + n) % 26 + 'a');
            } else if (Character.isUpperCase(ch)) {
                ch = (char) ((ch - 'A' + n) % 26 + 'A');
            }
            result += ch;
        }
        return result;
    }
}

class Solution3 {
    public String solution(String s, int _n) {
        return s.chars().map(c -> {
                    int n = _n % 26;
                    if (c >= 'a' && c <= 'z') {
                        return 'a' + (c - 'a' + n) % 26;
                    } else if (c >= 'A' && c <= 'Z') {
                        return 'A' + (c - 'A' + n) % 26;
                    } else {
                        return c;
                    }
                }).mapToObj(c -> String.valueOf((char) c))
                .reduce((a, b) -> a + b).orElse("");
    }

}