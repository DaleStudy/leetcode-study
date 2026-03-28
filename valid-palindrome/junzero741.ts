// TC: O(n)
// SC: O(1)
function isPalindrome(s: string): boolean {

     let L = 0;
     let R = s.length-1;
    
    while(R > 0 && L < s.length - 1 && L <= R) {
        if(!isAlphanumeric(s[L])) {
            L++;
            continue;
        }
        if(!isAlphanumeric(s[R])) {
            R--;
            continue;
        }
        if(s[L].toLowerCase() !==  s[R].toLowerCase()) {
            return false;
        }
        L++;
        R--;
    }

    return true;
};

function isAlphanumeric(str: string): boolean {
    return /^[a-zA-Z0-9]+$/.test(str);
}
