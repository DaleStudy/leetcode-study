// TC: O(V + E), V = numCourses, E = prerequisites.length
// SC: O(V + E)

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  // 0: [1]
  // 1: []

  const graph = new Map<number, number[]>();

  // Initialize all courses
  for (let i = 0; i < numCourses; i++) {
    graph.set(i, []);
  }

  // Build the graph
  for (const [crs, pre] of prerequisites) {
    graph.get(crs)!.push(pre);
  }

  const traversing = new Set<number>();
  const finished = new Set<number>();

  const dfs = (crs: number): boolean => {
    if (traversing.has(crs)) return false; // cycle detected

    if (finished.has(crs)) return true; // already visited

    traversing.add(crs);

    for (const pre of graph.get(crs)!) {
      if (!dfs(pre)) return false;
    }

    traversing.delete(crs);
    finished.add(crs);

    return true;
  };

  for (const crs of graph.keys()) {
    if (!dfs(crs)) return false;
  }

  return true;
}

