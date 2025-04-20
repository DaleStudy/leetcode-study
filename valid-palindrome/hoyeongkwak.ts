/*
time complexity : O(n)
space complexity : O(n)
*/
function isPalindrome(s: string): boolean {
    if (s.length === 1) return true
    const splitS = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase()
    const revS = splitS.split('').reverse().join('')
    return splitS === revS
};
