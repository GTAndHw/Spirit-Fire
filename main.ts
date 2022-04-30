console.log("Game Begin")
namespace SpriteKind {
    export const Gas = SpriteKind.create()
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    projectile = sprites.createProjectileFromSprite(assets.image`
        myImages.image0
    `, mySprite, 0, -150)
    projectile.startEffect(effects.ashes)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Gas, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    statusbar.value = 100
})
statusbars.onZero(StatusBarKind.Energy, function on_on_zero(status: StatusBarSprite) {
    game.over(false)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    
    sprite2.destroy(effects.fire, 100)
    otherSprite2.destroy()
    info.changeScoreBy(1)
    if (info.score() == 10) {
        info.changeScoreBy(5)
        mySprite.sayText("+5 Level Up Bonus!", 2000, false)
        enemySpeed = 70
    }
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap3(sprite3: Sprite, otherSprite3: Sprite) {
    info.changeLifeBy(-1)
    otherSprite3.destroy(effects.disintegrate, 200)
    scene.cameraShake(4, 500)
})
let myEnemy : Sprite = null
let myFuel : Sprite = null
let projectile : Sprite = null
let enemySpeed = 0
let statusbar : StatusBarSprite = null
let mySprite : Sprite = null
scene.setBackgroundImage(assets.image`
    Galaxy
`)
scroller.scrollBackgroundWithSpeed(0, 10)
mySprite = sprites.create(assets.image`
    Rocket
`, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setStayInScreen(true)
animation.runImageAnimation(mySprite, assets.animation`
        myAnimations.anim1
    `, 500, true)
statusbar = statusbars.create(20, 4, StatusBarKind.Energy)
statusbar.attachToSprite(mySprite, -25, 0)
enemySpeed = 50
game.onUpdateInterval(5000, function on_update_interval() {
    
    myFuel = sprites.createProjectileFromSide(assets.image`
        Spider
    `, 0, 80)
    myFuel.x = randint(5, 155)
    myFuel.setKind(SpriteKind.Gas)
})
game.onUpdateInterval(2000, function on_update_interval2() {
    
    myEnemy = sprites.createProjectileFromSide(assets.image`
        Spider
    `, 0, enemySpeed)
    myEnemy.x = randint(5, 155)
    myEnemy.setKind(SpriteKind.Enemy)
    animation.runImageAnimation(myEnemy, assets.animation`
            Flying Spider
        `, 100, true)
})
game.onUpdateInterval(300, function on_update_interval3() {
    statusbar.value += -1
})
