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
# CSS Styling (große Buttons!)
# -----------------------------
st.markdown("""
<style>
.card {
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 20px;
}
.counter-row {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 10px;
}
.big-number {
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}
.stButton button {
    width: 60px;
    height: 45px;
    font-size: 20px;
    border-radius: 10px;
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
if st.button("🔄 Reset"):
    for res, data in Ressourcen.items():
        for i in range(data["anzahl"]):
            st.session_state[f"{res}_{i}"] = 6
    st.rerun()


# -----------------------------
# Ressourcen Cards
# -----------------------------
Ergebnisse = []

for res, data in Ressourcen.items():

    st.markdown(
        f'<div class="card" style="background-color:{data["farbe"]}20;">'
        f'<h3 style="color:{data["farbe"]};">{res}</h3>',
        unsafe_allow_html=True
    )

    anzahl = data["anzahl"]

    # Erste Zeile (max 3)
    first_row = min(3, anzahl)
    cols1 = st.columns(first_row)

    for i in range(first_row):
        with cols1[i]:
            key = f"{res}_{i}"
            st.markdown('<div class="big-number">%d</div>' % st.session_state[key], unsafe_allow_html=True)
            minus, plus = st.columns(2)
            if minus.button("−", key=f"minus_{key}"):
                if st.session_state[key] > 0:
                    st.session_state[key] -= 1
                    st.rerun()
            if plus.button("+", key=f"plus_{key}"):
                if st.session_state[key] < 12:
                    st.session_state[key] += 1
                    st.rerun()

    # Zweite Zeile
    if anzahl > 3:
        remaining = anzahl - 3
        cols2 = st.columns(remaining)

        for i in range(remaining):
            with cols2[i]:
                key = f"{res}_{i+3}"
                st.markdown('<div class="big-number">%d</div>' % st.session_state[key], unsafe_allow_html=True)
                minus, plus = st.columns(2)
                if minus.button("−", key=f"minus_{key}"):
                    if st.session_state[key] > 0:
                        st.session_state[key] -= 1
                        st.rerun()
                if plus.button("+", key=f"plus_{key}"):
                    if st.session_state[key] < 12:
                        st.session_state[key] += 1
                        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Score berechnen (live)
    werte = [st.session_state[f"{res}_{i}"] for i in range(anzahl)]
    summe = func.Score(werte)
    Ergebnisse.append((res, summe))


# -----------------------------
# Live Ergebnis (immer sichtbar)
# -----------------------------
st.divider()
st.subheader("Ergebnis")

cols = st.columns(len(Ergebnisse))
for col, (res, erg) in zip(cols, Ergebnisse):
    col.metric(label=res, value=erg)