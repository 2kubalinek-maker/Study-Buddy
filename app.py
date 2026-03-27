import streamlit as st
import google.generativeai as genai
from PIL import Image

# Nastavení AI - tvůj klíč
genai.configure(api_key="AIzaSyBJvt1LTgSLgzQ-nYAuaIrZurSBAssC6QU")

st.set_page_config(page_title="AI Study Buddy", layout="centered")

st.title("🎓 AI Study Buddy")
st.write("Nahraj fotku svých zápisků a já ti udělám výtah.")

file = st.file_uploader("Vyber fotku sešitu", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption='Tvůj sešit', use_column_width=True)
    
    if st.button("🧠 Analyzovat zápisky"):
        model = genai.GenerativeModel('gemini-pro-vision')
        with st.spinner('AI čte tvůj sešit...'):
            response = model.generate_content([
                "Přečti tyhle zápisky v češtině. Udělej stručný výtah v odrážkách, vypiš 3 klíčové pojmy a navrhni 3 otázky na procvičení.", 
                img
            ])
            st.markdown("---")
            st.markdown(response.text)
          
