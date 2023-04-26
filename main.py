#*******************Gerador QRCODE REMESSAS *******************
#        Desenvolvido por Frederico de Jesus Almeida
#              Analista de Suporte PLENO - Multi
#*******************   26/03/2023  ****************************

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkinter import Canvas
import tkinter.simpledialog as sd


def dia():
    # Pegando o dia
    data_var = datetime.now().strftime("%d/%m/%Y")
    return data_var

def hora():
    # Pegando a Hora
    now = datetime.now()
    hora_atual = now.strftime("%H:%M:%S")
    return hora_atual

def layout_etiqueta(conteudo_qrcode):

    hora_atual = hora()
    data_var = dia()
    remessa = conteudo_qrcode


    codigo_zpl = '^XA~TA000~JSN^LT0^MNW^MTT^PON^PMN^LH0,0^JMA^PR4,4~SD20^JUS^LRN^CI0^XZ \n' \
                     '^XA\n' \
                     '^MMT\n' \
                     '^PW799\n' \
                     '^LL0400\n' \
                     '^LS0\n' \
                     '^FT62,53^A0N,28,38^FH\^FDEWM - SAP/APOLLO  - ^FS\n' \
                     '^FT644,53^A0N,28,28^FH\\^FD' + hora_atual + '^FS\n' \
                     '^FT473,53^A0N,28,28^FH\\^FD' + data_var +'^FS\n' \
                     '^FT25,297^A0N,28,28^FH\^FDENDERE\80O :^FS\n' \
                     '^FT25,337^A0N,28,28^FH\^FDQTD CAIXA : ^FS\n' \
                     '^FT25,381^A0N,28,28^FH\^FDUSU\B5RIO : ^FS ^FT326,234^BQN,2,7\n' \
                     '^FH\^FDLA,' + conteudo_qrcode + ' ^FS\n' \
                     '^FO177,298^GB590,0,1^FS\n' \
                     '^FO177,333^GB590,0,1^FS\n' \
                     '^FO177,373^GB590,0,1^FS\n' \
                     '^FT287,247^A0N,28,28^FH\^FDREMESSA N\F8' + remessa + '^FS\n' \
                     '^PQ1,0,1,Y^XZ'
    return codigo_zpl

def impressora(conteudo):
    codigo_zpl = layout_etiqueta(conteudo)
    # Configuração da porta da impressora
    port = "LPT1"  # Altere para a porta correta da sua impressora

    # Abre o arquivo de porta da impressora e envia o comando ZPL
    with open(port, "wb") as printer:
        printer.write(codigo_zpl.encode("utf-8"))

def clear_entry(event):
    entry.delete(0, tk.END)

def get_data(event):
    conteudo_qrcode = entry.get()
    if (conteudo_qrcode.isdigit() and (len(conteudo_qrcode) >= 8 )):
        impressora(conteudo_qrcode)
        hora()
        dia()
        print( conteudo_qrcode)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Por favor, insira uma remessa Válida!")
        entry.delete(0, tk.END)


root = tk.Tk()
root.geometry("330x120")
root.title("Gerador de Etiquetas Remessa")

# Cria o label "Insira a remessa"
label = tk.Label(root, text="Insira a remessa:")
label.grid(row=0, column=0, padx=(10, 5), pady=10)

# Cria a caixa de entrada
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=(5, 10), pady=10)

entry.bind("<Return>", get_data)
entry.bind("<KP_Enter>", get_data)
entry.bind("<Button-1>", clear_entry)

# Crie um botão "Sair"
quit_button = tk.Button(root, text="Sair", command=root.quit)

# Adicione o botão na janela
quit_button.grid(row=1, column=1, pady=(0, 10), sticky="E")

# Crie um canvas e adicione-o à sua janela
canvas = Canvas(root, width=300, height=20)
canvas.grid(row=2, column=0, columnspan=2)
canvas.create_text(150, 10, text="© 2023 Frederico Almeida. Todos os direitos reservados.", justify="center")

root.mainloop()
