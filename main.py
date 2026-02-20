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
# Kompaktes CSS für Mobile
# -----------------------------
st.markdown("""
<style>
.block-container { padding-top:0.5rem; padding-bottom:0.5rem; }
/* Resource Card */
.resource-card { padding:6px; border-radius:12px; margin-bottom:6px; }
/* Zahl */
.counter-number { font-size:18px; font-weight:600; width:28px; text-align:center; display:inline-block; }
/* ± Buttons */
.stButton button { width:32px !important; height:32px !important; font-size:18px !important; padding:0 !important; border-radius:6px !important; }
/* Reset Button breiter mit Symbol */
#reset-button button { width:100px !important; height:36px !important; font-size:20px !important; white-space:nowrap !important; }
div[data-testid="column"] { padding-left:2px !important; padding-right:2px !important; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session State initialisieren
# -----------------------------
for res, data in Ressourcen.items():
    for i in range(data["anzahl"]):
        key = f"{res}_{i}"
        if key not in st.session_state:
            st.session_state[key] = 7  # Startwert auf 7

# -----------------------------
# Reset Button mit Symbol
# -----------------------------
if st.button("🔄 Reset"):
    for res, data in Ressourcen.items():
        for i in range(data["anzahl"]):
            st.session_state[f"{res}_{i}"] = 7  # Resetwert auf 7
    st.rerun()

# -----------------------------
# Ressourcen Anzeige kompakt
# -----------------------------
Ergebnisse = []

for res, data in Ressourcen.items():
    st.markdown(
        f'<div class="resource-card" style="background-color:{data["farbe"]}15;">'
        f'<div style="font-weight:600; color:{data["farbe"]}; margin-bottom:4px;">{res}</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(data["anzahl"])
    for i in range(data["anzahl"]):
        key = f"{res}_{i}"
        with cols[i]:
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
    werte = [st.session_state[f"{res}_{i}"] for i in range(data["anzahl"])]
    Ergebnisse.append((res, func.Score(werte)))

# -----------------------------
# Ergebnis in einer Zeile
# -----------------------------
st.divider()
st.subheader("Ergebnis")
cols = st.columns(len(Ergebnisse))
for col, (res, erg) in zip(cols, Ergebnisse):
    col.metric(label=res, value=erg)