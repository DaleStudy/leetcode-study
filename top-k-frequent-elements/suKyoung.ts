// 1번풀이 (brute force)
type FrequencyMap = Record<number, number>;

function topKFrequentCountDown(nums: number[], k: number): number[] {
  const freqMap = buildFrequencyMap1(nums);
  return pickTopKDescending(freqMap, k);
}

function buildFrequencyMap1(nums: number[]): FrequencyMap {
  const map: FrequencyMap = {};
  for (const num of nums) {
    map[num] = (map[num] || 0) + 1;
  }
  return map;
}

function pickTopKDescending(freqMap: FrequencyMap, k: number): number[] {
  const result: number[] = [];
  const entries = Object.entries(freqMap).map(([key, value]) => [
    Number(key),
    value,
  ]);
  let currentFrequent = Math.max(...entries.map(([_, freq]) => freq));

  while (result.length < k && currentFrequent > 0) {
    for (const [num, freq] of entries) {
      if (freq === currentFrequent) {
        result.push(num);
        if (result.length === k) break;
      }
    }
    currentFrequent--;
  }

  return result;
}


// 2번풀이(Bucket Sort)
function topKFrequent(nums: number[], k: number): number[] {
    const frequencyMap = buildFrequencyMap2(nums);
    const frequencyBuckets = buildFrequencyBuckets(nums.length, frequencyMap);

    return collectTopKFrequent(frequencyBuckets, k);
  }
  
  function buildFrequencyMap2(nums: number[]): FrequencyMap {
    const freqMap: FrequencyMap = {};
    for (const num of nums) {
      freqMap[num] = (freqMap[num] || 0) + 1;
    }
    return freqMap;
  }
  
  function buildFrequencyBuckets(
    size: number,
    freqMap: FrequencyMap
  ): number[][] {
    const buckets: number[][] = Array(size + 1).fill(null).map(() => []);
  
    for (const [numStr, frequent] of Object.entries(freqMap)) {
      const num = Number(numStr);
      buckets[frequent].push(num);
    }
  
    return buckets;
  }
  
  function collectTopKFrequent(buckets: number[][], k: number): number[] {
    const result: number[] = [];
  
    for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
      for (const num of buckets[i]) {
        result.push(num);
        if (result.length === k) break;
      }
    }
  
    return result;
  }
  

// 3번풀이 (MinHeap)
function topKFrequentHeap(nums: number[], k: number): number[] {
    const freqMap: Record<number, number> = {};
  
    for (const num of nums) {
      freqMap[num] = (freqMap[num] || 0) + 1;
    }
  
    const heap: [number, number][] = [];  
    for (const [numStr, frequent] of Object.entries(freqMap)) {
      const num = Number(numStr);
  
      heap.push([num, frequent]);
      heap.sort((a, b) => b[1] - a[1]);

      if (heap.length > k) {
        heap.pop();
      }
    }
  
    return heap.map(([num]) => num);
  }
  