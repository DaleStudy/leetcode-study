/**
 * Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear
 * 
 * Example 1:
 * Input: ["lint","code","love","you"]
 * Output: ["lint","code","love","you"]
 * Explanation:
 * One possible encode method is: "lint:;code:;love:;you"
 * 
 * Example 2:
 * Input: ["we", "say", ":", "yes"]
 * Output: ["we", "say", ":", "yes"]
 * Explanation:
 * One possible encode method is: "we:;say:;:::;yes"
 * 
 * 
 * 
 * encode: 
 * result = ""
 * loop strs,
 * 
 *  loop str,
 *      char to charCode
 *      not last str AND last char ? charCode + "*"
 *      not last str AND not last char ?  charCode + "+"
 * 
 * 
 * 
 * decode:
 * strs = []
 * split str with "*",  => ["12+79+NaN", "92+32"]
 * split each element with "+", => [ ["12", "79", "NaN"], ["92", "32"] ]
 * loop outer array,
 *  str = null
 *  loop inner array,
 *      element is "NaN" ? ""
 *      element is not "NaN" ? String.fromCharCode(Number(element))
 *      str += 
 *  str is not null ? strs.push(str)
 *  
 */

// TC: O(N)
// SC: O(N)
class Solution {
    encode (strs: string[]): string {
        return strs.map((str) => {
            if(str.length === 0) {
                return "EMPTY"
            }
            const codes = [];
            for(let i = 0; i < str.length; i++) {
                codes.push(str.charCodeAt(i));
            }
            return codes.join('+');
        }).join("*")

    }

    decode(str: string): string[] {
        if(str.length === 0) {
            return [];
        }

        return str.split("*").map((encodedStr) => {
            if(encodedStr === "EMPTY") {
                return "";
            }

            return encodedStr
                    .split("+")
                    .map((code) => String.fromCharCode(Number(code)))
                    .join("");
        })
    }
}
const solution = new Solution();



const tc = [
    ["lint","code","love","you"], // "72+79+80+94*12+34+56+78*"
    ["we", "say", ":", "yes"],
    ["", "a", "", "b"], // "NaN*74*NaN*75"
    [";::''',,,,.....", ".....,,,,'''::;"],
]

function runTc(tc: string[]): boolean {
    const encoded = solution.encode(tc);
    const decoded = solution.decode(encoded);
    if(tc.length !== decoded.length) {
        return false;
    }
    
    return tc.every((el, idx) => el === decoded[idx]);
}

const totalTc = tc.length;
const failedTc = tc.reduce((acc, cur) => runTc(cur) ? acc : acc+1, 0);

console.log(`success: ${totalTc-failedTc}/${totalTc}`);

