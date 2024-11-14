#Questão 4
tempo_seg = int(input(' Tempo necessário para a realização da avaliação (em segundos): '))

tempo_de_aula = 50  # minutos

tempo_min = int(tempo_seg / 60)   # segundos para minutos

quant_aulas = (tempo_min / tempo_de_aula)

print(' Quantidade de aulas necessárias:  {:.1f}'.format(quant_aulas))




