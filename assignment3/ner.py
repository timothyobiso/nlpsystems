import spacy
from spacy import displacy
import io
from collections import defaultdict


nlp = spacy.load("en_core_web_sm")


def get_entities(text):
    doc = nlp(text)
    return [(ent.start_char, ent.end_char, ent.text, ent.label_) for ent in doc.ents]


def get_tokens(text):
    doc = nlp(text)
    return [token.text for token in doc]


def get_parse(text):
    # use the entire doc if no sentence is passed
    parse = []
    doc = nlp(text)

    # collect the positions of word types
    # repeats = defaultdict(list)
    # for token in doc:
    #     repeats[token.text].append(token.i)

    for token in doc:

        # token_text = token.text
        # if len(repeats[token_text]) > 1:
        #     token_text += '-' + str(repeats[token_text].index(token.i))
        #
        # head_text = token.head.text
        # if len(repeats[head_text]) > 1:
        #     head_text += '-' + str(repeats[head_text].index(token.head.i))

        parse.append((token.text, token.dep_, token.head.text))

    return parse


def get_parse_per_sentence(sentences):
    return [get_parse(sent.text) for sent in sentences]


def get_parse_table(sentence):
    table = "<table><tr><th>Token</th><th>Dependency</th><th>Head</th></tr>"
    for token in nlp(sentence):
        table += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (token.text, token.dep_, token.head.text)
    table += "</table>"
    return table


def get_parse_graph(sentence):
    graph = ""
    for sent in nlp(sentence).sents:
        graph += displacy.render(sent, style="dep", options={"compact": True, "bg": "#09a3d5", "color": "white", "font": "Source Sans Pro"})

    return graph


def get_entities_with_markup(text):
    doc = nlp(text)
    entities = doc.ents
    starts = {e.start_char: e.label_ for e in entities}
    ends = {e.end_char for e in entities}
    buffer = io.StringIO()
    for i, char in enumerate(text):
        if i in ends:
            buffer.write('</entity>')
        if i in starts:
            buffer.write('<entity class="%s">' % starts[i])
        buffer.write(char)
    markup = buffer.getvalue()
    return '<markup>%s</markup>' % markup

