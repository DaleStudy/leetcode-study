export class Solution {
  alienOrder(words: string[]): string {
    const indegree = new Map<string, number>();
    const graph = new Map<string, Set<string>>();

    for (const word of words) {
      for (const ch of word) {
        if (graph.has(ch)) continue;
        graph.set(ch, new Set<string>());
        indegree.set(ch, 0);
      }
    }

    for (let i = 0; i < words.length - 1; i++) {
      const word1 = words[i];
      const word2 = words[i + 1];

      let pointer = 0;
      while (pointer < word1.length && pointer < word2.length && word1[pointer] === word2[pointer]) {
        pointer++;
      }

      if (pointer < word1.length && pointer === word2.length) {
        return "";
      }

      if (pointer < word1.length && pointer < word2.length) {
        const neighbors = graph.get(word1[pointer])!;
        if (!neighbors.has(word2[pointer])) {
          neighbors.add(word2[pointer]);
          indegree.set(word2[pointer], (indegree.get(word2[pointer]) || 0) + 1);
        }
      }
    }

    const queue: string[] = [];
    const result: string[] = [];

    for (const [ch, degree] of indegree) {
      if (degree === 0) {
        queue.push(ch);
      }
    }

    while (queue.length > 0) {
      const current = queue.shift()!;
      result.push(current);

      for (const neighbor of graph.get(current) || []) {
        indegree.set(neighbor, (indegree.get(neighbor) || 0) - 1);
        if (indegree.get(neighbor) === 0) {
          queue.push(neighbor);
        }
      }
    }

    if (indegree.size === result.length) {
      return result.join("");
    }

    return "";
  }
}
