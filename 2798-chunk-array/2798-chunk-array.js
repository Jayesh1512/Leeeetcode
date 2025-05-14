/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    var answer = [];
    var cur = [];

    // iterate through arr
    for (var i = 0; i < arr.length; ++i) {
        cur.push(arr[i]);

        // if subarray is of length size, push our subarray
        if (cur.length === size) {
            answer.push(cur);
            cur = [];
        }
    }
    // if we haven't pushed everything from arr, push them (aka push cur)
    if (cur.length !== 0) answer.push(cur);

    return answer;
};