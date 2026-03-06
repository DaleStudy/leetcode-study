import java.util.PriorityQueue

typealias Number = Int
typealias Frequency = Int

class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val frequencyMap = HashMap<Number, Frequency>(k)
        nums.forEach {
            frequencyMap.merge(it, 1, Int::plus)
        }
        val heap = PriorityQueue<Int>(frequencyMap.size) { num1, num2 ->
            frequencyMap[num2]!!.compareTo(frequencyMap[num1]!!)
        }
        heap.addAll(frequencyMap.keys)
        return IntArray(k) { heap.poll() }
    }
}
