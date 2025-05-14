/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const map = new Map();
    
    // Process arr1: add all objects to the map
    for (const obj of arr1) {
        map.set(obj.id, { ...obj });
    }
    
    // Process arr2: merge with existing objects or add new ones
    for (const obj of arr2) {
        if (map.has(obj.id)) {
            const existingObj = map.get(obj.id);
            // Merge properties, with arr2's properties overriding arr1's
            map.set(obj.id, { ...existingObj, ...obj });
        } else {
            map.set(obj.id, { ...obj });
        }
    }
    
    // Convert map values to an array and sort by id
    const joinedArray = Array.from(map.values()).sort((a, b) => a.id - b.id);
    
    return joinedArray;
};