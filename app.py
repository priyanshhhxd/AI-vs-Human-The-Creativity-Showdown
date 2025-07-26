import streamlit as st
import openai

# -------------------- SETUP --------------------
st.set_page_config(page_title="AI vs Human Showdown", page_icon="🤖")
st.title("🤖 AI vs Human: The Creativity Showdown")
st.write("Can AI outshine human creativity? Let's find out!")

# Put your OpenAI API key here
openai.api_key = "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"

# -------------------- INPUT SECTION --------------------
prompt = st.text_input("👉 Enter a creative prompt (poem, joke, quote, etc.)")

# Human writes their response
human_text = st.text_area("✍️ Your response:")

# Button to generate AI answer
if st.button("⚡ Generate AI Answer"):
    if prompt:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        ai_text = response.choices[0].message["content"]

        st.subheader("🤖 AI Response:")
        st.write(ai_text)

        # Showdown section if human wrote something
        if human_text:
            st.subheader("⚔️ Creativity Showdown")
            st.write(f"**Human:** {human_text}")
            st.write(f"**AI:** {ai_text}")

            st.success("🎯 Verdict: You decide who wins – AI 🦾 or Human ❤️!")
        else:
            st.info("Write your own response to compare!")
    else:
        st.warning("Enter a prompt first!")
