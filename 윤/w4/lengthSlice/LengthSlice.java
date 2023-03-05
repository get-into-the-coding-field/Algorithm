package 윤.w4.lengthSlice;

/*
    프로그래머스 120913번 : 잘라서 배열로 저장하기
*/

import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class LengthSlice {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        System.out.println(solution.solution("abc1Addfggg4556b", 6));
    }
}

/*
내가 쓴 답
*/

class Solution {
    public String[] solution(String my_str, int n) {
        ArrayList<String> arrayList = new ArrayList();
        int firstStr = 0;
        int lastStr = n;
        String str = "";
        while (firstStr < my_str.length()) {
            str = lastStr > my_str.length() ? my_str.substring(firstStr) : my_str.substring(firstStr, lastStr);
            arrayList.add(str);
            str = "";
            firstStr += n;
            lastStr += n;
        }
        return arrayList.toArray(new String[arrayList.size()]);
    }
}
/*
다른 사람이 쓴 답
*/

class Solution1 {
    public String[] solution(String my_str, int n) {

        int resultCnt = (my_str.length() + n - 1) / n;
        String[] answer = new String[resultCnt];

        for (int i = 0; i < resultCnt; i++) {
            int start = n * i;
            int end = start + n >= my_str.length() ? my_str.length() : start + n;
            answer[i] = my_str.substring(start, end);
        }

        return answer;
    }
}

class Solution2 {
    public String[] solution(String myStr, int n) {
        return IntStream.range(0, myStr.length() / n + (myStr.length() % n > 0 ? 1 : 0))
                .mapToObj(i -> i == myStr.length() / n ? myStr.substring(i * n) : myStr.substring(i * n, (i + 1) * n))
                .toArray(String[]::new);
    }
}

class Solution3 {
    public String[] solution(String my_str, int n) {
        String[] answer = {};

        if (my_str.length() % n == 0) answer = new String[my_str.length() / n];
        else answer = new String[my_str.length() / n + 1];

        for (int i = 0; i < answer.length; i++) {
            answer[i] = (i * n + n <= my_str.length() - 1 ? my_str.substring(i * n, i * n + n) : my_str.substring(i * n));
        }

        return answer;
    }
}

class Solution4 {
    public String[] solution(String my_str, int n) {
        List<String> list = new ArrayList<>();
        String cut = "";

        for (int i = 0; i < my_str.length(); i++) {
            cut += my_str.charAt(i);
            if (cut.length() == n || i + 1 == my_str.length()) {
                list.add(cut);
                cut = "";
            }
        }
        String[] answer = new String[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}
