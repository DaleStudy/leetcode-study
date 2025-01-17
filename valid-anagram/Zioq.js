/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if( s.length !== t.length ) {return false} 

    // Change string to arr
    // let s_arr = s.split('');
    // let t_arr = t.split('');
    /* WHAT IF SORT IS NOT ALLOWED */
    // let s_arr_sort = s_arr.sort();
    // let t_arr_sort = t_arr.sort();
    // return JSON.stringify(s_arr_sort) === JSON.stringify(t_arr_sort); // Comparison array


    // Use map to count characters in the s
    // And remove character with t from map

    const map = new Map();

    for (let c of s) {
        map[c] = (map[c] || 0) + 1;
    }

    for (let c of t) {
        if (!map[c]) return false;
        map[c]--;
    }

    return true;    
};
/* 
    Time Complexity: O(n)
    Space Complexity: O(n)
*/


console.log(isAnagram("anagram","nagaram"));
console.log(isAnagram("rat","car"));

