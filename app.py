import streamlit as st
import ollama
from trends import get_trends


# --------------------------------------------------
# CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="CreatorMindAI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# FINAL CSS (FIXED VISIBILITY + POLISH)
# --------------------------------------------------

st.markdown("""

<style>

/* FONT */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');


html, body, [class*="css"] {

font-family: 'Inter', sans-serif;

color: #374151;

}


/* BACKGROUND */

.stApp {

background:

linear-gradient(180deg,#f9f8ff 0%,#eef2ff 100%);

}


/* NAVBAR */

.navbar {

display:flex;

justify-content:space-between;

align-items:center;

padding:18px 40px;

background: rgba(255,255,255,0.7);

backdrop-filter: blur(14px);

border-radius:14px;

box-shadow:0 4px 20px rgba(0,0,0,0.05);

margin-bottom:50px;

}


.logo {

font-size:26px;

font-weight:600;

background: linear-gradient(90deg,#6366f1,#a855f7);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}


.navright {

color:#6b7280;

}


/* HERO */

.hero-title {

font-size:72px;

font-weight:700;

line-height:1.1;

background: linear-gradient(90deg,#111827,#6366f1);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}


.hero-sub {

font-size:22px;

color:#6b7280;

margin-top:15px;

}


/* BUTTON */

.stButton button {

background: linear-gradient(90deg,#6366f1,#a855f7);

color:white;

border:none;

border-radius:12px;

height:52px;

font-weight:500;

}


/* INPUT */

.stTextInput input {

background:white !important;

border-radius:12px !important;

border:1px solid #e5e7eb !important;

padding:12px !important;

color:#111827 !important;

}


/* SELECT */

.stSelectbox div {

background:white !important;

border-radius:12px !important;

color:#111827 !important;

}


/* SECTION TITLE */

.section {

font-size:40px;

font-weight:700;

margin-top:70px;

margin-bottom:30px;

color:#4f46e5;

}


/* CARD */

.card {

background:white;

padding:30px;

border-radius:20px;

border:1px solid rgba(99,102,241,0.1);

box-shadow:0 10px 30px rgba(99,102,241,0.08);

color:#374151;

}


/* FEATURE CARD TEXT */

.card h4 {

color:#4f46e5;

margin-bottom:10px;

}


.card p {

color:#6b7280;

}


/* CHAT USER */

.chat-user {

background: linear-gradient(90deg,#6366f1,#a855f7);

color:white;

padding:14px;

border-radius:14px;

margin:10px;

max-width:60%;

}


/* CHAT AI */

.chat-ai {

background:#eef2ff;

padding:14px;

border-radius:14px;

margin:10px;

max-width:60%;

color:#111827;

}


/* FOOTER */

.footer {

text-align:center;

margin-top:100px;

color:#9ca3af;

}


</style>

""", unsafe_allow_html=True)



# --------------------------------------------------
# NAVBAR
# --------------------------------------------------

st.markdown("""

<div class="navbar">

<div class="logo">CreatorMindAI</div>

<div class="navright">AI Content Platform</div>

</div>

""", unsafe_allow_html=True)



# --------------------------------------------------
# HERO
# --------------------------------------------------

col1,col2 = st.columns([1.3,1])

with col1:

    st.markdown('<div class="hero-title">Your AI Creator<br>For Everything</div>', unsafe_allow_html=True)

    st.markdown('<div class="hero-sub">Generate reels, blogs and ideas instantly.</div>', unsafe_allow_html=True)

    st.button("Start Creating")


with col2:

    st.image(

    "https://images.unsplash.com/photo-1677442136019-21780ecad995",

    width=520

    )



# --------------------------------------------------
# FEATURES
# --------------------------------------------------

st.markdown('<div class="section">Features</div>', unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:

    st.markdown('<div class="card"><h4>AI Content Generator</h4><p>Create viral reels and blogs instantly.</p></div>', unsafe_allow_html=True)

with c2:

    st.markdown('<div class="card"><h4>Trend Discovery</h4><p>Discover trending content ideas.</p></div>', unsafe_allow_html=True)

with c3:

    st.markdown('<div class="card"><h4>AI Assistant</h4><p>Ask questions and learn faster.</p></div>', unsafe_allow_html=True)



# --------------------------------------------------
# GENERATOR
# --------------------------------------------------

st.markdown('<div class="section">Generate Content</div>', unsafe_allow_html=True)

topic = st.text_input("Enter topic")

col1,col2 = st.columns(2)

style = col1.selectbox("Style",["Hinglish","English"])

level = col2.selectbox("Level",["Beginner","Advanced"])


if st.button("Generate"):

    response=ollama.chat(

    model="llama3",

    messages=[{"role":"user","content":topic}]

    )

    st.markdown(f'<div class="card">{response["message"]["content"]}</div>', unsafe_allow_html=True)



# --------------------------------------------------
# CHAT
# --------------------------------------------------

st.markdown('<div class="section">Chat</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:

    st.session_state.messages=[]


msg=st.text_input("Ask CreatorMind")


if st.button("Send"):

    st.session_state.messages.append(("user",msg))

    response=ollama.chat(

    model="llama3",

    messages=[{"role":"user","content":msg}]

    )

    st.session_state.messages.append(("ai",response["message"]["content"]))


for role,text in st.session_state.messages:

    if role=="user":

        st.markdown(f'<div class="chat-user">{text}</div>', unsafe_allow_html=True)

    else:

        st.markdown(f'<div class="chat-ai">{text}</div>', unsafe_allow_html=True)



# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown('<div class="footer">CreatorMindAI • Built by Aditya</div>', unsafe_allow_html=True)
