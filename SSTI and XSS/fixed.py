from flask import Flask, render_template, request

@app.route("/user")
def user() :
    name = request.args.get("name")
    return render_template("user.html", name=name)

if __name__ == '__main__':
    app.run()