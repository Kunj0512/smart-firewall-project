import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src import preprocess, train_model, recommend_rules, feedback

st.title("Smart Firewall Rule Recommender")

uploaded_file = st.file_uploader("Upload Log File", type="csv")
if uploaded_file:
    # Load and clean data
    df = preprocess.load_and_clean_data(uploaded_file)
    st.subheader("Log Data Preview")
    st.write(df.head())

    # Simple traffic analytics
    if "action" in df.columns:
        st.subheader("Traffic Overview")
        action_counts = df["action"].value_counts()
        st.bar_chart(action_counts)

    # Train model
    if st.button("Train Model"):
        train_model.train_model(df)
        st.success("Model Trained Successfully!")

    st.subheader("Firewall Rule Recommendation")
    port = st.number_input("Enter Port Number to Check", min_value=1, max_value=65535, value=80, step=1)

    rule = None
    if st.button("Get Recommendation"):
        rule = recommend_rules.generate_rule(port)
        st.info(f"Recommended Action: {rule['action']}")
        st.json(rule)

        # Allow user to download rule as JSON
        rule_json = json.dumps(rule, indent=2)
        st.download_button(
            label="Download Rule as JSON",
            data=rule_json,
            file_name=f"firewall_rule_port_{port}.json",
            mime="application/json"
        )

    st.subheader("Feedback")
    feedback_comment = st.text_area("Share feedback about this recommendation (optional)")
    if st.button("Submit Feedback"):
        # If no new rule was just generated, fall back to a minimal placeholder
        if rule is None:
            rule = {"note": "No rule generated in this session", "port": int(port)}
        feedback.save_feedback(rule, feedback_comment or "No comment provided")
        st.success("Thank you! Your feedback has been recorded.")
