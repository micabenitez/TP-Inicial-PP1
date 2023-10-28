# Proyecto Machine Learning

TP Inicial - Proyecto Profesional I / Lab. de Construcción de Software
 
Implementación de un modelo de Machine Learning que predice si una persona corre el riesgo de sufrir un ataque cerebrovascular (ACV) en función de diversos factores como edad, género, nivel de glucosa en sangre,
tabaquismo, hipertensión, enfermedades cardíacas, tipo de residencia, tipo de trabajo e índice de masa corporal. 

### [DEMO](https://prediccionacv.streamlit.app/)

## UI
![image](https://github.com/micabenitez/TP-Inicial-PP1/assets/117873822/d86b40e5-56bb-478d-a07e-d68b2df3c22d)


# Características
### Modelo utilizado
* XGBoost

### Matriz de confusión
  ![image](https://github.com/micabenitez/TP-Inicial-PP1/assets/117873822/464b8a99-4b53-458c-8d8c-824ab9d45fad)
### Curva ROC/AUC
![image](https://github.com/micabenitez/TP-Inicial-PP1/assets/117873822/6617f6e2-8de6-4c43-be13-c890dcc2da1c)
### Métricas del modelo 
 ![image](https://github.com/micabenitez/TP-Inicial-PP1/assets/117873822/6f818058-4277-4d04-8a2f-99bfd3e91fc9)
- **Exactitud (Accuracy):** La exactitud mide la proporción de predicciones correctas (verdaderos positivos y verdaderos negativos) con respecto al total de predicciones.
 
- **Precisión (Precision):** Esta métrica mide la capacidad del modelo para predecir correctamente los positivos.

- **Recuperación o Sensibilidad (Recall o Sensitivity):** Mide la capacidad del modelo para capturar todos los casos positivos y es útil cuando es crítico no perder ningún caso positivo.

- **Puntaje F1 (F1 Score):** El puntaje F1 es la media armónica entre precisión y recuperación. Es útil cuando se busca un equilibrio entre la precisión y la capacidad de recuperación. 




