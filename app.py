import streamlit as st
import google.generativeai as genai
from PIL import Image

# Nastavení AI - tvůj klíč
genai.configure(api_key="AIzaSyBJvt1LTgSLgzQ-nYAuaIrZurSBAssC6QU")

# Nastavení vzhledu stránky
st.set_page_config(page_title="AI Study Buddy", layout="centered")

st.title("🎓 AI Study Buddy")
st.write("Nahraj fotku svých zápisků a já ti udělám výtah.")

# Nahrávání souboru
file = st.file_uploader("Vyber fotku sešitu", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption='Tvůj sešit', use_column_width=True)
    
    if st.button("🧠 Analyzovat zápisky"):
        # Použití nejnovějšího modelu pro rok 2026
        model = genai.GenerativeModel('gemini-1.5-flash') 
        
        with st.spinner('AI čte tvůj sešit a přemýšlí...'):
            try:
                # Odeslání textového příkazu i obrázku najednou
                response = model.generate_content([
                    "Přečti tyhle ručně psané poznámky v češtině. Udělej z nich stručný výtah v odrážkách, vypiš 3 klíčové pojmy a navrhni 3 otázky na procvičení.", 
                    img
                ])
                
                # Zobrazení výsledku
                st.markdown("---")
                st.subheader("📝 Výsledek analýzy:")
                st.write(response.text)
                
            except Exception as e:
                # Ošetření chyb (např. špatný region nebo klíč)
                st.error(f"Chyba při komunikaci s AI: {e}")
                
