################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign .5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

style face:
    xpos 100
    ypos 510
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("named", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
image named = ConditionSwitch (
    "setting_choice == 'fushigi'","gui/namebox1.png",
    "setting_choice == ''", "gui/namebox1.png",
    "setting_choice == 'gakuen'", "gui/namebox2.png")
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    color "#000000"
    kerning -2
    outlines [ (3, "#FFFFFF", 0, 0 ) ]


style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign 0
            xpos .37
            xsize gui.dialogue_width
            ypos -.5

            text prompt style "input_prompt"
            input id "input"

screen first_name():
    style_prefix "first_name"
    input:
        default("Alice")
        length(10)
        value VariableInputValue("firstname")
        xalign .4
        yalign .49
    imagebutton auto "gui/button/name_%s.png":
        action Jump("last_name")
        yalign .49
        xalign .85
        keysym('K_RETURN', 'K_KP_ENTER')
    text "First name:":
        xalign .42
        yalign .39
        color "#000000"
        size 45
    text "Last name:":
        xalign .88
        yalign .39
        color "#000000"
        size 45
    text "[lastname]":
        yalign .49
        xalign .85
    showif name_seen == True:
        textbutton "OK":
            action Jump("confirm")
            xalign .88
            yalign .88
            activate_sound "se_name_regist.wav"
            hover_sound ""
screen last_name():
    style_prefix "last_name"
    text "[firstname]":
        xalign .4
        yalign .49
    input:
        default("Lidell")
        length(10)
        value VariableInputValue("lastname")
        yalign .49
        xalign .85
    imagebutton auto "gui/button/name_%s.png":
        action Jump("first_name")
        xalign .4
        yalign .49
    text "Last name:":
        xalign .88
        yalign .39
        color "#000000"
        size 45
    text "First name:":
        xalign .42
        yalign .39
        color "#000000"
        size 45
    textbutton "OK":
        action Jump("confirm")
        xalign .88
        yalign .88
        keysym('K_RETURN', 'K_KP_ENTER')
screen fushigi_move():
    imagebutton auto "gui/button/hatter_%s.png":
        action Jump("Hatter_confirm")
        hover_sound "audio/system_sounds/hover_button.wav"
        activate_sound "audio/system_sounds/activate_button.wav"
        at transform:
            xalign 0.01 yalign 0.97
    imagebutton auto "gui/button/amuse_%s.png":
        action Jump("Amuse_confirm")
        hover_sound "audio/system_sounds/hover_button.wav"
        activate_sound "audio/system_sounds/activate_button.wav"
        at transform:
            xalign 0.99 yalign 0.48
    imagebutton auto "gui/button/castle_%s.png":
        action Jump("Castle_confirm")
        hover_sound "audio/system_sounds/hover_button.wav"
        activate_sound "audio/system_sounds/activate_button.wav"
        at transform:
            xalign .03 yalign .33
    imagebutton auto "gui/button/tower_%s.png":
        action Jump("Tower_confirm")
        hover_sound "audio/system_sounds/hover_button.wav"
        activate_sound "audio/system_sounds/activate_button.wav"
        at transform:
            xalign 1.02 yalign .99
screen fushigi_map1():
    showif place_of_stay == "Hatter":
        imagebutton auto "gui/button/amuse_%s.png":
            action Jump("Amuse_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign 0.99 yalign 0.48
        imagebutton auto "gui/button/castle_%s.png":
            action Jump("Castle_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign .03 yalign .33
        imagebutton auto "gui/button/tower_%s.png":
            action Jump("Tower_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign 1.02 yalign .99
    showif place_of_stay == "Amuse":
        imagebutton auto "gui/button/hatter_%s.png":
            action Jump("Hatter_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign 0.01 yalign 0.97
        imagebutton auto "gui/button/castle_%s.png":
            action Jump("Castle_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign .03 yalign .33
        imagebutton auto "gui/button/tower_%s.png":
            action Jump("Tower_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign 1.02 yalign .99
    showif place_of_stay == "Tower":
        imagebutton auto "gui/button/hatter_%s.png":
            action Jump("Hatter_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign 0.01 yalign 0.97
        imagebutton auto "gui/button/castle_%s.png":
            action Jump("Castle_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign .03 yalign .33
        imagebutton auto "gui/button/amuse_%s.png":
            action Jump("Amuse_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign 0.99 yalign 0.48
    showif place_of_stay == "Castle":
        imagebutton auto "gui/button/hatter_%s.png":
            action Jump("Hatter_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign 0.01 yalign 0.97
        imagebutton auto "gui/button/tower_%s.png":
            action Jump("Tower_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign 1.02 yalign .99
        imagebutton auto "gui/button/amuse_%s.png":
            action Jump("Amuse_check1")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign 0.99 yalign 0.48
    showif renpy.seen_label("fushigi_a") == True:
        imagebutton auto "gui/button/circus_%s.png":
            action Jump("Circus_confirm")
            hover_sound "audio/system_sounds/hover_button.wav"
            activate_sound "audio/system_sounds/activate_button.wav"
            at transform:
                xalign .49 yalign .48
screen gakuen_move():
    imagebutton auto "buttons/gakuen_hatter_%s.png":
        action Jump("Gakuen_hatter_confirm")
        hover_sound "audio/system_sounds/hover_button.wav"
        activate_sound "audio/system_sounds/activate_button.wav"
        at transform:
            xalign -.075 yalign .41
    imagebutton auto "buttons/gakuen_amuse_%s.png":
        action Jump("Gakuen_amuse_confirm")
        hover_sound "audio/system_sounds/hover_button.wav"
        activate_sound "audio/system_sounds/activate_button.wav"
        at transform:
            xalign 1.06 yalign .76
    imagebutton auto "buttons/gakuen_castle_%s.png":
        action Jump("Gakuen_castle_confirm")
        hover_sound "audio/system_sounds/hover_button.wav"
        activate_sound "audio/system_sounds/activate_button.wav"
        at transform:
            xalign 1.065 yalign 0.235
    imagebutton auto "buttons/gakuen_tower_%s.png":
        action Jump("Gakuen_tower_confirm")
        hover_sound "audio/system_sounds/hover_button.wav"
        activate_sound "audio/system_sounds/activate_button.wav"
        at transform:
            xalign -.074 yalign 0.95
screen pierce_zoo_choice():
    hbox xcenter .5 yalign 1.01:
        spacing -45
        imagebutton auto "gui/button/pick_gowland_%s.png":
            action Jump("fushigi_end_pierce2")
        imagebutton auto "gui/button/pick_pierce_%s.png":
            action Jump("fushigi_end_zoo1")
screen hatter_man_choice():
    if setting_choice == "fushigi":
        add "gui/button/charasel_headline_gen.png" xalign .5 yalign -.05
    if setting_choice == "gakuen":
        add "gui/button/charasel_headline_par.png" xalign .5 yalign -.05
    hbox xcenter .5 yalign 1.01:
        spacing -45
        showif setting_choice == "fushigi":
            imagebutton auto "gui/button/pick_hatter_%s.png":
                action Jump("fushigi_blood_start")
            imagebutton auto "gui/button/pick_elliot_%s.png":
                action Jump("fushigi_elliot1")
            imagebutton auto "gui/button/pick_deedam_%s.png":
                action Jump("fushigi_dad1")
        showif setting_choice == "gakuen":
            imagebutton auto "gui/button/choose_blood_%s.png":
                action Jump("gakuen_blood_start")
            imagebutton auto "gui/button/choose_elliot_%s.png":
                action Jump("gakuen_elliot1")
            imagebutton auto "gui/button/choose_deedam_%s.png":
                action Jump("gakuen_dad1")
screen amuse_man_choice():
    if setting_choice == "fushigi":
        add "buttons/charasel_headline_gen.png" xalign .5 yalign -.05
    if setting_choice == "gakuen":
        add "buttons/charasel_headline_par.png" xalign .5 yalign -.05
    hbox xcenter .5 yalign 1.01:
        spacing -45
        showif setting_choice == "fushigi":
            imagebutton auto "gui/button/pick_gowland_%s.png":
                action Jump("fushigi_gowland1")
            imagebutton auto "gui/button/pick_boris_%s.png":
                action Jump("fushigi_boris_start")
            imagebutton auto "gui/button/pick_pierce_%s.png":
                action Jump("fushigi_pierce1")
        showif setting_choice == "gakuen":
            imagebutton auto "gui/button/choose_gowland_%s.png":
                action Jump("gakuen_gowland1")
            imagebutton auto "gui/button/choose_boris_%s.png":
                action Jump("gakuen_boris1")
            imagebutton auto "gui/button/choose_pierce_%s.png":
                action Jump("gakuen_pierce1")
screen castle_man_choice():
    if setting_choice == "fushigi":
        add "buttons/charasel_headline_gen.png" xalign .5 yalign -.05
    if setting_choice == "gakuen":
        add "buttons/charasel_headline_par.png" xalign .5 yalign -.05
    hbox xcenter .5 yalign 1.01:
        spacing -45
        showif setting_choice == "fushigi":
            imagebutton auto "gui/button/pick_peter_%s.png":
                action Jump("fushigi_peter1")
            imagebutton auto "gui/button/pick_vivaldi_%s.png":
                action Jump("fushigi_vivaldi1")
            imagebutton auto "gui/button/pick_ace_%s.png":
                action Jump("fushigi_ace_start")
        showif setting_choice == "gakuen":
            imagebutton auto "gui/button/choose_peter_%s.png":
                action Jump("gakuen_peter1")
            imagebutton auto "gui/button/choose_vivaldi_%s.png":
                action Jump("gakuen_vivaldi1")
            imagebutton auto "gui/button/choose_ace_%s.png":
                action Jump("gakuen_ace1")
screen tower_man_choice():
    if setting_choice == "fushigi":
        add "gui/button/charasel_headline_gen.png" xalign .5 yalign -.05
    if setting_choice == "gakuen":
        add "gui/button/charasel_headline_par.png" xalign .5 yalign -.05
    hbox xcenter .5 yalign 1.01:
        spacing -45
        showif setting_choice == "fushigi":
            imagebutton auto "gui/button/pick_julius_%s.png":
                action Jump("fushigi_julius1")
            imagebutton auto "gui/button/pick_nightmare_%s.png":
                action Jump("fushigi_nightmare1")
            imagebutton auto "gui/button/pick_gray_%s.png":
                action Jump("fushigi_gray1")
        showif setting_choice == "gakuen":
            imagebutton auto "gui/button/choose_julius_%s.png":
                action Jump("gakuen_julius1")
            imagebutton auto "gui/button/choose_nightmare_%s.png":
                action Jump("gakuen_nightmare1")
            imagebutton auto "gui/button/choose_gray_%s.png":
                action Jump("gakuen_gray1")
            showif extrajoker == True:
                imagebutton auto "buttons/choose_joker_%s.png":
                    action Jump("gakuen_joker1")
style input_prompt is default
screen setting_choice_screen():
    style_prefix "setting_choice"
    vbox xcenter .75 ysize 500 ycenter .55:
        textbutton "Original Version":
            style "setting_button"
            action Jump("fushigi_intro")
        textbutton "School Parody":
            style "setting_button"
            action Jump("gakuen_op_1")
        textbutton "Recommendation Quiz":
            style "setting_button"
            action Jump("mode_choice")
screen confirm_screen():
    style_prefix "confirm_screen"
    hbox xalign .88 yalign .85:
        spacing 50
        textbutton "OK":
            style "meow_button"
            action Jump("signature")
        textbutton "NG":
            style "meow_button"
            action Jump("redo")
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
style name_button:
    hover_color "#C4E8A4"
    hover_background "#C4E8A4"
    background None
    hover_sound "audio/system_sounds/hover_button.wav"
    activate_sound "audio/system_sounds/activate_button.wav"
style name_button_text:
    color "#000000"
    size 45
style meow_button_text:
    color "#000000"
    size 45
style meow_button:
    hover_color "#C4E8A4"
    hover_background "#C4E8A4"
    background None
    hover_sound "audio/system_sounds/hover_button.wav"
    activate_sound "audio/system_sounds/activate_button.wav"
style setting_button:
    background "gui/setting_idle_background.png"
    hover_background "gui/setting_hover_background.png"
    text_align .5
    hover_sound "audio/system_sounds/hover_button.wav"
    activate_sound "audio/system_sounds/activate_button.wav"
style setting_button_text:
    color "#000000"
    size 45
    idle_outlines [ (2, "#f1ecc2", 0, 0 ) ]
    hover_outlines [ (2, "#fef89d", 0, 0 ) ]
    xcenter 312
    yoffset 15

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    vbox:
        if setting_choice == "gakuen":
            style "gakuen_choice_vbox"
        if setting_choice == "fushigi":
            style "fushigi_choice_vbox"
        if setting_choice == "":
            style "fushigi_choice_vbox"
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True
style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style gakuen_choice_vbox:
    xcenter .5
    xfill True
    ymaximum 690
    yoffset 20
style fushigi_choice_vbox:
    xcenter .5
    xfill True
    spacing 100
    yalign .5
style choice_vbox:
    xfill True
    xcenter .5
style choice_button is default:
    xsize 1269
    ysize 144
    hover_sound "audio/system_sounds/hover_button.wav"
    activate_sound "audio/system_sounds/activate_button.wav"
    background "question_choice"
    hover_background "question_hover"
image question_choice  = ConditionSwitch(
    "setting_choice == 'gakuen'","GUI/button/selectbar_idle.png",
    "setting_choice == ''","GUI/button/choice_idle_background.png",
    "setting_choice == 'fushigi'","GUI/button/choice_idle_background.png",
    )
image question_hover = ConditionSwitch(
    "setting_choice == 'gakuen'","GUI/button/selectbar_hover.png",
    "setting_choice == ''","GUI/button/choice_hover_background.png",
    "setting_choice == 'fushigi'","GUI/button/choice_hover_background.png",
    )
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    size 50
    ycenter .5

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('Options')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    hover_sound "audio/system_sounds/hover_button.wav"
    activate_sound "audio/system_sounds/activate_button.wav"

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.
screen navigation():
    if main_menu:
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.96

            spacing gui.navigation_spacing

            textbutton _("Start"):
                action [renpy.run(cockdefine()), Start()]
                hover_sound "audio/system_sounds/hover_button.wav"
                ##this sets up who says the 'presenting!' line
                ## I mispelled 'clock' at one point and kind of just rolled with it
                if dick == 0:
                    activate_sound "audio/new_game/jok_k0004.wav"
                elif dick == 15:
                    activate_sound "audio/new_game/jok_k0004.wav"
                elif dick == 30:
                    activate_sound "audio/new_game/jok_k0004.wav"
                elif dick == 45:
                    activate_sound "audio/new_game/jok_k0004.wav"
                elif cock < 5:
                    activate_sound "audio/new_game/ace_k0001.wav"
                elif cock < 10:
                    activate_sound "audio/new_game/blo_k0001.wav"
                elif cock < 15:
                    activate_sound "audio/new_game/bor_w0033.wav"
                elif cock < 20:
                    activate_sound "audio/new_game/dad_k0002.wav"
                elif cock < 25:
                    activate_sound "audio/new_game/eri_k0001.wav"
                elif cock < 30:
                    activate_sound "audio/new_game/gor_k0001.wav"
                elif cock < 35:
                    activate_sound "audio/new_game/gra_t0131.wav"
                elif cock < 40:
                    activate_sound "audio/new_game/jul_k0001.wav"
                elif cock < 45:
                    activate_sound "audio/new_game/nig_k0001.wav"
                elif cock < 50:
                    activate_sound "audio/new_game/pet_k0001.wav"
                elif cock < 55:
                    activate_sound "audio/new_game/pie_k0001.wav"
                elif cock < 61:
                    activate_sound "audio/new_game/viv_k0001.wav"
            textbutton _("Load"):
                action ShowMenu("load")
                hover_sound "audio/system_sounds/hover_button.wav"
            textbutton _("CG Images"):
                ##action ShowMenu("cg_images")
                hover_sound "audio/system_sounds/hover_button.wav"

            textbutton _("Replay Scene"):
                ##action ShowMenu("replay_scene")
                hover_sound "audio/system_sounds/hover_button.wav"

            textbutton _("Options"):
                action ShowMenu("options")
                hover_sound "audio/system_sounds/hover_button.wav"

            textbutton _("About"):
                action ShowMenu("about")
                hover_sound "audio/system_sounds/hover_button.wav"
    if _in_replay:
            textbutton _("End Replay"):
                action EndReplay(confirm=True)
                hover_sound "audio/system_sounds/hover_button.wav"

style navigation_button_text is gui_button_text
style gam_button:
    hover_sound "audio/system_sounds/hover_button.wav"
    activate_sound "audio/system_sounds/activate_button.wav"
    ypadding 27
    xpadding 25
    size_group "navy"
style gam_button_text:
    idle_outlines [ (2, "#f1ecc2", 0, 0 ) ]
    hover_outlines [ (2, "#fef89d", 0, 0 ) ]
    color "#000000"
    size 30
style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound "audio/system_sounds/hover_button.wav"
    activate_sound "audio/system_sounds/activate_button.wav"


style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    idle_outlines [ (2, "#f1ecc2", 0, 0 ) ]
    hover_outlines [ (2, "#fef89d", 0, 0 ) ]
    color "#000000"


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

screen blanket():
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    add "gui/option_bg.png"
    vbox:
        style_prefix "navy"

        xalign .25
        yalign 0.43
        spacing 10
        textbutton _("Save"):
            action Jump("blert")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("Load"):
            action ShowMenu("load")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("History"):
            action ShowMenu("history")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("Sound Settings"):
            action [ShowMenu("sound_settings"), Hide("options"), Hide("blanket")]
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
    vbox:
        style_prefix "navy"

        xalign .75
        yalign 0.43
        spacing 10
        textbutton _("Voice Settings"):
            ##action ShowMenu("voice_settings")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("Screen Settings"):
            ##action ShowMenu("load")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("Subtitle Settings"):
            ##action ShowMenu("History")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("Default Settings"):
            ##action ShowMenu("sound_settings")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
    textbutton ("Return to Title"):
        action MainMenu()
        hover_sound "audio/system_sounds/hover_button.wav"
        xalign .5 yalign .95
        style "gem_button"
screen options():
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    key "mouseup_3" action Hide("options")
    add "gui/option_bg.png"
    vbox:

        xalign .25
        yalign 0.43
        spacing 10
        textbutton _("Sound Settings"):
            action [ShowMenu("sound_settings"), Hide("options"), Hide("blanket"), Hide("game_menu"), Hide("main_menu")]
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("Voice Settings"):
            ##action ShowMenu("voice_settings")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("Character Settings"):
            ##action ShowMenu("character_settings")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
    vbox:
        style_prefix "navy"

        xalign .75
        yalign 0.43
        spacing 10
        textbutton _("Subtitle Settings"):
            ##action ShowMenu("subtitle_settings")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("Recollection Name"):
            ##action ShowMenu("recollection_name")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
        textbutton _("Revert"):
            ##action ShowMenu("Revert")
            hover_sound "audio/system_sounds/hover_button.wav"
            style "gem_button"
style gem_button:
    hover_sound "audio/system_sounds/hover_button.wav"
    activate_sound "audio/system_sounds/activate_button.wav"
    ypadding 25
    xpadding 20
    size_group "gem"
style gem_button_text:
    idle_outlines [ (2, "#f1ecc2", 0, 0 ) ]
    hover_outlines [ (2, "#fef89d", 0, 0 ) ]
    color "#000000"
    size 25
style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 500
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    tag menu
    add "gui/option_bg.png"
    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    viewport id "vp":
        draggable True
        mousewheel True

        style_prefix "about"
        vbox:
            xalign .2
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            label "To do:"
            text "- Change clock animation"
            text "- Sharpen blurry images"
            text "- Figure out what the other animations mean"
            text "- Make a seperate layer for CG as opposed to just having them be on the 'master' layer?"
            text "- Check characters appear and disappear smoothly"
            text "- Check that the scene transitions match up (at least vaguely) with the original game"
            text "- change 'flash' effect so it's consistent?"
            text "- Change text font to match AnKna translation"
            text "- add CG screen"
            text "- add Replay Scene screen"
            text "- add voice settings screen"
            text "- Figure out how to change volume of system sounds"
            text "- add subtitle settings screen"
            text "- add recollection name screen"
            text "- add \"revert\" option"
            text "- replace japanese text on ImageButtons"
            text "- check game runs smoothly"
            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text:
    color "#ffffff"
    size 20
    outlines [ (3, "#000000", 0, 0 ) ]
style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
style slot_button:
    idle_background "slot_idle_background"
    hover_background "slot_hover_background"
image slot_hover_background = ConditionSwitch(
    "setting_choice == 'gakuen'","GUI/button/save_play_par.png",
    "setting_choice == ''","GUI/button/save_play_gen.png",
    "setting_choice == 'fushigi'","GUI/button/save_play_gen.png",
    )
image slot_idle_background  = ConditionSwitch(
    "setting_choice == 'gakuen'","GUI/button/save_empty_par.png",
    "setting_choice == ''","GUI/button/save_empty_gen.png",
    "setting_choice == 'fushigi'","GUI/button/save_empty_gen.png",
    )
style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen Options():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    ## Avoid predicting this screen, as it can be very large.
    predict False
    add "gui/history_screen.png"
    viewport id "vp":
        draggable True
        mousewheel True

        vbox:
            xalign .25
            yalign .1
            for h in _history_list:
                if h.who:
                    label h.who:
                        style "history_name"
                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                text h.what

            if not _history_list:
                label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xalign .25
    xmaximum 500
    yalign .1
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill False

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600

image cat  = ConditionSwitch(
    "setting_choice == 'gakuen'","GUI/Linebreak2.png",
    "setting_choice == ''","GUI/Linebreak.png",
    "setting_choice == 'fushigi'","GUI/Linebreak.png",
    )
image ctc_blink:
    "cat"
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat
screen codex():

    tag menu

    use game_menu(_("Codex"), scroll="viewport"):

        style_prefix "codex"

        has vbox:
            spacing 20

        text _("{b}Mechanical Engineering:{/b} Where we learn to build things like missiles and bombs.")

        text _("{b}Civil Engineering:{/b} Where we learn to build targets.")

screen voice_settings():
    add "gui/option_bg.png"
    add "gui/overlay/sound_settings_header.png":
        xalign .5
        yalign .22
screen character_settings():
    add "gui/option_bg.png"
    add "gui/overlay/sound_settings_header.png":
        xalign .5
        yalign .22
screen sound_settings():
    tag sound_settings
    style_prefix "sound_settings"
    add "gui/option_bg.png"
    add "gui/overlay/sound_settings_header.png":
        xalign .5
        yalign .22
    add "gui/overlay/sound_settings_back_hover.png":
        xalign .5
        yalign .83
    vbox:
        yalign .7
        xalign .5
        spacing 40
        hbox:
            spacing 20
            text "System":
                yalign .1
                style "sound_setting_info"
            imagebutton auto "gui/button/0_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", 0), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/1_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", .2), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/2_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", .4), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/3_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", .6), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/4_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", .8), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/5_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", 1), ShowMenu("sound_settings")]
        hbox:
            spacing 20
            text "BGM":
                yalign .1
                style "sound_setting_info"
            imagebutton auto "gui/button/0_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("music", 0), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/1_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("music", .2), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/2_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("music", .4), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/3_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("music", .6), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/4_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("music", .8), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/5_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("music", 1), ShowMenu("sound_settings")]
        hbox:
            spacing 20
            text "Sound Effects":
                yalign .1
                style "sound_setting_info"
            imagebutton auto "gui/button/0_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", 0), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/1_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", .2), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/2_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", .4), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/3_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", .6), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/4_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", .8), ShowMenu("sound_settings")]
            imagebutton auto "gui/button/5_%s.png":
                hover_sound "audio/system_sounds/hover_button.wav"
                activate_sound "audio/system_sounds/activate_button.wav"
                action [preferences.set_volume("sfx", 1), ShowMenu("sound_settings")]
style sound_setting_info:
    size_group "sound_setting"
    yalign 0
    size 30
