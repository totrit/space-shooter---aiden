def on_a_pressed():
    global game_state
    game_state = 2
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    global game_state
    game_state = 3
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

projectile: Sprite = None
game_state = 0
nathan = sprites.create(img("""
        .................ccfff..............
        ................cddbbf..............
        ...............cddbbf...............
        .........ffffffccbbcf...............
        ......fffbbbbbbbbcccff..............
        .....fbbbbbbbbbbbbbbbcfff......ccccc
        .....bcbbbbbffbcbcbbbbcccff...cdbbbc
        .....bbb1111ffbbcbcbbbcccccffcddbbc.
        .....fb11111111bcbcbbbcccccccbdbbf..
        ......fccc33c11bbbbbbcccccccccbbcf..
        .......fc131cc11bbbbccccccccffbccf..
        ........f33c1111bbbcccccbdbc..fbbcf.
        .........ff1111cbbbfdddddcc....fbbf.
        ...........ccc1fbdbbfddcc.......fbbf
        ..............ccfbdbbfc..........fff
        .................fffff..............
        """),
    SpriteKind.enemy)
aiden = sprites.create(img("""
        ......ffff..............
        ....fff22fff............
        ...fff2222fff...........
        ..fffeeeeeefff..........
        ..ffe222222eef..........
        ..fe2ffffff2ef..........
        ..ffffeeeeffff......ccc.
        .ffefbf44fbfeff....cddc.
        .ffefbf44fbfeff...cddc..
        .fee4dddddd4eef.ccddc...
        fdfeeddddd4eeffecddc....
        fbffee4444ee4fddccc.....
        fbf4f222222f1edde.......
        fcf.f222222f44ee........
        .ff.f445544f............
        ....ffffffff............
        .....ff..ff.............
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        """),
    SpriteKind.player)
nathan.set_position(74, 10)
aiden.set_position(82, 109)
controller.move_sprite(aiden)
aiden.set_stay_in_screen(True)
nathan.set_stay_in_screen(True)
game_state = 1
textSprite = textsprite.create("Space Shooter -- Aiden")
textSprite.set_position(75, 60)

def on_on_update():
    if game_state == 3:
        game.game_over(False)
game.on_update(on_on_update)

def on_update_interval():
    global projectile
    if game_state == 2:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . 2 2 2 2 2 2 2 2 . . . .
                . . . 2 4 4 4 5 5 4 4 4 2 2 2 .
                . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 .
                . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2
                . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2
                2 4 5 5 d 5 5 5 d d d 5 5 5 4 4
                2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4
                4 4 4 4 . . 2 4 5 5 . . 4 4 4 4
                . . b b b b 2 4 4 2 b b b b . .
                . b d d d d 2 4 4 2 d d d d b .
                b d d b b b 2 4 4 2 b b b d d b
                b d d b b b b b b b b b b d d b
                b b d 1 1 3 1 1 d 1 d 1 1 d b b
                . . b b d d 1 1 3 d d 1 b b . .
                . . 2 2 4 4 4 4 4 4 4 4 2 2 . .
                . . . 2 2 4 4 4 4 4 2 2 2 . . .
                """),
            nathan,
            0,
            50)
        nathan.x += randint(-100, 100)
game.on_update_interval(1000, on_update_interval)
