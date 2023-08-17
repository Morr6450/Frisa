import streamlit as st
import pandas as pd
import base64
import io

st.set_page_config(page_title='Fundacion Frisa', page_icon=':man-woman-boy-boy:', layout='wide')

st.title(' :man-woman-boy-boy: :earth_americas: Fundacion Frisa')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(':file uploader: Sube un archivo', type=(["csv", "txt", "xlsx", "xls"]))

if fl is not None:
    content = fl.read()
    content_type = fl.type
    
    if content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(io.BytesIO(content), encoding='cp1252')
    else:
        df = pd.read_csv(io.StringIO(content.decode('utf-8')), encoding='cp1252')

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
    # Guardar el DataFrame actualizado en el archivo CSV y codificación cp1252
    df.to_csv('Prueba_de_datos.csv', index=False, encoding='cp1252')

# Agregar el botón de descarga del archivo CSV actualizado
if not df.empty:
    csv_filename = 'Prueba_de_datos_actualizado.csv'
    csv_data = df.to_csv(index=False, encoding='cp1252')
    b64 = base64.b64encode(csv_data.encode()).decode()
    st.markdown(f'<a href="data:file/csv;base64,{b64}" download="{csv_filename}">Descargar CSV Actualizado</a>', unsafe_allow_html=True)
