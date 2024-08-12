type Nums = [number, number][];

/*
 * TC: O(nlogn)
 * SC: O(n)
 * */
function topKFrequent(nums: number[], k: number): number[] {
  const counting = (arr: number[]) =>
    arr.reduce((acc, n) => {
      const val = acc.get(n) ?? 0;
      acc.set(n, val + 1);
      return acc;
    }, new Map<number, number>());

  const toValues = (map: Map<number, number>) => Array.from(map.entries());

  const sorting = (arr: Nums) => arr.sort((a, b) => b[1] - a[1]);

  const getK = (arr: Nums, k: number) => arr.slice(0, k).map((v) => v[0]);

  return pipe(counting, toValues, sorting, (arr: Nums) => getK(arr, k))(nums);
}

const pipe =
  (...fns: Function[]) =>
  (x: any) =>
    fns.reduce((v, f) => f(v), x);
