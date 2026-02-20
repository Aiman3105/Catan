import streamlit as st
import functions as func

st.set_page_config(layout="centered")

# Ressourcen + Anzahl Karten
Ressourcen = {
    "Stein": 5,
    "Getreide": 6,
    "Schaf": 6,
    "Holz": 6,
    "Lehm": 5
}

st.title("Ressourcen Rechner")

# Mobile-Optimierung + größere +/- Buttons
st.markdown("""
<style>
/* Zahl größer & verhindert iOS-Zoom */
div[data-testid="stNumberInput"] input {
    padding: 6px !important;
    text-align: center;
    font-size: 16px !important;
}

/* +/- Buttons größer für Touch */
div[data-testid="stNumberInput"] button {
    height: 38px !important;
    width: 38px !important;
}

/* Weniger Abstand zwischen Spalten */
div[data-testid="column"] {
    padding-left: 4px !important;
    padding-right: 4px !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# Eingabebereich
# ------------------------
for ressource, anzahl in Ressourcen.items():

    st.write(f"**{ressource}**")

    cols = st.columns([1] * anzahl)

    for i in range(anzahl):
        cols[i].number_input(
            "",
            key=f"{ressource}_{i + 1}",
            min_value=0,
            max_value=12,
            step=1,
            value=6,  # 🔥 Startwert jetzt 6
            label_visibility="collapsed"
        )

    st.divider()

# ------------------------
# Berechnung
# ------------------------
if st.button("Rechne", use_container_width=True):

    Ergebnisse = []

    for ressource, anzahl in Ressourcen.items():
        werte = [
            st.session_state.get(f"{ressource}_{i}", 6)
            for i in range(1, anzahl + 1)
        ]

        summe = func.Score(werte)
        Ergebnisse.append((ressource, summe))

    st.subheader("Ergebnis")

    # Alle Ergebnisse nebeneinander
    cols = st.columns(len(Ergebnisse))

    for col, (res, erg) in zip(cols, Ergebnisse):
        col.metric(label=res, value=erg)