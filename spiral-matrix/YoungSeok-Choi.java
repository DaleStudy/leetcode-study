import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> res = new ArrayList<>();
    public boolean[][] visit;
    
    public List<Integer> spiralOrder(int[][] m) {
        int min = Math.min(m.length, m[0].length);
        int w = m.length;
        int h = m[0].length;

        visit = new boolean[w][h];

        for(int i = 0; i < (min / 2) + 1; i++) {
            spiralDepth(i, m);
        }

        return res;
    }

    public void spiralDepth(int d, int[][] m) {
        int w = m[0].length;
        int h = m.length;

        for(int i = d; i < (w - d); i++) {
            visit(d, i, m);
        }

       for (int i = d + 1; i < h - d; i++) {
            visit(i, w - d - 1, m);
        }

        // NOTE: 우측하단 에서 왼쪽으로 이동하거나, 좌하단에서 위로 이동할 때 가로(혹은 세로)가 1일때 방어하는 로직
        if ((h - d - 1) != d) {
            // 우상단 에서 아래로 내려오면서 우 하단 구석 인덱스는 출력했기 때문에 - 2를 뺴주고, 왼쪽의 끝까지 출력해야하기 때문에 >= 연산을 사용해 for 반복횟수결정
            for (int i = w - d - 2; i >= d; i--) { 
                visit(h - d - 1, i, m);
            }
        }

        if ((w - d - 1) != d) {
            for (int i = h - d - 2; i > d; i--) {
                visit(i, d, m);                
            }
        }
    }

    public void visit(int x, int y, int[][] m) {
        if(!visit[x][y]) {
            visit[x][y] = true;
            res.add(m[x][y]); 
        }
    }
}
