/**
 * 
 * In graph theory, a tree is an undirected graph 
 * in which any two vertices are connected by exactly one path, 
 * or equivalently a connected acyclic undirected graph.
 * 
 * 
 * 그래프가 valid tree인지 확인하는 함수
 * @param {number} n - 노드의 수
 * @param  {number[][]} edges - 간선의 정보
 * @returns {boolean} - 주어진 간선 정보로 만들어진 그래프가 트리인지 여부
 * 
 * 시간 복잡도: O(n)
 * - 모든 노드를 한 번씩 방문하여 그래프가 트리인지 확인
 * 
 * 공간 복잡도: O(n)
 * - 인접 리스트로 그래프, 방문배열
 */
function validTree(n: number, edges: number[][]): boolean {
    // 노드와 간선의 수 비교
    if (edges.length !== n-1) {
        return false
    }

    // 인접 리스트 형태로 그래프 생성
    const grapph: Map<number, number[]> = new Map()
    for (let i = 0; i < n; i++) {
        grapph.set(i, []);
    };
    for (const [a, b] of edges) {
        grapph.get(a)?.push(b)
        grapph.get(a)?.push(b)
    };

    // 방문 배열 생성
    const visited: boolean[] = new Array(n).fill(false);

    // DFS 깊이 우선 탐색
    const dfs = (node:number, parent: number): boolean => {
        visited[node] = true;
        for (const neighbor of grapph.get(node)!) {
            if (!visited[neighbor]) {
                if (!dfs(neighbor, node)) {
                    return false;
                }
            } else if (neighbor !== parent) {
                // 이미 방문한 노드가 부모가 아니면 사이클 발생
                return false;
            }
        }
        return true;
    }

    // DFS를 0번 노드부터 시작
    // 시작 지점은 -1로 설정
    if(!dfs(0, -1)) {
        return false;
    };

    // 모든 노드가 방문되었는지 확인
    for (const isVisited of visited) {
        if (!isVisited) {
            return false;
        }
    }

    return true;
}

