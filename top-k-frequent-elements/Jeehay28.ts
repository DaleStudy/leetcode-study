// Approach 2: Min-Heap
// ⏳ Time Complexity: O(n log(k))
// 💾 Space Complexity: O(n)

function topKFrequent(nums: number[], k: number): number[] {
  const map = new Map<number, number>();
  // step 1: count frequency of each number
  for (const num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
  }

  // step 2: use a min-heap to keep only top k frequent elements
  // A Min-Heap is a special type of binary heap (tree-based data structure) where:
  // The smallest element is always at the root (top).

  const minHeap: [number, number][] = [];

  // Time Complexity: O(n log k)
  // Sorting is within a fixed size k which is much smaller than O(n log n) sorting all elements.
  for (const [num, freq] of map.entries()) {
    if (minHeap.length < k) {
      minHeap.push([num, freq]);
      minHeap.sort((a, b) => a[1] - b[1]);
    } else if (freq > minHeap[0][1]) {
      minHeap.shift(); // Remove smallest frequency
      minHeap.push([num, freq]);
      minHeap.sort((a, b) => a[1] - b[1]);
    }
  }

  // step 3: extract the top k freqeuent elements from the heap
  return minHeap.map(([num, freq]) => num);
}


// Approach 1: Map & Sorting (Using Map in TypeScript)
// ⏳ Time Complexity: O(n log(n))
// 💾 Space Complexity: O(n)
// function topKFrequent(nums: number[], k: number): number[] {

//     const map = new Map<number, number>()

//     for (const num of nums) {
//         map.set(num, (map.get(num) || 0) + 1);
//     }

//     // const sorted = [...map.entries()].sort((a, b) => b[1] - a[1]);
//     const sorted = Array.from(map).sort((a, b) => b[1] - a[1]);

//     return sorted.slice(0, k).map(item => item[0]);
// };

