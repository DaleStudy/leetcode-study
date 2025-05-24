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

/*
*/
function cloneGraph(node: _Node | null): _Node | null {
    const clones = new Map<_Node, _Node>()
	const dfs = (n: _Node) => {
        if (n === null) return n

        if (clones.has(n)) {
            return clones.get(n)
        }

        const copy = new _Node(n.val)
        clones.set(n, copy)

        for (const neighbor of n.neighbors) {
            copy.neighbors.push(dfs(neighbor))
        }
        return copy
    }
    return dfs(node)
};
