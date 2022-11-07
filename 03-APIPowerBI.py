from fastapi import FastAPI

import pandas as pd


app = FastAPI()

one_hot_enc = pd.read_pickle('one_hot_enc.pkl')
modelo = pd.read_pickle('knn_model.pkl')
scaler = pd.read_pickle('scaler.pkl')

@app.get('/modelo/v1={idade}&v2={renda}&v3={situacao_moradia}&v4={tempo_trabalhado}&v5={motivo_emprestimo}&v6={score}&v7={valor_emprestimo}&v8={taxa_juros}&v9={devedor}&v10={tempo_historico_credito}')

def previsao_modelo(idade, renda, situacao_moradia, tempo_trabalhado, motivo_emprestimo, score, valor_emprestimo, taxa_juros, devedor, tempo_historico_credito):
    dados = {
        'idade': [float(idade)],
        'renda': [float(renda)],
        'situacao_moradia': [situacao_moradia],
        'tempo_trabalhado': [float(tempo_trabalhado)],
        'motivo_emprestimo': [motivo_emprestimo],
        'score': [score],
        'valor_emprestimo': [float(valor_emprestimo)],
        'taxa_juros': [float(taxa_juros)],
        'devedor': [float(devedor)],
        'tempo_historico_credito': [float(tempo_historico_credito)]
    }

    dados = pd.DataFrame(dados)

    dados['score'] = dados['score'].map({'G': 0, 'F': 1, 'E': 2, 'D': 3, 'C': 4, 'B': 5, 'A': 6})

    dados = one_hot_enc.transform(dados)
    dados_transformados = pd.DataFrame(dados, columns=one_hot_enc.get_feature_names_out())

    dados_transformados = scaler.transform(dados_transformados)
    dados_transformados = pd.DataFrame(dados_transformados, columns = one_hot_enc.get_feature_names_out())

    return {'result': modelo.predict(dados_transformados).tolist()[0],
            'probability_0': modelo.predict_proba(dados_transformados).tolist()[0][0],
            'probability_1': modelo.predict_proba(dados_transformados).tolist()[0][1]}
