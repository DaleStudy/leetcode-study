import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// 문제 해결에 용이하게 주어진 단방향 그래프를 양방향으로 바꾸어 DFS 실행
class Solution {

    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        boolean[] visited = new boolean[n];

        // 인접 리스트 초기화
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        // 양방향 그래프 구성
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        int count = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, graph, visited);
                count++;
            }
        }

        return count;
    }

    private void dfs(int node, List<List<Integer>> graph, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, graph, visited);
            }
        }
    }
}

// NOTE: 문제에서 주어진 무방향 그래프를 탐색하다, 앞 순번 DFS에서 연결 요소로 판단한 정점을 뒤 DFS 에서 다시 방문한 경우의
// 처리가 까다로웠다
class WrongSolution {

    Map<Integer, Boolean> visitMap = new HashMap<>();
    boolean[] visit;
    public int cnt = 0;

    public int countComponents(int n, int[][] edges) {

        visit = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (!visit[i]) {
                visitMap = new HashMap<>();
                cnt++;
                dfs(i, edges);

            }
        }

        return cnt;
    }

    public void dfs(int v, int[][] edges) {
        visit[v] = true;
        visitMap.put(v, true);

        for (int i = 0; i < edges.length; i++) {
            if (edges[i][0] == v && !visit[edges[i][1]]) {
                dfs(edges[i][1], edges);
            } else if (edges[i][0] == v && visit[edges[i][1]]) {
                if (!visitMap.containsKey(edges[i][1])) {
                    cnt--;
                }
            }
        }
    }
}
