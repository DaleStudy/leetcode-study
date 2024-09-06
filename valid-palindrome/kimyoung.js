var isPalindrome = function (s) {
    let left = 0, right = s.length - 1;
    while (left < right) {
        while (left < right && !isAlphaNumeric(s[left])) { // increment the left index until it's an alphanumeric character
            left++;
        }
        while (left < right && !isAlphaNumeric(s[right])) { // decrement the right index until it's an alphanumeric character
            right--;
        }
        if (s[left++].toLowerCase() !== s[right--].toLowerCase()) return false; // compare the two string values, if different return false;
    }
    return true;
};

function isAlphaNumeric(char) { // use ASCII code to findout if char is alphanumeric or not
    const asciiCode = char.charCodeAt(0);
    return (asciiCode >= 65 && asciiCode <= 90) ||
        (asciiCode >= 97 && asciiCode <= 122) ||
        (asciiCode >= 48 && asciiCode <= 57)
}

// time - O(n) iterate through the string once
// space - O(1) no extra space created
