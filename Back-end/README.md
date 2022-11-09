#!Before start on Windows!
Go to Back-end directory in cmd and type in:
$ py -3 -m venv venv 
$ venv\Scripts\activate
$ pip install Flask

#!Before start on MacOS/Linux!
Go to Back-end directory in cmd and type in:
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask

#!If Vue isn't downloaded then!
npm install -g @vue/cli
## OR
yarn global add @vue/cli

To run: $flask --app main run
Debug mode: $flask --app main --debug run


!!HMTL Escaping!!

from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

!!HMTL Escaping!!
