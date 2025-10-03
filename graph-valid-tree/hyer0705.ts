// Time Complexity: O(n)
// Space Complexity: O(n)
export class Solution {
  /**
   * @param n: An integer
   * @param edges: a list of undirected edges
   * @return: true if it's a valid tree, or false
   */
  validTree(n: number, edges: number[][]): boolean {
    if (n === 0) return true;
    if (edges.length !== n - 1) return false;

    const graph: number[][] = Array.from({ length: n }, () => []);

    for (const [s, e] of edges) {
      graph[s].push(e);
      graph[e].push(s);
    }

    const visited = new Set<number>();

    const queue = [0];
    visited.add(0);

    let pointer = 0;
    while (pointer < queue.length) {
      const currentNode = queue[pointer++];

      for (const nextNode of graph[currentNode]) {
        if (!visited.has(nextNode)) {
          queue.push(nextNode);
          visited.add(nextNode);
        }
      }
    }

    return visited.size === n;
  }
}
