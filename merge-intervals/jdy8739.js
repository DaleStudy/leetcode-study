/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
    const sort = intervals.sort((a, b) => a[0] - b[0]);

    const mergedIntervals = [sort[0]];

    for (let i = 1; i < sort.length; i++) {
        /** 현재 합쳐진 인터벌의 마지막 요소 */
        const lastMergedInterval = mergedIntervals[mergedIntervals.length - 1];

        const endOfMergedInterval = lastMergedInterval[1];

        const next = sort[i][0];

        if (endOfMergedInterval < next) {
            mergedIntervals.push(sort[i]);
        } else {
            lastMergedInterval[1] = Math.max(lastMergedInterval[1], sort[i][1]);
        }
    }

    return mergedIntervals;
};

// 시간복잡도 O(nlogn) -> sort 함수의 시간복잡도가 O(nlogn)이기 때문에
// 공간복잡도 O(n) -> intervals 배열을 정렬하여 arr이라는 식별자의 배열을 만들어야 하기 때문에 필요한 공간
