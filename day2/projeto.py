import yfinance
import pyautogui
import pyperclip

ticker = input("Digite o código da ação: ")
dados = yfinance.Ticker(ticker)

dados.history()

tabela = dados.history("6mo")
fechamento = tabela.Close

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

destinatario = "cristianoviieira@gmail.com"
assunto = "Análise diária"
mensagem = f"""
Bom dia,
Segue abaixo as análises da ação {ticker} dos últimos seis meses:
Cotação máxima: R${round(maxima,2)}
Cotação mínima: R${round(minima,2)}
Cotação atual: R${round(atual,2)}
Atenciosamente,
Seu nome.
"""

pyautogui.PAUSE = 1
pyautogui.click(x=2234, y=897)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.click(x=1007, y=1067)
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=1682, y=1566)
pyautogui.hotkey("alt", "f4")
print("E-mail enviado com sucesso!")
