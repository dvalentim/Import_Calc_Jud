from msilib.schema import Class
from modulos import *

class Id_Google():
    def id_google(self):
        #--------------------------
        #Captura o ID da Sheets
        #--------------------------
        if self.entrada_link.get() != '':
            self.texto_saida.delete("1.0", tk.END)
            self.imprimir_texto_saida()
            link = self.entrada_link.get()
            a = link.rfind('/')
            a = a - 1

            while link[a] != '/':
                a = a - 1

            b = link.rfind('/')
            a = a + 1
            self.SAMPLE_SPREADSHEET_ID = link[a:b]
            if len(self.SAMPLE_SPREADSHEET_ID) == 44:
                self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
                """Shows basic usage of the Sheets API.
                Prints values from a sample spreadsheet.
                """
                self.creds = None  # Minhas credencias dentro da Planilha do Google
                #O arquivo token.json armazena os tokens de usuário, e é
                # criado automaticamente quando o fluxo de autorização é concluído
                # pela primeira vez.
                if os.path.exists('token.json'):  # Caso exista uma credencial valida (tolken.json) ele carrega
                    self.creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
                    self.texto_saida.delete("1.0", tk.END)
                    self.texto_saida.insert(tk.END, f'Link parece estar correto...\n')
                    self.texto_saida.insert(tk.END, f'Informe se deseja editar a Sheets ou Gerar pdf...\n')
                    self.bt_link['state'] = tk.DISABLED
                    self.bt_opcoes['state'] = tk.NORMAL
                    
                # Caso não exista uma credencial o ususário fará o login.
                if not self.creds or not self.creds.valid:  #
                    if self.creds and self.creds.expired and self.creds.refresh_token:
                        self.creds.refresh(Request())
                    else:
                        flow = InstalledAppFlow.from_client_secrets_file(
                            'client_secret.json', self.SCOPES)
                        self.creds = flow.run_local_server(port=0)
                    # Sava a credencial para a próxima execução
                    with open('token.json', 'w') as token:
                        token.write(self.creds.to_json())
                    self.texto_saida.delete("1.0", tk.END)
                    self.texto_saida.insert(tk.END, f'Link parece estar correto...\n')
                    self.texto_saida.insert(tk.END, f'Informe se deseja editar a Sheets ou Gerar pdf...\n')
                    self.bt_link['state'] = tk.DISABLED
                    self.rdbt_opcao['state'] = tk.NORMAL
                    self.bt_opcoes['state'] = tk.NORMAL

            else:
                self.texto_saida.delete("1.0", tk.END)
                self.texto_saida.insert(tk.END, f'Informe o link da Sheets corretamente...')
                self.entrada_link.delete(0, 'end')
        else:
            self.texto_saida.delete("1.0", tk.END)
            self.texto_saida.insert(tk.END, f'Informe o link da Sheets...')
            