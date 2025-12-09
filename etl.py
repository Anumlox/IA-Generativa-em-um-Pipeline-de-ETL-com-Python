# Importamento das bibliotecas

import pandas as pd
from openai import OpenAI

# Configuração da API

# Chave da OpenAI
client = OpenAI(api_key="")


def gerar_resposta(texto):

    # Gera respostas acolhedoras e cuidadosa

    prompt = (
        f"Mensagem: '{texto}'. "
        "Gere uma resposta acolhedora, empática, segura, sem diagnóstico, voce quer ajudar a pessoa."
        "e oferecendo apoio emocional prático."
    )

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é uma IA acolhedora que dá apoio emocional seguro, voce tem sentimento de mãe de querer ajudar."},
            {"role": "user", "content": prompt}
        ]
    )

    return resposta.choices[0].message.content


# Extract
print("Leitura de dados...")
df = pd.read_csv("dados.csv")
print("Dados carregados com sucesso!\n")

print(df.head())
print("\n----------------------------------------\n")

# Transform
print("Gerando respostas com IA... (pode levar alguns segundos)")

df["resposta_gerada"] = df["mensagem"].apply(gerar_resposta)

print("Respostas geradas com sucesso!\n")

# Load
df.to_csv("resultado.csv", index=False)

print("Arquivo 'resultado.csv' salvo com sucesso!")
print("Pipeline ETL finalizado!")
