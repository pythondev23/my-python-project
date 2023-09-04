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

def convert_hex_to_rgb(hex_code: str) -> int:   
    hex = "0123456789ABCDEF"
    return (hex.index(hex_code[0])*16) + (hex.index(hex_code[1]))
    
# 2) umwandeln:
if check_hex(hex_in):

    r = convert_hex_to_rgb(hex_in[1:3])
    g = convert_hex_to_rgb(hex_in[3:5])
    b = convert_hex_to_rgb(hex_in[5:7])

    col_R, col_G, col_B = st.columns(3)

    with col_R:
        st.subheader("Rot:")
        st.subheader(r)

    with col_G:
        st.subheader("Grün:")
        st.subheader(g)
        
    with col_B:
        st.subheader("Blau:")
        st.subheader(b)
        
else:
    st.error("Das ist kein valider Hex-Code!")