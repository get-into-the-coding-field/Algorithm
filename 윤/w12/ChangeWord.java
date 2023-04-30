package 윤.w12;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

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
        visited = new boolean[words.length]; // 체크했는지 확인
        dfs(begin, target, words, 0);
        return answer;
    }

    public static void dfs(String begin, String target, String[] words, int cnt) {
        if (begin.equals(target)) { // 원하는 단어랑 동일해졌을 때
            answer = cnt; // 횟수를 answer에 담고 리턴한다
            return;
        }

        for (int i = 0; i < words.length; i++) {
            if (visited[i]) { // 체크된 단어 즉, 이미 쓴 단어는 돌아간다.
                continue;
            }

            int k = 0;
            for (int j = 0; j < begin.length(); j++) {
                if (begin.charAt(j) == words[i].charAt(j)) { // 단어끼리 비교해서
                    k++; // 다른 알파벳이 몇개인지 확인하기
                }
            }

            if (k == begin.length() - 1) {  // 위에서 확인했을 시, 다른 단어 개수가 1이면 변환가능한 단어
                visited[i] = true; // 탐색한걸로 표시하고
                dfs(words[i], target, words, cnt + 1); // dfs 탐색 돌리기
                visited[i] = false;
            }
        }
    }
}

class Solution1 {

    static class Node {
        String next;
        int edge;

        public Node(String next, int edge) {
            this.next = next;
            this.edge = edge;
        }
    }

    public int solution(String begin, String target, String[] words) {
        int n = words.length, ans = 0;

        // for (int i=0; i<n; i++)
        //  if (words[i] != target && i == n-1) return 0;

        Queue<Node> q = new LinkedList<>();


        boolean[] visit = new boolean[n];
        q.add(new Node(begin, 0));

        while (!q.isEmpty()) {
            Node cur = q.poll();
            if (cur.next.equals(target)) {
                ans = cur.edge;
                break;
            }

            for (int i = 0; i < n; i++) {
                if (!visit[i] && isNext(cur.next, words[i])) {
                    visit[i] = true;
                    q.add(new Node(words[i], cur.edge + 1));
                }
            }
        }

        return ans;
    }

    static boolean isNext(String cur, String n) {
        int cnt = 0;
        for (int i = 0; i < n.length(); i++) {
            if (cur.charAt(i) != n.charAt(i)) {
                if (++cnt > 1) return false;
            }
        }

        return true;
    }
}

class Solution2 {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        boolean[] chk = new boolean[words.length];
        Queue<TempWord> queue = new LinkedList<>();
        queue.add(new TempWord(begin, 0));
        while (!queue.isEmpty()) {
            TempWord tw = queue.poll();
            if (tw.word.equals(target)) {
                answer = tw.step;
                break;
            }
            for (int i = 0; i < words.length; i++) {
                if (!chk[i] && canTransform(tw.word, words[i])) {
                    chk[i] = true;
                    queue.add(new TempWord(words[i], tw.step + 1));
                }
            }
        }
        return answer;
    }

    boolean canTransform(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                count++;
            }
        }
        return count == 1 ? true : false;
    }
}

class TempWord {
    String word;
    int step;

    TempWord(String word, int step) {
        this.word = word;
        this.step = step;
    }
}


class Solution3 {

    public static boolean is_change_able(String a, String b) {
        int diff = 0;

        for (int l = 0; l < a.length(); l++) {
            if (a.charAt(l) != b.charAt(l))
                diff++;

            if (diff >= 2)
                return false;
        }
        return true;
    }

    public static int[][] conn;
    public static int[] dist;

    public static int solution(String begin, String target, String[] words) {
        int answer = 0;
        int target_index = -1;
        int words_length = words.length;
        conn = new int[words.length][words.length];
        dist = new int[words.length];

        for (int w1 = 0; w1 < words_length; w1++) {
            dist[w1] = Integer.MAX_VALUE;

            if (words[w1].equals(target))
                target_index = w1;

            for (int w2 = w1 + 1; w2 < words_length; w2++) {
                if (is_change_able(words[w1], words[w2])) {
                    conn[w1][w2] = 1;
                    conn[w2][w1] = 1;
                }
            }
        }

        // 목표 단어가 없어서 변환할 수 없는 경우
        if (target_index == -1)
            return 0;

        // BFS 시작
        Queue<int[]> q = new LinkedList<>();

        for (int w1 = 0; w1 < words_length; w1++) {
            // 변경할 수 있는 경우
            if (is_change_able(begin, words[w1])) {
                q.add(new int[]{w1, 1});
            }
        }


        while (!q.isEmpty()) {
            int[] cur = q.poll();

            // target 에 도달한 경우
            if (cur[0] == target_index) {
                answer = cur[1];
                break;
            } else {
                for (int i = 0; i < words_length; i++) {
                    if (conn[cur[0]][i] == 1 && dist[i] > cur[1] + 1) {
                        dist[i] = cur[1] + 1;
                        q.add(new int[]{i, cur[1] + 1});
                    }
                }
            }
        }
        return answer;
    }
}

class Solution4 {
    public int solution(String begin, String target, String[] words) {
        return Arrays.stream(words)
                .collect(Collectors.collectingAndThen(Collectors.toList(), Words::from))
                .calculateMinConversionCount(begin, target);
    }

    private static class Words {
        private final List<Word> words;
        private final Map<Word, Boolean> usedWords;

        public Words(List<Word> words) {
            this.words = words;
            this.usedWords = words.stream()
                    .collect(Collectors.toMap(Function.identity(), word -> Boolean.FALSE));
        }

        public static Words from(List<String> words) {
            List<Word> words1 = words.stream()
                    .map(Word::new)
                    .collect(Collectors.toList());

            return new Words(words1);
        }

        public Integer calculateMinConversionCount(String begin, String target) {
            Word word = new Word(begin);
            Word targetWord = new Word(target);

            MinCount minCount = new MinCount();
            calculateMinConversionCount(word, targetWord, 0, minCount);

            if (minCount.isDefaultCount()) {
                return 0;
            }

            return minCount.getCount();
        }

        private void calculateMinConversionCount(Word word, Word targetWord, Integer count, MinCount minCount) {
            if (word.equals(targetWord)) {
                minCount.updateMin(count);
            }

            List<Word> nextWords = getNextWords(word);

            if (nextWords.isEmpty() || minCount.isLessEqualsThan(count)) {
                return;
            }

            for (Word from : nextWords) {
                this.usedWords.put(from, Boolean.TRUE);
                calculateMinConversionCount(from, targetWord, count + 1, minCount);
                this.usedWords.put(from, Boolean.FALSE);
            }
        }

        private List<Word> getNextWords(Word from) {
            return this.words.stream()
                    .filter(to -> this.isConvertible(from, to))
                    .collect(Collectors.toList());
        }

        private boolean isConvertible(Word from, Word to) {
            return !this.usedWords.get(to) && from.isConvertibleTo(to);
        }
    }

    private static class Word {
        private final String word;

        public Word(String word) {
            this.word = word;
        }

        public boolean isConvertibleTo(Word word) {
            return IntStream.range(0, this.word.length())
                    .filter(index -> this.word.charAt(index) != word.word.charAt(index))
                    .count() == 1L;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Word word1 = (Word) o;
            return Objects.equals(word, word1.word);
        }

        @Override
        public int hashCode() {
            return Objects.hash(word);
        }
    }

    private static class MinCount {
        private static final Integer DEFAULT_COUNT = Integer.MAX_VALUE;
        private Integer count;

        public MinCount() {
            this.count = DEFAULT_COUNT;
        }

        public void updateMin(Integer count) {
            this.count = Integer.min(this.count, count);
        }

        public Integer getCount() {
            return count;
        }

        public boolean isDefaultCount() {
            return DEFAULT_COUNT.equals(this.count);
        }

        public boolean isLessEqualsThan(Integer count) {
            return this.count <= count;
        }
    }
}