import streamlit as st

st.set_page_config(
    page_title="StorySpark AI",
    page_icon="📖",
    layout="centered",
)

st.title("✨ StorySpark AI")
st.subheader("Turn your imagination into a story")

st.write(
    "Upload an image or describe your idea. "
    "Choose a genre and let AI bring it to life."
)

user_prompt = st.text_area(
    "Describe your story idea",
    placeholder="A student discovers a mysterious key...",
    height=120,
)

uploaded_image = st.file_uploader(
    "Upload an image for inspiration",
    type=["png", "jpg", "jpeg", "webp"],
)

if uploaded_image:
    st.image(
        uploaded_image,
        caption="Your inspiration",
        use_container_width=True,
    )

genre = st.selectbox(
    "Choose a genre",
    ["Fantasy", "Mystery", "Comedy", "Adventure", "Science Fiction"],
)

tone = st.selectbox(
    "Choose a tone",
    ["Magical", "Suspenseful", "Funny", "Heartwarming", "Dramatic"],
)

if st.button("✨ Generate My Story", type="primary"):
    if not user_prompt.strip() and uploaded_image is None:
        st.warning("Enter a story idea or upload an image.")
    else:
        st.info(
            "Frontend is ready. AI integration will be connected "
            "after the Gemma module is merged."
        )
