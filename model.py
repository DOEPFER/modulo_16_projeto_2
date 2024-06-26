import streamlit         as st
import pandas            as pd

import pickle
from io                  import BytesIO

custom_params = {"axes.spines.right": False, "axes.spines.top": False}

@st.cache_data(show_spinner=True)
def load_file(file_data):
    try:
        return pd.read_csv(file_data, sep=',')
    except:
        return st.write('Não foi possível ler o arquivo')
    
@st.cache_data
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

def main():
    st.set_page_config(page_title = 'Projeção de renda', layout="wide", initial_sidebar_state='expanded')

    st.write('# Projeção de renda')

    st.sidebar.write("## Enviar arquivo para projeção")
    file = st.sidebar.file_uploader("Arquivo de dados", type = ['csv'])

    if (file is not None):

        data_raw = load_file(file)
        data = data_raw.copy()

        st.write('## Dados enviados')
        st.markdown("---")
        st.write(data_raw)

        with open('model/decision_tree_regression.pkl', 'rb') as model:
            decision_tree_regression = pickle.load(model)

        data['renda'] = decision_tree_regression.predict(data)

        _xlsx = to_excel(data)
        st.download_button(label='Download das projeções em EXCEL', data=_xlsx, file_name= 'projections.xlsx')

if __name__ == '__main__':
	main()