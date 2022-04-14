from modulos import *

class Dados_CNIS():
    def ad_cnis(self):
        self.bt_link['state'] = NORMAL
        self.bt_opcoes['state'] = NORMAL
        with open("Dados_Import.txt", 'w', encoding="utf-8") as manipulador:
            manipulador.write(self.texto_entrada.get("1.0", END))
        self.analisa_cnis()
    
 #Função analisa os dados do CNIS
    def analisa_cnis(self):
        #self.bt_addcnis['state'] = DISABLED
        self.identidade_cnis = []
        contador = 0
        self.dnascimento = 'informar'
        with open("Dados_Import.txt", 'r', encoding="utf-8") as manipulador:
            for linha in manipulador:
                contador = contador + 1
                if 'Data de nascimento:' in linha:
                    posicao1 = linha.rfind('/') - 5
                    posicao2 = linha.rfind('/') + 5
                    self.dnascimento = linha[posicao1:posicao2]
                    break
                if contador == 6:
                    self.identidade_cnis.append(linha.rstrip())
                    break
        if self.identidade_cnis != []:
            self.dnascimento = self.identidade_cnis[0]
            self.texto_saida.delete("1.0", END)
            self.texto_entrada.delete("1.0", END)
            #self.imprimir_texto_saida()
            self.texto_saida.delete("1.0", END)
            self.texto_entrada.delete("1.0", END)
            self.texto_saida.insert(END, f'Processo nº........: {self.nprocesso}\n')
            self.texto_saida.insert(END, f'Nome do autor......: {self.nautor}\n')
            self.texto_saida.insert(END, f'Nome do reu........: {self.nreu}\n')
            self.texto_saida.insert(END, f'JEF................: {self.nvara}\n')
            self.texto_saida.insert(END, f'Assunto............: {self.vassunto}\n')
            self.texto_saida.insert(END, f'Valor da Causa.....: {self.vcausa}\n')
            self.texto_saida.insert(END, f'Data do protocolo..: {self.dajuizamanto}\n')
            self.texto_saida.insert(END, f'Data da citação....: {self.dcitacao}\n')
            self.texto_saida.insert(END, f'Data de nascimento.: {self.dnascimento}\n')
            self.bt_verprocesso['state'] = DISABLED
            self.bt_opcoes['state'] = DISABLED
            #self.bt_addcnis['state'] = DISABLED
        else:
            self.texto_saida.delete("1.0", END)
            self.texto_saida.insert(END, f'Informe os dados do CNIS\n')   