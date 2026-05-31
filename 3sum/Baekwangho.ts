/**
합산이 0이 되는 서로소 조합을 찾아야 한다.. 좌표가 다른 같은 값은 허용하되,
같은 수로 구성된 조합은 중복을 불허한다.

기본적으로 3가지 수를 중복없이 조합해서 뽑은 다음, 정렬을 사용하여 set 으로 구분할 수 있지 않을까?


function threeSum(nums: number[]): number[][] {
  const arraySet = new Set<string>();

  for (let i = 0; i <= nums.length - 3; i++) {
    for (let j = i + 1; j <= nums.length - 2; j++) {
      for (let k = j + 1; k <= nums.length - 1; k++) {
        if (nums[i] + nums[j] + nums[k] === 0) {
          const sorted = [nums[i], nums[j], nums[k]];
          sorted.sort((a, b) => a - b);
          const string = sorted.join("#");
          arraySet.add(string);
        }
      }
    }
  }

  return Array.from(arraySet).map((el) =>
    el.split("#").map((el) => Number(el))
  );
}
 */

/**
시간 초과해버렸다. 어떻게 효율적으로 풀 수 있을까?
two sum 을 보니 해시테이블을 쓴다고 한다. nums 를 해시테이블로 변환하고,
이중 반복문에서 이를 활용해보자.

function threeSum(nums: number[]): number[][] {
  const arraySet = new Set<string>();
  const hash = new Map<number, number[]>();
  nums.forEach((val, idx) => {
    const idxes = hash.get(val);
    if (idxes && idxes.length) {
      hash.set(val, [...idxes, idx]);
    } else {
      hash.set(val, [idx]);
    }
  });

  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      const idxes = hash.get(0 - (nums[i] + nums[j]));

      idxes?.forEach((idx) => {
        if (idx != i && idx != j) {
          const sorted = [nums[i], nums[j], nums[idx]];
          sorted.sort((a, b) => a - b);
          const string = sorted.join("#");
          arraySet.add(string);
        }
      });
    }
  }

  return Array.from(arraySet).map((el) =>
    el.split("#").map((el) => Number(el))
  );
}

 */

/**
... 0으로만 가득찬 배열에서 time limit 이 발생했다.
풀이를 보고오니, 위 로직에서 0으로 가득찬 arraySet 을 순회하는 곳에서 결국 O(n^3) 이 되어버린다는 점을 확인할 수 있었다.
확실한 것은, 정렬을 추가했을 경우 위 로직도 통과 가능한 정도로 만들어볼 수 있지 않을까 싶었다.

function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);
  const arraySet = new Set<string>();
  const hash = new Map<number, number[]>();

  nums.forEach((val, idx) => {
    const idxes = hash.get(val);
    if (idxes && idxes.length) {
      hash.set(val, [...idxes, idx]);
    } else {
      hash.set(val, [idx]);
    }
  });

  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      const idxes = hash.get(0 - (nums[i] + nums[j])) ?? [];

      for (let k = 0; k < idxes.length; k++) {
        const idx = idxes[k];
        if (idx != i && idx != j) {
          const sorted = [nums[i], nums[j], nums[idx]];
          sorted.sort((a, b) => a - b);
          const string = sorted.join("#");
          arraySet.add(string);

          break;
        }
      }
    }
  }

  return Array.from(arraySet).map((el) =>
    el.split("#").map((el) => Number(el))
  );
}

근데 어떻게든 못만듦.
 */

/**
어제 해답을 보았으니, 다시한번 풀어보자.
핵심은 투 포인터를 사용하는 것, 자료구조에 얽메이지 않는 것
 */

function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);
  const results = [];

  // [-4, -1, -1, 0, 1, 2]
  for (let i = 0; i < nums.length; i++) {
    while (nums[i - 1] === nums[i]) i++;

    let low = i + 1;
    let high = nums.length - 1;
    while (low < high) {
      const sum = nums[i] + nums[low] + nums[high];
      if (sum < 0) {
        low++;
      } else if (sum > 0) {
        high--;
      } else {
        while (nums[high] === nums[high - 1]) high--;
        while (nums[low] === nums[low + 1]) low++;
        results.push([nums[i], nums[low], nums[high]]);
        low++;
        high--;
      }
    }
  }

  return results;
}
