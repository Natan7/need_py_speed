while True:
    clock.tick(60)
    # Fechar o game
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pygame.event.set_repeat(1,1)
            if event.key == pygame.K_LEFT:
                pos_carro[0] -= 1
            elif event.key == pygame.K_RIGHT:
                pos_carro[0] += 1
        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.key.get_pressed()[K_ESCAPE]:
            sys.exit()

