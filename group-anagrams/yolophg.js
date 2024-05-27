// Time Complexity: O(n * k)
// Space Complexity: O(n * k)

var groupAnagrams = function(strs) {
    const map = new Map();
    for (const str of strs) {
        // initialize an array to count the frequency of characters.
        const count = new Array(26).fill(0); 
        // increment the count for each character.
        for (const char of str) {
            count[char.charCodeAt(0) - 'a'.charCodeAt(0)]++; 
        }
        // generate a unique key based on character frequencies.
        const key = count.join('#'); 
        // if the key exists, push the original string to its group.
        if (map.has(key)) {
            map.get(key).push(str); 
        } else { // else, create a new group with the key.
            map.set(key, [str]);
        }
    }

    // return the groups of the map as an array.
    return Array.from(map.values()); 
};
