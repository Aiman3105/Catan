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

# Mobile Optimierung
st.markdown("""
<style>
div[data-testid="stNumberInput"] input {
    padding: 6px !important;
    text-align: center;
    font-size: 16px !important;
}
div[data-testid="stNumberInput"] button {
    height: 40px !important;
    width: 40px !important;
}
</style>
""", unsafe_allow_html=True)


# ------------------------
# Eingabebereich
# ------------------------
for ressource, anzahl in Ressourcen.items():

    st.write(f"**{ressource}**")

    # Erste Zeile (max 3)
    first_row = min(3, anzahl)
    cols1 = st.columns(first_row)

    for i in range(first_row):
        cols1[i].number_input(
            "",
            key=f"{ressource}_{i+1}",
            min_value=0,
            max_value=12,
            step=1,
            value=6,
            label_visibility="collapsed"
        )

    # Zweite Zeile (falls nötig)
    if anzahl > 3:
        remaining = anzahl - 3
        cols2 = st.columns(remaining)

        for i in range(remaining):
            cols2[i].number_input(
                "",
                key=f"{ressource}_{i+4}",
                min_value=0,
                max_value=12,
                step=1,
                value=6,
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

    cols = st.columns(len(Ergebnisse))

    for col, (res, erg) in zip(cols, Ergebnisse):
        col.metric(label=res, value=erg)