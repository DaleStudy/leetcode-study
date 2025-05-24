/**
 * [Problem]: [133] Clone Graph
 * (https://leetcode.com/problems/longest-repeating-character-replacement/description/)
 */

//  Definition for _Node.
class _Node {
    val: number;
    neighbors: _Node[];

    constructor(val?: number, neighbors?: _Node[]) {
        this.val = val === undefined ? 0 : val;
        this.neighbors = neighbors === undefined ? [] : neighbors;
    }
}

function cloneGraph(node: _Node | null): _Node | null {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function dfsFunc(node: _Node | null): _Node | null {
        if (!node) return null;
        const map = new Map<_Node, _Node>();

        function dfs(node: _Node): _Node {
            if (map.has(node)) return map.get(node)!;

            const copy = new _Node(node.val);
            map.set(node, copy);

            for (const neighbor of node.neighbors) {
                copy.neighbors.push(dfs(neighbor));
            }

            return copy;
        }

        return dfs(node);
    }
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function bfsFunc(node: _Node | null): _Node | null {
        if (!node) return null;

        const map = new Map<_Node, _Node>();
        const queue: _Node[] = [];

        const clone = new _Node(node.val);
        map.set(node, clone);
        queue.push(node);

        while (queue.length > 0) {
            const cur = queue.shift()!;

            for (const neighbor of cur.neighbors) {
                if (!map.has(neighbor)) {
                    map.set(neighbor, new _Node(neighbor.val));
                    queue.push(neighbor);
                }

                map.get(cur)!.neighbors.push(map.get(neighbor)!);
            }
        }
        return clone;
    }
}
