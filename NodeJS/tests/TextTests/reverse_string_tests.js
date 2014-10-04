var strModule = require("../../Text/reverse_string");

exports['reverseStringTest'] = function(test) {
    test.equal(strModule.reverseString('test'), 'tset');
    test.equal(strModule.reverseString('siemka'), 'akmeis');
    test.equal(strModule.reverseString(), null);
    test.equal(strModule.reverseString(''), '');
    test.equal(strModule.reverseString(45), '54');
    test.done();
}