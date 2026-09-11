import streamlit as st
from summarizer import  summarize_website_content, get_available_models
import streamlit as st


st.set_page_config(
    page_title="AI Website Summarizer",
    page_icon="🧠",
    layout="centered"
)


st.title("AI Website Summarizer")

st.caption(
    "Enter a website URL, choose one of your locally installed Ollama models, "
    "and generate a concise AI-powered summary."
)


st.info(
    """
    This app runs the LLM locally using Ollama.

    If you do not have Ollama installed, install it first.

    After installing Ollama, download a model using a command such as:

    `ollama pull llama3.2`

    You can also try other models available in Ollama.
    """
)


st.divider()


url = st.text_input(
    label="Website URL",
    placeholder="https://example.com"
)


available_models_locally = get_available_models()


if available_models_locally:

    model = st.selectbox(
        label="Choose a local model",
        options=available_models_locally
    )

else:

    model = None

    st.warning(
        "No local Ollama models were detected. "
        "Make sure Ollama is running and at least one model is installed."
    )


summarize_clicked = st.button(
    label="Summarize Website",
    type="primary",
    use_container_width=True
)


if summarize_clicked:

    if not url:
        st.error("Please enter a website URL.")

    elif not model:
        st.error("Please install or select an Ollama model first.")

    else:

        try:

            with st.spinner(
                f"Scraping and summarizing using {model}..."
            ):

                summary = summarize_website_content(
                    url=url,
                    model=model
                )


            st.success("Summary generated successfully.")

            st.subheader("Summary")

            st.markdown(summary)

        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )