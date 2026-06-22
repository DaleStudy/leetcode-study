/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {

    let result = [];

    let sortedIntervals = intervals.toSorted((a, b) => a[0] - b[0]);

    for (let interval of sortedIntervals) {

        if (result.length == 0) {
            result.push(interval);
            continue;
        }

        let intervalStart = interval[0];
        let intervalEnd = interval[1];

        let lastItemInResult = result[result.length - 1];

        let start = lastItemInResult[0];
        let end = lastItemInResult[1];

        let isIntervalStartInRange = intervalStart >= start && intervalStart <= end;

        if (isIntervalStartInRange) {
            if (intervalEnd > end) {
                result[result.length - 1][1] = intervalEnd;
            }
        } else {
            result.push(interval);
        }

    }

    return result;

};
