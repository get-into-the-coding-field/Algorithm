package 윤.w9;

/*
    프로그래머스 2단계 12951 : JadenCase 문자열 만들기
*/

public class JadenCase {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        System.out.println("======================================");
        System.out.println("my answer : " + solution.solution("3people unFollowed me")); // "3people Unfollowed Me"
        System.out.println("======================================");
    }
}

/*
내가 쓴 답
*/

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean isFirstChar = true;
        for (char c : s.toCharArray()) {
            if (isFirstChar) {
                sb.append(Character.toUpperCase(c));
                isFirstChar = false;
            } else {
                sb.append(Character.toLowerCase(c));
            }
            if (c == ' ') {
                isFirstChar = true;
            }
        }
        return sb.toString();
    }
}

// 하다가 테스트 많이 틀린거
class Solution1 {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        String[] wordList = s.toLowerCase().split(" ", -1);

        for (int i = 0; i < wordList.length; i++) {
            if (wordList[i].length() == 0) {
                continue;
            }
            char firstChar = Character.toUpperCase(wordList[i].charAt(0));
            if (Character.isUpperCase(wordList[i].charAt(0))) {
                sb.append(firstChar).append(wordList[i].substring(1).toLowerCase()).append(" ");
            } else {
                sb.append(firstChar).append(wordList[i].substring(1)).append(" ");
            }
        }

        return sb.toString().trim();
    }
}

// 하다가 테스트 많이 틀린거
class Solution2 {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        String[] wordList = s.toLowerCase().split(" ", -1);

        for (int i = 0; i < wordList.length; i++) {
            if (wordList[i].length() == 0) {
                continue;
            }
            char firstChar = Character.toUpperCase(wordList[i].charAt(0));
            if (Character.isUpperCase(wordList[i].charAt(0))) {
                sb.append(firstChar).append(wordList[i].substring(1).toLowerCase()).append(" ");
            } else {
                sb.append(firstChar).append(wordList[i].substring(1)).append(" ");
            }
        }

        return sb.toString().trim();
    }
}


///< 다른 사람 풀이 >///////////////////////////////////////////////////


class Solution3 {
    public String solution(String s) {
        String answer = "";
        String[] sp = s.toLowerCase().split("");
        boolean flag = true;

        for (String ss : sp) {
            answer += flag ? ss.toUpperCase() : ss;
            flag = ss.equals(" ") ? true : false;
        }

        return answer;
    }
}

class Solution4 {
    public String solution(String s) {
        String answer = "";

        String[] str = s.split(" ");

        for (String ss : str)
            if (ss.length() > 0)
                answer += ss.substring(0, 1).toUpperCase() + ss.substring(1).toLowerCase() + " ";
            else
                answer += " ";
        if (s.charAt(s.length() - 1) != ' ')
            answer = answer.substring(0, answer.length() - 1);
        return answer;
    }
}

class Solution5 {
    public String solution(String s) {
        String answer = "";

        boolean isFirst = true;
        for (String data : s.toLowerCase().split("")) {
            answer += isFirst ? data.toUpperCase() : data;
            isFirst = data.equals(" ") ? true : false;
        }

        return answer;
    }
}

class Solution6 {
    public String solution(String s) {
        boolean isNextUpper = true;
        StringBuffer sb = new StringBuffer();

        for (int inx = 0; inx < s.length(); inx++) {
            char c = s.charAt(inx);
            if (inx == 0 || isNextUpper) {
                sb.append(Character.toUpperCase(c));
                isNextUpper = false;
            } else {
                sb.append(Character.toLowerCase(c));
            }

            if (c == ' ') {
                isNextUpper = true;
            }
        }
        return sb.toString();
    }
}