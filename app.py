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
        # ZMĚNA MODELU NA STABILNĚJŠÍ VERZI
        model = genai.GenerativeModel('gemini-1.0-pro-vision-latest') 
        
        with st.spinner('AI čte tvůj sešit a přemýšlí...'):
            try:
                # Drobná úprava příkazu (promptu)
                response = model.generate_content([
                    "Přečti tyhle ručně psané poznámky. Udělej z nich stručný výtah v odrážkách, vypiš 3 klíčové pojmy a navrhni 3 otázky na procvičení.", 
                    img
                ])
                st.markdown("---")
                st.markdown(response.text)
            except Exception as e:
                # Pokud to i tak hodí chybu, vypíše ji srozumitelněji
                st.error(f"Chyba při komunikaci s AI: {e}")
