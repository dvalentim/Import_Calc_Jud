import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "TelaApp.ui"


class TelaappApp:
    def __init__(self, master=None):
        # build ui
        self.base = ttk.Notebook(master)
        self.painel_1 = ttk.Panedwindow(self.base, orient='vertical')
        self.moldura_legenda = ttk.Frame(self.painel_1)
        self.legenda_1 = ttk.Label(self.moldura_legenda)
        self.legenda_1.configure(font='{Arial} 12 {}', text='Informe os dados a importar')
        self.legenda_1.pack(pady='20', side='top')
        self.moldura_legenda.configure(height='200', width='200')
        self.moldura_legenda.pack(side='top')
        self.painel_1.add(self.moldura_legenda, weight='2')
        self.panedwindow3 = ttk.Panedwindow(self.painel_1, orient='horizontal')
        self.texto_entrada = ScrolledText(self.panedwindow3)
        self.texto_entrada.configure(font='{Arial} 12 {}')
        self.texto_entrada.pack(side='top')
        self.panedwindow3.add(self.texto_entrada, weight='12')
        self.frame2 = ttk.Frame(self.panedwindow3)
        self.lb_link = tk.Label(self.frame2)
        self.lb_link.configure(background='#dcdcdc', font='{Arial} 12 {}', text='Informe o link da planilha')
        self.lb_link.pack(pady='10', side='top')
        self.entrada_link = tk.Entry(self.frame2)
        self.entrada_link.configure(relief='flat', state='normal', width='30')
        self.entrada_link.pack(pady='10', side='top')
        self.bt_link = ttk.Button(self.frame2)
        self.bt_link.configure(state='disabled', text='OK')
        self.bt_link.pack(pady='10', side='top')
        self.bt_link.configure(command=self.id_google)
        self.rdbt_opcao = tk.Radiobutton(self.frame2)
        self.valor_check = tk.IntVar(value=1)
        self.rdbt_opcao.configure(background='#dcdcdc', font='{Arial} 12 {}', overrelief='flat', text='Altera dados da Sheets')
        self.rdbt_opcao.configure(value='1', variable=self.valor_check)
        self.rdbt_opcao.pack(pady='10', side='top')
        self.radiobutton2 = tk.Radiobutton(self.frame2)
        self.radiobutton2.configure(background='#dcdcdc', font='{Arial} 12 {}', text='Gera pdf com os dados', variable=self.valor_check)
        self.radiobutton2.pack(pady='10', side='top')
        self.bt_opcoes = ttk.Button(self.frame2)
        self.bt_opcoes.configure(state='disabled', text='OK')
        self.bt_opcoes.pack(pady='10', side='top')
        self.bt_opcoes.configure(command=self.opcoes)
        self.frame2.configure(height='200', width='200')
        self.frame2.pack(side='top')
        self.panedwindow3.add(self.frame2, weight='0')
        self.panedwindow3.configure(height='200', width='200')
        self.panedwindow3.pack(side='top')
        self.painel_1.add(self.panedwindow3, weight='12')
        self.fr_botoes = ttk.Frame(self.painel_1)
        self.bt_verprocesso = ttk.Button(self.fr_botoes)
        self.bt_verprocesso.configure(text='VerProcesso')
        self.bt_verprocesso.pack(padx='5', side='left')
        self.bt_verprocesso.configure(command=self.cria_txt)
        self.bt_apagar = ttk.Button(self.fr_botoes)
        self.bt_apagar.configure(text='Apagar')
        self.bt_apagar.pack(padx='5', side='left')
        self.bt_apagar.configure(command=self.apagar)
        self.fr_botoes.configure(height='200', width='200')
        self.fr_botoes.pack(side='top')
        self.painel_1.add(self.fr_botoes, weight='1')
        self.fr_saida = ttk.Frame(self.painel_1)
        self.texto_saida = tk.Text(self.fr_saida)
        self.texto_saida.configure(background='#404040', foreground='#ffff00', height='10', width='50')
        _text_ = '''Saidas...'''
        self.texto_saida.insert('0.0', _text_)
        self.texto_saida.pack(fill='x', side='top')
        self.fr_saida.configure(height='200', width='200')
        self.fr_saida.pack(side='top')
        self.painel_1.add(self.fr_saida, weight='1')
        self.painel_1.configure(height='200', width='200')
        self.painel_1.pack(side='top')
        self.base.add(self.painel_1, text='ImpProc')
        self.painel_2 = ttk.Panedwindow(self.base, orient='vertical')
        self.titulo_parametros = ttk.Frame(self.painel_2)
        self.legenda_parametros = ttk.Label(self.titulo_parametros)
        self.legenda_parametros.configure(font='{Arial} 12 {}', text='Informe a imagem a ser processada')
        self.legenda_parametros.pack(pady='20', side='top')
        self.titulo_parametros.configure(height='200', width='200')
        self.titulo_parametros.pack(side='top')
        self.painel_2.add(self.titulo_parametros, weight='1')
        self.panedwindow1 = ttk.Panedwindow(self.painel_2, orient='horizontal')
        self.texto_entrada_parametros = ScrolledText(self.panedwindow1)
        self.texto_entrada_parametros.pack(side='top')
        self.panedwindow1.add(self.texto_entrada_parametros, weight='1')
        self.panedwindow1.configure(height='200', width='200')
        self.panedwindow1.pack(side='top')
        self.painel_2.add(self.panedwindow1, weight='1')
        self.frame1 = ttk.Frame(self.painel_2)
        self.bt_export_parametros = ttk.Button(self.frame1)
        self.bt_export_parametros.configure(text='ExpPar�metros')
        self.bt_export_parametros.pack(padx='5', side='left')
        self.bt_apagar_parametros = ttk.Button(self.frame1)
        self.bt_apagar_parametros.configure(text='Apagar')
        self.bt_apagar_parametros.pack(padx='5', side='left')
        self.frame1.configure(height='200', width='200')
        self.frame1.pack(side='top')
        self.painel_2.add(self.frame1, weight='1')
        self.frame4 = ttk.Frame(self.painel_2)
        self.texto_saida_parametros = tk.Text(self.frame4)
        self.texto_saida_parametros.configure(background='#404040', foreground='#ffff00', height='10', width='50')
        _text_ = '''Saidas...'''
        self.texto_saida_parametros.insert('0.0', _text_)
        self.texto_saida_parametros.pack(fill='x', side='top')
        self.frame4.configure(height='200', width='200')
        self.frame4.pack(side='top')
        self.painel_2.add(self.frame4, weight='1')
        self.painel_2.configure(height='200', width='200')
        self.painel_2.pack(side='top')
        self.base.add(self.painel_2, text='Par�metros')
        self.base.configure(height='600', width='600')
        self.base.pack(side='top')

        # Main widget
        self.mainwindow = self.base
    
    def run(self):
        self.mainwindow.mainloop()

    def id_google(self):
        pass

    def opcoes(self):
        pass

    def cria_txt(self):
        pass

    def apagar(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = TelaappApp(root)
    app.run()

