jornada_media = float(input('Insira a jornada media de funcionarios:')) #média das horas trabalhadas por todos os funcionarios em um mês
                  #aqui da para se pensar algumas coisas como: atrelhar o código à uma planilha de excel. Além disso, vincular ao código uma maneira de
                  #saber qual mês estamos e de qual ano, fazendo assim o cálculo automático.
total_trab = float(input('Insira o total de trabalhadores')) #total de trabalhadores
dias_uteis = float(input('Insira o total de dias uteis:'))# aqui da pra pensar em como fazer para tirar sábados e domingos, ou algum tipo de configuração como uma contagem
                                                          # de dias uteis
print('A horas de exposição a riscos dos funcionarios é', jornada_media * total_trab * dias_uteis,'horas-homem')