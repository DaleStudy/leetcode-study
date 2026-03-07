
// TC: O(NlogN)
// SC: O(N)
function topKFrequent(nums: number[], k: number): number[] {
    
    /**
    Map ( O(N) )
    1 : 4
    4 : 1
    3 : 3
    2 : 2 

    -> convert it to array ( O(N) ) : [[1,4], [4,1], [3,3], [2,2]] 
    -> sort by value ( O(NlogN) ): [[1,4], [3,3], [2,2], [4,1]]
    -> slice(0,k) ( (O(N) ) : [[1,4], [3,3]] 
    -> make array from keys ( (O(N) ) : [1,4]
     */

     const numMap = new Map<number, number>();
     const n = nums.length;

     for(let i = 0; i < n; i++) {
        const num = nums[i];
        const frequency = (numMap.get(num) || 0)
        numMap.set(num, frequency + 1);
     }


    const numFrequencyArr = Array.from(numMap);
    const sortedNumFrequencyKeysArr = 
        numFrequencyArr
            .sort((a,b) => b[1]-a[1])
            .map((entry) => entry[0]);
    

     return sortedNumFrequencyKeysArr.slice(0, k)
};
