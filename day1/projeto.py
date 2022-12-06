from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo_estimado = input("Digite o prazo estimado: ")

valor_total_estimado = int(horas_estimadas) * int(valor_hora)

pdf = FPDF()

pdf.add_page()
pdf.set_font("Helvetica")

pdf.image("template.png", x=0, y=0)

pdf.text(115, 147, projeto)
pdf.text(115, 161, horas_estimadas)
pdf.text(115, 176, valor_hora)
pdf.text(115, 191, prazo_estimado)
pdf.text(115, 206, str(valor_total_estimado))
pdf.output("pdf_projeto.pdf")

print("Orgamento gerado com sucesso!")
