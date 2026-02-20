import streamlit as st
import functions as func

st.set_page_config(layout="centered")

Ressourcen = ["Stein", "Getreide", "Schaf", "Holz", "Lehm"]

st.title("Test")
st.title("Ressourcen Rechner")

werte_gesamt = {}

# Jede Ressource als eigener Block (Mobile-optimiert)
for ressource in Ressourcen:
    with st.container():
        st.subheader(ressource)

        cols = st.columns(5)
        for i in range(5):
            werte_gesamt[f"{ressource}_{i + 1}"] = cols[i].number_input(
                f"Karte {i + 1}",
                key=f"{ressource}_{i + 1}",
                min_value=0,
                max_value=12,
                step=1,
                value=0
            )

        st.divider()

# Berechnung
if st.button("Rechne", use_container_width=True):

    Ergebnisse = []

    for ressource in Ressourcen:
        werte = [
            st.session_state.get(f"{ressource}_{i}", 0)
            for i in range(1, 6)
        ]

        summe = func.Score(werte)
        Ergebnisse.append(summe)

    st.subheader("Ergebnis")

    for res, erg in zip(Ressourcen, Ergebnisse):
        st.write(f"**{res}:** {erg}")