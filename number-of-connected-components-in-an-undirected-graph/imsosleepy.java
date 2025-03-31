// 그래프에서 연결된 컴포넌트 개수를 구하는 문제
// 인접 리스트로 변환, DFS로 연결을 확인한다
// 그래프 변환 → O(E) (간선 수), DFS/BFS 탐색 → O(V + E) (노드 + 간선)
class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        boolean[] visited = new boolean[n];
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
        if (visited[node]) return;
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            dfs(neighbor, graph, visited);
        }
    }
}
