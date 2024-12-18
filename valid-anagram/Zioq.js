/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if( s.length !== t.length ) {return false} 

    // Change string to arr
    let s_arr = s.split('');
    let t_arr = t.split('');

    let s_arr_sort = s_arr.sort();
    let t_arr_sort = t_arr.sort();

    return JSON.stringify(s_arr_sort) === JSON.stringify(t_arr_sort); // Comparison array
};
/* 
    Time Complexity: O(n log n) (dominated by sorting).
    Space Complexity: O(n) (dominated by the arrays and string representations).

*/


// console.log(isAnagram("anagram","nagaram"));
// console.log(isAnagram("rat","car"));

