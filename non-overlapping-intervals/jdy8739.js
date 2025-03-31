/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {

    const sort = intervals.sort((a, b) => {
        if (a[1] === b[1]) {
            return a[0] - b[0];
        }

        return a[1] - b[1];
    });

    let count = 0;
    let max = sort[0][1];

    for (let i = 0; i < sort.length - 1; i++) {
        const right = sort[i + 1][0];

        if (max > right) {
            count++;
        } else {
            max = sort[i + 1][1];
        }
    }

    return count;
};

// 시간복잡도 - O(nlogn) 인터벌 뒷 숫자 정렬 시 정렬로 인한 시간복잡도 발생
// 공간복잡도 - O(1) 특별한 자료구조가 사용되지 않아 상수 공간복잡도 발생
