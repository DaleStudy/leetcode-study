// TC: O(N)
// SC: O(N)
function longestConsecutive(nums: number[]): number {
     let finalMaxSequence = 0;

    // O(n)
     const numsSet = new Set(nums);

    // O(n)
     for(const num of numsSet) {
        if(numsSet.has(num - 1)) {
            continue;
        }
        let currentMaxSequence = 1;
        while(numsSet.has(num + currentMaxSequence)) {
            currentMaxSequence++;
        }
        finalMaxSequence = Math.max(finalMaxSequence, currentMaxSequence);
     }

     return finalMaxSequence;
    
};