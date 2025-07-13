/**
 * [Problem]: [892] Alien Dictionary
 * (https://www.lintcode.com/problem/892/)
 */

//시간복잡도 O(n+e)
//공간복잡도 O(n+e)
export class Solution {
    /**
     * @param words: a list of words
     * @return: a string which is correct order
     */
    alienOrder(words: string[]): string {
        // Write your code here
        const graph: Map<string, Set<string>> = new Map();

        // 모든 문자를 그래프 노드로 초기화
        for (const word of words) {
            for (const char of word) {
                if (!graph.has(char)) {
                    graph.set(char, new Set());
                }
            }
        }

        // 문자 간 선후관계(edge) 설정
        for (let i = 1; i < words.length; i++) {
            const prev = words[i - 1];
            const curr = words[i];
            let isDiff = false;

            for (let j = 0; j < Math.min(prev.length, curr.length); j++) {
                const p = prev[j];
                const c = curr[j];

                if (p !== c) {
                    graph.get(p)!.add(c);
                    isDiff = true;
                    break;
                }
            }

            if (!isDiff && prev.length > curr.length) {
                return "";
            }
        }

        const visited: Set<string> = new Set();
        const visiting: Set<string> = new Set();
        const output: string[] = [];

        function dfs(node: string): boolean {
            if (visited.has(node)) return true;
            if (visiting.has(node)) return false;

            visiting.add(node);

            for (const neighbor of graph.get(node)!) {
                if (!dfs(neighbor)) return false;
            }

            visiting.delete(node);
            visited.add(node);
            output.push(node);

            return true;
        }

        for (const node of graph.keys()) {
            if (!dfs(node)) return "";
        }

        return output.reverse().join("");
    }
}
