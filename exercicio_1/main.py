import service as s

while True:
    print(f'\nEscolha o comando:')
    print(f'1. Adicionar contato')
    print(f'2. Atualizar contato')
    print(f'3. Excluir contato')
    print(f'4. Listar contatos')
    print(f'5. Sair')
    opt = input('Opção:')
    if opt == '1':
        nome = input('Digite o nome:')
        fav = input('É favorito (S/N):')
        s.contato_criar(nome, fav)
    elif opt == '2':
        s.contato_listar()
        idx = input('Digite o índice do contato para edição: ')
        contato = s.contato_pegar(idx, True)
        if contato:
            nome = input('Digite o nome:')
            fav = input('É favorito (S/N):')
            s.contato_atualizar(idx, nome, fav)
    elif opt == '3':
        s.contato_listar()
        idx = input('Digite o índice do contato para exclusão: ')
        s.contato_excluir(idx)
    elif opt == '4':
        s.contato_listar()
    elif opt == '5':
        break
    else:
        print('Opção inválida')
    print()

print('Fim!')