""""11.	Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3."""

materia1 = float(input("Digite sua nota: "))
materia2 = float(input("Digite sua nota: "))
materia3 = float(input("Digite sua nota: ")) 

media = (materia1 + materia2 + materia3) / 3 
aprovado = media > 7 
print("O aluno foi aprovado? ", aprovado)