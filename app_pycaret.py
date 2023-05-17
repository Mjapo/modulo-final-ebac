import streamlit as st
import pandas as pd
import tempfile
import base64
import os

def convert_to_ftr(df):
    # Realize aqui a conversão para o formato FTR
    # ...
    # Retorne o arquivo FTR (pode ser o caminho do arquivo salvo)
    # Certifique-se de fornecer o caminho completo para o arquivo, incluindo a extensão .ftr
    ftr_file = "arquivo.ftr"
    df.to_feather(ftr_file)
    return ftr_file

# Interface do Streamlit
st.title("Conversor de CSV para FTR")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Conversão temporária para arquivo CSV
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(uploaded_file.read())

    # Leitura do arquivo CSV
    df = pd.read_csv(tmp.name)

    # Exibição dos dados
    st.subheader("Dados do arquivo CSV")
    st.dataframe(df)

    # Botão para conversão
    if st.button("Converter para FTR"):
        # Conversão para FTR
        ftr_file = convert_to_ftr(df)

        # Download do arquivo FTR
        st.markdown(f"### Download do arquivo FTR")
        with open(ftr_file, "rb") as f:
            bytes_data = f.read()
            base64_data = base64.b64encode(bytes_data).decode("utf-8")
            href = f'<a href="data:application/octet-stream;base64,{base64_data}" download="arquivo.ftr">Clique aqui para baixar</a>'
            st.markdown(href, unsafe_allow_html=True)





