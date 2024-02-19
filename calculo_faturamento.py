import json

def carregar_faturamento_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        dados_faturamento = json.load(file)
    return dados_faturamento['faturamento_diario']

def calcular_estatisticas_faturamento(faturamento_diario):
    faturamento_valido = [valor for valor in faturamento_diario.values() if isinstance(valor, (int, float))]
    
    if faturamento_valido:
        menor_valor = min(faturamento_valido)
        maior_valor = max(faturamento_valido)
        
        media_mensal = sum(faturamento_valido) / len(faturamento_valido)
        
        dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)
        
        return menor_valor, maior_valor, dias_acima_da_media
    else:
        return None, None, None

nome_arquivo = 'faturamento.json'
faturamento_diario = carregar_faturamento_do_arquivo(nome_arquivo)
menor, maior, acima_da_media = calcular_estatisticas_faturamento(faturamento_diario)

if menor is not None:
    print("Menor valor de faturamento diário:", menor)
    print("Maior valor de faturamento diário:", maior)
    print("Número de dias com faturamento diário acima da média mensal:", acima_da_media)
else:
    print("Não há dados válidos para calcular as estatísticas de faturamento.")
