nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def dados_loja():	
	if not nome_loja:
		raise Exception("O campo nome da loja é obrigatório")
	
	if not logradouro:
		raise Exception("O campo logradouro do endereço é obrigatório")
		
	if not municipio:
		raise Exception("O campo município do endereço é obrigatório")

	if not estado:
		raise Exception("O campo estado do endereço é obrigatório")

	if not cnpj:
		raise Exception("O campo CNPJ da loja é obrigatório")	

	if not inscricao_estadual:
		raise Exception("O campo inscrição estadual da loja é obrigatório")

	_numero = "s/n" if not numero else str(numero)
	
	_complemento = " " + complemento if complemento else ""	

	_bairro = bairro + " - " if bairro else ""

	_cep = "CEP:" + cep if cep else ""
	
	_telefone = "Tel " + telefone if telefone else ""
	
	_telefone = " " + _telefone if cep and telefone else _telefone

	_observacao = observacao if observacao else ""

	nota = nome_loja + "\n"
	nota += "%s, %s%s\n" %(logradouro,_numero,_complemento)
	nota += "%s%s - %s\n" % (_bairro,municipio,estado)
	nota += "%s%s\n" % (_cep,_telefone)
	nota += "%s\n" % (_observacao)
	nota += "CNPJ: %s\n" %(cnpj)
	nota += "IE: %s" % (inscricao_estadual)

	return nota