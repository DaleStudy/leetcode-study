// # Palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring non-alphanumeric characters - letters and number).
// # the solution should first filter out non-alphanumeric characters and convert the string to lowercase.
// # Then, it should check if the cleaned string is equal to its reverse.


// Time complexity = O(n), as it checks, replaces, converts to lowercase, and reverses all characters in the string
// Space complexity = O(n), as it creates a new string with a maximum length equal to the original string
function isPalindrome(s: string): boolean {
    let filteredString: string = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    let reversed: string = filteredString.split("").reverse().join("")

    if (filteredString === reversed) {
        return true
    } else {
        return false
    }
};
