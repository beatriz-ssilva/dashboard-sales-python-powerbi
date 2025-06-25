import pandas as pd
import os

#caminhos dos arquivos
INPUT_FILE = os.path.join('..', 'data', 'vendas.csv')
OUTPUT_FILE = os.path.join('..', 'data', 'vendas_limpo.csv')

def carregar_dados(caminho):
    try:
        df = pd.read_csv(caminho)
        print("✅ Dados carregados com sucesso.")
        return df
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho}")
        exit()
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        exit()

def limpar_dados(df):
    print("Visualizando os primeiros dados:")
    print(df.head())

    #limpeza
    df = df.dropna()
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
    df['Valor'] = df['Valor'].astype(float)
    df['Quantidade'] = df['Quantidade'].astype(int)

    #nova coluna Receita
    df['Receita'] = df['Valor'] * df['Quantidade']
    
    return df

def salvar_dados(df, caminho):
    df.to_csv(caminho, index=False)
    print(f"Arquivo exportado com sucesso para: {caminho}")

if __name__ == "__main__":
    df_original = carregar_dados(INPUT_FILE)
    df_tratado = limpar_dados(df_original)
    salvar_dados(df_tratado, OUTPUT_FILE)
    print("✅ Processo de limpeza concluído com sucesso!")
