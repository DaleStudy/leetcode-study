import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {

  private final int[] dy = { -1, 1, 0, 0 };
  private final int[] dx = { 0, 0, -1, 1 };
  private int M = 0, N = 0;

  /**
   * 특정 노드에서 시작에서 이웃 노드를 거쳐 두 바다로 갈 수 있는 노드 리스트를 출력하기
   * 특정 노드에서 전체 탐색? => O(NxM) x O(NxM) 탐색 필요.
   * 
   * 그럼 태평양, 대서양 각각에서 도달할 수 있는 노드 리스트 찾기(본인 이상 값을 가진 노드로 탐색)
   * 그리고 겹치는 지점 찾기 => 답
   * 3xO(NxM)
   * 
   * Runtime: 11 ms (Beats 28.23%)
   * Memory: 46.9 MB (Beats 98.39%)
   * Space Complexity: O(NxM)
   * - 노드 방문 여부를 체크하기 위한 flowed O(NxM)
   * - 방문하는 노드를 큐에 찾기 qu O(NxM)
   * > 2O(NxM) => O(NxM)
   * Time Complexity: O(NxM)
   * - 태평양 인접 노드 탐색 O(NxM)
   * - 대서양 인접 노드 탐색 O(NxM)
   * - 두 대양 인접 노드 검색 O(NxM)
   * > 3O(NxM)
   */
  public List<List<Integer>> pacificAtlantic(int[][] heights) {
    M = heights.length;
    N = heights[0].length;
    int[][] flowed = new int[M][N]; // 1이면 태평양 인접, 2면 대서양, 3이면 둘 다, 0이면 인접X

    // (0,0) ~ (0,N-1)을 1로 넣고 bfs 돌리기
    Queue<int[]> qu = new LinkedList<>();
    for (int i = 0; i < N; i++) {
      int[] temp = { 0, i };
      flowed[0][i] += 1;
      qu.add(temp);
    }
    // (1, 0) ~ (M-1, 0)
    for (int i = 1; i < M; i++) {
      int[] temp = { i, 0 };
      flowed[i][0] += 1;
      qu.add(temp);
    }
    // 태평양 탐색
    bfs(qu, flowed, heights, 1);

    // printMp(flowed);

    // System.out.println("------------");

    qu = new LinkedList<>();
    // (M-1, 0) ~ (M-1, N-1)
    for (int i = 0; i < N; i++) {
      int[] temp = { M - 1, i };
      flowed[M - 1][i] += 2;
      qu.add(temp);
    }
    // (0, 0) ~ (M-2, N-1)
    for (int i = 0; i < M - 1; i++) {
      int[] temp = { i, N - 1 };
      flowed[i][N - 1] += 2;
      qu.add(temp);
    }
    // 태평양 탐색
    bfs(qu, flowed, heights, 2);
    List<List<Integer>> ans = new ArrayList<>();

    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (flowed[i][j] == 3) {
          List<Integer> tmp = new ArrayList<>(Arrays.asList(i, j));
          ans.add(tmp);
        }
      }
    }

    return ans;

  }

  private void bfs(Queue<int[]> qu, int[][] flowed, int[][] heights, int oceanTp) {
    while (!qu.isEmpty()) {
      int[] node = qu.poll();
      int h = heights[node[0]][node[1]];

      // 사방을 보면서 적절한 노드를 큐에 넣기
      for (int n = 0; n < 4; n++) {
        int ny = node[0] + dy[n];
        int nx = node[1] + dx[n];

        // 섬 밖 위치인지 체크
        if (ny < 0 || ny >= M || nx < 0 || nx >= N) {
          continue;
        }
        // 방문했던 위치면 넘어가기
        if (flowed[ny][nx] >= oceanTp) {
          continue;
        }
        // 바다에서 섬으로 갈 수 있는 방향인지 체크
        if (h > heights[ny][nx]) {
          continue;
        }
        flowed[ny][nx] += oceanTp;
        int[] temp = { ny, nx };
        qu.add(temp);
      }
    }
  }

  private void printMp(int[][] mp) {
    int my = mp.length;
    int mx = mp[0].length;
    for (int y = 0; y < my; y++) {
      for (int x = 0; x < mx; x++) {
        System.out.print(mp[y][x] + " ");
      }
      System.out.print('\n');
    }
  }
}