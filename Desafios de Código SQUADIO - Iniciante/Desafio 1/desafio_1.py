# Desafio: A Aventura do Explorador

## Quantidade de entradas
quantidade_passos = int(input())

## Fitro inicial para formatação da saída
if quantidade_passos > 0:
    ## Aqui, vamos gerar a informação
    for i in range(1,quantidade_passos+1):
        if i == 1: ## Singular (já que é apenas 1 passo) do texto de saida
            print(f'Explorador: {i} passo')
        else: ## Plural (mais de um passo) do texto de saida
            print(f'Explorador: {i} passos')
else:
    print("Nenhum passo dado na floresta.")