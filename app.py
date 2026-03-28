import streamlit as st
import google.generativeai as genai

# Nastavení AI - tvůj klíč
genai.configure(api_key="AIzaSyBJvt1LTgSLgzQ-nYAuaIrZurSBAssC6QU")

st.set_page_config(page_title="AI Studijní Pomocník", layout="centered")

st.title("⚡ AI Studijní Pomocník")
st.write("Vlož text z učebnice a já z něj udělám podklady pro učení.")

# Textové pole pro vložení učiva
user_text = st.text_area("Sem vlož text (témata, poznámky, články):", height=200)

col1, col2, col3 = st.columns(3)

with col1:
    btn_summary = st.button("📝 Udělat výtah")
with col2:
    btn_quiz = st.button("❓ Vytvořit kvíz")
with col3:
    btn_points = st.button("🏷️ Klíčové body")

if user_text:
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    if btn_summary:
        with st.spinner('Připravuji výtah...'):
            response = model.generate_content(f"Udělej stručný a přehledný výtah z tohoto textu: {user_text}")
            st.success("Hotovo!")
            st.write(response.text)

    if btn_quiz:
        with st.spinner('Generuji otázky...'):
            response = model.generate_content(f"Vytvoř 5 testových otázek (včetně správných odpovědí) na základě tohoto textu: {user_text}")
            st.success("Kvíz je na světě!")
            st.write(response.text)

    if btn_points:
        with st.spinner('Hledám klíčové pojmy...'):
            response = model.generate_content(f"Vypiš nejdůležitější pojmy a jejich stručné vysvětlení z tohoto textu: {user_text}")
            st.success("Klíčové body:")
            st.write(response.text)
else:
    if btn_summary or btn_quiz or btn_points:
        st.warning("Nejdříve do pole vlož nějaký text!")
