def converte_real_para_euro(valor_em_real):
    valor_em_euro = valor_em_real * 6.4
    return valor_em_euro

valor_inicial_em_real = 50.0
valor_convertido_em_euro = converte_real_para_euro(valor_inicial_em_real)

valor_arredondado_em_euro = round(valor_convertido_em_euro, 2)
valor_em_euro_texto = valor_arredondado_em_euro.replace(‘.’, ‘,’)
print(valor_em_euro_texto)