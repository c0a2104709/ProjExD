import pygame as pg
import sys
import random

#練習７
def check_bound(obj_rct, scr_rct):
    # 第１引数：こうかとんrectまたは爆弾rect
    # 第２引数：スクリーンrect
    # 範囲内：+1/範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    clock = pg.time.Clock()
    #練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig\pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()


    #練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    #練習５
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    vx, vy = +1, +1

    #2個目の爆弾
    bomb2_sfc = pg.Surface((20, 20))
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (0, 0, 255), (10, 10), 10)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0, scrn_rct.width)
    bomb2_rct.centery = random.randint(0, scrn_rct.height)
    #５秒経過後に追加 
    if pg.time.get_ticks() >= 5000:
        scrn_sfc.blit(bomb2_sfc, bomb2_rct)
    #２倍速い
    vx2, vy2 = +2, +2

    #3倍大きい3個目の爆弾
    bomb3_sfc = pg.Surface((60, 60))
    bomb3_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb3_sfc, (0, 255, 0), (30, 30), 30)
    bomb3_rct = bomb3_sfc.get_rect()
    bomb3_rct.centerx = random.randint(0, scrn_rct.width)
    bomb3_rct.centery = random.randint(0, scrn_rct.height)
    #10秒経過後に追加 
    if pg.time.get_ticks() >= 10000:
        scrn_sfc.blit(bomb3_sfc, bomb3_rct)
    vx3, vy3 = +1, +1

    #残り時間を表示
    font = pg.font.Font(None, 80)
    time = 60
    txt = font.render(str(time), True, (0, 0, 0))
    scrn_sfc.blit(txt, (750, 50))

    #練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT: #ウインドウの✖ボタンがクリックされたら
                return
        
        t = pg.time.get_ticks()
        #1000ミリ秒毎に時間を残り時間を減らす
        if t % 1000 == 0:
            time -= 1
        txt = font.render(str(time), True, (0, 0, 0))
        scrn_sfc.blit(txt, (750, 50))

        #練習４
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        #練習６
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)

        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        #練習８
        if tori_rct.colliderect(bomb_rct): 
            return

        #２個目の爆弾のプログラム
        if pg.time.get_ticks() >= 5000:
            bomb2_rct.move_ip(vx2, vy2)
            scrn_sfc.blit(bomb2_sfc, bomb2_rct)
            yoko2, tate2 = check_bound(bomb2_rct, scrn_rct)
            vx2 *= yoko2
            vy2 *= tate2
        if tori_rct.colliderect(bomb2_rct):
            return

        #３個目の爆弾のプログラム
        if pg.time.get_ticks() >= 10000:
            bomb3_rct.move_ip(vx3, vy3)
            scrn_sfc.blit(bomb3_sfc, bomb3_rct)
            yoko3, tate3 = check_bound(bomb3_rct, scrn_rct)
            vx3 *= yoko3
            vy3 *= tate3
        if tori_rct.colliderect(bomb3_rct):
            return

        #６０秒経過後
        if pg.time.get_ticks() >= 60000:
            font2 = pg.font.Font(None, 100)
            txt2 = font.render("CLEAR", True, (0, 0, 0))
            scrn_sfc.blit(txt2, (600, 200))
            #終了させずに10秒停止
            pg.time.wait(10000)
            return
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()