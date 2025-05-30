/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if (s.length === 0 || t.length === 0) return "";
    
    const dictT = {};
    for (let char of t) {
        dictT[char] = (dictT[char] || 0) + 1;
    }
    
    const required = Object.keys(dictT).length;
    let formed = 0;
    
    const windowCounts = {};
    
    let left = 0, right = 0;
    
    let minLen = Infinity;
    let minLeft = 0, minRight = 0;
    
    while (right < s.length) {
        const character = s[right];
        windowCounts[character] = (windowCounts[character] || 0) + 1;
        
        if (dictT[character] && windowCounts[character] === dictT[character]) {
            formed++;
        }
        
        while (left <= right && formed === required) {
            const currentLen = right - left + 1;
            
            if (currentLen < minLen) {
                minLen = currentLen;
                minLeft = left;
                minRight = right;
            }
            
            const leftChar = s[left];
            windowCounts[leftChar]--;
            
            if (dictT[leftChar] && windowCounts[leftChar] < dictT[leftChar]) {
                formed--;
            }
            
            left++;
        }
        
        right++;
    }
    
    return minLen === Infinity ? "" : s.substring(minLeft, minRight + 1);
};