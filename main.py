print("Game Begin")
@namespace
class SpriteKind:
    Gas = SpriteKind.create()

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        myImages.image0
    """), mySprite, 0, -150)
    projectile.start_effect(effects.ashes)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    statusbar.value = 100
sprites.on_overlap(SpriteKind.player, SpriteKind.Gas, on_on_overlap)

def on_on_zero(status):
    game.over(False)
statusbars.on_zero(StatusBarKind.energy, on_on_zero)

def on_on_overlap2(sprite2, otherSprite2):
    global enemySpeed
    sprite2.destroy(effects.fire, 100)
    otherSprite2.destroy()
    info.change_score_by(1)
    if info.score() == 10:
        info.change_score_by(5)
        mySprite.say_text("+5 Level Up Bonus!", 2000, False)
        enemySpeed = 70
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_life_by(-1)
    otherSprite3.destroy(effects.disintegrate, 200)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

myEnemy: Sprite = None
myFuel: Sprite = None
projectile: Sprite = None
enemySpeed = 0
statusbar: StatusBarSprite = None
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    Galaxy
"""))
scroller.scroll_background_with_speed(0, 10)
mySprite = sprites.create(assets.image("""
    Rocket
"""), SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
animation.run_image_animation(mySprite,
    assets.animation("""
        myAnimations.anim1
    """),
    500,
    True)
statusbar = statusbars.create(20, 4, StatusBarKind.energy)
statusbar.attach_to_sprite(mySprite, -25, 0)
enemySpeed = 50

def on_update_interval():
    global myFuel
    myFuel = sprites.create_projectile_from_side(assets.image("""
        Spider
    """), 0, 80)
    myFuel.x = randint(5, 155)
    myFuel.set_kind(SpriteKind.Gas)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global myEnemy
    myEnemy = sprites.create_projectile_from_side(assets.image("""
        Spider
    """), 0, enemySpeed)
    myEnemy.x = randint(5, 155)
    myEnemy.set_kind(SpriteKind.enemy)
    animation.run_image_animation(myEnemy,
        assets.animation("""
            Flying Spider
        """),
        100,
        True)
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    statusbar.value += -1
game.on_update_interval(300, on_update_interval3)
