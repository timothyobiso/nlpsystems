from ner import *

import streamlit as st
import pandas as pd
import altair as alt
import graphviz
from collections import Counter

example = (
    "When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

st.markdown("# Named Entity Recognition")
text = st.text_area("Enter some text", height=150, value=example)

view = st.sidebar.radio("View", ["Entities", "Parse"])

doc = nlp(text)

if view == "Entities":
    entities = get_entities(text)
    tokens = get_tokens(text)
    counter = Counter(tokens)
    words = list(sorted(counter.most_common(30)))
    st.write(entities)

    chart = pd.DataFrame({
        'frequency': [w[1] for w in words],
        'word': [w[0] for w in words]
    })

    bar_chart = alt.Chart(chart).mark_bar().encode(x='word', y='frequency')

    st.markdown(f"Total number of tokens: {len(tokens)}<br/>Total number of types: {len(counter)}", unsafe_allow_html=True)

    st.table(entities)
    st.altair_chart(bar_chart, use_container_width=True)
elif view == "Parse":
    dependencies = get_parse(text)
    sentence_dependencies = get_parse_per_sentence(doc.sents)

    tab1, tab2 = st.tabs(('Table', 'Graph'))
    with tab1:
        st.table(dependencies)
    with tab2:
        for sentence in sentence_dependencies:
            graph = graphviz.Digraph()
            for d in sentence:
                graph.edge(d[2], d[0], label=d[1])
            st.graphviz_chart(graph)

