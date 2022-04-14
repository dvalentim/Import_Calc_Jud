from modulos import *

class Deletar():
    def apagar(self):
        self.texto_entrada.delete("1.0", END)
        self.texto_saida.delete("1.0", END)
        self.entrada_link.delete(0, 'end')
        self.texto_saida.insert(END, f'Saídas...')
        self.bt_link['state'] = DISABLED
        self.bt_opcoes['state'] = DISABLED
        self.bt_verprocesso['state'] = NORMAL
        self.bt_verprocesso['text'] = "VerProcesso"
        self.bt_verprocesso['command'] = self.cria_txt