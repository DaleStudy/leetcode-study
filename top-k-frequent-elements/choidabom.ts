// https://leetcode.com/problems/top-k-frequent-elements/

// TC: O(nlogn)
// SC: O(n)

function topKFrequent(nums: number[], k: number): number[] {
    const map = new Map()

    for (const num of nums) {
      if (map.has(num)){
        map.set(num, map.get(num) + 1)
      } else {
        map.set(num, 1)
      }
    }

    const sortedMap = [...map].sort((a, b)=> b[1]- a[1]) 
    return sortedMap.splice(0, k).map((item)=> item[0])
};
