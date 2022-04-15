from modulos import *
from telaApp import *

class Parametros:

    def converte_data(self, data):
        #formata o dia
        posicao1 = len(data)-2
        posicao2 = len(data)
        dia = data[posicao1:posicao2]
        #formata o mês
        posicao1 = len(data)-5
        posicao2 = len(data)-3
        mes = data[posicao1:posicao2]
        #formata o ano
        posicao1 = 0
        posicao2 = 4
        ano = data[posicao1:posicao2]
        self.data_formatada = f'{dia}/{mes}/{ano}'
    
    def periodo_especial(self):
        data_inicial = ''
        data_final = ''
        periodo = []
        
        with open("script/Dados_Import.txt", 'r', encoding="utf-8") as manipulador:
            for linha in manipulador:
                #captura o tipo de cálculo
                if 'data inicial:' in linha:
                    if linha[40:41] == '-':
                        break 
                    else:
                        #data inicial
                        data_inicial = linha[40:50]
                        self.converte_data(data_inicial)
                        data_inicial = self.data_formatada
                        #data final
                        data_final = linha[76:86]
                        self.converte_data(data_final)
                        data_final = self.data_formatada
                        dicionario = {'inicio': data_inicial, 'final' : data_final}
                        periodo.append(dicionario)
                if 'Seção 4 de 19' in linha:
                    break
        print(periodo)


                        

        

        
    def variaveis_iniciais(self):

        self.vtipo_calculo = ''
        self.vdib = ''
        self.vespecie = ''
        with open("script/Dados_Import.txt", 'r', encoding="utf-8") as manipulador:
            for linha in manipulador:
                #captura o tipo de cálculo
                if 'Tipo de cálculo:' in linha:
                    posicao1 = len('Tipo de cálculo:') + 1
                    posicao2 = len(linha)-1
                    self.vtipo_calculo = linha[posicao1:posicao2]
                #captura a DIB do benefício
                if 'Data de início do benefício (DIB):' in linha:
                    posicao1 = len('Data de início do benefício (DIB):') + 1
                    posicao2 = len(linha)-12
                    self.vdib = linha[posicao1:posicao2]
                    self.converte_data(self.vdib)
                    self.vdib = self.data_formatada
                #captura a espécie do benefício
                if 'Espécie do benefício:' in linha:
                    posicao1 = len('Espécie do benefício:') + 1
                    posicao2 = len(linha)-7
                    self.vespecie = linha[posicao1:posicao2]
                #interrupção da execução
                if 'Seção 3 de 19' in linha:
                   break
        print(self.vtipo_calculo)
        print(self.vdib)
        print(self.vespecie)


    def exp_parametros(self):
        with open("script/Dados_Import.txt", 'w', encoding="utf-8") as manipulador:
            manipulador.write(self.texto_entrada_parametros.get("1.0", tk.END))
        self.variaveis_iniciais()
        self.periodo_especial()