MAX = 25;

var arguments = process.argv.slice(2),
    howMany,
    formattedPI;

if (arguments.length == 0 || arguments.length > 1) {
    console.log("Wrong number of arguments!");
    process.exit(1);
}

howMany = parseInt(arguments[0]);
if (howMany == 0 || howMany > MAX) {
    console.log("Your value exceeds MAX: " + MAX);
    process.exit(1);
}

formattedPI = Math.PI.toFixed(howMany);
console.log(formattedPI)
