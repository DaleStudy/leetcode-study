function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const graph: number[][] = Array.from({ length: numCourses }, () => [])
    for (const [course, prereq] of prerequisites) {
        graph[course].push(prereq)
    }
    const traversing = new Set<number>()
    const finished = new Set<number>()
    
    const finish = (crs: number): boolean => {
        if (traversing.has(crs)) return false
        if (finished.has(crs)) return true

        traversing.add(crs)
        for (const pre of graph[crs]) {
            if (!finish(pre)) return false
        }
        traversing.delete(crs)
        finished.add(crs)
        return true
    }
    for (let crs = 0; crs < numCourses; crs++) {
        if (!finish(crs)) return false
    }
    return true
};
