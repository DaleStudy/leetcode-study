/**
 * @param - candidates: 정수 배열, target: 대상 정수
 * @returns - 선택한 숫자의 합이 해당하는 모든 고유 조합 반환
 * @description
 * 1. 요소는 여러번 사용 가능
 */

function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  function recursive(remain: number, idx: number, path: number[]) {
    if (remain === 0) {
      result.push([...path]);
      return;
    }

    for (let i = idx; i < candidates.length; i++) {
      const currentNum = candidates[i];
      if (currentNum > remain) {
        break;
      }

      path.push(currentNum);
      recursive(remain - currentNum, i, path);
      path.pop();
    }
  }

  recursive(target, 0, []);
  return result;
}

const candidates = [2, 3, 5];
const target = 8;
combinationSum(candidates, target);
