class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val indexMap = nums.mapIndexed { index, num -> num to index }
            .groupBy({ it.first }, {it.second})

        indexMap.forEach { (firstNum, firstIndicies) ->
            val secondNum = target - firstNum
            if (firstNum == secondNum) {
                if (firstIndicies.size > 1) {
                    return intArrayOf(firstIndicies[0], firstIndicies[1])
                }
            } else {
                val secondIndicies = indexMap[secondNum]
                if (secondIndicies != null) {
                    return intArrayOf(firstIndicies[0], secondIndicies[0])
                }
            }
        }
        
        return intArrayOf()
    }
}
