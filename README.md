# Avaliação de Carros

Este é um script simples em Python para avaliar carros com base em sua nota e ajustar o preço conforme a nota atribuída.

## Descrição

O script pede ao usuário para inserir uma nota para o carro e o preço do carro. Com base na nota, ele ajusta o preço do carro da seguinte forma:

- Se a nota for entre 0 e 50 (inclusive), o preço do carro é reduzido em 30%.
- Se a nota for entre 51 e 80 (inclusive), o preço do carro permanece o mesmo.
- Se a nota for entre 81 e 100 (inclusive), o preço do carro é aumentado em 20%.
- Se a nota for fora do intervalo de 0 a 100, uma mensagem de valor inválido é exibida.

## Como usar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Salve o script em um arquivo com a extensão `.py` (por exemplo, `avaliacao_carros.py`).
3. Abra um terminal ou prompt de comando.
4. Navegue até o diretório onde o script foi salvo.
5. Execute o script com o comando `python avaliacao_carros.py`.
6. Siga as instruções na tela para inserir a nota e o preço do carro.

## Exemplo de uso

```bash
Digite a nota do carro: 45
Digite o preço do carro: 50000
O preço final do carro é: 35000.0
