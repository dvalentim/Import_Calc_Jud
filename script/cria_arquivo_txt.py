from http.client import ImproperConnectionState
from modulos import *
from importar_processo import *

class Cria_Arquivo_Txt(Importar_Processo):
    """Cria um *.txt com os dados do Widget Text no diretório do programa."""
    def cria_txt(self):
        self.caminho = os.path.dirname(__file__)
        self.nomeArquivo = self.caminho + "//Dados_Import.txt"
        self.Arquivo = open(self.nomeArquivo, "w", encoding="utf-8")
        self.Arquivo.write(self.texto_entrada.get("1.0", tk.END))
        self.Arquivo.close()
        #função executada no arquivo importar_processo.py
        self.importar() 