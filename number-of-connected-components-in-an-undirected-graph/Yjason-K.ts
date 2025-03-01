/**
 * 주어진 무방향 그래프의 연결된 컴포넌트(연결 요소)의 개수를 반환하는 함수
 *
 * @param {number} n - 노드의 수
 * @param {number[][]} edges - 간선의 정보
 * @returns {number} - 연결된 컴포넌트의 개수
 *
 * 시간 복잡도: O(n)
 *  - 모든 노드를 한 번씩 방문하여 연결된 컴포넌트의 개수를 계산
 * 공간 복잡도: O(n)
 *   - 인접 리스트와 방문 배열 사용
 */
function countComponents(n: number, edges: number[][]): number {
    // 인접 리스트 형태로 그래프 생성
    const graph: Map<number, number[]> = new Map();
    for (let i = 0; i < n; i++) {
        graph.set(i, []);
    }
    for (const [a, b] of edges) {
        graph.get(a)?.push(b);
        graph.get(b)?.push(a);
    }

    // 방문 배열 생성
    const visited: boolean[] = new Array(n).fill(false);
    let count = 0;

    // 깊이 우선 탐색 (DFS)
    const dfs = (node: number): void => {
        visited[node] = true;
        for (const neighbor of graph.get(node)!) {
            if (!visited[neighbor]) {
                dfs(neighbor);
            }
        }
    }

    // 모든 노드를 순회하며 아직 방문하지 않은 노드가 있으면 DFS 수행
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            // 새로운 연결 요소 발견
            count++; 
            dfs(i);
        }
    }

    return count;
}

