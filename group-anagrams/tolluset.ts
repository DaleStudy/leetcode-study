/* n: strs.length, m: strs.mean
 * TC: O(n * m * logm)
 * SC: O(n * m)
 * */
function groupAnagramsV2(strs: string[]): string[][] {
  const map: { [key: string]: string[] } = {};

  const strSort = (str: string) => str.split("").sort().join("");

  for (const str of strs) {
    const sortedStr = strSort(str);

    if (map[sortedStr]) {
      map[sortedStr].push(str);
    } else {
      map[sortedStr] = [str];
    }
  }

  return Object.values(map);
}

const tc1V2 = groupAnagramsV2(["eat", "tea", "tan", "ate", "nat", "bat"]); // [["bat"],["nat","tan"],["ate","eat","tea"]]
console.info("🚀 : tolluset.ts:19: tc1V2=", tc1V2);

/**
 * @FAILED - Time Limit Exceeded
 * TC: O(n^2)
 * SC: O(n)
 */
function groupAnagrams(strs: string[]): string[][] {
  const n = strs.length;

  const res: string[][] = [];

  const strSort = (str: string) => str.split("").sort().join("");

  for (let i = 0; i < n; i++) {
    const bucket: string[] = [];
    const cur = strs[i];

    if (cur === "#") {
      continue;
    }

    bucket.push(cur);

    const sortedCur = strSort(cur);

    for (let j = i + 1; j < n; j++) {
      const tmpSortedStr = strSort(strs[j]);

      if (tmpSortedStr === "#") {
        continue;
      }

      if (sortedCur === tmpSortedStr) {
        bucket.push(strs[j]);
        strs[j] = "#";
      }
    }

    strs[i] = "#";

    res.push(bucket);
  }

  return res;
}

const tc1 = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]); // [["bat"],["nat","tan"],["ate","eat","tea"]]
console.info("🚀 : tolluset.ts:7: tc1=", tc1);
