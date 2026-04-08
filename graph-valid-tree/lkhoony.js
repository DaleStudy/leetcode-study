export class Solution {
    /**
     * @param {number} n - number of nodes
     * @param {number[][]} edges - undirected edges
     * @return {boolean}
     */
    validTree(n, edges) {
      if (n === 0) return true;
  
      // 인접 리스트 생성
      const adj = {};
      for (let i = 0; i < n; i++) {
        adj[i] = [];
      }
      for (const [n1, n2] of edges) {
        adj[n1].push(n2);
        adj[n2].push(n1);
      }
  
      const visit = new Set();
  
      const dfs = (i, prev) => {
        if (visit.has(i)) return false;
  
        visit.add(i);
  
        for (const j of adj[i]) {
          if (j === prev) continue;
          if (!dfs(j, i)) return false;
        }
  
        return true;
      };
  
      return dfs(0, -1) && visit.size === n;
    }
  }

