/**
 * Runtime: 7ms, Memory: 55.02MB
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
*/

/**
 * @param {string} s
 * @return {boolean}
 */
function isPalindrome(s) {
	const alphanumeric = getAlphanumeric(s)
	return alphanumeric === alphanumeric.split("").reverse().join("")
}

function getAlphanumeric(string) {
    const number = /[0-9]/
    const alphabet = /[a-zA-Z]/
	let alphanumeric = []
    
	for (const str of string) {
		if (number.test(str) || alphabet.test(str)) {
			alphanumeric.push(str)
		}
	}
	return alphanumeric.join("").toLowerCase()
}
