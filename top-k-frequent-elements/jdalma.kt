package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import java.util.PriorityQueue

class `top-k-frequent-elements` {

    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        return third(nums, k)
    }

    // Map 정렬
    private fun first(nums: IntArray, k: Int): IntArray {
        val map = mutableMapOf<Int, Int>()

        nums.forEach {
            map.compute(it) { _, oldValue ->
                if (oldValue == null) 1
                else oldValue + 1
            }
        }

        return map.entries.sortedByDescending { it.value }
            .map { it.key }
            .slice(0 until k)
            .toIntArray()
    }

    // 우선순위 큐 사용
    private fun second(nums: IntArray, k: Int): IntArray {
        val map = mutableMapOf<Int, Int>()

        nums.forEach { map.put(it, map.getOrDefault(it, 0) + 1) }

        val heap: PriorityQueue<Map.Entry<Int, Int>> = PriorityQueue<Map.Entry<Int, Int>> {
            v1, v2 -> v2.value.compareTo(v1.value)
        }.apply {
            this.addAll(map.entries)
        }

        return (0 until k).map { heap.poll().key }.toIntArray()
    }

    // 이차원배열로 빈번도 저장
    private fun third(nums: IntArray, k: Int): IntArray {
        val map = mutableMapOf<Int, Int>()

        nums.forEach { map.put(it, map.getOrDefault(it, 0) + 1) }

        val freq = Array<MutableList<Int>>(nums.size + 1) { mutableListOf() }
        map.entries.forEach {
            val frequency = it.value
            freq[frequency].add(it.key)
        }

        val result = IntArray(k)
        var index = 0
        (freq.size - 1 downTo 0).forEach { i ->
            freq[i].forEach {
                result[index++] = it
                if (index == k) {
                    return result
                }
            }
        }

        return IntArray(0)
    }

    @Test
    fun `배열에서_가장_빈도가_높은_K개의_원소를_출력한다`() {
        topKFrequent(intArrayOf(1,1,1,2,2,3), 2) shouldBe intArrayOf(1,2)
        topKFrequent(intArrayOf(1,1,1,2,2,3,3,4), 3) shouldBe intArrayOf(1,2,3)
        topKFrequent(intArrayOf(2,2,3,3,1,1,4), 3) shouldBe intArrayOf(2,3,1)
        topKFrequent(intArrayOf(4,1,-1,2,-1,2,3), 2) shouldBe intArrayOf(-1,2)
    }
}
