package leetcode_study

/**
 * Set 자료 구조로 변경 후 원소의 개수를 비교해 문제 해결
 * 시간 복잡도 : O(n)
 * -> 모든 Array의 원소를 순회해야함.
 * 공간 복잡도 : O(n)
 * -> IntArray의 요소 개수에 비례하여 추가적인 공간이 필요함.
 */
fun containsDuplicate(nums: IntArray): Boolean {
    val changeSet = nums.toSet()
    return changeSet.size != nums.size
}
