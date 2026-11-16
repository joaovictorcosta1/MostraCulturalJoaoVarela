Atividade Prática em Python — Calculadora de Média Escolar
Descrição

Programa de linha de comando que recebe as notas de um aluno, calcula a média aritmética e informa a situação final: Aprovado, Recuperação ou Reprovado.

Objetivo

Praticar conceitos básicos de Python:

Entrada e saída de dados (input / print)
Funções
Estruturas condicionais (if, elif)
Laços de repetição (while, for)
Listas e compreensão de listas
Tratamento de erros (try / except)
Como funciona
O programa pede o nome do aluno e a quantidade de notas.
Cada nota é validada (deve ser um número entre 0 e 10).
A média é calculada e a situação é definida pelas regras abaixo:
Média	Situação
≥ 7,0	Aprovado
≥ 5,0 e < 7,0	Recuperação
< 5,0	Reprovado
Como executar

Requisito: Python 3.8 ou superior.

bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

# 2. Entre na pasta da atividade
cd SEU-REPOSITORIO/atividade-python-pratica

# 3. Execute o script
python script.py
Exemplo de uso
text
=== Calculadora de Média Escolar ===
Nome do aluno: Maria
Quantidade de notas: 3
Nota 1: 8
Nota 2: 6,5
Nota 3: 7

--- Resultado ---
Aluno: Maria
Notas: [8.0, 6.5, 7.0]
Média: 7.17
Situação: Aprovado
Estrutura da pasta
text
atividade-python-pratica/
├── README.md
└── script.py
