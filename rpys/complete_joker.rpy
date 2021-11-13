label complete_joker:
scene bg_gen17_cst_a
play music circus_a_ali
show jo_t_01_5 at center
$ show_mes("frame_gen_chara")
voice jok_k0006
White_Joker "「コンプリートおめでとう。\n
ふふ、無事にコンプリート出来たみたいだね」"
hide jo_t_01_5 at center
show jo_t_01_5 at left
show jo_t_03_19 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_k0007
Black_Joker "「おまえ、途中でへばっていただろ？\n
もう、ここまで来ねえのかと思ったぜ」"
hide jo_t_01_5 at left
show jo_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_k0008
White_Joker "「あれ、ジョーカーとしては、もう会わないことを願っていたんじゃないの？\n
そんなことも言っていただろう？」"
hide jo_t_03_19 at right
show jo_t_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_k0009
Black_Joker "「……っけ、覗き見してんじゃねえよ、ジョーカー。\n
こいつはここまで来た、自分の意志でな……」"
hide jo_t_01_3 at left
show jo_t_03_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_k0010
White_Joker "「そうだね、願うも何も、俺達の意志は関係ないか……。\n
ふふ、君は自分でおもちゃ箱を開いたんだ、俺達が望む望まざるに関わらずにね」"
hide jo_t_02_2 at right
show jo_t_02_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
"「…………」"
hide jo_t_03_7 at left
show jo_t_01_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_k0011
White_Joker "「連れて行ってあげるよ。\n
君なら最高の道化になれる」"
play sound se_0173
hide jo_t_01_3 at left
hide jo_t_02_14 at right
with Dissolve(1.3)
stop music fadeout 5.0
scene bg_gen17_cst_k
with Dissolve(1.3)
$ hi_mes()
with Dissolve(1.6)
pause 1.3
hide bg_gen17_cst_k
with Dissolve(1.3)
play music jail_p_ali fadein 5.0
pause 1.3
scene pri
with Dissolve (2.5)
pause 1.3
show jo_k_02_8 at center
with dis
$ show_mes("frame_gen_chara")
with dis
voice jok_k0012
Black_Joker "「……おまえが望むなら、捕まえてやる。\n
おまえは俺の囚人だからな」"
pause 1.6
# return
