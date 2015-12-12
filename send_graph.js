// Create a function to log the response from the Mandrill API
function log(obj) {
    $('#response').text(JSON.stringify(obj));
}

// create a new instance of the Mandrill class with your API key
var m = new mandrill.Mandrill('9wu4qbG2pO9YHS0tU31vpg');

// create a variable for the API call parameters
var params = {
    "message": {
        "from_email":"joepbailey@gmail.com",
        "to":[{"email":"joe@merilant.com"}],
        "subject": "Trying this one more time from the Mandrill API",
        "text": "Will the Mandrill API work?"
    }
};

function sendTheMail() {
// Send the email!

    m.messages.send(params, function(res) {
        log(res);
    }, function(err) {
        log(err);
    });
}