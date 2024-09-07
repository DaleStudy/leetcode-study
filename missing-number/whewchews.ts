/*
* 조건 
* [0, n] 중에 없는 값을 리턴, n == nums.length
* 모든 값은 unique

* 아이디어
* => nums.length는 실제 배열 index보다 1이 더 크기 때문에  항상 없는 값이 1개 존재함
* 0부터 n까지의 모든 값을 set에 저장해둔다.
* set 자료구조를 사용하는 이유는 
* 1. nums에 들어오는 값이 중복값이 존재하지 않기 때문
* 2. 같은 동작을 배열에서 하게 되면
* 각 인덱스를 1로 두고 값이 있을때마다 0으로 변경, 1이 있는 index를 찾음으로 풀 수 있음
* => 이 경우, 남은 값을 찾을 때 배열을 한번 다 돌아야 해서 시간복잡도가 O(n) 더 소요됨.
* nums 배열을 돌며 값이 있을때 마다 set에서 값을 삭제한다.
* set에서 남은 값을 찾아 리턴해준다.
* 
*/
function missingNumber(nums: number[]): number {
  // TC: O(n)
  // SC: O(n)
  const numSet: Set<number> = new Set(
    Array(nums.length + 1)
      .fill(0)
      .map((v, i) => i)
  );

  // TC: O(n)
  nums.forEach((n) => {
    numSet.delete(n);
  });

  // TC: O(1)
  // SC: O(1)
  const [lastNum] = numSet.values();
  return lastNum;
}

// TC: O(n)
// SC: O(n)
