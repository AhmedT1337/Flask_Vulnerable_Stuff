from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def user() :
    name = request.args.get("name")
    page = f"<h1>Hello {name}</h1>"
    return render_template_string(page)


if __name__ == '__main__':
    app.run()