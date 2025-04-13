/*
요구사항 : 숫자 배열에서, 2개 이상 존재하는 숫자가 있는지 확인하여, 존재하면 true, 없으면 false
문제풀이 : uniqueNums라는 빈 Set선언하고, nums을 순회하면서 uniqueNums에 숫자가 존재하지 않으면, 추가해주고,
존재하는 경우에는 2개 이상의 같은 숫자가 존재하기 때문에 순회를 중단하고 true를 반환한다.
시간복잡도 : O(n)
공간복잡도 : O(n)
*/
function containsDuplicate(nums: number[]): boolean {
    const uniqueNums = new Set<number>()
    for (const num of nums) {
        if (uniqueNums.has(num)) {
            return true
        } 
        uniqueNums.add(num)
    }
    return false
}