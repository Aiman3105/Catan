import streamlit as st
import functions as func

st.set_page_config(layout="centered")

# -----------------------------
# Ressourcen Definition
# -----------------------------
Ressourcen = {
    "Stein": {"anzahl": 5, "farbe": "#9E9E9E"},
    "Getreide": {"anzahl": 6, "farbe": "#FBC02D"},
    "Schaf": {"anzahl": 6, "farbe": "#66BB6A"},
    "Holz": {"anzahl": 6, "farbe": "#2E7D32"},
    "Lehm": {"anzahl": 5, "farbe": "#D84315"},
}

st.title("Ressourcen Rechner")

# -----------------------------
# Kompaktes CSS
# -----------------------------
st.markdown("""
<style>

/* Weniger Abstand global */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* Resource Card */
.resource-card {
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 14px;
}

/* Counter Box */
.counter-box {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    margin-bottom: 6px;
}

/* Zahl */
.counter-number {
    font-size: 20px;
    font-weight: 600;
    width: 28px;
    text-align: center;
}

/* Buttons */
.stButton button {
    width: 36px !important;
    height: 36px !important;
    padding: 0px !important;
    font-size: 18px !important;
    border-radius: 8px !important;
}

/* Weniger Abstand zwischen Spalten */
div[data-testid="column"] {
    padding-left: 4px !important;
    padding-right: 4px !important;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Session State initialisieren
# -----------------------------
for res, data in Ressourcen.items():
    for i in range(data["anzahl"]):
        key = f"{res}_{i}"
        if key not in st.session_state:
            st.session_state[key] = 6


# -----------------------------
# Reset Button
# -----------------------------
if st.button("Reset"):
    for res, data in Ressourcen.items():
        for i in range(data["anzahl"]):
            st.session_state[f"{res}_{i}"] = 6
    st.rerun()


# -----------------------------
# Ressourcen Anzeige
# -----------------------------
Ergebnisse = []

for res, data in Ressourcen.items():

    st.markdown(
        f'<div class="resource-card" style="background-color:{data["farbe"]}15;">'
        f'<div style="font-weight:600; color:{data["farbe"]}; margin-bottom:6px;">{res}</div>',
        unsafe_allow_html=True
    )

    anzahl = data["anzahl"]

    # Zeile 1 (max 3)
    first_row = min(3, anzahl)
    cols1 = st.columns(first_row)

    for i in range(first_row):
        key = f"{res}_{i}"
        with cols1[i]:

            c1, c2, c3 = st.columns([1,1,1])

            if c1.button("−", key=f"minus_{key}"):
                if st.session_state[key] > 0:
                    st.session_state[key] -= 1
                    st.rerun()

            c2.markdown(
                f'<div class="counter-number">{st.session_state[key]}</div>',
                unsafe_allow_html=True
            )

            if c3.button("+", key=f"plus_{key}"):
                if st.session_state[key] < 12:
                    st.session_state[key] += 1
                    st.rerun()

    # Zeile 2
    if anzahl > 3:
        remaining = anzahl - 3
        cols2 = st.columns(remaining)

        for i in range(remaining):
            key = f"{res}_{i+3}"
            with cols2[i]:

                c1, c2, c3 = st.columns([1,1,1])

                if c1.button("−", key=f"minus_{key}"):
                    if st.session_state[key] > 0:
                        st.session_state[key] -= 1
                        st.rerun()

                c2.markdown(
                    f'<div class="counter-number">{st.session_state[key]}</div>',
                    unsafe_allow_html=True
                )

                if c3.button("+", key=f"plus_{key}"):
                    if st.session_state[key] < 12:
                        st.session_state[key] += 1
                        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Score live berechnen
    werte = [st.session_state[f"{res}_{i}"] for i in range(anzahl)]
    summe = func.Score(werte)
    Ergebnisse.append((res, summe))


# -----------------------------
# Ergebnis
# -----------------------------
st.divider()
st.subheader("Ergebnis")

cols = st.columns(len(Ergebnisse))
for col, (res, erg) in zip(cols, Ergebnisse):
    col.metric(label=res, value=erg)