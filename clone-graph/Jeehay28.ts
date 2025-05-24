class _Node {
  val: number;
  neighbors: _Node[];

  constructor(val?: number, neighbors?: _Node[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}

// TC: O(V + E), where V is the number of vertices and E is the number of edges
// SC: O(V + E)
function cloneGraph(node: _Node | null): _Node | null {
  // 1: [2, 4]
  // 2: [1, 3]
  // 3: [2, 4]
  // 4: [1, 3]

  const clones = new Map<_Node, _Node>();
  // original Node: cloned Node

  if (!node) return null;

  const dfs = (node: _Node) => {
    if (clones.has(node)) {
      return clones.get(node);
    }

    const clone = new _Node(node.val);
    clones.set(node, clone);

    for (const nei of node.neighbors) {
      clone.neighbors.push(dfs(nei)!);
    }

    return clone;
  };

  return dfs(node)!;
}


// TC: O(V + E)
// SC: O(V + E)
// function cloneGraph(node: _Node | null): _Node | null {
//   if (!node) return null;

//   const clone: _Node = new _Node(node.val);
//   const clones = new Map<_Node, _Node>();
//   clones.set(node, clone);
//   const queue: _Node[] = [node]; // BFS -> use queue

//   while (queue.length > 0) {
//     const node = queue.shift()!;
//     for (const nei of node.neighbors) {
//       if (!clones.has(nei)) {
//         clones.set(nei, new _Node(nei.val));
//         queue.push(nei);
//       }
//       clones.get(node)!.neighbors.push(clones.get(nei)!);
//     }
//   }

//   return clone;
// }


