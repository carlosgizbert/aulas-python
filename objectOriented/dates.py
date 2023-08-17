from datetime import datetime, timezone, timedelta

data_atual = datetime.now()
diferenca_fuso = timedelta(hours=-3)
fuso_horario = timezone(diferenca_fuso)
data_e_hora_sao_paulo = data_atual.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

print(data_e_hora_sao_paulo_em_texto)
