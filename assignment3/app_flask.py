from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from ner import *
from collections import Counter

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

LENGTH = 200


class Relation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(db.String(LENGTH), nullable=False)
    child = db.Column(db.String(LENGTH), nullable=False)
    rel = db.Column(db.String(LENGTH), nullable=False)

    def __repr__(self):
        return f"Relation('{self.parent}'---'{self.rel}'-->'{self.child}')"

    def __hash__(self):
        return hash((self.parent, self.child, self.rel))

    def __eq__(self, other):
        return self.parent == other.parent and self.child == other.child and self.rel == other.rel

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("form.html", input=open("input.txt").read())
    else:
        text = request.form['text']
        markup_paragraph = ""
        for line in get_entities_with_markup(text).split('\n'):
            if line.strip() == "":
                markup_paragraph += "</p>\n"
            else:
                markup_paragraph += line
        session['ents'] = get_entities(text)
        for ent in get_parse(text):
            db.session.add(Relation(parent=ent[2], child=ent[0], rel=ent[1]))
            db.session.commit()
        return render_template("result.html",
                               markup=markup_paragraph,
                               dep_graph=get_parse_graph(text),
                               dep_table=get_parse_table(text))


@app.route('/db', methods=['GET'])
def db_page():
    entities = session.get('ents', [])


    table = "<table><tr><th><Entity></th><th>Parent</th><th>Relation</th><th>Child</th><th>Count></tr>"
    for ent in entities:
        table += "<tr><td>%s</td>" % ent[2]
        first = True
        relations = Counter(Relation.query.where(Relation.child.in_([str(s) for s in nlp(ent[2])])).all())
        print(relations)
        for r in relations:
            if first:
                first = False
            else:
                table += "<tr><td></td>"
            table += "<td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (r.parent, r.rel, r.child, relations[r])
    return render_template("db.html", table=table)


if __name__ == '__main__':
    app.run(debug=True)
