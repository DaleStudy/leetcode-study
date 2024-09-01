const twoSum = function (nums, target) {
  /* -------------------------------------------------------------------------- */
  /*                  target/2인 element가 2개 있을 경우 early return               */
  /* -------------------------------------------------------------------------- */
  let indices = [];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === target / 2) indices.push(i);
    if (indices.length === 2) break;
  }

  if (indices.length === 2) return indices;

  /* -------------------------------------------------------------------------- */
  /*                       absDNums[i] === absDNums[j]인 경우                     */
  /* -------------------------------------------------------------------------- */

  indices = []; //indices 초기화

  const dNums = nums.map((num) => num - target / 2); //nums의 각 값을 target/2 값과의 편차들로 변환
  const absDNums = dNums.map(Math.abs); //dNumbs의 각 값에 절댓값 취해주기

  const uniqueAbsDNums = new Map(); //uniqueAbsDNums은 absDNums의 각 값을 key 값으로 하고 그 key의 부호를 boolean으로 변환한 값을 value로 갖는 map임
  let j;
  for (let i = 0; i < absDNums.length; i++) {
    if (
      uniqueAbsDNums.has(absDNums[i]) && //앞에 나온 수들 중 하나와 절댓값이 같은 수 등장 (absDNums[i])
      dNums[i] > 0 != uniqueAbsDNums.get(absDNums[i]) //절댓값이 같은 이유가 앞에 나온 수들 중 하나와 아예 같은 값이어서가 아니라 부호만 반대인 수이기 때문이라는 것 체크 (두 수가 target/2로 같았다면 이 조건으로 걸러져 버리기 때문에 앞에서 early return하길 잘했음)
    ) {
      j = i;
      break;
    }
    uniqueAbsDNums.set(absDNums[i], dNums[i] > 0);
  }

  for (let i = 0; i < absDNums.length; i++) {
    // j index 앞에 나오는, absDNums[j]와 같은 절댓값을 가지는 수 찾기(위 for문에서 j를 찾은 방식 덕분에 이 수는 absDNums[j]와 절댓값은 같지만 부호는 반대인 수일 것임)
    if (absDNums[i] === absDNums[j]) {
      indices.push(i);
      indices.push(j);
      break;
    }
  }
  return indices;
};
