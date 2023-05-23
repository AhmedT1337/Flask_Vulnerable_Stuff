from flask import Flask, request, url_for, render_template_string

import requests

app = Flask(__name__)

@app.route("/show")
def show():
    if request.args.get("url") :
        url = request.args.get("url")
        
        try : 
            content = requests.get(url).text
            return render_template_string(content)
        except :
            return "url not valid"
        
        return content
    else :
        return "please provide a value in url get argument"


@app.route("/")
def home():
    return f"""
    <h1>SSRF</h1>
                <br>
                usage:
                    <br><code>{url_for('show')}?url=&lt;url&gt;</code><br>
                <br>
    """

if __name__ == '__main__' :
    app.run(debug=True)