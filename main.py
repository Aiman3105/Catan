import streamlit as st

Ressourcen = ["Stein", "Getreide", "Schaf", "Holz", "Lehm"]

# Kopfzeile
header = st.columns(6)
header[0].write("Ressource")
for i in range(1, 6):
    header[i].write(f"Karte {i}")

# Tabellenzeilen
for ressource in Ressourcen:
    cols = st.columns(6)

    cols[0].write(ressource)

    for i in range(1, 6):
        cols[i].text_input(
            "",
            key=f"{ressource}_{i}",
            label_visibility="collapsed"
        )

st.session_state
