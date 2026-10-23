# Controle de Estoque de Medicamentos 

Projeto em python que nasceu de um trabalho da faculdade sobre sistemas. Inspirado na rotina da farmácia do SUS, pensei em algo para facilitar e ajudar o controle do estoque dos medicamentos, tanto os que chegam quanto os que saem.

## O que faz 
- Cadastra medicamentos (nome, validade, quantidade, lote)
- Valida a quantidade e a validade digitada
- Consulta o estoque (nome e quantidade)
- Classifica a validade em: vencido, próximo ao vencimento ou dentro da validade
- Salva os dados em JSON e protege o arquivo caso ele esteja corrompido

## Como rodar
É necessário o Python 3.12 ou mais recente. 
No terminal, dentro da pasta do projeto:
```
python estoque_med.py
```
## Próximos passos
- Organizar o código em funções
- Consultar a validade de um medicamento específico
