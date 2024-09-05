package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `longest-consecutive-sequence` {
    fun longestConsecutive(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        return usingUnionFind(nums)
    }

    /**
     * 1. 배열을 정렬하여 순서대로 순회하며 연속 수열 길이를 확인한다.
     * TC: O(n * log(n)), SC: O(1)
     */
    private fun usingSort(nums: IntArray): Int {
        nums.sort()

        var (length, maxLength) = 1 to 0
        for (index in 0 until nums.size - 1) {
            if (nums[index] == nums[index + 1]) {
                continue
            } else if (nums[index] + 1 == nums[index + 1]) {
                length++
            } else {
                maxLength = max(length, maxLength)
                length = 1
            }
        }
        return max(length, maxLength)
    }

    /**
     * 2. Set의 자료구조를 활용하여 가장 작은 값부터 while문을 통한 최대 증가 값을 반환한다.
     * TC: O(n), SC: O(n)
     */
    private fun usingSet(nums: IntArray): Int {
        val numberSet = nums.toSet()
        var maxLength = 0

        for (number in nums) {
            if (numberSet.contains(number - 1)) {
                continue
            }
            var length = 1
            while (numberSet.contains(number + length)) {
                length++
            }
            maxLength = max(maxLength, length)
        }

        return maxLength
    }

    /**
     * 3. Union-Find
     * TC: O(n), SC: O(n)
     */
    private fun usingUnionFind(nums: IntArray): Int {
        val nodes = mutableMapOf<Int, Int>()
        val dsu = DSU(nums.size)

        for ((i,n) in nums.withIndex()) {
            if (n in nodes) continue

            nodes[n - 1]?.let { dsu.union(i, it) }
            nodes[n + 1]?.let { dsu.union(i, it) }

            nodes[n] = i
        }

        return dsu.maxLength()
    }

    @Test
    fun `입력받은 정수 배열의 최대 연속 수열 길이를 반환한다`() {
        longestConsecutive(intArrayOf()) shouldBe 0
        longestConsecutive(intArrayOf(100,4,200,1,3,2)) shouldBe 4
        longestConsecutive(intArrayOf(11,23,12,13,14,21)) shouldBe 4
        longestConsecutive(intArrayOf(0,3,7,2,5,8,4,6,0,1)) shouldBe 9
        longestConsecutive(intArrayOf(11,64,43,12,13,10,9,8,7)) shouldBe 7
    }
}

class DSU(val n: Int) {
    private val parent = IntArray(n) { it }
    private val size = IntArray(n) { 1 }

    private fun find(x: Int): Int {
        if (parent[x] != x)
            parent[x] = find(parent[x])
        return parent[x]
    }

    fun union(x: Int, y: Int) {
        val root = find(x)
        val child = find(y)
        if(root != child) {
            parent[child] = root
            size[root] += size[child]
        }
    }

    fun maxLength(): Int {
        var res = 0
        for (i in parent.indices) {
            if (parent[i] == i)
                res = maxOf(res, size[i])
        }
        return res
    }
}
