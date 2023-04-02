package 윤.w8;

/*
    프로그래머스 2단계 42885 : 구명보트
*/

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class LifeBoat {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        System.out.println("======================================");
        int[] numbers = {70, 80, 50};
        System.out.println("my answer : " + solution.solution(numbers, 100)); // 3
        System.out.println("======================================");
    }
}

/*
내가 쓴 답
*/

// sort로
class Solution {
    public int solution(int[] people, int limit) {
        int boat = 0;
        int light = 0;
        int heavy = people.length - 1;

        Arrays.sort(people);
        while (light <= heavy) {
            if (people[light] + people[heavy] <= limit) { // 만약 같이 태울 수 있으면 그다음 가벼운 사람 선택해야하니까 ++
                light++;
            }
            heavy--; // 가장 무거운 애 혼자만 태워야하니까 바로 그 아래 무거운 애 선택하도록 --
            boat++;
        }
        return boat;
    }
}

/*
다른 사람이 쓴 답
*/


class Solution1 {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1;
        for (; i < j; --j) {
            if (people[i] + people[j] <= limit)
                ++i;
        }
        return people.length - i;
    }
}

class Solution2 {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int n = people.length;
        Arrays.sort(people);

        int i = n - 1;
        int j = 0;

        while (i > j) {
            if (people[i] + people[j] <= limit) {
                i--;
                j++;
            } else {
                i--;
            }
        }

        return answer = (n - j);
    }
}

class Solution3 {
    public int solution(int[] people, int limit) {
        int answer = 0;

        Arrays.sort(people);
        boolean[] visited = new boolean[people.length];

        int index = people.length - 1;
        for (int i = 0; i < people.length; ++i) {
            if (!visited[i]) {
                int person = people[i];
                visited[i] = true;
                ++answer;

                for (int j = index; j > i; --j) {
                    if (!visited[j]) {
                        int partner = people[j];
                        if (partner + person <= limit) {
                            visited[j] = true;
                            index = j - 1;
                            break;
                        }
                    }
                    --index;
                }
            }
        }

        return answer;
    }
}

class Solution4 {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        Deque<Integer> deque = new LinkedList<>();
        for (int i = 0; i < people.length; i++) {
            deque.push(people[i]);
        }

        while (!deque.isEmpty()) {
            answer++;
            int std = deque.pollFirst();
            if (!deque.isEmpty()) {
                if (std + deque.peekLast() <= limit) {
                    deque.pollLast();
                }
            }
        }
        return answer;
    }
}
