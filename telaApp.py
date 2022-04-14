from modulos import *
from cria_arquivo_txt import *
from ident_google import *
from decisao import *
from deletar import *

class TelaApp(Cria_Arquivo_Txt, Id_Google, Decisao, Deletar):
    def __init__(self, master=None):
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
        self.lb_link = Label(self.frame2)
        self.lb_link.configure(background='#dcdcdc', font='{Arial} 12 {}', text='Informe o link da planilha')
        self.lb_link.pack(pady='10', side='top')
        self.entrada_link = Entry(self.frame2)
        self.entrada_link.configure(relief='flat', state='normal', width='30')
        self.entrada_link.pack(pady='10', side='top')
        self.bt_link = ttk.Button(self.frame2, command = self.id_google, state = DISABLED)
        self.bt_link.configure(text='OK')
        self.bt_link.pack(pady='10', side='top')
        self.rdbt_opcao = Radiobutton(self.frame2)
        self.valor_check = IntVar(value=1)
        self.rdbt_opcao.configure(background='#dcdcdc', font='{Arial} 12 {}', justify='left',
                                  text='Altera dados da Sheets')
        self.rdbt_opcao.configure(value='1', variable=self.valor_check)
        self.rdbt_opcao.pack(pady='10', side='top')
        self.radiobutton2 = Radiobutton(self.frame2)
        self.radiobutton2.configure(background='#dcdcdc', font='{Arial} 12 {}', text='Gera pdf com os dados', value='2')
        self.radiobutton2.configure(variable=self.valor_check)
        self.radiobutton2.pack(pady='10', side='top')
        self.bt_opcoes = ttk.Button(self.frame2, command = self.opcoes, state = DISABLED)
        self.bt_opcoes.configure(text='OK')
        self.bt_opcoes.pack(pady='10', side='top')
        self.frame2.configure(height='200', width='200')
        self.frame2.pack(side='top')
        self.panedwindow3.add(self.frame2, weight='0')
        self.panedwindow3.configure(height='200', width='200')
        self.panedwindow3.pack(side='top')
        self.painel_1.add(self.panedwindow3, weight='12')
        self.fr_botoes = ttk.Frame(self.painel_1)
        self.bt_verprocesso = ttk.Button(self.fr_botoes, command= self.cria_txt)
        self.bt_verprocesso.configure(text='VerProcesso')
        self.bt_verprocesso.pack(padx='5', side='left')
        self.bt_apagar = ttk.Button(self.fr_botoes, command= self.apagar)
        self.bt_apagar.configure(text='Apagar')
        self.bt_apagar.pack(padx='5', side='left')
        self.fr_botoes.configure(height='200', width='200')
        self.fr_botoes.pack(side='top')
        self.painel_1.add(self.fr_botoes, weight='1')
        self.fr_saida = ttk.Frame(self.painel_1)
        self.texto_saida = Text(self.fr_saida)
        self.texto_saida.configure(background='#404040', foreground='#ffff00', height='10', width='50')
        _text_ = '''Saidas...'''
        self.texto_saida.insert('0.0', _text_)
        self.texto_saida.pack(fill='x', side='top')
        self.fr_saida.configure(height='200', width='200')
        self.fr_saida.pack(side='top')
        self.painel_1.add(self.fr_saida, weight='1')
        self.painel_1.configure(height='200', width='200')
        self.painel_1.pack(side='top')
        self.base.add(self.painel_1, text='ImpTxt')
        self.painel_2 = ttk.Panedwindow(self.base, orient='vertical')
        self.frame3 = ttk.Frame(self.painel_2)
        self.label4 = ttk.Label(self.frame3)
        self.label4.configure(font='{Arial} 12 {}', text='Informe a imagem a ser processada')
        self.label4.pack(pady='20', side='top')
        self.frame3.configure(height='200', width='200')
        self.frame3.pack(side='top')
        self.painel_2.add(self.frame3, weight='1')
        self.painel_2.configure(height='200', width='200')
        self.painel_2.pack(side='top')
        self.base.add(self.painel_2, text='ImpImagem')
        self.base.configure(height='600', width='600')
        self.base.pack(side='top')
        