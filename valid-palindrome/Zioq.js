/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {

    let text = s.replace(/[^0-9a-z]/gi, '');
    text = text.replace(/\s/g, '').toLowerCase();

    const str_arr = text.split("");
    if( str_arr % 2 === 1 ) {   
        return false;
    }

    let length = str_arr.length - 1 ;
    for ( const [i, value] of str_arr.entries()) {
        if( value == str_arr[length -i] ) continue;
        if(value != str_arr[length - i]) {
            return false
        }
    }
    return true;
};

/* 
    Space Complexity - O(n) - Create a array to store elements
    Time Complexity - O(n) - Traverse through the array
*/

/* Test code */
console.log(isPalindrome("A man, a plan, a canal: Panama")); // true
console.log(isPalindrome("race a car")); // false
console.log(isPalindrome(" ")); // true
