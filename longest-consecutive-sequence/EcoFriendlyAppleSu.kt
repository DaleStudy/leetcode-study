package leetcode_study

/**
 * HashSet을 사용한 풀이.
 * 시간 복잡도 O(n)
 * -> Loop를 두 번 돌기 때문에 O(n^2)이라고 생각할 수 있으나 최악의 상황이여도 O(n + (n-1))로 O(n)이 됨.
 * -> 1 부터 10억까지의 연속된 수가 Set 자료구조에 담겨 있고 최악의 상황으로 1이 마지막 순번에 뽑힌다고 가정했을 때, (Set은 순서가 존재하지 않음)
 * -> 1 부터 Longest Count 하더라도 주어진 nums에서 n 번 set에서 10억 -1번을 순회하므로 O(n^2)이 아닌 O(n)이 됨.
 */
fun longestConsecutive(nums: IntArray): Int {
    val numSet: HashSet<Int> = nums.toHashSet()
    var longest = 0

    for (num in nums) {
        // 현재 요소보다 크기가 1 작은 숫자를 갖고 있다면 현재 요소는 최소값이 아니므로 다음으로 넘어감
        if (numSet.contains(num -1)) {
            continue
        }
        // 현재 요소보다 1 작은 연속된 숫자가 없으므로 현재 원소를 1 카운트 한 length 할당
        var length = 1
        while (numSet.contains(num + length)) {
            length++
        }
        longest = max(longest, length)
    }
    return longest
}

/**
 * Time Limit 발생.
 * 시간 복잡도 O(n^2)
 * -> nums 안에 존재하는 요소마다 중복을 포함한 Loop(while) 진행
 */
fun longestConsecutive01(nums: IntArray): Int {
    // 결과를 담을 리스트
    val resultList = mutableListOf<Int>()

    // 1차 loop
    for (i in nums.indices) {
        var tempResult = 0
        var currentNum = nums[i]
        // 2차 loop
        while (true) {
            if (nums.contains(currentNum)) {
                tempResult += 1
                currentNum += 1
            } else {
                break
            }
        }
        resultList.add(tempResult)
    }
    if (resultList.isEmpty()) {
        return 0
    }
    return resultList.max()
}
