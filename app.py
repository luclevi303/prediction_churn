import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## Creation de l'application de prediction de churn client 

st.title("Prediction de Churn Client ")

tab1, tab2, tab3= st.tabs(["Description de l'application","Prediction","Analyse "])

with tab1:
    st.set_page_config(layout="wide")
    with st.expander("A propos de l'application "):
        st.write("L'Application Predict_churn est une solution analytique créee pour aider les entreprises dans le domanie de la telecommunication a determiner ,avec plus de precision, la probabilité qu'un client se désabonne afin d'adopter les strategies adéquates pour y remider a temps ")

    

