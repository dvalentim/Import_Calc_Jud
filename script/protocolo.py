from modulos import *
from adiciona_cnis import *

class Data_Protocolo(Dados_CNIS):
    def data_ajuizamento(self):
        with open("script/Dados_Import.txt", 'w', encoding="utf-8") as manipulador:
            manipulador.write(self.texto_entrada.get("1.0", tk.END))
        self.busca_dprotocolo()

    def formatar_data(self, data):
        ultimo_espaço = data.rfind(" ")
        tamanho_data = len(data)
        ano = data[ultimo_espaço+1:tamanho_data-1]
        primeiro_espaço = data.find(" ")
        mes = data[primeiro_espaço+1:tamanho_data-6]
        dia = data[0:2]
        if mes == 'jan':
            mes = '01'
        elif mes == 'fev':
            mes = '02'
        elif mes == 'mar':
            mes = '03'
        elif mes == 'abr':
            mes = '04'
        elif mes == 'mai':
            mes = '05'
        elif mes == 'jun':
            mes = '06'
        elif mes == 'jul':
            mes = '07'
        elif mes == 'ago':
            mes = '08'
        elif mes == 'set':
            mes = '09'
        elif mes == 'out':
            mes = '10'
        elif mes == 'nov':
            mes = '11'
        else:
            mes = '12'
        formato = dia
        formato = formato + mes
        formato = formato + ano
        self.dajuizamanto = dia + '/' + mes + '/' + ano
        

    def busca_dprotocolo(self):
        identidade_protocolo = []
        contador = 0
        with open("script/Dados_Import.txt", 'r', encoding="utf-8") as manipulador:
            for linha in manipulador:
                contador = contador + 1
                if 'Autuação' in linha:
                    identidade_protocolo.append(linha)
                    break
        if identidade_protocolo != []:
            with open("script/Dados_Import.txt", 'r', encoding="utf-8") as manipulador:
                frase = manipulador.readlines()[contador]
            self.formatar_data(frase)
            self.texto_saida.delete("1.0", tk.END)
            self.texto_entrada.delete("1.0", tk.END)
            self.texto_saida.insert(tk.END, f'Informe os dados do CNIS\n')
            self.bt_verprocesso['text'] = "+CNIS"
            self.bt_verprocesso['command'] = self.ad_cnis
            

        else:
            self.texto_saida.delete("1.0", tk.END)
            self.texto_saida.insert(tk.END, f'Informe os dados do PJe\n')
        