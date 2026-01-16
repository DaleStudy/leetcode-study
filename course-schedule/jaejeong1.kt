import java.util.LinkedList
import java.util.Queue

class `Course-Schedule` {
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        // 시간복잡도: O(N), 공간복잡도: O(N)

        // 그래프와 선이수 과목 개수 배열 초기화
        val adj = Array(numCourses) { mutableListOf<Int>() }
        val indegree = IntArray(numCourses)

        // 데이터 채우기 (preCourse 를 들어야 course 를 들을 수 있음)
        // indegree[course] 는 course 를 듣기 위한 선이수 과목 개수
        for (pre in prerequisites) {
            val course = pre[0]
            val preCourse = pre[1]

            adj[preCourse].add(course)
            indegree[course]++
        }

        // 선이수 과목 개수가 0인 과목을 큐에 추가
        val queue: Queue<Int> = LinkedList()
        for (i in 0 until numCourses) {
            if (indegree[i] == 0) {
                queue.offer(i)
            }
        }

        var completedCourses = 0

        while (queue.isNotEmpty()) {
            val current = queue.poll()
            completedCourses++
            // 완료한 과목을 선이수 과목으로 갖는 과목들의 선이수 과목 개수를 차감
            for (nextCourse in adj[current]) {
                indegree[nextCourse]--
                // 선이수 과목 개수가 0이 되면 큐에 추가
                if (indegree[nextCourse] == 0) {
                    queue.offer(nextCourse)
                }
            }
        }
        // 완료한 과목 개수와 입력 과목 개수가 같은지
        return completedCourses == numCourses
    }
}
