function filterStr(inputString) {
    return inputString.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
}

var isPalindrome = function(s) {
    const filtered = filterStr(s);
    const reversed = filtered.split('').reverse().join('');
    return filtered === reversed;
};
