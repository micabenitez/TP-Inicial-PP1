import numpy as np
import pickle
from sklearn import svm
import streamlit as st

# Path del modelo preentrenado
MODEL_PATH = 'modelo/model.pkl'


def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Título
    html_temp = """
        <h1 style="color:#058ED9;text-align:center;">Predicción de ACV </h1>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    with st.form("my_form"):
        col1, col2 = st.columns(2)
        with col1:
            # Input de datos
            genero = st.radio(
                        "Género",
                    ('Masculino', 'Femenino')
                )
            
            edad = st.number_input(label='Edad',
                    min_value = 1,
                    max_value = 85,
                    value=50,
                    step=1)
            
            hipertension = st.radio(
                        "Tiene hipertensión?",
                    ('Si', 'No')
                )
        
            enfCardiacas = st.radio(
                        "Tiene enfermedades cardíacas?",
                    ('Yes', 'No'),
                )

            matrimonio = st.radio(
                        "Estado civil",
                    ('Casado/Divorciado', 'Soltero'),
                )
            
        
        with col2:
            residencia = st.radio(
                        "Tipo de residencia",
                        ('Urbana', 'Rural')
                    )
        
            nivelGlucosa= st.slider(
                    label = "Nivel de glucosa en sangre",
                    min_value = 50.0,
                    max_value = 280.0,
                    value=130.0,
                    step=0.1
                )
            
            bmi = st.number_input(
                    label = "Índice de masa corporal (BMI)",
                    min_value = 10.0,
                    max_value = 50.0,
                    value=25.0,
                    step=1.0
                )
            work_type = st.selectbox(
                    label='Tipo de trabajo',
                    options=('Autónomo', 'Sector Público','Sector Privado')
                    )

            smoking = st.selectbox(
                    label='Tabaquismo',
                    options=('Nunca fumó', 'Ex-fumador','Fumador')
                    )
           
        submit = st.form_submit_button("Evaluar")

    if submit == True:
        if genero == 'Masculino':
            gender = 1
        else:
            gender = 0

        if hipertension == 'Si':
            hypertension = 1
        else:
            hypertension = 0

        if enfCardiacas == 'Si':
            heart_disease = 1
        else:
            heart_disease = 0

        if matrimonio == 'Casado/Divorciado':
            ever_married = 1
        else:
            ever_married = 0

        if residencia == 'Urbana':
            Residence_type = 1
        else:
            Residence_type = 0

        if work_type == 'Autónomo':
            work_type_Government_Job=0
            work_type_Private=0
            work_type_Self_employed=1
        elif work_type == 'Sector Público':
            work_type_Government_Job=1
            work_type_Private=0
            work_type_Self_employed=0
        elif work_type == 'Sector Privado':
            work_type_Government_Job=0
            work_type_Private=1
            work_type_Self_employed=0
        else:
            work_type_Government_Job=0
            work_type_Private=0
            work_type_Self_employed=0

        if smoking== 'Nunca fumó':
            smoking_status_Former_Smoker=0
            smoking_status_Never_Smoked=1
            smoking_status_Smoker=0
        elif smoking == 'Ex-fumador':
            smoking_status_Former_Smoker=1
            smoking_status_Never_Smoked=0
            smoking_status_Smoker=0
        elif smoking== 'Fumador':
            smoking_status_Former_Smoker=0
            smoking_status_Never_Smoked=0
            smoking_status_Smoker=1

        
        x = [gender,
             edad,
            hypertension,
            heart_disease,
            ever_married,
            Residence_type,
            nivelGlucosa,
            bmi,
            work_type_Government_Job,
            work_type_Private,
            work_type_Self_employed,
            smoking_status_Former_Smoker,
            smoking_status_Never_Smoked,
            smoking_status_Smoker
        ]

        y_pred = model.predict(np.asarray(x).reshape(1,-1))
        pred = y_pred
        if pred==1:
            pred = 'Propenso a sufrir un ACV'
        elif pred==0:
            pred = 'No propenso a sufrir un ACV'
        
        st.info(pred)
        
if __name__ == '__main__':
    main()