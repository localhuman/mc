// Avoid `console` errors in browsers that lack a console.
if (!(window.console && console.log)) {
    (function() {
        var noop = function() {};
        var methods = ['assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error', 'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log', 'markTimeline', 'profile', 'profileEnd', 'markTimeline', 'table', 'time', 'timeEnd', 'timeStamp', 'trace', 'warn'];
        var length = methods.length;
        var console = window.console = {};
        while (length--) {
            console[methods[length]] = noop;
        }
    }());
}

//IE Array indexOf fix
Array.prototype.indexOf = function(obj, start) {
    for (var i = (start || 0), j = this.length; i < j; i++) {
        if (this[i] === obj) { return i; }
    }
    return -1;
}

//helper for checking array equality
//Array.prototype.compare = function(testArr) {
//    if (this.length != testArr.length) return false;
//    for (var i = 0; i < testArr.length; i++) {
//        if (this[i] instanceof Array && this[i].compare) {
//            if (!this[i].compare(testArr[i])) return false;
//        }
//        if (this[i] !== testArr[i]) return false;
//    }
//    return true;
//}

// Place any jQuery/helper plugins in here.
