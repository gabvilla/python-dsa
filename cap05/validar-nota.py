disciplina = 'Data Science'
nota_final = 90
semestre = 2

# %s = string placeholder / %r = number placeholder. Put the placeholder values/variables after the placeholder assign
if disciplina == 'Data Science' and nota_final >= 80 and semestre != 1:
   print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
   print('Lamento, acho que você precisa estudar mais')

