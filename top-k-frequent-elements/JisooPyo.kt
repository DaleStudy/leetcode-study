package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import java.util.*

/**
 * Leetcode
 * 347. Top K Frequent Elements
 * Medium
 */
class TopKFrequentElements {
    /**
     * Runtime: 30 ms(Beats: 68.62 %)
     * Time Complexity: O(n log n)
     *   - list 정렬
     *
     * Memory: 42.20 MB(Beats: 58.82 %)
     * Space Complexity: O(n)
     */
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val countMap: MutableMap<Int, Int> = HashMap()

        for (num in nums) {
            countMap[num] = countMap.getOrDefault(num, 0) + 1
        }

        val list = mutableListOf<Node>()
        for (key in countMap.keys) {
            list.add(Node(key, countMap[key]!!))
        }
        list.sortDescending()

        val answer = IntArray(k)
        for (i in 0 until k) {
            answer[i] = list[i].value
        }
        return answer
    }

    /**
     * 개선된 버전: 우선순위 큐를 사용
     *
     * Runtime: 19 ms(Beats: 96.30 %)
     * Time Complexity: O(n log n)
     *
     * Memory: 44.83 MB(Beats: 18.35 %)
     * Space Complexity: O(n)
     */
    fun topKFrequent2(nums: IntArray, k: Int): IntArray {
        val countMap = nums.groupBy { it }
            .mapValues { it.value.size }

        val pq = PriorityQueue<Node>(compareByDescending { it.count })
        countMap.forEach { (num, count) ->
            pq.offer(Node(num, count))
        }

        return IntArray(k) { pq.poll().value }
    }

    data class Node(var value: Int, var count: Int) : Comparable<Node> {
        override fun compareTo(other: Node): Int {
            return this.count.compareTo(other.count)
        }
    }

    @Test
    fun test() {
        topKFrequent(intArrayOf(1, 1, 1, 2, 2, 3), 2) shouldBe intArrayOf(1, 2)
        topKFrequent(intArrayOf(1), 1) shouldBe intArrayOf(1)

        topKFrequent2(intArrayOf(1, 1, 1, 2, 2, 3), 2) shouldBe intArrayOf(1, 2)
        topKFrequent2(intArrayOf(1), 1) shouldBe intArrayOf(1)
    }
}
