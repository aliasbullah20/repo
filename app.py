import streamlit as st
import pandas as pd

st.set_page_config(page_title="Aplikasi IPDA", layout="wide")
st.title("🌾 APLIKASI IPDA - Indeks Pertanaman")

st.success("File app.py berhasil dibuat Bos!")

# --- INPUT DATA ---
st.header("Input Data Lahan")
col1, col2 = st.columns(2)
with col1:
    luas_baku = st.number_input("Luas Baku Sawah (Ha)", value=100.0)
    luas_tanam_padi = st.number_input("Luas Tanam Padi (Ha)", value=80.0)
with col2:
    luas_tanam_palawija = st.number_input("Luas Tanam Palawija (Ha)", value=20.0)
    luas_tanam_lain = st.number_input("Luas Tanam Lain (Ha)", value=10.0)

# --- HITUNG ---
if st.button("HITUNG IPDA"):
    total_tanam = luas_tanam_padi + luas_tanam_palawija + luas_tanam_lain
    ipda = (total_tanam / luas_baku * 100) if luas_baku != 0 else 0
    
    st.metric("Total Luas Tanam", f"{total_tanam} Ha")
    st.metric("Nilai IPDA", f"{ipda:.2f} %")
    
    # Tabel
    data = {
        "Uraian": ["Luas Baku", "Padi", "Palawija", "Lain", "Total Tanam", "IPDA"],
        "Nilai": [luas_baku, luas_tanam_padi, luas_tanam_palawija, luas_tanam_lain, total_tanam, f"{ipda:.2f}%"]
    }
    st.dataframe(pd.DataFrame(data), use_container_width=True)
