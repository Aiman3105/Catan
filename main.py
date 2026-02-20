# Zeile 1 (max 3)
first_row = min(3, anzahl)
cols1 = st.columns(3)  # Immer 3 Spalten

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

# Zeile 2 (unter derselben 3-Spalten-Struktur)
if anzahl > 3:
    remaining = anzahl - 3
    cols2 = st.columns(3)  # Immer 3 Spalten, gleiche Breite wie oben

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