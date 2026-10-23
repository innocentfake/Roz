import streamlit as st
from datetime import date

st.set_page_config(page_title="For Roz | A Quiet Constellation", page_icon="🌹", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
:root { color-scheme: dark; }
.stApp {
 background: radial-gradient(ellipse at top, #1d2038 0%, #0b0c14 48%, #07080d 100%);
 color: #eee8e6;
}
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
h1,h2,h3,.serif { font-family: 'Cormorant Garamond', serif !important; }
.block-container { max-width: 1050px; padding-top: 2.2rem; padding-bottom: 4rem; }
.hero {
 border: 1px solid rgba(226,190,194,.2); border-radius: 28px;
 padding: 4rem 2rem; text-align: center;
 background: linear-gradient(145deg, rgba(43,38,62,.78), rgba(13,15,27,.82));
 box-shadow: 0 20px 80px rgba(0,0,0,.25);
}
.eyebrow { letter-spacing: .28em; text-transform: uppercase; color: #d6aab3; font-size: .75rem; }
.hero h1 { font-size: clamp(3.5rem, 9vw, 6.4rem); line-height: .95; margin: 1rem 0; color: #f5e9e8; font-weight: 500; }
.hero p { max-width: 620px; margin: 0 auto; color: #c8c3d1; font-size: 1.05rem; line-height: 1.9; }
.rule { height: 1px; background: linear-gradient(90deg, transparent, #815866, transparent); margin: 2.5rem 0; }
.card {
 background: rgba(255,255,255,.035); border: 1px solid rgba(226,190,194,.15);
 border-radius: 20px; padding: 1.5rem; min-height: 190px;
}
.card h3 { color: #e7bdc5; font-size: 1.7rem; margin-top: 0; }
.card p { color: #c7c3cf; line-height: 1.8; }
.quote { font-family: 'Cormorant Garamond', serif; font-size: 1.7rem; line-height: 1.5; color: #f0dfe3; text-align: center; padding: 1.4rem 1rem; }
.small { color: #8e899b; font-size: .82rem; text-align:center; }
div.stButton > button { border-radius: 999px; border: 1px solid #966b7b; background: #5b3448; color: #fff4f4; }
div.stButton > button:hover { border-color: #e4b8c3; background: #704459; color: white; }
textarea, input { background-color: #141521 !important; color: #f2e8eb !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">a small universe in words</div>
  <h1>For Roz</h1>
  <p>Some people arrive like a line in a book you weren't searching for —<br>
  and somehow, you keep returning to the page.</p>
  <div style="margin-top:1.8rem;color:#d5a4b0;font-size:1.3rem;">☾ &nbsp; ✦ &nbsp; 🌹 &nbsp; ✦ &nbsp; ☽</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center;font-size:2.4rem;">A few quiet corners</h2>', unsafe_allow_html=True)
cols = st.columns(3)
with cols[0]:
    st.markdown('<div class="card"><h3>Between the pages</h3><p>For the worlds Dostoevsky and Kafka left behind, and the strange comfort of finding someone who might understand them.</p></div>', unsafe_allow_html=True)
with cols[1]:
    st.markdown('<div class="card"><h3>Unsent letters</h3><p>Words that don’t need an answer. A place for honesty, without pressure, expectation, or a demand to be understood.</p></div>', unsafe_allow_html=True)
with cols[2]:
    st.markdown('<div class="card"><h3>Under the same moon</h3><p>Some feelings are better kept gentle: a little wonder, a little distance, and room for real life to unfold naturally.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
st.markdown('<div class="quote">“Maybe some people are not meant to become a story.<br>Maybe they simply remind us that we can still feel one.”</div>', unsafe_allow_html=True)
st.markdown('<p class="small">An original line written for this little corner of the internet.</p>', unsafe_allow_html=True)

st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
left, right = st.columns([1, 1])
with left:
    st.markdown('<h2 style="font-size:2.2rem;">A letter, kept private</h2>', unsafe_allow_html=True)
    st.write("Write something for yourself. This demo does not send it to Roz or publish it.")
    letter = st.text_area("Unsent words", placeholder="Dear Roz…", height=170, label_visibility="collapsed")
    if st.button("Fold this letter ✉️"):
        if letter.strip():
            st.session_state["saved_letter"] = letter.strip()
            st.success("Folded. It stays in this browser session only.")
        else:
            st.info("Write a few words first.")
    if st.session_state.get("saved_letter"):
        with st.expander("Open the letter again"):
            st.write(st.session_state["saved_letter"])
with right:
    st.markdown('<h2 style="font-size:2.2rem;">A little reminder</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card"><p>Curiosity is not a promise, and a feeling is not a claim on another person. Let friendship be friendship. Let every answer be freely given. Let real conversations matter more than signs.</p><p style="color:#d5a4b0;">— keep it kind, keep it real</p></div>', unsafe_allow_html=True)

st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
st.markdown('<p class="small">Made as a personal literary tribute. No private messages, photos, or identifying details are collected.</p>', unsafe_allow_html=True)
