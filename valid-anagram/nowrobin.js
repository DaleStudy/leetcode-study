/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
        if(s.length !== t.length) return false
  return  s.split('').sort().join('') == t.split('').sort().join('')
};


