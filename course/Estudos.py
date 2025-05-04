from fpdf import FPDF
from fpdf.enums import XPos, YPos

# Criação do objeto PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Adicionar título
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(200, 10, text="Plano de Estudo para Conquista de Emprego", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
pdf.ln(10)

# Adicionar introdução
pdf.set_font('Helvetica', '', 12)
pdf.multi_cell(0, 10, text="Este plano de estudo foi criado para ajudar a maximizar seu tempo e conquistar um emprego como desenvolvedor de forma eficiente. A rotina foca no aprendizado prático de Python, desenvolvimento e portfólio. Você poderá ajustar a intensidade do seu aprendizado conforme o tempo disponível.")
pdf.ln(10)

# Adicionar rotina
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(200, 10, text="Segunda-feira e Terça-feira (Dias Presenciais - 7h às 20h)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font('Helvetica', '', 12)
pdf.multi_cell(0, 10, text=""" 
- 6h30: Acorda e se prepara para o trabalho
- 7h00 - 7h30: Deslocamento para o trabalho (ouvir podcasts sobre programação)
- 9h00 - 18h00: Trabalho presencial
- 20h00 - 20h30: Chegada em casa e jantar
- 20h30 - 21h30: Estudo (1h de Python)
- 21h30 - 22h30: Lazer (jogo com amigos)
- 22h30 - 23h00: Preparação para dormir
""")
pdf.ln(10)

# Adicionar quarta e sexta
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(200, 10, text="Quarta-feira e Sexta-feira (Autoescola + Home Office)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font('Helvetica', '', 12)
pdf.multi_cell(0, 10, text=""" 
- 7h00: Acorda e se prepara para a autoescola
- 7h30 - 9h00: Autoescola
- 9h40 - 18h00: Home office
- 20h00 - 21h30: Estudo (1h30 de Python)
- 21h30 - 22h30: Lazer (jogo com amigos)
- 22h30 - 23h00: Preparação para dormir
""")
pdf.ln(10)

# Quinta-feira
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(200, 10, text="Quinta-feira (Dia com Mais Flexibilidade)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font('Helvetica', '', 12)
pdf.multi_cell(0, 10, text=""" 
- 7h00: Acorda e se prepara para o trabalho
- 9h00 - 18h00: Trabalho
- 19h00 - 20h30: Estudo (1h30 de Python)
- 20h30 - 22h00: Lazer (jogo ou descanso)
- 22h00 - 23h00: Preparação para dormir
""")
pdf.ln(10)

# Sábado
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(200, 10, text="Sábado (Dia de Revisão e Projetos)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font('Helvetica', '', 12)
pdf.multi_cell(0, 10, text=""" 
- 8h00: Acorda e se prepara para o dia
- 9h00 - 12h00: Estudo (3h de Python)
- 12h00 - 14h00: Almoço e descanso
- 14h00 - 17h00: Projetos pessoais ou portfólio
- 17h00 - 19h00: Lazer
- 19h00 - 20h00: Revisão ou preparação para entrevistas
""")
pdf.ln(10)

# Domingo
pdf.set_font('Helvetica', 'B', 14)
pdf.cell(200, 10, text="Domingo (Dia de Descanso ou Revisão Leve)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font('Helvetica', '', 12)
pdf.multi_cell(0, 10, text=""" 
- 9h00: Acorda e se prepara para o dia
- 10h00 - 11h00: Estudo leve ou revisão
- 11h00 - 14h00: Descanso
- 14h00 - 17h00: Projetos práticos ou aperfeiçoamento no portfólio
- 17h00 - 20h00: Lazer
- 20h00 - 21h00: Preparação para a semana
""")

# Salvar PDF
pdf.output("Plano_Estudo_Desenvolvedor.pdf")
