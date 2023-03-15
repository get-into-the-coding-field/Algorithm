package 윤.w5.competition;

import java.util.*;
import java.util.stream.IntStream;

/*
    프로그래머스 2단계 : 양궁게임
*/


public class Competition {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        int[] numbers = {2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0};
        System.out.println(solution.solution(5, numbers));
    }
}

/*
내가 쓴 답
*/

class Solution {
    public int[] solution(int n, int[] info) {
        int[] answer = new int[11]; // 반환은 동일하게 11점
        int[] tmp = new int[11]; // 예시 후보
        int maxDiff = 0; // 가장 큰 값

        for (int subset = 1; subset < (1 << 10); ++subset) { // 비트연산을 통해 구하기
            int ryan = 0;
            int apeach = 0;
            int cnt = 0; // 몇개 사용했는지 카운팅 용도
            for (int i = 0; i < 10; ++i) {
                if ((subset & 1 << i) != 0) { // i번째 비트만 1로 켜진다
                    // &는 둘 다 1인 경우 1 반환하고, 그렇지 않은 경우 0 반환
                    // <<는 비트를 왼쪽으로 n만큼 이동
                    // subset이라는 변수가 표현하는 부분집합에서 i번째 비트가 1인지 아닌지를 검사
                    // subset & 1 << i는 subset과 1 << i를 비트 연산한 결과를 반환하는데, 이 결과가 0이 아니라면 i번째 비트가 1이라는 뜻입니다.
                    // 따라서, (subset & 1 << i) != 0은 subset의 i번째 비트가 1인지 아닌지를 검사하는 조건문
                    // subset에 부분집합을 하게되면 0이 아닌 값이니까
                    ryan += 10 - i; // 라이언이 가져가는 점수
                    tmp[i] = info[i] + 1; // 라이언이 맞춘 화살개수는 어피치 +1
                    cnt += tmp[i]; // 라이언 사용 개수는 바로 위 tmp[i]인거
                } else {
                    tmp[i] = 0; // 라이언이 못이겼으면 안쏘면 되지
                    if (info[i] > 0) // 어피치가 이긴게 0보다 큰거면
                        apeach += 10 - i; // 이게 어피치가 가져가는 점수인거
                }
            }

            if (cnt > n) continue; // 화살을 더 쓰게 되었으면 무시시켜야함

            tmp[10] = n - cnt; // 전체사용개수 - 지금사용개수 (0점개수기록)

            // maxDiff 보다 큰거 계산하기
            if (ryan - apeach == maxDiff) { // 둘이 점수가 같다면
                for (int i = 10; i >= 0; --i) { // for문 돌려서 끝에서부터 하나하나 비교
                    if (tmp[i] > answer[i]) {
                        maxDiff = ryan - apeach;
                        answer = Arrays.copyOf(tmp, tmp.length);
                        break;
                    } else if (tmp[i] < answer[i]) {
                        break;
                    }
                }
            } else if (ryan - apeach > maxDiff) { // 라이언이 이긴다면
                maxDiff = ryan - apeach;
                answer = Arrays.copyOf(tmp, tmp.length); // tmp에 있는거 가져오기
            }
        }
        // 만약 라이언이 못이긴다고 하면 maxDiff가 0으로 남아있을테니까 분기처리하기
        if (maxDiff == 0) {
            return new int[]{-1}; // 지면 -1 반환해야하니까
        }
        return answer;
    }
}


/*
다른 사람이 쓴 답
*/


class Solution1 {

    int max, ans[], apeach[];

    void find(int n, int cur) {
        int score = 0, state[] = new int[11];
        for (int i = 1; i <= 10; i++) {
            if ((cur & 1 << i) > 0) {
                n -= state[10 - i] = apeach[10 - i] + 1;
                if (n < 0) return;
                score += i;
            } else if (apeach[10 - i] > 0) score -= i;
        }
        if (score <= 0) return;
        state[10] = n;
        if (max < score) {
            max = score;
            ans = state;
        } else if (max == score) {
            for (int i = 10; i >= 0; i--) {
                if (ans[i] != state[i]) {
                    if (state[i] > ans[i])
                        ans = state;
                    return;
                }
            }
        }
    }

    int[] solution(int n, int[] info) {
        apeach = info;
        for (int i = 1; i < 1 << 11; i++)
            if (Integer.bitCount(i) <= n)
                find(n, i);

        return max == 0 ? new int[]{-1} : ans;
    }
}


class Solution2 {
    public int[] answer = new int[]{-1};
    public Set<String> drStrange = new LinkedHashSet<String>();

    public void search(int indexNumX, int indexNumY, int n, int[] info, String ryanInfo, int countN) {
        if (indexNumX == 1 && (info[indexNumY] + 1 + countN) <= n) {
            ryanInfo += (info[indexNumY] + 1) + ",";
            countN += info[indexNumY] + 1;
        } else {
            ryanInfo += "0,";
        }

        if (countN == n) {
            if (ryanInfo.substring(0, ryanInfo.length() - 1).split(",").length < 11) {
                ryanInfo += "0,".repeat(11 - ryanInfo.substring(0, ryanInfo.length() - 1).split(",").length);
            }
            ryanInfo = ryanInfo.substring(0, ryanInfo.length() - 1);
            drStrange.add(ryanInfo);
            return;
        }

        if (indexNumY == 10) {
            ryanInfo = ryanInfo.substring(0, ryanInfo.length() - 1);
            ryanInfo = ryanInfo.substring(0, ryanInfo.lastIndexOf(",")) + "," + (n - countN);
            drStrange.add(ryanInfo);
            return;
        }

        search(0, indexNumY + 1, n, info, ryanInfo, countN);
        search(1, indexNumY + 1, n, info, ryanInfo, countN);
    }

    public int[] solution(int n, int[] info) {
        search(0, 0, n, info, "", 0);
        search(1, 0, n, info, "", 0);

        int beforeScore = 0, beforeDif = 0;
        String beforeStr = "";

        for (String s : drStrange) {
            int[] answerCandidate = new int[11];
            int nowScore = 0, enemyScore = 0;
            int nowDif = 0;

            for (int i = 0; i < s.split(",").length; i++) {
                if (Integer.parseInt(s.split(",")[i]) > info[i]) {
                    nowScore += 10 - i;
                } else {
                    if (info[i] != 0) enemyScore += 10 - i;
                }
                answerCandidate[i] = Integer.parseInt(s.split(",")[i]);
            }
            nowDif = nowScore - enemyScore;
            if (nowDif > beforeDif) {
                answer = answerCandidate.clone();
                beforeDif = nowDif;
                beforeStr = s;
            } else if (nowDif == beforeDif && answer.length > 1) {
                for (int i = 10; i > -1; i--) {
                    if (answer[i] < answerCandidate[i]) {
                        answer = answerCandidate.clone();
                        break;
                    } else if (answer[i] > answerCandidate[i]) {
                        break;
                    }
                }
            }
        }
        return answer;
    }
}

class Solution3 {
    public int count(int[] info, int bin) {
        int cnt = 0;
        for (int i = 0; i < 11; ++i) {
            if ((bin >> i & 1) == 1) {
                cnt += info[10 - i] + 1;
            }
        }
        return cnt;
    }

    public int sum(int[] score, int bin) {
        int s = 0;
        for (int i = 0; i < 11; ++i) {
            if ((bin >> i & 1) == 1) {
                s += score[10 - i];
            }
        }
        return s;
    }

    public boolean check(int bin, int b) {
        for (int i = 0; i < 11; ++i) {
            if ((bin >> i & 1) == (b >> i & 1))
                continue;
            return (b >> i & 1) == 1;
        }
        return true;
    }

    public int[] solution(int n, int[] info) {
        var apeach = IntStream.range(0, 11).map(i -> info[i] > 0 ? 10 - i : 0).sum();
        var score = IntStream.range(0, 11).map(i ->
                info[i] > 0 ? 20 - 2 * i : 10 - i).toArray();
        int max = -1;
        int bin = 0;
        var answer = new int[11];
        for (int b = 0; b < 2048; ++b) {
            if (count(info, b) <= n) {
                var s = sum(score, b);
                if (max < s) {
                    max = s;
                    bin = b;
                } else if (max == s && check(bin, b)) {
                    bin = b;
                }
            }
        }
        for (int i = 0; i < 11; ++i) {
            if ((bin >> i & 1) == 1) {
                answer[10 - i] = info[10 - i] + 1;
            }
        }
        answer[10] = n - count(info, bin);
        if (max <= apeach)
            answer = new int[]{-1};
        return answer;
    }
}

class Solution4 {

    int[] answer = {-1};
    int[] apeach = new int[11];
    int[] ryan = new int[11];
    int n;
    int scoreGap = 0;

    public int[] solution(int n, int[] info) {
        this.apeach = info;
        this.n = n;

        dfs(true, 10, 0);
        dfs(false, 10, 0);

        return answer;
    }

    public void dfs(boolean yes, int level, int myScore) {
        if (level < 0) {
            calculate();
            return;
        }

        if (!yes) {
            dfs(true, level - 1, myScore);
            dfs(false, level - 1, myScore);

            return;
        }

        int need = apeach[level] + 1;
        if (n >= need) {
            n -= need;
            ryan[level] = need;
            dfs(true, level - 1, myScore + level);
            dfs(false, level - 1, myScore + level);
            ryan[level] = 0;
            n += need;
        }
    }

    public void calculate() {
        int apeachScore = 0;
        int ryanScore = 0;

        for (int i = 0; i <= 10; i++) {
            if (apeach[i] == 0 && ryan[i] == 0) {
                continue;
            }

            if (apeach[i] >= ryan[i]) {
                apeachScore += (10 - i);
            } else {
                ryanScore += (10 - i);
            }
        }

        if (ryanScore > apeachScore && scoreGap < (ryanScore - apeachScore)) {
            scoreGap = (ryanScore - apeachScore);

            answer = new int[11];
            for (int i = 0; i <= 10; i++) {
                answer[i] = ryan[i];
            }
            if (n != 0) {
                answer[10] += n;
            }
        }

        return;
    }
}