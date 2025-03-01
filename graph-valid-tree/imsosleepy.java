// 저번주 course-schedule 문제와 유사한 사이클이 존재하지 않아야하는 트리를 찾는 문제
// 차이가 있다면 course-schedule는 방향 그래프지만 이 문제는 무방향 그래프라는 차이가 있음
// 무방향 그래프는 이전 노드(부모)를 통해 다시 돌아온 후 연결을 판단해야하는 경우가 있어거 구현이 조금 더 어려움
public class GraphValidTree {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false; // 트리는 반드시 (n-1)개의 간선 필요

        // 그래프 인접 리스트 생성
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        Set<Integer> visited = new HashSet<>();
        if (!dfs(graph, 0, -1, visited)) return false;

        return visited.size() == n;
    }

    private boolean dfs(Map<Integer, List<Integer>> graph, int node, int parent, Set<Integer> visited) {
        if (visited.contains(node)) return false; // 사이클 발견

        visited.add(node);
        for (int neighbor : graph.get(node)) {
            if (neighbor == parent) continue;
            if (!dfs(graph, neighbor, node, visited)) return false;
        }
        return true;
    }
}
