from modulos import *

class Edita_Sheets:
    def modifica_sheets(self):
        service = build('sheets', 'v4', credentials=self.creds)

        # Call the Sheets API
        sheet = service.spreadsheets()  # representa todas as abas da Sheets

        # ler informações da Googel Sheets
        result = sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                    range='Processo!D5:D9').execute()
        valores = result.get('values', [])

############################################################################################################
#Captura o tipo de planilha do Google Sheets (RMI, TC ou ATRASADOS)                                        #
############################################################################################################

        metadados_planilha = service.spreadsheets().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID).execute()
        planilha = metadados_planilha.get('properties', '')# captura o dados de proprities
        self.nome_sheets = planilha.get('title', '')# Captura o título da planilha

        posicao1 = self.nome_sheets.find('(')
        posicao2 = len(self.nome_sheets)
        titulo = self.nome_sheets[posicao1:posicao2]

        # adicionar/editar valores na Google Sheets
        if titulo == '(TC)':
            #Edita a página Processo
            valores_ad_processo = [[self.nprocesso],
                                [self.nautor],
                                [self.nreu],
                                [self.dajuizamanto],
                                [self.dcitacao],
                                [],
                                [],
                                [],
                                [self.dnascimento]]
            result = sheet.values().update(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range='Processo!D5', valueInputOption="USER_ENTERED",
                                        body={"values": valores_ad_processo}).execute()

            #Subseção
            posicao1 = self.nvara.rfind('de')
            posicao2 = len(self.nvara)
            jef = self.nvara[posicao1+3:posicao2]
            
            valores_ad_processo = [['Juizado Especial Federal'],
                                ['São Paulo'],
                                [jef],
                                ['Tempo de Contribuição']]
            result = sheet.values().update(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range='Configuracoes!D10', valueInputOption="USER_ENTERED",
                                        body={"values": valores_ad_processo}).execute()

        self.texto_saida.delete("1.0", END)
        self.texto_saida.insert(END, f'Planilha do Google {self.nome_sheets} modificada\n')
        self.texto_saida.insert(END, f'Informado:\n')
        self.texto_saida.insert(END, f'nº do processo......: {self.nprocesso}\n')
        self.texto_saida.insert(END, f'nome do autor.......: {self.nautor}\n')
        self.texto_saida.insert(END, f'nome do reu.........: {self.nreu}\n')
        self.texto_saida.insert(END, f'data do protocolo...: {self.dajuizamanto}\n')
        self.texto_saida.insert(END, f'data da citação.....: {self.dcitacao}\n')
        self.texto_saida.insert(END, f'Data de nascimento..: {self.dnascimento}\n')
