/**
 * 문제 설명
 * - 그래프를 탐색하면서 완전 복제하는 문제
 *
 * 아이디어
 * 1) 그래프 탐색 알고리즘
 * - 그래프 복사는 네트워크 유형에 해당하므로 bfs 혹은 dfs로 풀이한다.
 */

/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     neighbors: _Node[]
 *
 *     constructor(val?: number, neighbors?: _Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 *
 */

class _Node {
  val: number;
  neighbors: _Node[];

  constructor(val?: number, neighbors?: _Node[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}

function cloneGraph(node: _Node | null): _Node | null {
  if (node === null) return null;

  const visited = new Map<_Node, _Node>();

  function dfs(cur: _Node): _Node {
    if (visited.has(cur)) {
      return visited.get(cur)!;
    }

    const cloned = new _Node(cur.val);
    visited.set(cur, cloned);

    for (const neighbor of cur.neighbors) {
      cloned.neighbors.push(dfs(neighbor));
    }

    return cloned;
  }

  return dfs(node);
}

/**
 * BFS 풀이
function cloneGraph(node: _Node | null): _Node | null {
	if(!node) return null;

    const visited = new Map<_Node, _Node>();

    const cloneStart = new _Node(node.val);
    visited.set(node, cloneStart);

    const queue: _Node[] = [node];

    while(queue.length > 0) {
        const cur = queue.shift();
        const curClone = visited.get(cur);

        for(const neighbor of cur.neighbors) {
            if(!visited.get(neighbor)) {
                visited.set(neighbor, new _Node(neighbor.val));
                queue.push(neighbor);
            }
            
            curClone.neighbors.push(visited.get(neighbor));
        }
    }
    return cloneStart;
};
 */
