/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
    const sort = intervals.sort((a, b) => a[0] - b[0]);

    const arr = [sort[0]];

    for (let i = 1; i < sort.length; i++) {
        const endOfArr = arr[arr.length - 1][1];

        const next = sort[i][0];

        if (endOfArr < next) {
            arr.push(sort[i]);
        } else {
            arr[arr.length - 1][1] = Math.max(arr[arr.length - 1][1], sort[i][1]);
        }
    }

    return arr;
};

// 시간복잡도 O(nlogn) -> sort 함수의 시간복잡도가 O(nlogn)이기 때문에
// 공간복잡도 O(n) -> intervals 배열을 정렬하여 arr이라는 식별자의 배열을 만들어야 하기 때문에 필요한 공간
