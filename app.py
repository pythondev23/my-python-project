import streamlit as st

st.title("Farben-Converter")

hex_in = st.text_input(
    "Hex-Code:", 
    max_chars=7,
    placeholder="#01DE3F"
)

# 1) validität überprüfen:
def check_hex(hex_code: str) -> bool:
    """
    True, wenn hex_code ok
    - länge des strings: exakt 7
    - erstes zeichen: #
    - erlaubte zeichen: 0-9 und A-F / a-f
    """
    if len(hex_code) != 7:
        return False
    if hex_code[0] != "#":
        return False
    for elem in hex_code[1:]:
        if elem not in "0123456789ABCDEF":
            return False
    
    return True
    
    # alternative für - erlaubte zeichen: 0-9 und A-F / a-f
    #if len(set(hex_code).difference(set("0123456789ABCDEF"))) == 0:
    #    return True
   
    
st.write("Valide?", check_hex(hex_in))

# 2) umwandeln:

col_R, col_G, col_B = st.columns(3)

with col_R:
    st.subheader("Rot:")
    st.write("...")

with col_G:
    st.subheader("Grün:")
    st.write("...")
    
with col_B:
    st.subheader("Blau:")
    st.write("...")