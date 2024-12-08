/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let map = new Map(); // key에는 해당되는 숫자, value에는 해당되는 숫자의 갯수

    // 숫자별 빈도수
    nums.forEach((num) => {
        map.set(num, (map.get(num) || 0) + 1);
    });

    // 결과를 배열로 바꿔주고 내림차순 정렬
    let sortedResult = Array.from(map.entries()).sort((a,b) => b[1] - a[1]);
    //console.log(sortedResult);
    //console.log(sortedResult.slice(0,k));

    // k갯수의 숫자 반환
    return sortedResult.slice(0,k).map(item => item[0]);
};

// 여기서 위 코드의 시간복잡도와 공간복잡도를 생각해보자...
// 시간복잡도 => O(m log m) ** 더 개선할 방법 찾아보기
// forEach 통한 배열 순회: 배열의 크기가 n이라고 한다면 O(n)
// sortedResult (정렬): O(m log m)
// k갯수의 숫자 반환: k개 항목에 대해 연산하니까 O(k)

// 공간복잡도 => O(n)
// map의 크기: 배열의 크기가 n이라고 한다면 O(n)
// sortedResult: O(m)
// k개 숫자 저장: O(k)
