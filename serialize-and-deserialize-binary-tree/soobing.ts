/**
 * 문제 설명
 * - 이진 트리를 직렬화/역직렬화 하는 문제
 *
 * 아이디어
 * 1) 트리를 순회하면서 value값만 담는다.
 *  - DFS, BFS 둘 다 가능
 *  - DFS는 재귀 기반이라 코드가 간결하고, BFS 보다 메모리 사용량은 적지만, 깊은 트리에서는 스택 오버플로우가 발생할 수 있다.
 *  - 반면에 BFS는 큐를 많이 사용해서 폭이 넓은 트리에서 비효율적일 수 있지만,
 */

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
  const result: string[] = [];

  const dfs = (node: TreeNode | null) => {
    if (node === null) {
      result.push("null");
      return;
    }

    result.push(node.val.toString());
    dfs(node.left);
    dfs(node.right);
  };

  dfs(root);
  return result.join(",");
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
  const values = data.split(",");
  let i = 0;
  const dfs = () => {
    if (values[i] === "null") {
      i++;
      return null;
    }

    const node = new TreeNode(Number(values[i]));
    i++;
    node.left = dfs();
    node.right = dfs();
    return node;
  };
  return dfs();
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */

/*
 * Encodes a tree to a single string.
 */
function serializeBFS(root: TreeNode | null): string {
  if (!root) return "null";

  const queue: (TreeNode | null)[] = [root];
  const result: string[] = [];

  while (queue.length > 0) {
    const node = queue.shift();
    if (node) {
      result.push(node.val.toString());
      queue.push(node.left);
      queue.push(node.right);
    } else {
      result.push("null");
    }
  }
  return result.join(",");
}

/*
 * Decodes your encoded data to tree.
 */
function deserializeBFS(data: string): TreeNode | null {
  const values = data.split(",");

  if (values[0] === "null") return null;

  const root = new TreeNode(Number(values[0]));
  let i = 1;
  const queue: (TreeNode | null)[] = [root];

  while (queue.length > 0 && i < values.length) {
    const current = queue.shift();
    const left = values[i++];
    const right = values[i++];

    if (left !== "null") {
      current!.left = new TreeNode(Number(left));
      queue.push(current!.left);
    }

    if (right !== "null") {
      current!.right = new TreeNode(Number(right));
      queue.push(current!.right);
    }
  }
  return root;
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
