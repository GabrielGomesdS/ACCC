import json
from collections import defaultdict

# Exemplo fictício de dados
dados_json = '''
{
  "usuarios": [
    {"id": 1, "login": "usuario1", "idade": 25, "genero": "masculino", "compras": [{"id_item": 101, "preco": 20.0}, {"id_item": 102, "preco": 30.0}]},
    {"id": 2, "login": "usuario2", "idade": 30, "genero": "feminino", "compras": [{"id_item": 101, "preco": 20.0}, {"id_item": 103, "preco": 15.0}]},
    {"id": 3, "login": "usuario3", "idade": 35, "genero": "nao_divulgado", "compras": [{"id_item": 102, "preco": 30.0}, {"id_item": 104, "preco": 25.0}]}
  ]
}
'''

# Carregando dados JSON
dados = json.loads(dados_json)

# Inicializando variáveis para análise
compradores = set()
itens_exclusivos = set()
total_compras = 0
rendimento_total = 0.0
compras_por_genero = defaultdict(list)
itens_por_contagem = defaultdict(int)
itens_por_valor = defaultdict(float)

# Analisando dados
for usuario in dados["usuarios"]:
    compradores.add(usuario["login"])
    for compra in usuario["compras"]:
        itens_exclusivos.add(compra["id_item"])
        total_compras += 1
        rendimento_total += compra["preco"]
        compras_por_genero[usuario["genero"]].append(compra["preco"])
        itens_por_contagem[compra["id_item"]] += 1
        itens_por_valor[compra["id_item"]] += compra["preco"]

# Contagem de compradores
numero_total_compradores = len(compradores)

# Análise Geral de Compras
numero_itens_exclusivos = len(itens_exclusivos)
preco_medio_compra = rendimento_total / total_compras
numero_total_compras = total_compras
rendimento_total

# Informações Demográficas Por Gênero
total_compradores_masculinos = len(compras_por_genero["masculino"])
total_compradores_femininos = len(compras_por_genero["feminino"])
total_compradores_nao_divulgados = len(compras_por_genero["nao_divulgado"])

percentagem_masculinos = (total_compradores_masculinos / numero_total_compradores) * 100
percentagem_femininos = (total_compradores_femininos / numero_total_compradores) * 100
percentagem_nao_divulgados = (total_compradores_nao_divulgados / numero_total_compradores) * 100

# Análise de Compras Por Gênero
compras_masculinas = compras_por_genero["masculino"]
compras_femininas = compras_por_genero["feminino"]
compras_nao_divulgadas = compras_por_genero["nao_divulgado"]

numero_compras_masculinas = len(compras_masculinas)
numero_compras_femininas = len(compras_femininas)
numero_compras_nao_divulgadas = len(compras_nao_divulgadas)

preco_medio_compra_masculino = sum(compras_masculinas) / numero_compras_masculinas if numero_compras_masculinas > 0 else 0
preco_medio_compra_feminino = sum(compras_femininas) / numero_compras_femininas if numero_compras_femininas > 0 else 0
preco_medio_compra_nao_divulgado = sum(compras_nao_divulgadas) / numero_compras_nao_divulgadas if numero_compras_nao_divulgadas > 0 else 0

valor_total_compra_masculino = sum(compras_masculinas)
valor_total_compra_feminino = sum(compras_femininas)
valor_total_compra_nao_divulgado = sum(compras_nao_divulgadas)

# Compras por faixa etária (exemplo: dividindo em faixas de 10 anos)
faixas_etarias = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
compras_por_faixa_etaria = defaultdict(int)

for usuario in dados["usuarios"]:
    for faixa_etaria in faixas_etarias:
        if faixa_etaria <= usuario["idade"] < faixa_etaria + 10:
            compras_por_faixa_etaria[faixa_etaria] += len(usuario["compras"])

# Identificando os 5 principais compradores pelo valor total de compra
top_compradores = sorted(dados["usuarios"], key=lambda x: sum(c["preco"] for c in x["compras"]), reverse=True)[:5]

# Imprimindo resultados
print("Contagem de Compradores:")
print("Número total de compradores:", numero_total_compradores)

print("\nAnálise Geral de Compras:")
print("Número de itens exclusivos:", numero_itens_exclusivos)
print("Preço médio de compra:", preco_medio_compra)
print("Número total de compras:", numero_total_compras)
print("Rendimento total:", rendimento_total)

print("\nInformações Demográficas Por Gênero:")
print("Porcentagem e contagem de compradores masculinos:", percentagem_masculinos, total_compradores_masculinos)
print("Porcentagem e contagem de compradores do sexo feminino:", percentagem_femininos, total_compradores_femininos)
print("Porcentagem e contagem de outros / não divulgados:", percentagem_nao_divulgados, total_compradores_nao_divulgados)

print("\nAnálise de Compras Por Gênero:")
print("Número de compras (masculino, feminino, não divulgado):", numero_compras_masculinas, numero_compras_femininas, numero_compras_nao_divulgadas)
print("Preço médio de compra (masculino, feminino, não divulgado):", preco_medio_compra_masculino, preco_medio_compra_feminino, preco_medio_compra_nao_divulgado)
print("Valor Total de Compra (masculino, feminino, não divulgado):", valor_total_compra_masculino, valor_total_compra_feminino, valor_total_compra_nao_divulgado)

print("\nCompras por faixa etária:")
for faixa_etaria, numero_compras in compras_por_faixa_etaria.items():
    print(f"Faixa etária {faixa_etaria}-{faixa_etaria+10}: {numero_compras} compras")

print("\nIdentificar os 5 principais compradores pelo valor total de compra:")
for comprador in top_compradores:
    total_compra_comprador = sum(c["preco"] for c in comprador["compras"])
    print(f"Login: {comprador['login']}, Número de compras: {len(comprador['compras'])}, Preço médio de compra: {total_compra_comprador / len(comprador['compras'])}, Valor Total de Compra: {total_compra_comprador}")

# Identificando os 5 itens mais populares por contagem de compras
top_itens_contagem = sorted(itens_por_contagem.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nIdentificar os 5 itens mais populares por contagem de compras:")
for item_id, numero_compras in top_itens_contagem:
    nome_item = f"Item-{item_id}"
    preco_item = 10.0  # Substitua pelo preço real do item
    valor_total_item = numero_compras * preco_item
    print(f"ID do item: {item_id}, Nome do item: {nome_item}, Número de compras: {numero_compras}, Preço do item: {preco_item}, Valor Total de Compra: {valor_total_item}")

# Identificando os 5 itens mais lucrativos pelo valor total de compra
top_itens_valor = sorted(itens_por_valor.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nIdentificar os 5 itens mais lucrativos pelo valor total de compra:")
for item_id, valor_total_item in top_itens_valor:
    nome_item = f"Item-{item_id}"
    preco_item = 10.0  # Substitua pelo preço real do item
    numero_compras_item = itens_por_contagem[item_id]
    print(f"ID do item: {item_id}, Nome do item: {nome_item}, Número de compras: {numero_compras_item}, Preço do item: {preco_item}, Valor Total de Compra: {valor_total_item}")
