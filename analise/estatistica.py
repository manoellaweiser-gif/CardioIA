import pandas as pd

arquivo = "/Users/mac/Desktop/CardioIA/dados/heart_disease_final.csv"

df = pd.read_csv(arquivo)

print(df.head())


print("IDADE")
print(df["idade"].describe())

print("\nCOLESTEROL")
print(df["colesterol"].describe())

print("\nPRESSÃO ARTERIAL")
print(df["pressao_arterial"].describe())

print("\nFREQUÊNCIA CARDÍACA MÁXIMA")
print(df["frequencia_cardiaca_max"].describe())

print("\nSEXO")
print(df["sexo"].value_counts())

print("\nDIAGNÓSTICO")
print(df["diagnostico"].value_counts().sort_index())