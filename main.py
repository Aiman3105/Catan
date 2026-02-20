import streamlit as st
import functions as func

st.set_page_config(layout="centered")

Ressourcen = {
    "Stein": 5,
    "Getreide": 6,
    "Schaf": 6,
    "Holz": 6,
    "Lehm": 5
}

st.title("Ressourcen Rechner")

# Optional: etwas kompaktere Optik per CSS
st.markdown("""
<style>
div[data-testid="stNumberInput"] input {
    padding: 4px !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# Eingabebereich
for ressource, anzahl in Ressourcen.items():
    st.write(f"**{ressource}**")

    cols = st.columns(anzahl)

    for i in range(anzahl):
        cols[i].number_input(
            "",
            key=f"{ressource}_{i+1}",
            min_value=0,
            max_value=12,
            step=1,
            value=0,
            label_visibility="collapsed"
        )

    st.divider()


# Ergebnis in einer Zeile
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

    cols = st.columns(len(Ergebnisse))
    for col, (res, erg) in zip(cols, Ergebnisse):
        col.metric(label=res, value=erg)