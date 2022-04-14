from modulos import *
from protocolo import *

class Quebra_Identidade(Data_Protocolo):
    def imprimir_texto_saida(self):
        # self.texto_saida.insert(END, f'Processo nº........: {self.nprocesso}\n')
        # self.texto_saida.insert(END, f'Nome do autor......: {self.nautor}\n')
        # self.texto_saida.insert(END, f'Nome do reu........: {self.nreu}\n')
        # self.texto_saida.insert(END, f'JEF................: {self.nvara}\n')
        # self.texto_saida.insert(END, f'Assunto............: {self.vassunto}\n')
        # self.texto_saida.insert(END, f'Valor da Causa.....: {self.vcausa}\n')
        # self.texto_saida.insert(END, f'Data da citação....: {self.dcitacao}\n')
        #self.bt_verprocesso['state'] = DISABLED
        self.bt_verprocesso['text'] = "+Protocolo"
        self.bt_verprocesso['command'] = self.data_ajuizamento
        self.texto_saida.insert(END, f'Informe a data do protocolo no campo acima...\n')


    def quebra_identidade(self):
        if self.identidade != []:
            # número do porcesso
            numero = self.identidade[0]
            posicao1 = numero.find(':')
            posicao1 = posicao1 + 2
            posicao2 = len(numero)
            self.nprocesso = numero[posicao1:posicao2]
            #print(self.nprocesso)
            #Vara do processo
            vara = self.identidade[1]
            posicao1 = vara.find(':')
            posicao1 = posicao1 + 2
            posicao2 = len(vara)
            self.nvara = vara[posicao1:posicao2]
            #print(self.nvara)
            #Valor da causa
            causa = self.identidade[2]
            posicao1 = causa.find('$')
            posicao1 = posicao1 + 2
            posicao2 = len(causa)
            self.vcausa = causa[posicao1:posicao2]
            #print(self.vcausa)
            #Assunto
            assunto = self.identidade[3]
            posicao1 = assunto.find(':')
            posicao1 = posicao1 + 2
            posicao2 = len(assunto)
            self.vassunto = assunto[posicao1:posicao2]
            #print(self.vassunto)
            # Captura o nome do Autor
            autor = self.identidade[4]
            posicao1 = 0
            posicao2 = autor.find('(')
            posicao2 = posicao2 - 1
            self.nautor = autor[posicao1:posicao2]
            #print(self.nautor)
            # Captura o nome do Réu
            reu = self.identidade[5]
            posicao1 = 0
            posicao2 = reu.find('(')
            posicao2 = posicao2 - 1
            self.nreu = reu[posicao1:posicao2]
            #print(self.nreu)
            #Captura a data da citação
            if len(self.identidade) == 7:
                citacao = self.identidade[6]
                posicao1 = citacao.find('/')
                posicao1 = posicao1 - 2
                posicao2 = posicao1 + 10
                self.dcitacao = citacao[posicao1:posicao2]
            self.texto_saida.delete("1.0", END)
            self.imprimir_texto_saida()
            self.texto_entrada.delete("1.0", END)

        else:
            self.texto_entrada.delete("1.0", END)
            self.texto_saida.delete("1.0", END)
            self.texto_saida.insert(END, f'Texto digitado não é válido!!!')