!Before start on Windows!
Go to Back-end directory in cmd and type in:
$ venv\Scripts\activate

!Before start on MacOS/Linux!
Go to Back-end directory in cmd and type in:
$ . venv/bin/activate

To run: $flask --app main run
Debug mode: $flask --app main --debug run

!!HMTL Escaping!!

from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

!!HMTL Escaping!!