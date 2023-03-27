package 윤.w7;

/*
    프로그래머스 0단계 120869 : 외계인 사전
*/

import java.util.Arrays;
import java.util.stream.Collectors;

public class AlienDictionary {
    public static void main(String[] args) throws Exception {
        Solution3 solution = new Solution3();
        String[] spell = {"s", "o", "m", "d"};
        String[] dic = {"sdom", "dzx", "smm", "sunmmo", "som"};
        System.out.println("======================================");
        System.out.println("my answer : " + solution.solution(spell, dic));
        System.out.println("======================================");
    }
}

/*
내가 쓴 답
*/

class Solution {
    public int solution(String[] spell, String[] dic) {
        for (String word : dic) {
            for (String sp : spell) {
                word = word.replaceFirst(sp, "-");
                if (word.replaceAll("-", "").length() == 0 && spell.length == word.length()) {
                    return 1;
                }
            }
        }
        return 2;
    }
}

/*
다른 사람이 쓴 답
*/


class Solution1 {
    public int solution(String[] spell, String[] dic) {
        int answer = 2;

        for (String dicS : dic) {

            boolean isRight = true;
            for (String spellS : spell) {
                if (dicS.indexOf(spellS) == -1) {
                    isRight = false;
                    break;
                }
            }
            if (isRight) {
                answer = 1;
                break;
            }
        }
        return answer;
    }
}

class Solution2 {
    public int solution(String[] spell, String[] dic) {
        return Arrays.stream(dic).map(s -> s.chars().sorted().mapToObj(i -> String.valueOf((char) i)).collect(Collectors.joining())).collect(Collectors.toList())
                .contains(Arrays.stream(spell).sorted().collect(Collectors.joining())) ? 1 : 2;
// String[] dic = {"sdom", "dzx", "smm", "sunmmo", "som"} 일때, 변환을 거치면 sort가 되니까 dmos, dxz, mms, mmnosu, mos 이런식으로 Arraylist에 담긴다. 그렇게 비교하는 것!
    }
}

class Solution3 {
    public int solution(String[] spell, String[] dic) {
        int answer = 2;

        for (String s : dic) {
            int count = 0;
            if (spell.length == s.length()) {
                for (int i = 0; i < s.length(); i++) {
                    int breakCount = 0;
                    for (int j = 0; j < spell.length; j++) {
                        if (s.charAt(j) == spell[i].charAt(0)) {
                            count++;
                            breakCount++;
                            System.out.println(s + " : " + i + "|| s.length() : " + s.length() + "|| count : " + count);
                            if (breakCount == 1) {
                                break;
                            }
                        }
                    }


                }
            }
            if (count == s.length()) answer = 1;
            count = 0;

        }

        return answer;
    }
}