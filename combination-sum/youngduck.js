/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  // 작은숫자 부터 더해서, 더 큰 숫자를 더해볼필요없이 미리 리턴시키기위한용도, 중복값도 방지가능
  candidates.sort();
  const result = [];

  const sumArr = (arr) => {
    if (arr.length === 0) return 0;
    else {
      const sum = arr.reduce((acc, cur) => acc + cur);

      return sum;
    }
  };

  const backtrack = (targetArr, startIndex) => {
    const sumData = sumArr(targetArr);

    if (sumData === target) {
      result.push([...targetArr]);
      return;
    }

    for (let i = startIndex; i < candidates.length; i++) {
      if (sumData < target) {
        backtrack([...targetArr, candidates[i]], i);
      } else if (sumData > target) {
        continue;
      }
    }
  };

  // 백트랙킹 방식으로 풀예정 (재귀)
  // target보다 작을경우 계속 더함. 클경우 재귀멈춤 backtrack인수에
  // targetArr만줬더니 result에 중복값이 생김. ex) 7을만들때[2,2,3],[2,3,2]같은 중복생김
  // 자기자신 이상의 index를 타게하기위해서 startIndex
  backtrack([], 0);

  return result;
};
