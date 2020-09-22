import cupom
import pytest

# Refatoramento da verificação de campo obrigatório
def verifica_campo_obrigatorio(mensagem_esperada):
  with pytest.raises(Exception) as excinfo:
    cupom.dados_loja()
  the_exception = excinfo.value
  assert mensagem_esperada == str(the_exception)

# Todas as variáveis preenchidas
cupom.nome_loja = "Loja 1"
cupom.logradouro = "Log 1"
cupom.numero = 10
cupom.complemento = "C1"
cupom.bairro = "Bai 1"
cupom.municipio = "Mun 1"
cupom.estado = "E1"
cupom.cep = "11111-111"
cupom.telefone = "(11) 1111-1111"
cupom.observacao = "Obs 1"
cupom.cnpj = "11.111.111/1111-11"
cupom.inscricao_estadual = "123456789"

TEXTO_ESPERADO_LOJA_COMPLETA = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_loja_completa():
    assert cupom.dados_loja() == TEXTO_ESPERADO_LOJA_COMPLETA

def test_nome_vazio():
    cupom.nome_loja = ""
    verifica_campo_obrigatorio("O campo nome da loja é obrigatório") 
    cupom.nome_loja = "Loja 1"

def test_logradouro_vazio():
    cupom.logradouro = ""
    verifica_campo_obrigatorio("O campo logradouro do endereço é obrigatório")
    cupom.logradouro = "Log 1"

TEXTO_ESPERADO_SEM_NUMERO = '''Loja 1
Log 1, s/n C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_numero_zero():
    cupom.numero = 0
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_NUMERO
    cupom.numero = 10

TEXTO_ESPERADO_SEM_COMPLEMENTO = '''Loja 1
Log 1, 10
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_complemento():
    cupom.complemento = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_COMPLEMENTO
    cupom.complemento = "C1"

TEXTO_ESPERADO_SEM_BAIRRO = '''Loja 1
Log 1, 10 C1
Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_bairro():
    cupom.bairro = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_BAIRRO
    cupom.bairro = "Bai 1"

def test_municipio_vazio():
    cupom.municipio = ""
    verifica_campo_obrigatorio("O campo município do endereço é obrigatório")
    cupom.municipio = "Mun 1"

def test_estado_vazio():
    cupom.estado = ""
    verifica_campo_obrigatorio("O campo estado do endereço é obrigatório")
    cupom.estado = "E1"

TEXTO_ESPERADO_SEM_CEP = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_cep():
    cupom.cep = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_CEP
    cupom.cep = "11111-111"

TEXTO_ESPERADO_SEM_TELEFONE = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_telefone():
    cupom.telefone = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_TELEFONE
    cupom.telefone = "(11) 1111-1111"

TEXTO_ESPERADO_SEM_OBSERVACAO = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111

CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_observacao():
    cupom.observacao = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_OBSERVACAO
    cupom.observacao = "Obs 1"

def test_cnpj_vazio():
    cupom.cnpj = ""
    verifica_campo_obrigatorio("O campo CNPJ da loja é obrigatório")
    cupom.cnpj = "42.591.651/0797-34"

def test_inscricao_estadual_vazia():
    cupom.inscricao_estadual = ""
    verifica_campo_obrigatorio("O campo inscrição estadual da loja é obrigatório")
    cupom.inscricao_estadual = "244.898.500.113"

def test_exercicio2_customizado():
  # Defina seus próprios valores para as variáveis a seguir
	cupom.nome_loja = "Tropical"
	cupom.logradouro = "Rua siqueira Campos"
	cupom.numero = 580
	cupom.complemento = ""
	cupom.bairro = "Centro"
	cupom.municipio = "Paulista"
	cupom.estado = "Pernambuco"
	cupom.cep = "53401-320"
	cupom.telefone = "(81) 3438-5714"
	cupom.observacao = ""
	cupom.cnpj = "37.886.772/0001-82"
	cupom.inscricao_estadual = "4232303-79"

	#E atualize o texto esperado abaixo
	assert cupom.dados_loja() == '''Tropical
Rua siqueira Campos, 580
Centro - Paulista - Pernambuco
CEP:53401-320 Tel (81) 3438-5714

CNPJ: 37.886.772/0001-82
IE: 4232303-79'''
	cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
	cupom.logradouro = "Av. Projetada Leste"
	cupom.numero = 500
	cupom.complemento = "EUC F32/33/34"
	cupom.bairro = "Br. Sta Genebra"
	cupom.municipio = "Campinas"
	cupom.estado = "SP"
	cupom.cep = "13080-395"
	cupom.telefone = "(19) 3756-7408"
	cupom.observacao = "Loja 1317 (PDP)"
	cupom.cnpj = "42.591.651/0797-34"
	cupom.inscricao_estadual = "244.898.500.113"