tamanho_arquivo_mb = float(input("Informe o tamanho do arquivo em MB: "))
velocidade_internet_mbps = float(input("Informe a velocidade da Internet em Mbps: "))

tempo_download_minutos = (tamanho_arquivo_mb * 8) / velocidade_internet_mbps


print("O tempo aproximado de download do arquivo é de", tempo_download_minutos, "minutos")
