/*
* HTTP Cloud Function.
*
* @param {Object} req Cloud Function request context.
* @param {Object} res Cloud Function response context.
*/
var fs = require('fs');
exports.helloHttp = function helloHttp (req, res) {
	response = "This is a sample response from your webhook!" //Default response from the webhook to show it's working
	//res.writeHead(200, {'Content-Type': 'text/css'});

	res.use(express.static(__dirname + '/public'));
	var link = res.createElement( "link" );
	link.href = "/src/style.css";
	link.type = "text/css";
	link.rel = "stylesheet";
	res.getElementsByTagName("head")[0].appendChild( link );

	res.setHeader('Content-Type', 'application/json');
	//res.write(fs.readFileSync(__dirname + 'style.css', 'utf8'));
	res.send(JSON.stringify({ "speech": response, "displayText": response 
	}));
};

