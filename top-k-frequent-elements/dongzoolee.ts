function topKFrequent(nums: number[], k: number): number[] {
  const mp: { [k: number]: number } = {};
  nums.forEach((n) => (typeof mp[n] === "number" ? mp[n]++ : (mp[n] = 1)));

  const unq_nums = [...new Set(nums)];
  unq_nums.sort((a, b) => {
    if (mp[a] === mp[b]) {
      return 0;
    }

    return mp[a] < mp[b] ? 1 : -1;
  });

  return unq_nums.slice(0, k);
}
