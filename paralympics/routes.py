from flask import current_app as app


@app.route('/')
#@app.route("/<name>")
def hello(name=None):
    return f"Hello!"

