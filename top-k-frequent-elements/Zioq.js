/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
	
	const map = new Map();
	let arr = []

	nums.forEach( e => {
		if(map.has(e)) {
			let current_value = map.get(e)
			map.set(e, current_value +1)
		} else {
			map.set(e, 1)
		}
	})
	const store = [...map.entries()].sort((a,b) => b[1] - a[1])
	for( let i = 0 ; i < k && i < store.length ; i++ ) {
		arr.push(store[i][0])
	}
	return arr
 
};


/* Test code */
console.log(topKFrequent([1,1,1,2,2,3],2)); // true
console.log(topKFrequent([1,2],1)); // true
