// week 2's goal
// only focusing on not using for... not a good approach :(

function isAnagram(s: string, t: string): boolean {
    if(s.length !== t.length) return false
    let sArray : string[] = s.split('').sort()
    s = sArray.join('')
    let tArray : string[] = t.split('').sort()
    t = tArray.join('')
    if(s === t) return true
    else return false
};

// reflection: not to be hurry & have more time for pondering
