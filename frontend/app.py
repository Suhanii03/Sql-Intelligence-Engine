import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="SQL Intelligence Engine", layout="wide")

st.title("🚀 SQL Intelligence Engine")
st.caption("Natural Language → SQL → Insights")

query = st.text_input("Enter your query:")

if st.button("Run Query"):

    if query.strip() == "":
        st.warning("Enter a query")
    else:
        with st.spinner("Processing..."):

            response = requests.get(
                f"http://127.0.0.1:8000/query?user_query={query}"
            )
            data = response.json()

            df = pd.DataFrame(data["results"])

            st.subheader("🧠 Generated SQL")
            st.code(data["generated_sql"], language="sql")

            st.subheader("📊 Results")
            st.dataframe(df, use_container_width=True)

            st.subheader("📈 Insights")
            st.json(data["insights"])

            if not df.empty:
                st.subheader("📉 Visualization")
                st.bar_chart(df)

            st.subheader("⚡ Optimization Suggestions")
            for s in data["optimization_suggestions"]:
                st.info(s)