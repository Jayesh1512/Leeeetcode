/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let result = init; // Start with the initial value
    for (let i = 0; i < nums.length; i++) {
        result = fn(result, nums[i]); // Apply the reducer function sequentially
    }
    return result; // Return the final accumulated value
};