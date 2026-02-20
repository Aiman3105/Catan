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

# Eingabebereich
for ressource, anzahl in Ressourcen.items():
    with st.container():
        st.subheader(ressource)

        # Mobile-optimiert (max 3 pro Reihe)
        cols = st.columns(min(anzahl, 3))

        for i in range(anzahl):
            col = cols[i % len(cols)]
            col.number_input(
                f"Karte {i+1}",
                key=f"{ressource}_{i+1}",
                min_value=0,
                max_value=12,
                step=1,
                value=6
            )

        st.divider()

# Berechnung
if st.button("Rechne", use_container_width=True):

    Ergebnisse = []

    for ressource, anzahl in Ressourcen.items():
        werte = [
            st.session_state.get(f"{ressource}_{i}", 0)
            for i in range(1, anzahl + 1)
        ]

        summe = func.Score(werte)
        Ergebnisse.append((ressource, summe))

    st.subheader("Ergebnis")

    for res, erg in Ergebnisse:
        st.write(f"**{res}:** {erg}")