from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() :
    return "just that, debugger on and werkzeug_debug_pin is set to 'off' in the environment"

app.run(debug=True)