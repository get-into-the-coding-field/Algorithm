package 윤.w1.aTob;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
/*
    프로그래머스 120886번 : a로 b 만들기
*/

public class AToB {
    public static void main(String[] args) throws Exception {
        solution solution = new solution();
//        int[] numbers = {1, 2, -3, 4, -5};
        System.out.println(solution.solution("allpe", "apple"));
    }
}

/*
내가 쓴 답
*/

// 순서를 바꾸어 만들 수 있다
// 모든 요소가 다 있어야한다
// (1) char를 하나씩 for문 돌려서 있으면 삭제하기 -> 없으면 바로 0 반환
// (2) 삭제를 다하고 마지막에 남은게 있으면, 즉 길이가 1이상이면 -> 0반환 / 0이면 1반환
//class Solution {
//    public int solution(String before, String after) {
//        for (String c : before.split("")) {
//            if (after.contains(c)) {
//                after = after.replace(c, " ");
//            }
//        }
//        return after.trim().length() == 0 ? 1 : 0;
//    }
//}
// 이 로직이 실패한 이유 -> replace로 다 바꿔버렸기 때문에 여러 문자들이 모두 한번에 바뀜
// replaceFirst()를 사용하면 첫번째 문자만 새 문자로 대체되기 때문에 사용 가능하다.
// (replaceAll()은 정규식에 따라 입력 문자열에 대해 수행 할 작업 유형을 자유롭게 선택 가능!)

class solution {
    public int solution(String before, String after) {
        char[] beforeChar = before.toCharArray();
        char[] afterChar = after.toCharArray();
        Arrays.sort(beforeChar);
        Arrays.sort(afterChar);
        String sortedBefore = new String(beforeChar);
        String sortedAfter = new String(afterChar);
        return sortedAfter.equals(sortedBefore) ? 1 : 0;
    }
}

/*
다른 사람이 적은 답 이해
*/

class Solution1 {
    public int solution(String before, String after) {
        for (int i = 0; i < before.length(); i++) {
            after = after.replaceFirst(before.substring(i, i + 1), "");
        }
        return after.length() == 0 ? 1 : 0;
    }
}

class Solution2 {
    public int solution(String before, String after) {
        return isCheck(getList(before), getList(after)) ? 1 : 0;
    }

    private boolean isCheck(List<Integer> first, List<Integer> second) {
        for (int i = 0; i < first.size(); i++) {
            if (first.get(i) != second.get(i)) {
                return false;
            }
        }
        return true;
    }

    private List<Integer> getList(String str) {
        return Arrays.stream(str.split(""))
                .collect(Collectors.groupingBy(s -> s))
                .values()
                .stream()
                .map(List::size)
                .collect(Collectors.toList());
    }
}
