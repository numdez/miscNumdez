import math
import locale
import decimal
import requests
import tkinter as tk


from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

url = 'https://api.exchangerate-api.com/v4/latest/USD'



class RealTimeCurrencyConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD' : 
            amount = round(float(amount) / self.currencies[from_currency], 4) 
  
        # limiting the precision to 4 decimal places 
        amount = round(float(amount) * self.currencies[to_currency], 4) 
        return amount

def round_up(x, place=2):
    context = decimal.getcontext()
    original_rounding = context.rounding
    context.rounding = decimal.ROUND_CEILING

    rounded = round(decimal.Decimal(str(x)), place)
    context.rounding = original_rounding
    return float(rounded)

converter = RealTimeCurrencyConverter(url)

cur_from = 'USD'
cur_dest = 'BRL'
amount = 70
convertido = converter.convert(cur_from.upper(), cur_dest.upper(), amount)

salarioBruto = 811.4

tempoSalario = 12
salariosRecebidos = 1
tempoRestante = tempoSalario-salariosRecebidos

taxaBanco = 50

gastosMensais = 0

salarioReal = salarioBruto - taxaBanco - gastosMensais

precoAlvo = 1245.83
precoAlvo2 = 2450.00
precoAlvo3 = 1245.83
precoAlvo4 = 1245.83

importacao = True

#54 caracteres na maior linha

imposto1 = 0
imposto2 = 0
imposto3 = 0
imposto4 = 0

taxaImportacao = 0
taxaImportacao2 = 0
taxaImportacao3 = 0.702
taxaImportacao4 = 0


if importacao == True:
    imposto1 = float(convertido)
    imposto2 = precoAlvo2 * taxaImportacao2
    imposto3 = precoAlvo3 * taxaImportacao3
    imposto4 = precoAlvo * taxaImportacao4

precoReal = precoAlvo + imposto1
precoReal2 = precoAlvo2 + imposto2
precoReal3 = precoAlvo3 + imposto3
precoReal4 = precoAlvo4 + imposto4

guardar1 = precoReal / math.ceil(precoReal/salarioReal)
guardar2 = precoReal2 / math.ceil(precoReal2/salarioReal)
guardar3 = precoReal3 / math.ceil(precoReal3/salarioReal)
guardar4 = precoReal4 / math.ceil(precoReal4/salarioReal)

totalSalario = salarioReal * tempoSalario

percentualGasto1 = precoReal / totalSalario
percentualGasto2 = precoReal2 / totalSalario 
percentualGasto3 = precoReal3 / totalSalario
percentualGasto4 = precoReal4 / totalSalario

app = tk.Tk()
app.title("Comparação preços VR")

label128 = ttk.Label(app, text='Pico 4').grid(row=0, column=1)

label256 = ttk.Label(app, text='Quest 2').grid(row=0, column=4)

label512 = ttk.Label(app, text='Pico 4 Honesto').grid(row=0, column=7)

label1024 = ttk.Label(app, text='Pico 4 Sortudo').grid(row=0, column=10)

vr128 = ScrolledText(app, width=54, height=28)
vr128.insert(tk.INSERT, f'''Salário mensal bruto: {salarioBruto}   
Salário total bruto: {salarioBruto * tempoSalario}  
Taxa do banco: {taxaBanco}   
Taxa do banco total: {taxaBanco * tempoSalario} 
Salário mensal líquido: {salarioReal}  
Salário total líquido: {salarioReal * tempoSalario}  

Salário total bruto restante: {tempoRestante * salarioBruto}  
Taxa do banco total restante: {tempoRestante * taxaBanco}  
Salário total líquido restante: {tempoRestante * salarioReal}  

Preço no site: {precoAlvo}  
Meses para comprar: {math.ceil(precoAlvo/salarioReal)} 
Imposto: {round_up(imposto1)} 

Meses para pagar imposto (se for taxado): {math.ceil(imposto1/salarioReal)} 
Preço com imposto: {round_up(precoReal)}
Meses para pagar tudo: {math.ceil(precoReal/salarioReal)}
Quanto economizar por mês: {round_up(guardar1)}

Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardar1)}
Quanto pode gastar por mês líquido: {round_up(salarioReal - guardar1)}

Dinheiro gasto na compra: {round_up(precoReal)}
Percentual do salário gasto: {round_up(percentualGasto1*100)}%
Dinheiro total após a compra: {round_up(tempoRestante * salarioReal - precoReal)} 
Percentual do salário restante: {round_up(100-percentualGasto1*100)}%
Em dólares: {locale.currency(round_up(converter.convert('BRL', 'USD', precoReal)))}
''')
vr128.grid(row=3, column=1)

separator = ttk.Separator(app, orient="vertical")
separator.grid(row=2, column=4)

vr256 = ScrolledText(app, width=54, height=28)
vr256.insert(tk.INSERT, f'''Salário mensal bruto: {salarioBruto}   
Salário total bruto: {salarioBruto * tempoSalario}  
Taxa do banco: {taxaBanco}   
Taxa do banco total: {taxaBanco * tempoSalario} 
Salário mensal líquido: {salarioReal}  
Salário total líquido: {salarioReal * tempoSalario}  

Salário total bruto restante: {tempoRestante * salarioBruto}  
Taxa do banco total restante: {tempoRestante * taxaBanco}  
Salário total líquido restante: {tempoRestante * salarioReal}  

Preço no site: {precoAlvo2}  
Meses para comprar: {math.ceil(precoAlvo2/salarioReal)} 
Imposto: {round_up(imposto2)} 

Meses para pagar imposto (se for taxado): {math.ceil(imposto2/salarioReal)} 
Preço com imposto: {round_up(precoReal2)}
Meses para pagar tudo: {math.ceil(precoReal2/salarioReal)}
Quanto economizar por mês: {round_up(guardar2)}

Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardar2)}
Quanto pode gastar por mês líquido: {round_up(salarioReal - guardar2)}

Dinheiro gasto na compra: {round_up(precoReal2)}
Percentual do salário gasto: {round_up(percentualGasto2*100)}%
Dinheiro total após a compra: {round_up(tempoRestante * salarioReal - precoReal2)}
Percentual do salário restante: {round_up(100-percentualGasto2*100)}%
Em dólares: {locale.currency(round_up(converter.convert('BRL', 'USD', precoReal2)))}
''')
vr256.grid(row=3, column=4)

separator = ttk.Separator(app, orient="vertical")
separator.grid(row=2, column=7)

vr512 = ScrolledText(app, width=54, height=28)
vr512.insert(tk.INSERT, f'''Salário mensal bruto: {salarioBruto}   
Salário total bruto: {salarioBruto * tempoSalario}  
Taxa do banco: {taxaBanco}   
Taxa do banco total: {taxaBanco * tempoSalario} 
Salário mensal líquido: {salarioReal}  
Salário total líquido: {salarioReal * tempoSalario}  

Salário total bruto restante: {tempoRestante * salarioBruto}  
Taxa do banco total restante: {tempoRestante * taxaBanco}  
Salário total líquido restante: {tempoRestante * salarioReal}  

Preço no site: {precoAlvo3}  
Meses para comprar: {math.ceil(precoAlvo3/salarioReal)} 
Imposto: {round_up(imposto3)} 

Meses para pagar imposto (se for taxado): {math.ceil(imposto3/salarioReal)} 
Preço com imposto: {round_up(precoReal3)}
Meses para pagar tudo: {math.ceil(precoReal3/salarioReal)}
Quanto economizar por mês: {round_up(guardar3)}

Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardar3)}
Quanto pode gastar por mês líquido: {round_up(salarioReal - guardar3)}

Dinheiro gasto na compra: {round_up(precoReal3)}
Percentual do salário gasto: {round_up(percentualGasto3*100)}%
Dinheiro total após a compra: {round_up(tempoRestante * salarioReal - precoReal3)}
Percentual do salário restante: {round_up(100-percentualGasto3*100)}%
Em dólares: {locale.currency(round_up(converter.convert('BRL', 'USD', precoReal3)))}
''')
vr512.grid(row=3, column=7)

separator.grid(row=2, column=7)

vr1024 = ScrolledText(app, width=54, height=28)
vr1024.insert(tk.INSERT, f'''Salário mensal bruto: {salarioBruto}   
Salário total bruto: {salarioBruto * tempoSalario}  
Taxa do banco: {taxaBanco}   
Taxa do banco total: {taxaBanco * tempoSalario} 
Salário mensal líquido: {salarioReal}  
Salário total líquido: {salarioReal * tempoSalario}  

Salário total bruto restante: {tempoRestante * salarioBruto}  
Taxa do banco total restante: {tempoRestante * taxaBanco}  
Salário total líquido restante: {tempoRestante * salarioReal}  

Preço no site: {precoAlvo4}  
Meses para comprar: {math.ceil(precoAlvo4/salarioReal)} 
Imposto: {round_up(imposto4)} 

Meses para pagar imposto (se for taxado): {math.ceil(imposto4/salarioReal)} 
Preço com imposto: {round_up(precoReal4)}
Meses para pagar tudo: {math.ceil(precoReal4/salarioReal)}
Quanto economizar por mês: {round_up(guardar4)}

Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardar4)}
Quanto pode gastar por mês líquido: {round_up(salarioReal - guardar4)}

Dinheiro gasto na compra: {round_up(precoReal4)}
Percentual do salário gasto: {round_up(percentualGasto4*100)}%
Dinheiro total após a compra: {round_up(tempoRestante * salarioReal - precoReal4)}
Percentual do salário restante: {round_up(100-percentualGasto4*100)}%
Em dólares: {locale.currency(round_up(converter.convert('BRL', 'USD', precoReal4)))}
''')
vr1024.grid(row=3, column=10)

app.eval('tk::PlaceWindow . center')

app.mainloop()
