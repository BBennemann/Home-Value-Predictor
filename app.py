import streamlit as st
import pandas as pd
from ModelGenerator import Previsao

st.set_page_config(layout="wide")
st.title("🏠 Previsão de Valor de Imóveis")
st.markdown("Preencha as características do imóvel para obter uma estimativa de valor.")

# Formulário para agrupar todos os inputs
with st.form("model_features_form"):
    st.header("Características Principais e Qualidade")
    col1, col2, col3 = st.columns(3)
    with col1:
        MSSubClass = st.number_input("Código do Tipo de Moradia (MSSubClass)", value=60, step=1)
    with col2:
        OverallQual = st.slider("Qualidade Geral (OverallQual)", 1, 10, 7)
    with col3:
        OverallCond = st.slider("Condição Geral (OverallCond)", 1, 10, 5)

    st.divider()
    st.header("Datas e Venda")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        YearBuilt = st.number_input("Ano de Construção (YearBuilt)", 1800, 2025, 2003, format="%d")
    with col2:
        YearRemodAdd = st.number_input("Ano da Reforma (YearRemodAdd)", 1800, 2025, 2003, format="%d")
    with col3:
        GarageYrBlt = st.number_input("Ano da Garagem (GarageYrBlt)", 1800, 2025, 2003, format="%d")
    with col4:
        YrSold = st.number_input("Ano da Venda (YrSold)", 2000, 2025, 2008, format="%d")
        MoSold = st.slider("Mês da Venda (MoSold)", 1, 12, 7)

    st.divider()
    st.header("Áreas (em pés quadrados, exceto LotArea)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        LotArea = st.number_input("Área do Lote (LotArea)", value=9600, step=50)
        MasVnrArea = st.number_input("Área de Alvenaria (MasVnrArea)", value=0.0, step=10.0)
        TotalBsmtSF = st.number_input("Área Total do Porão (TotalBsmtSF)", value=1057.0, step=10.0)
    with col2:
        BsmtFinSF1 = st.number_input("Área Acabada do Porão-Tipo 1(BsmtFinSF1)", value=443.0, step=10.0)
        BsmtFinSF2 = st.number_input("Área Acabada do Porão-Tipo 2(BsmtFinSF2)", value=46.0, step=10.0)
        BsmtUnfSF = st.number_input("Área não Acabada do Porão (BsmtUnfSF)", value=567.0, step=10.0)
    with col3:
        # Nomes de variáveis corrigidos
        FirstFlrSF = st.number_input("Área do 1º Andar (1stFlrSF)", value=1087.0, step=10.0)
        SecondFlrSF = st.number_input("Área do 2º Andar (2ndFlrSF)", value=0.0, step=10.0)
        GrLivArea = st.number_input("Área Habitável (GrLivArea)", value=1515.0, step=10.0)
    with col4:
        GarageArea = st.number_input("Área da Garagem (GarageArea)", value=472.0, step=10.0)
        WoodDeckSF = st.number_input("Área do Deck de Madeira (WoodDeckSF)", value=94.0, step=10.0)
        OpenPorchSF = st.number_input("Área da Varanda Aberta (OpenPorchSF)", value=46.0, step=10.0)
        LowQualFinSF = st.number_input("Área de Baixa Qualidade (LowQualFinSF)", value=0, step=10)


    st.divider()
    st.header("Distribuição de Cômodos e Itens")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        FullBath = st.number_input("Banheiros Completos (Acima do Solo)", 0, 10, 2)
        HalfBath = st.number_input("Lavabos (Acima do Solo)", 0, 10, 0)
        BsmtFullBath = st.number_input("Banheiros Completos (Porão)", 0, 10, 0)
        BsmtHalfBath = st.number_input("Lavabos (Porão)", 0, 10, 0)
    with col2:
        BedroomAbvGr = st.number_input("Quartos (Acima do Solo)", 0, 15, 3)
        KitchenAbvGr = st.number_input("Cozinhas (Acima do Solo)", 0, 5, 1)
        TotRmsAbvGrd = st.number_input("Total de Cômodos (Acima do Solo)", 0, 20, 6)
    with col3:
        Fireplaces = st.number_input("Lareiras", 0, 5, 1)
        GarageCars = st.slider("Vagas na Garagem (Carros)", 0, 6, 2)
        PoolArea = st.number_input("Área da Piscina", value=0, step=10)
    with col4:
        EnclosedPorch = st.number_input("Área da Varanda Fechada", value=0, step=10)
        # Nome de variável corrigido
        ThreeSsnPorch = st.number_input("Área da Varanda de 3 Estações (3SsnPorch)", value=0, step=10)
        ScreenPorch = st.number_input("Área da Varanda com Tela", value=0, step=10)
        MiscVal = st.number_input("Valor de Itens Diversos ($)", value=0, step=50)

    # Botão de envio
    submitted = st.form_submit_button("Gerar Previsão")


if submitted:
    # O dicionário foi corrigido para usar as variáveis válidas
    dados_coletados = {
        'Id': [0],
        'MSSubClass': [MSSubClass],
        'LotArea': [LotArea],
        'OverallQual': [OverallQual],
        'OverallCond': [OverallCond],
        'YearBuilt': [YearBuilt],
        'YearRemodAdd': [YearRemodAdd],
        'MasVnrArea': [MasVnrArea],
        'BsmtFinSF1': [BsmtFinSF1],
        'BsmtFinSF2': [BsmtFinSF2],
        'BsmtUnfSF': [BsmtUnfSF],
        'TotalBsmtSF': [TotalBsmtSF],
        '1stFlrSF': [FirstFlrSF],       # Corrigido
        '2ndFlrSF': [SecondFlrSF],      # Corrigido
        'LowQualFinSF': [LowQualFinSF],
        'GrLivArea': [GrLivArea],
        'BsmtFullBath': [BsmtFullBath],
        'BsmtHalfBath': [BsmtHalfBath],
        'FullBath': [FullBath],
        'HalfBath': [HalfBath],
        'BedroomAbvGr': [BedroomAbvGr],
        'KitchenAbvGr': [KitchenAbvGr],
        'TotRmsAbvGrd': [TotRmsAbvGrd],
        'Fireplaces': [Fireplaces],
        'GarageYrBlt': [GarageYrBlt],
        'GarageCars': [GarageCars],
        'GarageArea': [GarageArea],
        'WoodDeckSF': [WoodDeckSF],
        'OpenPorchSF': [OpenPorchSF],
        'EnclosedPorch': [EnclosedPorch],
        '3SsnPorch': [ThreeSsnPorch],       # Corrigido
        'ScreenPorch': [ScreenPorch],
        'PoolArea': [PoolArea],
        'MiscVal': [MiscVal],
        'MoSold': [MoSold],
        'YrSold': [YrSold]
    }
    
    # Converter para DataFrame. A ordem das colunas será a mesma do dicionário.
    df_usuario = pd.DataFrame(dados_coletados)

    st.subheader("Previsão do preço:")
    features_ordenadas = ['Id', 'MSSubClass','LotArea','OverallQual','OverallCond','YearBuilt','YearRemodAdd','MasVnrArea','BsmtFinSF1','BsmtFinSF2','BsmtUnfSF','TotalBsmtSF','1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd','Fireplaces','GarageYrBlt','GarageCars','GarageArea','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal','MoSold','YrSold']

    df_usuario = df_usuario.reindex(columns=features_ordenadas, fill_value=0)
    previsao = Previsao(df_usuario)
    previsao = f"{previsao[0] :.2f}".replace('.', ',')
    st.markdown(f"Preço previsto para a casa: {previsao}")