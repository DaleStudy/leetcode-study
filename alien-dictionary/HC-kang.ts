/**
 * https://leetcode.com/problems/alien-dictionary
 * T.C. O(N * M) N: number of words, M: average length of word
 * S.C. O(1) 26 characters
 */
function alienOrder(words: string[]): string {
  const graph: Record<string, Set<string>> = {};
  const inDegree: Record<string, number> = {};

  // Initialize the graph
  for (const word of words) {
    for (const char of word) {
      if (!graph[char]) {
        graph[char] = new Set();
        inDegree[char] = 0;
      }
    }
  }

  // Build the graph
  for (let i = 0; i < words.length - 1; i++) {
    const word1 = words[i];
    const word2 = words[i + 1];

    // Check invalid case: if word1 is longer and is prefix of word2
    if (word1.length > word2.length && word1.startsWith(word2)) {
      return '';
    }

    let j = 0;
    while (j < Math.min(word1.length, word2.length)) {
      if (word1[j] !== word2[j]) {
        const curSet = graph[word1[j]];
        if (!curSet.has(word2[j])) {
          curSet.add(word2[j]);
          inDegree[word2[j]]++;
        }
        break;
      }
      j++;
    }
  }

  // Topological sort
  const queue: string[] = [];
  for (const [char, degree] of Object.entries(inDegree)) {
    if (degree === 0) {
      queue.push(char);
    }
  }

  const result: string[] = [];
  while (queue.length) {
    const char = queue.shift();
    result.push(char!);
    for (const next of graph[char!]) {
      inDegree[next]--;
      if (inDegree[next] === 0) {
        queue.push(next);
      }
    }
  }

  return result.length === Object.keys(inDegree).length //
    ? result.join('') 
    : '';
}
