from modulos import *

class Deletar():
    def apagar(self):
        self.texto_entrada.delete("1.0", tk.END)
        self.texto_saida.delete("1.0", tk.END)
        self.entrada_link.delete(0, 'end')
        self.texto_saida.insert(tk.END, f'Saídas...')
        self.bt_link['state'] = tk.DISABLED
        self.bt_opcoes['state'] = tk.DISABLED
        self.bt_verprocesso['state'] = tk.NORMAL
        self.bt_verprocesso['text'] = "VerProcesso"
        self.bt_verprocesso['command'] = self.cria_txt