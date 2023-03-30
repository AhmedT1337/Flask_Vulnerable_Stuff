from flask import Flask, render_template, request

@app.route("/user")
def user() :
    name = request.args.get("name")
    return render_template("user.html", name=name)

"""
OR you can use this code :
from flask import Flask, render_template, request, escape


@app.route("/user")
def user() :
    name = request.args.get("name")
    return f"<h1>Hello {escape(name)}</h1>"


if __name__ == '__main__':
    app.run()
    
"""

if __name__ == '__main__':
    app.run()
