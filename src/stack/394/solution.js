/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
    const regexp = /(\d+)\[(\w+)\]/;
    while (regexp.test(s)) {
        s = s.replace(regexp, (_, b, c) => c.repeat(b));
    }
    return s;
};
