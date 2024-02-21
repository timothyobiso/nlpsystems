from flask import Flask, request, render_template
from ner import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("form.html", input=open("input.txt").read())
    else:
        text = request.form['text']
        markup_paragraph = ""
        for line in get_entities_with_markup(text).split('\n'):
            if line.strip() == "":
                markup_paragraph += "<p/>\n"
            else:
                markup_paragraph += line
        return render_template("result.html",
                               markup=markup_paragraph,
                               dep_graph=get_parse_graph(text),
                               dep_table=get_parse_table(text))


@app.get('/get')
def index_get():
    return render_template("form.html", input=open("input.txt").read())

@app.post('/post')
def index_post():
    text = request.form['text']
    markup_paragraph = ""
    for line in get_entities_with_markup(text).split('\n'):
        if line.strip() == "":
            markup_paragraph += "<p/>\n"
        else:
            markup_paragraph += line
    return render_template("result.html",
                           markup=markup_paragraph,
                           dep_graph=get_parse_graph(text),
                           dep_table=get_parse_table(text))


if __name__ == '__main__':
    app.run(debug=True)
