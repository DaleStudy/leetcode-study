/**
 * nums 배열에서 가장 많이 등장하는 k개의 요소를 반환하는 문제
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 *
 * 풀이
 * countObject 객체를 생성해 nums 배열의 요소를 key로, 등장 횟수를 value로 저장한다.
 * 문제는 해결 했지만,  O(n log n)의 시간복잡도로 개선할 여지가 있다.
 * 개선하기 위해서 Heap 을 사용해볼 수 있다고하는데, Heap을 사용하는 방법을 알아야겠다.
 * Heap 을 사용하면 O(n log k)의 시간복잡도로 개선할 수 있다고 한다..
 */

function topKFrequent(nums: number[], k: number): number[] {
    const countObject: { [key: number]: number } = {};

    for(const num of nums){
        countObject[num] = (countObject[num] || 0) + 1;
    }

    const sortObject = Object.entries(countObject).sort((a,b) => b[1] - a[1]);

    return sortObject.slice(0, k).map(([key]) => Number(key));
};
