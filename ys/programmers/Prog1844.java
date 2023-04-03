package ys.programmers;

import java.util.LinkedList;
import java.util.Queue;

public class Prog1844 {
    static final int[] X_DIRECTION = {0, 0, -1, 1};
    static final int[] Y_DIRECTION = {-1, 1, 0, 0};
    static int X,Y;
    static boolean[][] isVisited;

    public static void main(String[] args) {
        int[][] ex1 = {{1, 0, 1, 1, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 1}, {1, 1, 1, 0, 1}, {0, 0, 0, 0, 1}};
        int[][] ex2 = {{1, 0, 1, 1, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 1}, {1, 1, 1, 0, 0}, {0, 0, 0, 0, 1}};

        System.out.println(solution(ex1));
        System.out.println(solution(ex2));
    }

    static int solution(int[][] maps) {
        Y = maps.length;
        X = maps[0].length;
        isVisited = new boolean[Y][X];

        return bfs(new Point(0, 0), maps);
    }

    static int bfs(Point point, int[][] maps) {
        Queue<Point> queue = new LinkedList<>();
        isVisited[point.y][point.x] = true;
        queue.add(point);
        int level = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Point cur = queue.poll();

                if (cur.y == Y - 1 && cur.x == X - 1) {
                    return level;
                }

                for (int j = 0; j < 4; j++) {
                    Point nextP = new Point(cur.x + X_DIRECTION[j], cur.y + Y_DIRECTION[j]);

                    if (nextP.y >= Y || nextP.y < 0 || nextP.x >= X || nextP.x < 0) {
                        continue;
                    }

                    if (!isVisited[nextP.y][nextP.x] && maps[nextP.y][nextP.x] != 0) {
                        queue.add(nextP);
                        isVisited[nextP.y][nextP.x] = true;
                    }
                }
            }
            level++;
        }
        return -1;
    }

    static class Point{
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
