import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title='Fundacion Frisa', page_icon=':man-woman-boy-boy:', layout='wide')

st.title(' :man-woman-boy-boy: :earth_americas: Fundacion Frisa')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(':file uploader: Sube un archivo', type=(["csv"]))

if fl is not None:
    df = pd.read_csv(fl, encoding='utf-8')

st.header('Archivo existente')
st.write(df)

st.sidebar.header('Opciones')
options_form = st.sidebar.form('options_form')

user_name = options_form.text_input("Nombre")
user_flastname = options_form.text_input("Apellido paterno")
user_slastname = options_form.text_input("Apellido materno")
user_mail = options_form.text_input("Correo Electronico")
user_phone = options_form.text_input("Telefono")
user_type = options_form.text_input("Convocatoria")
add_data = options_form.form_submit_button()

if add_data:
    new_data = {'Nombre': user_name, "Apellido paterno": user_flastname, "Apellido materno": user_slastname,
                "Correo Electronico": user_mail, "Telefono": int(user_phone), "Tipo de Convocatoria": user_type}
    #df = df.append(new_data, ignore_index=True)
    df.loc[len(df)] = new_data
    # Guardar el DataFrame actualizado en el archivo CSV con codificación utf-8
    #df.to_csv(index=False).encode('utf-8')

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')
# Agregar el botón de descarga del archivo CSV actualizado
if not df.empty:
    csv = convert_df(df)
    st.download_button(
       "Press to Download",
       csv,
       "file.csv",
       "text/csv",
       key='download-csv'
    )
