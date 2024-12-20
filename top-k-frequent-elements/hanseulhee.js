/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

function topKFrequent(nums, k) {
    // 숫자의 빈도를 저장할 Map 생성
    const frequency = new Map();

    // 빈도 계산
    for (const num of nums) {
        // Map에 이미 숫자가 있으면 +1, 없으면 1로 reset
        frequency.set(num, (frequency.get(num) || 0) + 1);
    }

    // 빈도 순으로 숫자 정렬 후 가장 빈도가 높은 k개의 숫자를 반환
    return [...frequency.entries()]          // entries를 이용해 Map을 배열로 변환
        .sort((a, b) => b[1] - a[1])          
        .slice(0, k)                           
        .map(entry => entry[0]);               
}
