package 윤.w2.emergency;

import java.util.*;
import java.util.stream.Collectors;

/*
    프로그래머스 120835번 : 진료 순서 정하기
*/
public class Emergency {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        int[] numbers = {3, 76, 24};
        System.out.println(solution.solution(numbers));
    }
}

/*
내가 쓴 답
*/

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        ArrayList arrEmergency = (ArrayList) Arrays.stream(emergency).boxed().collect(Collectors.toList());
        for (int i = 1; i < emergency.length + 1; i++) {
            Integer max = (Integer) Collections.max(arrEmergency);
            int maxIndex = arrEmergency.indexOf(max);
            answer[maxIndex] = i;
            arrEmergency.set(maxIndex, 0);
        }
        return answer;
    }
}

/*
다른 사람이 적은 답 이해
*/


class Solution1 {
    public int[] solution(int[] e) {
        return Arrays.stream(e).map(i -> Arrays.stream(e).boxed().sorted(Comparator.reverseOrder()).collect(Collectors.toList()).indexOf(i) + 1).toArray();
    }
}
// Comparator.reverseOrder() -> 역순으로 정렬하기

class Solution2 {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];

        for (int i = 0; i < answer.length; i++) {
            if (answer[i] != 0) {
                continue;
            }
            int idx = 1;
            for (int j = 0; j < answer.length; j++) {
                if (emergency[i] < emergency[j]) {
                    idx++;
                }
            }
            answer[i] = idx;
        }
        return answer;
    }
}

class Solution3 {
    public int[] solution(int[] emergency) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] emergencySort = Arrays.copyOfRange(emergency, 0, emergency.length);
        Arrays.sort(emergencySort);
        int size = emergency.length;
        for (int i = 0; i < emergencySort.length; i++) {
            int e = emergencySort[i];
            map.put(e, size - i);
        }
        for (int i = 0; i < emergency.length; i++) {
            emergency[i] = map.get(emergency[i]);
        }
        return emergency;
    }
}

class Solution4 {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        int[] sort = Arrays.copyOf(emergency, emergency.length);
        Arrays.sort(sort);
        Map<Integer, Integer> rank = new HashMap<Integer, Integer>();
        int rankIdx = 1;
        for (int idx = sort.length - 1; idx >= 0; idx--) {
            rank.put(sort[idx], rankIdx++);
        }
        for (int idx = 0; idx < emergency.length; idx++) {
            answer[idx] = rank.get(emergency[idx]);
        }
        return answer;
    }
}