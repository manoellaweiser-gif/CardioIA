import pandas as pd

# Arquivo original da base Cleveland
arquivo = "/Users/mac/Desktop/CardioIA/dados/processed.cleveland.data"

# Nome das colunas
colunas = [
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

# Ler o arquivo original
df = pd.read_csv(
    arquivo,
    header=None,
    names=colunas,
    na_values="?"
)

# Verificações
print(df.head())
print("\nDimensão:", df.shape)

print("\nLinhas:", df.shape[0])
print("Colunas:", df.shape[1])

print("\nValores ausentes:")
print(df.isnull().sum())

print("\nDuplicatas:")
print(df.duplicated().sum())

# Salvar CSV final
saida = "/Users/mac/Desktop/CardioIA/dados/heart_disease_final.csv"

df.to_csv(saida, index=False)

print("\nCSV salvo com sucesso!")