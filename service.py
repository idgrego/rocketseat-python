contatos = []

def trata_favorito(favorito):
    if favorito not in ['s', 'S', 'n', 'N']: return False
    else:
        favorito = favorito.upper() 
        return True if favorito == 'S' else False
    
def trata_indice(idx, print_message):
    try:
        return int(idx) - 1
    except:
        if print_message: print('Índice inválido')
        return -1

def contato_criar(nome, favorito):
    if not nome or len(nome) == 0: print('Nome é obrigatório')
    contato = { "nome": nome, "favorito": trata_favorito(favorito) }
    contatos.append(contato)
    print('Contato criado')

def contato_atualizar(idx, nome, favorito):
    contato = contato_pegar(idx, True)
    if contato:
        if not nome or len(nome) == 0: print('Nome é obrigatório')
        contato["nome"] = nome
        contato["favorito"] = trata_favorito(favorito)
        print('Contato atualizado')

def contato_excluir(idx):
    contato = contato_pegar(idx, True)
    if contato:
        contatos.remove(contato)
        print('Contato excluído')

def contato_pegar(idx, print_not_found):
    idx = trata_indice(idx, False)
    if idx >= 0 and idx < len(contatos):
        return contatos[idx]
    else:
        if print_not_found: print('Contato não encontrado')
        return None

def contato_listar():
    if len(contatos) == 0: print('Não há contatos cadastrados')
    for idx, item in enumerate(contatos):
        f = item['favorito']
        print(f"{idx + 1}. [{'✓' if f else ' '}] {item['nome']}")