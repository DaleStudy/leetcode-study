class _Node {
  val: number;
  neighbors: _Node[];

  constructor(val?: number, neighbors?: _Node[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}

// 결국 새로운 인스턴스를 만들어 참조가 끊긴 완전한 남남의 그래프를 생성

function cloneGraph(node: _Node | null): _Node | null {
  if (!node) {
    return null;
  }

  const visited = new Map<_Node, _Node>();

  visited.set(node, new _Node(node.val));

  const queue: _Node[] = [node];

  while (queue.length > 0) {
    const currentNode = queue.shift()!;

    for (const n of currentNode?.neighbors) {
      if (!visited.has(n)) {
        visited.set(n, new _Node(n.val));
        queue.push(n);
      }

      visited.get(currentNode)!.neighbors.push(visited.get(n)!);
    }
  }

  return null;
}

// function cloneGraph(node: _Node | null): _Node | null {
//   if (!node) {
//     return null;
//   }

//   const checkMap = new Map<number, _Node>();

//   function dfs(targetNode: _Node) {
//     if (checkMap.has(targetNode.val)) {
//       return checkMap.get(targetNode.val)!;
//     }

//     const newNode = new _Node(targetNode.val);
//     checkMap.set(targetNode.val, newNode);

//     for (const n of targetNode.neighbors) {
//       newNode.neighbors.push(dfs(n));
//     }

//     return newNode;
//   }

//   const result = dfs(node);

//   return result;
// }

const node1 = new _Node(1);
const node2 = new _Node(2);
const node3 = new _Node(3);
const node4 = new _Node(4);

node1.neighbors = [node2, node4];
node2.neighbors = [node1, node3];
node3.neighbors = [node2, node4];
node4.neighbors = [node1, node3];

cloneGraph(node1);



