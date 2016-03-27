var http = require('http');
var chalk = require('chalk');
var parseString = require('xml2js').parseString;
var striptags = require('striptags');
var blessed = require('blessed');

function getFeeds(link) {
    http.get(link, function(response) {
        var body = '';

        response.on('data', function(chunk) {
            body += chunk.toString();
        }).on('end', function() {
            parseString(body, function(err, result) {
                var root = result.rss.channel[0];
                var items = root.item;

                // TODO: parse atom xml
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

var screen = blessed.screen({
    smartCSR: true,
    title: 'RSS feeds',
    dockBorders: true
});

screen.key(['escape', 'q', 'C-c'], function() {
    return process.exit(0);
});

var rssSourcesBox = blessed.box({
    top: '0',
    left: '0',
    width: '50%',
    height: '100%',
    padding: {
        left: 1,
        right: 1
    },
    border: {
        type: 'line'
    },
    style: {
        fg: 'white',
        border: {
            fg: '#f0f0f0'
        },
        hover: {
            bg: 'green'
        }
    }
});

var feedBox = blessed.box({
    top: '0',
    left: '50%',
    width: '50%',
    height: '100%',
    keyable: true,
    padding: {
        left: 1,
        right: 1
    },
    border: {
        type: 'line'
    },
    style: {
        fg: 'white',
        border: {
            fg: '#f0f0f0'
        },
        hover: {
            bg: 'green'
        }
    }
});

var rssListWidget = blessed.List({
    keyable: true,
    focused: true,
    vi: true,
    keys: true,
    invertSelected: true,
    style: {
        selected: {
            fg: 'black',
            bg: 'blue'
        }
    }
});

var feedListWidget = blessed.List({
    keyable: true,
    vi: true,
    keys: true,
    invertSelected: true,
    style: {
        selected: {
            fg: 'black',
            bg: 'yellow'
        }
    }
});

rssListWidget.on('select', function(box, index) {
    var selectedItem = rssListWidget.getItem(index);
    feedListWidget.addItem(selectedItem.getContent());
    screen.render();
});

screen.key('+', function() {
    var promptBox = blessed.Prompt({
        left: 'center',
        top: 'center',
        width: '70%',
        height: '20%',
        border: {
            fg: 'red',
            type: 'line'
        }
    });

    screen.append(promptBox);
    promptBox.readInput('Add new feed', '', function(x, input) {
        rssListWidget.addItem(input);
        promptBox.destroy();
        screen.render();
    });
});

rssSourcesBox.append(rssListWidget);
feedBox.append(feedListWidget);

screen.append(rssSourcesBox);
screen.append(feedBox);
screen.render();
