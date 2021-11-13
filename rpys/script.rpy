# The script of the game goes in this file.
default _game_menu_screen = "blanket"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform left_center:
    xalign -.15
transform right_center:
    xalign 1.15
image clockrot:
    contains:
        "images/clock_anim_hand_hour.png"
        xalign .5 yalign .5
    contains:
        "images/clock_anim_numeral_roman.png"
        xalign .5 yalign .5
        alignaround (.5, .5)
        linear 4.2 rotate 1200
    contains:
        "images/clock_anim_hand_minute.png"
        xalign .5 yalign .5
        alignaround (.5, .5)
        linear 4.2 rotate 600
    contains:
        pause .9
        "images/clock_anim_numeral_normal.png"
        xalign .25 yalign .25
        zoom 1.5
        alignaround (.5, .5)
        linear 1.5 zoom 1 rotate 150 xalign .5 yalign .5
        zoom 20
    contains:
        pause 3.3
        "images/clock_anim_numeral_normal.png"
        xalign .5 yalign .5
        alignaround (.5, .5)
        linear 1.0 zoom 1.5 rotate 150


define babydis = Dissolve(1)
define adultdis = Dissolve(1.9)
init python:
    def clockanim():
        renpy.show("clockrot")
        renpy.with_statement(babydis)
        renpy.pause(1)
        renpy.hide("clockrot")
        renpy.with_statement(adultdis)

transform mesbox:
    xalign .5 yalign 1.01
transform fabox:
    xalign -.026 yalign 1.01
init python:
    def hi_mes():
        renpy.hide("frame_gen_togaki",layer="mbox")
        renpy.hide("frame_gen_heroine", layer="mbox")
        renpy.hide("frame_gen_monologue",layer="mbox")
        renpy.hide("frame_gen_chara",layer="mbox")
        renpy.hide("frame_par_togaki",layer="mbox")
        renpy.hide("frame_par_heroine", layer="mbox")
        renpy.hide("frame_par_monologue",layer="mbox")
        renpy.hide("frame_par_chara",layer="mbox")
        renpy.scene(layer="face")
    def face(ident):
        renpy.show(ident, at_list=[fabox], layer="face",)
    def show_mes(ident):
        renpy.show(ident, at_list=[mesbox], layer="mbox")
    def flash(ident):
        renpy.show("white")
        renpy.pause(ident)
        renpy.hide("white")
    def flash_orange(ident):
        renpy.show("orange")
        renpy.pause(ident)
        renpy.hide("orange")
    def flash_blue(ident):
        renpy.show("blue")
        renpy.pause(ident)
        renpy.hide("blue")
    def flash_black(ident):
        renpy.show("black")
        renpy.pause(ident)
        renpy.hide("black")
    def flash_purple(ident):
        renpy.show("purple")
        renpy.pause(ident)
        renpy.hide("purple")
    def flash_indigo(ident):
        renpy.show("indigo")
        renpy.pause(ident)
        renpy.hide("indigo")
    def flash_red(ident):
        renpy.show("red")
        renpy.pause(ident)
        renpy.hide("red")
    def flash_salmon(ident):
        renpy.show("salmon")
        renpy.pause(ident)
        renpy.hide("salmon")
    def flash_yellow(ident):
        renpy.show("yellow")
        renpy.pause(ident)
        renpy.hide("yellow")
    def flash_medium_blue(ident):
        renpy.show("medium_blue")
        renpy.pause(ident)
        renpy.hide("medium_blue")
    def flash_light_blue(ident):
        renpy.show("light_blue")
        renpy.pause(ident)
        renpy.hide("light_blue")
    def flash_sky_blue(ident):
        renpy.show("sky_blue")
        renpy.pause(ident)
        renpy.hide("sky_blue")
    def flash_orange_2(ident):
        renpy.show("orange_2")
        renpy.pause(ident)
        renpy.hide("orange_2")
    def flash_sea_green(ident):
        renpy.show("sea_green")
        renpy.pause(ident)
        renpy.hide("sea_green")
    def flash_light_green(ident):
        renpy.show("light_green")
        renpy.pause(ident)
        renpy.hide("light_green")
    def flash_turquoise_green(ident):
        renpy.show("turquoise_green")
        renpy.pause(ident)
        renpy.hide("turquoise_green")
    def flash_teal(ident):
        renpy.show("teal")
        renpy.pause(ident)
        renpy.hide("teal")
    def flash_light_red(ident):
        renpy.show("light_red")
        renpy.pause(ident)
        renpy.hide("light_red")
    def flash_dark_orange(ident):
        renpy.show("dark_orange")
        renpy.pause(ident)
        renpy.hide("dark_orange")
    def flash_color(ident1,ident2):
        flashed_color = ident1
        renpy.show(flashed_color)
        renpy.pause(ident2)
        renpy.hide(flashed_color)
    def time_effect():
        renpy.show("t1me")
        renpy.with_statement(check_long)
        renpy.hide("t1me")
        renpy.with_statement(check_long)
##defining transitions
define check_long = ImageDissolve("gui/check.png", 1.5, ramplen=128, reverse=True)
define expand_long = ImageDissolve("gui/expand.png", 1.5, ramplen=128, reverse=True)
define expand_medlong = ImageDissolve("gui/expand.png", 1, ramplen=128, reverse=True)
define expand_short = ImageDissolve("gui/expand.png", .3, ramplen=128, reverse=True)
define expand_extrashort = ImageDissolve("gui/expand.png", .1, ramplen=128, reverse=True)
define expand = ImageDissolve("gui/expand.png", .5, ramplen=128, reverse=True)
define open_m = ImageDissolve("gui/o.png", .5, ramplen=128, reverse=True)
define open_medium = ImageDissolve("gui/o.png", .8, ramplen=128, reverse=True)
define open_long = ImageDissolve("gui/o.png", 1.5, ramplen=128, reverse=True)
define open_extralong = ImageDissolve("gui/o.png", 2, ramplen=128, reverse=True)
define open_medlong = ImageDissolve("gui/o.png", 1, ramplen=128, reverse=True)
define compress_long = ImageDissolve("gui/compress.png", 1.5, ramplen=128, reverse=True)
define compress_medlong = ImageDissolve("gui/compress.png", 1, ramplen=128, reverse=True)
define compress_short = ImageDissolve("gui/compress.png", .2, ramplen=128, reverse=True)
define compress = ImageDissolve("gui/compress.png", .5, ramplen=128, reverse=True)
define compress_extralong = ImageDissolve("gui/compress.png", 4, ramplen=128, reverse=True)
define compress_extraextralong = ImageDissolve("gui/compress.png", 6, ramplen=128, reverse=True)
define spread_extraextrashort = ImageDissolve("gui/spread.png", .1, ramplen=128, reverse=True)
define spread_extrashort = ImageDissolve("gui/spread.png", .2, ramplen=128, reverse=True)
define spread_short = ImageDissolve("gui/spread.png", .4, ramplen=128, reverse=True)
define spread = ImageDissolve("gui/spread.png", .5, ramplen=128, reverse=True)
define spread_medium = ImageDissolve("gui/spread.png", .7, ramplen=128, reverse=True)
define spread_long = ImageDissolve("gui/spread.png", 1.2, ramplen=128, reverse=True)
define close_short = ImageDissolve("gui/clo.png", .4, ramplen=128, reverse=True)
define close_m = ImageDissolve("gui/clo.png", .5, ramplen=128, reverse=True)
define close_extrashort = ImageDissolve("gui/clo.png", .2, ramplen=128, reverse=True)
define close_medium = ImageDissolve("gui/clo.png", .8, ramplen=128, reverse=True)
define close_medlong = ImageDissolve("gui/clo.png", 1, ramplen=128, reverse=True)
define close_long = ImageDissolve("gui/clo.png", 1.5, ramplen=128, reverse=True)
define grad_r_extrashort = ImageDissolve("gui/grad_r.png", .2, ramplen=128, reverse=True)
define grad_r_medium = ImageDissolve("gui/grad_r.png", .8, ramplen=128, reverse=True)
define grad_l_short = ImageDissolve("gui/grad_l.png", .5, ramplen=128, reverse=True)
define grad_l_extrashort = ImageDissolve("gui/grad_l.png", .2, ramplen=128, reverse=True)
define grad_l_long = ImageDissolve("gui/grad_l.png", 1.2, ramplen=128, reverse=True)
define grad_t_short = ImageDissolve("gui/grad_t.png", .5, ramplen=128, reverse=True)
define grad_t_extrashort = ImageDissolve("gui/grad_t.png", .2, ramplen=128, reverse=True)
define grad_t = ImageDissolve("gui/grad_t.png", .5, ramplen=128, reverse=True)
define grad_t_long = ImageDissolve("gui/grad_t.png", 1.2, ramplen=128, reverse=True)
define grad_t_medlong = ImageDissolve("gui/grad_t.png", 1, ramplen=128, reverse=True)
define grad_b = ImageDissolve("gui/grad_b.png", .5, ramplen=128, reverse=True)
define grad_b_short = ImageDissolve("gui/grad_b.png", .3, ramplen=128, reverse=True)
define grad_b_medlong = ImageDissolve("gui/grad_b.png", 1, ramplen=128, reverse=True)
define grad_b_long = ImageDissolve("gui/grad_b.png", 1.5, ramplen=128, reverse=True)
define grad_b_extralong = ImageDissolve("gui/grad_b.png", 2, ramplen=128, reverse=True)
define stripe_l_short = ImageDissolve("gui/stripe_l.png", .5, ramplen=128, reverse=True)
define stripe_r_short = ImageDissolve("gui/stripe_r.png", .5, ramplen=128, reverse=True)
define stripe_l_long = ImageDissolve("gui/stripe_l.png", 1.2, ramplen=128, reverse=True)
define stripe_l_medlong = ImageDissolve("gui/stripe_l.png", 1, ramplen=128, reverse=True)
define stripe_l_extralong = ImageDissolve("gui/stripe_l.png", 2, ramplen=128, reverse=True)
define stripe_l_medium = ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)
define stripe_l = ImageDissolve("gui/stripe_l.png", .8, ramplen=128, reverse=True)
define eddy_short = ImageDissolve("gui/eddy.png", .1, ramplen=128, reverse=True)
define eddy_extralong = ImageDissolve("gui/eddy.png", 2, ramplen=128, reverse=True)
define spin_l = ImageDissolve("gui/spin_l.png", .1, ramplen=128, reverse=True)
define spin_r = ImageDissolve("gui/spin_r.png", .1, ramplen=128, reverse=True)
define dis = Dissolve(.5)

##defining characters
define Ace = Character("Ace", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Assistant = Character("Assistant", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Banny = Character("Bunny", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Black_Joker = Character("Black Joker", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Blood = Character("Blood", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Boris = Character("Boris", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Boy = Character("Boy", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Captain = Character("Captain", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Cat = Character("Cat", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Chef = Character("Chef", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Child = Character("Child", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Clerk = Character("Clerk", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Customer = Character("Customer", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Dam = Character("Dum", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Danin = Character("Acrobat", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Dealer = Character("Dealer", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Dee = Character("Dee", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Defender = Character("Actor", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Doctor = Character("Doctor", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Door = Character("Door", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Elliot = Character("Elliot", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Employee = Character("Tower Employee", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Engei_Buin = Character("Engui_buin", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Engei_head = Character("Engei_head", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Father = Character("Father", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Furyou = Character("Furyou", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Fuuki = Character("Fuuki", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Ghost = Character("Ghost", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Girl = Character("Girl", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Gowland = Character("Gowland", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Gray = Character("Gray", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Guide = Character("Guide", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Joker = Character("Joker", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Jimu_w = Character("Maid", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Julius = Character("Julius", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define King = Character("King", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Kousei = Character("Member", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Kyousi = Character("Member", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Kusuri = Character("Medicine", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Kyouzyu = Character("Kyouzyu", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Lorina = Character("Lorina", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Maid = Character("Maid", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Man = Character("Man", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Mask = Character("Mask", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Master = Character("Master", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Megami = Character("Megami", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Mermaid = Character("Mermaid", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Mother = Character("Mother", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Monster = Character("Monster", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Mouse = Character("Mouse", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Mouse_big = Character("Giant Mouse", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Nightmare = Character("Nightmare", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Nazo = Character("Nazo", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Park_Employee = Character("Park, Employee", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Peter = Character("Peter", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Pierce = Character("Pierce", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Punk = Character("Punk", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Servant = Character("Servant", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Soldier = Character("Soldier", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define T = Character(name=None, ctc="ctc_blink", ctc_position="nestled")
define Thug = Character("Thug", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Tower_Employee = Character( "Tower Staff", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Unknown = Character("???", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Hatena = Character("???", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Vivaldi = Character("Vivaldi", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define W = Character("Acrobat", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define White_Joker = Character("White Joker", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Woman = Character("Woman", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Seito = Character("Student", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Seinen = Character("Teacher", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define Yousei = Character("Yousei", ctc="ctc_blink", ctc_position="nestled", what_prefix='"', what_suffix='"')
define annoy= ImageDissolve("gui/rule17.png", 1, ramplen=4)
# The game starts here.
label blert:
hide screen blanket
show screen save()
$ ui.interact()
label start:
stop music
$ setting_choice = ""
$ place_of_stay = ""
$ extra_joker = False
scene inputname_bg
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "What is my name?"
$ hi_mes()
$ show_mes("frame_gen_togaki")
T "My first and last name can be up to 10 characters each."
$ hi_mes()
jump nameinput
label nameinput:
$ renpy.checkpoint()
show inputname_windo onlayer master:
    xalign 1.01
    yalign .5
hide text "[firstname]"
hide screen confirm_screen
$ firstname = "Alice"
$ lastname = "Lidell"
$ name_seen = False
label first_name:
$ hi_mes()
show screen first_name
hide screen last_name
$ ui.interact()
label last_name:
$ name_seen = True
hide screen first_name
show screen last_name
$ ui.interact()
label confirm:
hide screen first_name
hide screen last_name
show text "[firstname]":
    xalign .4 yalign .4
show text "[lastname]":
    xalign .7 yalign .7
$ familyname = lastname
hide inputname_windo
show inputname_window_name onlayer master:
    xalign 1.01
    yalign 0
show inputname_window_mo onlayer master:
    xalign .9
    yalign 1.01
show text "{color=#000000}[firstname]{/color}" onlayer mbox:
    xalign .42 yalign .19
show text "{color=#000000}[lastname]{/color}" onlayer screens:
    xalign .82 yalign .19
show inputname_window_yn onlayer transient:
    xalign .95 yalign .95
show screen confirm_screen
show text "{color=#000000}Is [firstname] [lastname] ok?{/color}" onlayer overlay:
    xalign .65 yalign .55
$ ui.interact()
label redo:
$ renpy.rollback(checkpoints=1, label="nameinput")

label signature:
hide screen confirm_screen
$ hi_mes()
scene inputname_bg
scene onlayer mbox
scene onlayer screens
play sound se_name_regist
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "Signature complete!"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_1")
T "Right-click to access the options screen.\n I haven't really figured out the interface yet, so you'll have to stick with me, ok?."
$ hi_mes()

jump setting_choice

label setting_choice:
$ renpy.checkpoint()
scene mo with fade
show screen setting_choice_screen
$ ui.interact()

label fushigi_intro:
hide screen setting_choice_screen
scene map_gen_bg with fade
$ setting_choice = "fushigi"
$ show_mes("frame_gen_togaki")
T "Where do you move to?"
$ hi_mes()
show screen fushigi_move
$ ui.interact()

label gakuen_stay_choice:
$ hi_mes()
show screen gakuen_move
$ ui.interact()

label Gakuen_hatter_confirm:
hide screen gakuen_move
$ show_mes("frame_par_togaki")
T "Will you stay in the Hatter Dormitory?"
$ hi_mes()
menu:
    "OK":
        jump gakuen_dormitory_common_hatter1
    "NG":
        jump gakuen_stay_choice
label Gakuen_amuse_confirm:
hide screen gakuen_move
$ show_mes("frame_par_togaki")
T "Will you stay in the Amusement Park Dormitory?"
$ hi_mes()
menu:
    "OK":
        jump gakuen_dormitory_common_amuse1
    "NG":
        jump gakuen_stay_choice
label Gakuen_castle_confirm:
hide screen gakuen_move
$ show_mes("frame_par_togaki")
T "Will you stay in the Red Rose Dormitory?"
$ hi_mes()
menu:
    "OK":
        jump gakuen_dormitory_common_castle1
    "NG":
        jump gakuen_stay_choice
label Gakuen_tower_confirm:
hide screen gakuen_move
$ show_mes("frame_par_togaki")
T "Will you stay in the Tower?"
$ hi_mes()
menu:
    "OK":
        jump gakuen_dormitory_common_tower1
    "NG":
        jump gakuen_stay_choice
label Hatter_confirm:
hide screen fushigi_move
$ show_mes("frame_gen_togaki")
T "Will you move to Hatter Mansion?"
$ hi_mes()
menu:
    "OK":
        jump fushigi_op_hatter1
    "NG":
        jump fushigi_intro

label Amuse_confirm:
hide screen fushigi_move
$ show_mes("frame_gen_togaki")
T "Will you move to the Amusement Park?"
$ hi_mes()
menu:
    "OK":
        jump fushigi_op_amuse1
    "NG":
        jump fushigi_intro
label Castle_confirm:
hide screen fushigi_move
$ show_mes("frame_gen_togaki")
T "Will you move to the Castle of Hearts?"
$ hi_mes()
menu:
    "OK":
        jump fushigi_op_castle1
    "NG":
        jump fushigi_intro
label Tower_confirm:
hide screen fushigi_move
$ show_mes("frame_gen_togaki")
T "Will you move to Clover Tower?"
$ hi_mes()
menu:
    "OK":
        jump fushigi_op_tower1
    "NG":
        jump fushigi_intro

label Hatter_check1:
hide screen fushigi_map1
if routechara == "Pierce":
    jump fushigi_common2_hatter
if routechara == "Nightmare":
    jump fushigi_common2_hatter
if routechara == "Gray":
    jump fushigi_common2_hatter
else:
    jump Nah
label Circus_confirm:
    jump fushigi_joker1
label Castle_check1:
hide screen fushigi_map1
if routechara == "Blood":
    jump fushigi_common2_castle
if routechara == "Deedam":
    jump fushigi_common2_castle
if routechara == "Julius":
    jump fushigi_common2_castle
else:
    jump Nah

label Amuse_check1:
hide screen fushigi_map1
if routechara == "Vivaldi":
    jump fushigi_common2_amuse
if routechara == "Ace":
    jump fushigi_common2_amuse
if routechara == "Elliot":
    jump fushigi_common2_amuse
else:
    jump Nah

label Tower_check1:
hide screen fushigi_map1
if routechara == "Peter":
    jump fushigi_common2_tower
if routechara == "Gowland":
    jump fushigi_common2_tower
if routechara == "Boris":
    jump fushigi_common2_tower
else:
    jump Nah

label Nah:

$ show_mes("frame_gen_togaki")
$ face("ali_t_05_15")
T "「いきなり押しかけるんだし……。\n
今回、ここはやめておこうかしら」"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()

label gameplay:
hide screen confirm_screen
scene map_bg_autumn_day
with annoy
scene charasel_bg_hatter_day
with annoy
play music hatter_gate_p_ali
jump fushigi_end_amuse1
scene bm_aut_01_1
with annoy
camera at vpunch
$ flash (.5)
pause 5
show dee_t_02_1 at center
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0001
Dam "「この前買ったばっかりの、新型手榴弾！\n
この威力、現場で盛大に試さなくちゃ」"
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
hide dee_t_02_1
show dee_t_02_1 at left
show dam_t_02_5 at right
with dis

voice dad_f0002
Dam "
「そうだね、兄弟。\n
必要経費で落としたんだもの、ぱあっと使わなくちゃもったいない」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "
門の前で交わされている会話の物騒なこと。\n
漏れ聞こえてくる内容は、穏やかとはいえない。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "
門番がこんな会話をしていたら、誰も屋敷の中へ入りたくないだろう。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "
（なんだって、いつもいつも物騒そうな……）"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
"
（……いや、物騒そう、じゃないわね。\n
実際に物騒なのよ、あの子達が安全だなんて口が裂けても言えない）"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
何しろ、ついている二つ名が『ブラッディ・ツインズ』だ。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
片時もその手から離さない大きな斧といい、彼らの持ち物で、安全なものなど私はこれまで見たことがない。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
外見だけでなく、中身も。\n
無邪気そうな見た目を裏切る子供達。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
"
「……また、仕事かしら」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
帽子屋屋敷に滞在して短くないが、ここの仕事の状況は不規則すぎて、いまだに掴めない。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
"
（時間帯さえ、ころころと変わる世界なんだから……。\n
不規則なのは当たり前だけど）"
$ hi_mes()
hide dee_t_02_1
show dee_t_01_2 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice dad_f0004
Dam "「あ、お姉さん！\n
どこかに行くの？」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
"
「！」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
見つかってしまった。"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
門に近付いたところで、こちらに気が付いた二人が振り返り、敷地へ入ってくる。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
"
「あ……、わ……」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
駆け寄られて、隠れていたわけでもないのに、慌ててしまう。\n
いつだって、彼らの手にはぎらぎらした斧があるのだ。"
$ hi_mes()
hide dam_t_02_5
show dam_t_01_2 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0005
Dam "
「どこかへ行くなら、護衛として僕達がついていってあげるよ。\n
ねえ、どこへ行くの？」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
まだ何も答えないうちから、出掛けることが決めつけられてしまっている。"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
"
「出掛けるとは言っていないでしょう？」"
$ hi_mes()
hide dee_t_01_2
show dee_t_01_5 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice dad_f0006
Dam "「え？でも、出掛けるんだよね？\n
……僕達には言えないようなところへ行くの？」"
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
"
「そ、そういうわけじゃないわよ」"
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
外見上は私のほうが年上。\n
だが、完全に押し負けてしまっている。"
$ hi_mes()
hide dam_t_01_2
show dam_t_01_6 at right
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0007
Dam "
「じゃあ、ついていってもいいよね？\n
いいでしょ、お姉さん」"
$ hi_mes()
hide dee_t_01_5
show dee_t_01_7 at left
with dis
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0008
Dam "「僕達がいれば、安全だよ？」"
$ hi_mes()
play sound se_0621
pause 3
play sound se_0621
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
"
今までずっと引き摺っていた物騒な箱から手を離した二人が、駆け寄ってくる。"
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
"
（いやあ……、むしろ、危険じゃないかしら。\n
……特に、その得体の知れない箱の中身とか、いかにも）"
$ hi_mes()
$ show_mes("frame_gen_heroine")

#return
