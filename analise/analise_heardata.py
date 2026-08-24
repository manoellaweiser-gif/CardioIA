import pandas as pd

# Arquivo original
arquivo = "/Users/mac/Desktop/CardioIA/dados_cardiacos.csv"

# Ler os dados
df = pd.read_csv(
    arquivo,
    header=None,
    sep=r"\s+"
)

# Nomear as 14 colunas
df.columns = [
    "idade",
    "sexo",
    "tipo_dor_peito",
    "pressao_arterial",
    "colesterol",
    "glicemia",
    "ecg",
    "frequencia_cardiaca_max",
    "angina_exercicio",
    "oldpeak",
    "inclinacao_st",
    "vasos_principais",
    "thal",
    "diagnostico"
]

# Verificar os dados
print(df.head())
print(df.shape)

print("Linhas:", df.shape[0])
print("Colunas:", df.shape[1])

# Salvar novo CSV
saida = "/Users/mac/Desktop/CardioIA/dados/heart_disease_final.csv"

df.to_csv(saida, index=False)






