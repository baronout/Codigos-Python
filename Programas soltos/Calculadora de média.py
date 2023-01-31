nome_do_aluno = str(input("Insira o nome do aluno: "))
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media_das_notas = round((nota1*0.4)+(nota2*0.6), 1)

posicao = nome_do_aluno.find(" ")
primeira_letra = nome_do_aluno[0]
nome_do_jeito_certo = primeira_letra.upper() + nome_do_aluno[1:posicao]




print(nome_do_jeito_certo,media_das_notas, sep="    ")