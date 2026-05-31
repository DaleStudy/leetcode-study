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

//Palindrom example: "A man, a plan, a canal: Panama"

// Using Two-pointer; It searches from given string directly so the Space complexity is O(n) - better method
// By using two index, searchs and compares from start and end of the string like this-><- 
// Do this while start index is less than end index
// Skip non-alphanumeric characters
// If both pointer are in characters, then convert to lowercase and compare
// If not equal, return false
// If all characters are equal, return true

// Time complexity = O(n), as it checks and converts to lowercase all characters in the string
// Space complexity = O(1), as it uses only a constant amount of extra space
function isPalindrome2(s: string): boolean {

    let left: number = 0;
    let right: number = s.length - 1;

    let isAlphaNum = (str: string): boolean => {
        return /^[a-zA-Z0-9]$/.test(str)
    }

    while (left < right) {
        if (!isAlphaNum(s[left])) {
            left++
            continue
        }
        if (!isAlphaNum(s[right])) {
            right--
            continue
        }
        if (s[left].toLowerCase() !== s[right].toLowerCase()) {
            return false
        }
        left++
        right--
    }
     return true
};
