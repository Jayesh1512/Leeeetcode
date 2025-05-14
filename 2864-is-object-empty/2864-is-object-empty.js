var isEmpty = function(obj) {
    for (let key in obj)
        return false;
    return true;
};