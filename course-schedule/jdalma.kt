package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `course-schedule` {

    /**
     * TC: O(node + edge), SC: O(node + edge)
     */
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        if (prerequisites.isEmpty()) return true

        return usingTopologySort(numCourses, prerequisites)
    }

    private fun usingTopologySort(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        val adj = List(numCourses) { mutableListOf<Int>() }
        val degree = IntArray(numCourses)
        for (e in prerequisites) {
            val (course, pre) = e[0] to e[1]
            adj[pre].add(course)
            degree[course]++
        }

        val queue = ArrayDeque<Int>().apply {
            degree.forEachIndexed { index, i ->
                if (i == 0) {
                    this.add(index)
                }
            }
        }

        var answer = 0
        while (queue.isNotEmpty()) {
            val now = queue.removeFirst()
            answer++

            queue.addAll(adj[now].filter { --degree[it] == 0 })
        }

        return answer == numCourses
    }

    @Test
    fun `코스의 개수와 코스 간 의존성을 전달하면 코스를 완료할 수 있는지 여부를 반환한다`() {
        canFinish(5,
            arrayOf(
                intArrayOf(0,1),
                intArrayOf(0,2),
                intArrayOf(1,3),
                intArrayOf(1,4),
                intArrayOf(3,4)
            )
        ) shouldBe true
        canFinish(5,
            arrayOf(
                intArrayOf(1,4),
                intArrayOf(2,4),
                intArrayOf(3,1),
                intArrayOf(3,2)
            )
        ) shouldBe true
        canFinish(2, arrayOf(intArrayOf(1, 0))) shouldBe true
        canFinish(2, arrayOf(intArrayOf(1, 0), intArrayOf(0, 1))) shouldBe false
        canFinish(20,
            arrayOf(
                intArrayOf(0,10),
                intArrayOf(3,18),
                intArrayOf(5,5),
                intArrayOf(6,11),
                intArrayOf(11,14),
                intArrayOf(13,1),
                intArrayOf(15,1),
                intArrayOf(17,4)
            )
        ) shouldBe false
    }
}
