import streamlit as st
import functions as func

st.set_page_config(layout="centered")

Ressourcen = ["Stein", "Getreide", "Schaf", "Holz", "Lehm"]

# zentrierter Container (macht es schmaler auf Mobile)
outer_left, main, outer_right = st.columns([1, 6, 1])

with main:

    # Kopfzeile
    header = st.columns([2,1,1,1,1,1])
    header[0].write("Ressource")
    for i in range(1, 6):
        header[i].write(f"Karte {i}")

    # Tabellenzeilen
    for ressource in Ressourcen:
        cols = st.columns([2,1,1,1,1,1])

        cols[0].write(ressource)

        for i in range(1, 6):
            cols[i].number_input(
                "",
                key=f"{ressource}_{i}",
                label_visibility="collapsed",
                min_value=0,
                max_value=12,
                step=1,
                value=0
            )

    werte=[]
    Summe=0
    Ergebnisse=[]
    Final=[]

    # Ergebnis
    if st.button("Rechne", use_container_width=True):
        Ergebnis = st.columns([2,1,1,1,1])

        for Ressource in Ressourcen:
            for i in range (1, 6):
                werte.append(st.session_state.get(f"{Ressource}_{i}", ""))
            Summe=func.Score(werte)
            Ergebnisse.append(Summe)
            werte=[]
            Summe=0

        Final = list(zip(Ressourcen, Ergebnisse))

        for i in range(0,5):
            Ergebnis[i].write(f"{Final[i][0]} : {Final[i][1]}")
