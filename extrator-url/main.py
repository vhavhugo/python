# fatiando strings
# texto = "abcde"

# texto = texto[0:2]
url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100&moedaDestino=dolar"
# print(url)

# url_base = url[8:19]
# print(url_base)

# url_parametro = url[28:36]
# print(url_parametro)

# indice_interrogacao = url.find('?')
# url_base = url[0:indice_interrogacao]
# print(url_base)

# url_parametros = url[indice_interrogacao+1:]
# print(url_parametros)

# Separa base e os parâmetros
# url = "https://bytebank.com/cambio?moedaOrigem=real"
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parãmetro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

