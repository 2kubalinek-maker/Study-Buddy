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
        with st.spinner('AI čte tvůj sešit...'):
            try:
                # Tady je ta změna: vynutíme přesný název modelu
                model = genai.GenerativeModel(model_name='gemini-1.5-flash')
                
                # Posíláme seznam: [textový prompt, obrázek]
                response = model.generate_content([
                    "Přečti tyhle ručně psané poznámky v češtině. Udělej z nich stručný výtah v odrážkách, vypiš 3 klíčové pojmy a navrhni 3 otázky na procvičení.", 
                    img
                ])
                
                st.markdown("---")
                st.subheader("📝 Výsledek od AI:")
                if response.text:
                    st.write(response.text)
                else:
                    st.write("AI přečetla obrázek, ale nevygenerovala žádný text.")
                
            except Exception as e:
                # Detailní výpis chyby, abychom věděli, co přesně se děje
                st.error(f"Chyba: {e}") 
