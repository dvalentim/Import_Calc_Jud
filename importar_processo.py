from modulos import *
from cria_variavel import *

class Importar_Processo(Quebra_Identidade):
#O método analise() cria uma lista chamada identidade com as informações do processo

    def importar(self):
        self.identidade = []
        contador1 = 0
        contador2 = 0
#Dados iniciais da capa do processo
        with open("Dados_Import.txt", 'r', encoding="utf-8") as manipulador:
            for linha in manipulador:
                if linha[0:len('Número:')] == 'Número:':
                    self.identidade.append(linha.rstrip())
                if linha[0:len('Órgão julgador:')] == 'Órgão julgador:':
                    self.identidade.append(linha.rstrip())
                if linha[linha.find('('):(linha.find(')')) + 1] == '(AUTOR)':
                    if linha == '(AUTOR)\n':
                        autor = linha
                        contador2 = contador1
                    else:
                        autor = ''
                        self.identidade.append(linha.rstrip())
                if linha[0:len('Valor da causa:')] == 'Valor da causa:':
                    self.identidade.append(linha.rstrip())
                if linha[0:len('Assuntos:')] == 'Assuntos:':
                    self.identidade.append(linha.rstrip())
                if linha[0:len('INSTITUTO NACIONAL DO SEGURO SOCIAL - INSS'
                               )] == 'INSTITUTO NACIONAL DO SEGURO SOCIAL - INSS':
                    self.identidade.append(linha.rstrip())
                    break
                contador1 = contador1 + 1
        if self.identidade != []:
            if autor != '':
                with open("Dados_Import.txt", 'r', encoding="utf-8") as manipulador:
                    frase = manipulador.readlines()[contador2 + 1]
                    self.identidade.append(frase.rstrip())

#data da citação
        contador1 = 0
        contador2 = 0
        if self.identidade != []:
            with open("Dados_Import.txt", 'r', encoding="utf-8") as manipulador:
                #percorrer linhas e enumera a partir de 1
                for linha, frase in enumerate(manipulador, 1):
                    # e verifica se a frase está na linha
                    if 'automaticamente realizada a citação' in frase:
                        # percorre a linhas e enumera a partir de contador1
                        for linha, frase in enumerate(manipulador, (contador1 + 1)):
                            if 'INSTITUTO NACIONAL DO SEGURO SOCIAL' in frase:
                                contador2 = contador1
                                break
                    if contador2 != 0:
                        break
                    else:
                        contador1 = contador1 + 1
            with open("Dados_Import.txt", 'r', encoding="utf-8") as manipulador:
                frase = manipulador.readlines()[contador2 - 1]
                self.identidade.append(frase.rstrip())
        self.quebra_identidade()