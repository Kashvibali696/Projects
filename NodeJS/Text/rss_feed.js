var http = require('http');
var chalk = require('chalk');
var parseString = require('xml2js').parseString;
var striptags = require('striptags');

function getFeeds(link) {
    http.get(link, function(response) {
        var body = '';

        response.on('data', function(chunk) {
            body += chunk.toString();
        }).on('end', function() {
            parseString(body, function(err, result) {
                var root = result.rss.channel[0];
                var items = root.item;

                console.log();
                console.log(chalk.green.underline.bold(root.title));
                for (var i = 0; i < items.length; ++i) {
                    var item = items[i];

                    console.log();
                    console.log('[Title] %s', chalk.blue.bold(item.title));
                    console.log(chalk.yellow(striptags(item.description[0]).trim()));
                }

            });
        });
    });
}

exports.getFeeds = getFeeds;

getFeeds('http://www.wykop.pl/rss/')
