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
        with st.spinner('AI hledá nejlepší model a čte tvůj sešit...'):
            try:
                # Pokusíme se použít nejmodernější dostupný model
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Instrukce pro AI
                prompt = "Přečti tyhle ručně psané poznámky v češtině. Udělej z nich stručný výtah v odrážkách, vypiš 3 klíčové pojmy a navrhni 3 otázky na procvičení."
                
                # Spuštění analýzy
                response = model.generate_content([prompt, img])
                
                st.markdown("---")
                st.subheader("📝 Výsledek od AI:")
                st.write(response.text)
                
            except Exception as e:
                # Pokud 1.5-flash selže (chyba 404), zkusíme starší verzi
                try:
                    model_backup = genai.GenerativeModel('gemini-pro-vision')
                    response = model_backup.generate_content([prompt, img])
                    st.markdown("---")
                    st.subheader("📝 Výsledek od AI (záložní model):")
                    st.write(response.text)
                except Exception as e2:
                    st.error(f"Omlouvám se, ani jeden model teď neodpovídá. Chyba: {e2}")
