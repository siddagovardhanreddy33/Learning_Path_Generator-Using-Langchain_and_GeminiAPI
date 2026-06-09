import json
import streamlit as st

from roadmap_generator import generate_learning_path

st.set_page_config(page_title="Learning Path Generator",page_icon="📚",layout="centered")
st.title("📚 AI Learning Path Generator")

st.markdown("""Generate a structured learning roadmapfor any skill using Gemini and LangChain.""")

skill = st.text_input("Enter a skill or domain",placeholder="Data Science")

if st.button("Generate Roadmap"):

    if not skill.strip():
        st.warning("Please enter a skill.")
        st.stop()
    try:
        with st.spinner("Generating roadmap..."):
            roadmap = generate_learning_path(skill)
        st.success("Roadmap Generated Successfully!")
        st.subheader("🎯 Learning Stages")
        for stage in roadmap["learning_stages"]:
            st.write(f"✅ {stage}")
        st.subheader("📚 Key Topics")

        for topic in roadmap["key_topics"]:
            st.write(f"📌 {topic}")
        st.subheader("📝 Learning Goal Summary")
        st.info(roadmap["learning_goal_summary"])
        st.subheader("📄 JSON Output")
        st.json(roadmap)
        st.download_button(
            label="📥 Download JSON",
            data=json.dumps(
                roadmap,
                indent=4
            ),
            file_name="learning_path.json",
            mime="application/json"
        )

    except Exception as e:
        st.error(f"Error: {str(e)}" )