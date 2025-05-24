/**
 * @param {string} s
 * @return {boolean}
 */

const BRACKETS = {
    SMALL_LEFT : '(',
    SMALL_RIGHT : ')',
    MIDIDUM_LEFT : '{',
    MIDIDUM_RIGHT : '}',
    LARGE_LEFT : '[',
    LARGE_RIGHT : ']',
};

const LEFT_BRAKCETS_SET = new Set([BRACKETS.SMALL_LEFT, BRACKETS.MIDIDUM_LEFT, BRACKETS.LARGE_LEFT]);

const BRACKET_MAPPER = {
    [BRACKETS.SMALL_RIGHT]: BRACKETS.SMALL_LEFT,
    [BRACKETS.MIDIDUM_RIGHT]: BRACKETS.MIDIDUM_LEFT,
    [BRACKETS.LARGE_RIGHT]: BRACKETS.LARGE_LEFT,
};

var isValid = function(s) {
    const stack = [];

    for (const bracket of s) {
        if (LEFT_BRAKCETS_SET.has(bracket)) {
            stack.push(bracket);
        } else {
            const poppedBracekt = stack.pop();

            if (poppedBracekt !== BRACKET_MAPPER[bracket]) {
                return false;
            }
        }
    }

    return stack.length === 0;
};
