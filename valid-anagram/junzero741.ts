// TC: O(n)
// SC: O(n)
function isAnagram(s: string, t: string): boolean {
     if(s.length !== t.length) {
        return false;
     } 

     const sMap = new Map<string, number>();
     const tMap = new Map<string, number>();

     for(let i = 0; i < s.length; i++) { // TC: O(N), SC: O(N)
        const sChar = s[i];
        const tChar = t[i];
        const sCharCount = sMap.get(sChar) || 0;
        const tCharCount = tMap.get(tChar) || 0;
        
        sMap.set(sChar, sCharCount + 1);
        tMap.set(tChar, tCharCount + 1);
     }

     for(let i = 0; i < s.length; i++) { // TC: O(N), SC: O(1)
        const char = s[i];

        if(sMap.get(char) !== tMap.get(char)) {
            return false;
        }
     }

     return true;
};
