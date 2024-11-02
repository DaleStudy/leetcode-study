/**
 * 정렬한 다음, 마지막 원소의 end값을 가지고 merge할지 원소 추가할지를 결정합니다.
 *
 * TC: O(N * logN)
 * 정렬에 의해 N * logN 복잡도를 갖습니다.
 *
 * SC: O(1)
 * N: intervals.length
 */

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);

  return intervals.reduce((result, current) => {
    if (result.length === 0) {
      result.push(current);
      return result;
    }

    const previous = result[result.length - 1];
    if (previous[1] >= current[0]) {
      result[result.length - 1][1] = Math.max(current[1], previous[1]);
    } else {
      result.push(current);
    }
    return result;
  }, []);
};
