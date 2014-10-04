var assert = require('assert');

function reverseString(text) {
    if (text === undefined || text === null) {
        return null;
    }

    text = text.toString();
    var len = text.length,
        mid = parseInt(text.length / 2),
        copy = '',
        old;

    for (var it = len - 1; it >= 0; it --) {
        copy += text[it];
    }

    return copy;
}

exports.reverseString = reverseString;
