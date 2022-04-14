from modulos import *
from gera_pdf import *
from editar_google_sheets import Edita_Sheets

class Decisao(GerarPdf, Edita_Sheets):
    def opcoes(self):
        a = self.valor_check.get()
        if self.valor_check.get() == 1:
            self.modifica_sheets()
        if self.valor_check.get() == 2:
            self.gerapdf()