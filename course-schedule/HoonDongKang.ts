/**
 * [Problem]: [207] Course Schedule
 * (https://leetcode.com/problems/course-schedule/description/)
 */

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // 시간복잡도 O(n+m)
    // 공간복잡도 O(n+m)
    function graphFunc(numCourses: number, prerequisites: number[][]): boolean {
        const graph: number[][] = Array.from({ length: numCourses }, () => []);

        for (const [course, prerequisite] of prerequisites) {
            graph[prerequisite].push(course);
        }

        let traversing = new Array(numCourses).fill(false);
        let visited = new Array(numCourses).fill(false);

        function dfs(course: number): boolean {
            if (traversing[course]) return false;
            if (visited[course]) return true;

            traversing[course] = true;
            for (let pre of graph[course]) {
                if (!dfs(pre)) {
                    return false;
                }
            }

            traversing[course] = false;
            visited[course] = true;
            return true;
        }

        for (let i = 0; i < numCourses; i++) {
            if (!visited[i] && !dfs(i)) {
                return false;
            }
        }
        return true;
    }
}
