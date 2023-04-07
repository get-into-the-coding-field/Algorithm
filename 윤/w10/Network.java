package 윤.w10;

/*
    프로그래머스 3단계 43162 : 네트워크
*/

import java.util.ArrayList;
import java.util.List;

public class Network {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        int[][] computers = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
        System.out.println("======================================");
        System.out.println("my answer : " + solution.solution(3, computers)); // 2
        System.out.println("======================================");
    }
}

/*
내가 쓴 답
*/

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean visited[] = new boolean[n];

        for (int i = 0; i < n; i++) { // n개 컴퓨터 - n번 돌면서 탐색하기
            if (!visited[i]) { // 안가본곳 가야지~
                dfs(computers, i, visited);
                answer++;
            }
        }
        return answer;
    }

    void dfs(int[][] computers, int i, boolean[] visited) {
        visited[i] = true;

        for (int j = 0; j < computers.length; j++) { // 컴퓨터길이만큼 돌면서 탐색
            if (i != j && computers[i][j] == 1 && !visited[j]) { // !자기자신 && 컴터 배열값=1 && visited false면 재귀호출
                dfs(computers, j, visited);
            }
        }
    }
}

/*
다른 사람이 쓴 답
*/

class Solution1 {
    static boolean[] visit;
    static List<Integer>[] list;
    static int free, group;

    public int solution(int n, int[][] computers) {
        list = new List[n];
        visit = new boolean[n];

        for (int i = 0; i < n; i++)
            list[i] = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (i != j && computers[i][j] == 1)
                    list[i].add(j);
                if (computers[i][j] == 1) cnt++;
            }
            if (cnt == 1) {
                visit[i] = true;
                free++;
            }
        }

        for (int i = 0; i < n; i++) {
            if (!visit[i]) {
                dfs(i);
                group++;
            }
        }

        return free + group;
    }

    static void dfs(int com) {
        visit[com] = true;
        for (int i : list[com])
            if (!visit[i]) dfs(i);
    }
}

class Solution2 {
    boolean visited[];
    int[][] data;

    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        data = computers;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                dfs(i);
            }
        }
        return answer;
    }

    void dfs(int index) {
        if (visited[index]) {
            return;
        }
        visited[index] = true;

        for (int i = 0; i < data[index].length; i++) {
            if (data[index][i] == 1) {
                dfs(i);
            }
        }

    }
}