label mode_choice:
hide screen setting_choice_screen
play music lovecheck2_ali fadein 1
$ rec_points = 0
scene bg_par01_ai_day with fade
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_1")
T " Ｑ１\n
Which type of book is better?"
$ hi_mes()
menu:
  "Ａ１ A helpful, practical instruction manual.":
    jump choice_Q1a
  "Ａ２ A high-fantasy adventure novel." :
    jump choice_Q1b

label choice_Q1a:
$ rec_points += 1

show go_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_k0000
Gowland " 「まあ、あんたらしいっちゃらしいが……。\n
たまには、息抜きに現実離れした話も悪くねえだろ？」"
play sound se_0284
jump choice_Q2

label choice_Q1b:

show ace_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice ace_k0000
Ace " 「はは、なんだ！君もやっぱり旅が好きなんじゃないか。\n
うんうん、照れなくてもいいんだぜ？俺と行こう！」"

hide ace_t_02_4 at center

play sound se_0284
jump choice_Q2

label choice_Q2:
scene al_01 with grad_l_short
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_03_7")
T " Ｑ２\n
「庭で転寝していたら、ウサギに呼ばれたんだけど……」"
$ hi_mes()
menu:
  "Ａ１「追いかけてみる」":
    jump choice_Q2a
  "Ａ２「ダメダメ、目を覚ますのよ」":
    jump choice_Q2b
label choice_Q2a:

show pia_t_03_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pie_k0000
Pierce " 「ウサちゃんって、可愛いよね！ちゅうしたいな！！\n
あっ！君にもちゅうしていい？ちゅう、ちゅう！！！」"

hide pia_t_03_6 at center

play sound se_0623
jump choice_Q3
label choice_Q2b:
$ rec_points += 1

show bor_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice bor_k0000
Boris " 「ウサギなんか追いかけてないで、猫と遊んでよ。\n
寂しさで参っちゃうのは、ウサギだけじゃないんだぜ？」"

hide bor_t_02_8 at center
with dis
play sound se_0623
jump choice_Q3
label choice_Q3:
scene s2_01 with grad_l_short
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_04_14")
T " Ｑ３\n「恋愛と勉強、今の自分にはどっちが重要？」"
$ hi_mes()
menu:
  "Ａ１「どちらも全力投球！」":
    jump choice_Q3a
  "Ａ２「勉強は苦手だな…」":
    jump choice_Q3b

label choice_Q3a:
$ rec_points += 1

show yuri_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jul_k0000
Julius " 「なんて暑苦しい……他所でやれ、他所で。\n
私を巻き込むな……って、引っ張るな！おいっ！？」"


play sound se_0339
jump choice_Q4
label choice_Q3b:

show eri_t_03b_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice eri_k0000
Elliot " 「だよな～。俺もあんたの気持ち痛いほどよくわかるぜ。\n
俺も、細かい計算みたいなのは得意じゃねえよ～、はあ～」"
$ hi_mes()
play sound se_0339
jump choice_Q4
label choice_Q4:

scene yume01 with grad_l_short

$ show_mes("frame_gen_heroine")
$ face ("ali_t_02_15")
T " Ｑ４\n
「時間は曖昧で、無意味なもの？」"
$ hi_mes()
menu:
  "Ａ１「そうかもしれない」" :
    jump choice_Q4a
  "Ａ２「規則正しい生活をしたい」":
    jump choice_Q4b

label choice_Q4a:
$ hi_mes()
$ show_mes("frame_gen_chara")
show bra_t_02_18 at center
with dis
voice blo_k0000
Blood " 「ふむ、やはりお嬢さんもそう思うだろう？\n
そんなものに縛られるのは御免だ。煩わしいことこの上ない」"

hide bra_t_02_18 at center

play sound se_0338
jump choice_Q5
label choice_Q4b:
$ hi_mes()
$ show_mes("frame_gen_chara")
show gre_t_02_1 at center
with dis
voice gra_k0000
Gray " 「俺も同感だ。\n
是非、ナイトメア様にも見習っていただきたい発言だな」"

hide gre_t_02_1 at center

play sound se_0338
jump choice_Q5
label choice_Q5:
scene bg_gen_sky_all_day with grad_l_short
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_06_15")
T " Ｑ５\n
「学校を選ぶなら」"
$ hi_mes()
menu:
  "Ａ１「家から通えるところがいいわね」":
    jump choice_Q5a
  "Ａ２「全寮制の学校に行きたいわね」":
    jump choice_Q5b

label choice_Q5a:

$ hi_mes()
$ show_mes("frame_gen_chara")
show nai_s_02_3 at center
with dis
voice nig_k0000
Nightmare " 「私も賛成だ。近ければ近いほどいい。\n
……いや、むしろ家から出ないですませたい！いやいっそ、引きこもろうじゃないか！」"

hide nai_s_02_3 at center
with dis
play sound se_0600
jump choice_Q6
label choice_Q5b:
$ rec_points += 1
play sound se_0084

$ hi_mes()
$ show_mes("frame_gen_chara")
show dee_t_02_4 at center
with dis
voice dad_k0000
Dee " 「昼も夜も同じ場所で生活するってことだね。\n
お姉さんと同室になるように管理者にお願いしに行こうよ、兄弟」"

play sound se_0084
hide dee_t_02_4 at center
$ hi_mes()
$ show_mes("frame_gen_chara")
show dee_t_02_4 at left
show dam_t_02_5 at right
with dis
voice dad_k0001
Dam " 「それはいい考えだね、兄弟。\n
お姉さんと、ずっと一緒にいられるようにお願いしに行こうよ」"

hide dee_t_02_4 at left

hide dam_t_02_5 at right
with dis
play sound se_0600
jump choice_Q6
label choice_Q6:
scene al_01 with grad_l_short
scene al_01_s with grad_l_short
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face ("ali_t_01_5")
T " Ｑ６\n
「私に幼馴染は……」"
$ hi_mes()
menu:
  "Ａ１「あれ？いたような気がする」" :
    jump choice_Q6a
  "Ａ２「そんな人はいません」" :
    jump choice_Q6b

label choice_Q6a:
$ rec_points += 1
$ hi_mes()
$ show_mes("frame_gen_chara")
show viv_t_01_2 at center
with dis
voice viv_k0000
Vivaldi " 「あんなウサギ男が幼馴染とは、不憫な子。\n
……でも、安心するが良い。わらわがおまえを守ってやろう」"

hide viv_t_01_2 at center
with dis
play sound se_0283
jump choice_result
label choice_Q6b:

show per_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_k0000
Peter " 「そんな！！……いーえ、それでもいいんです。それもあなたの {size=+20}愛！{/size}」"

hide per_t_03_11 at center
show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_k0000_5
Peter " 「僕は、ずっとあなたを！あなただけを見ていますよ！」"

hide per_t_02_13 at center
with dis
play sound se_0283


jump choice_result
label choice_result:

scene bg_gen17_cst_k with Fade(0.5, 0.5, 0.5)
pause 0.5

show jo_k_02_2 at center
with dis
pause 1.2
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_k0000
Black_Joker " 「遅せーよ、何ちんたらしてやがったんだ？\n
俺様を待たせるたあ、いい度胸してんじゃねえか」"

show bg_gen17_cst_a behind jo_k_02_2 with dis
pause 1.2
hide jo_k_02_2 at center
with dis
show jo_k_02_14 at left
show jo_t_03_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jok_k0001
White_Joker " 「もう、ジョーカー。せっかくここまで来てくれたこの子に失礼だろ？\n
判定を聞きにきたんだよね。そうだなあ……」"
$ hi_mes()
hide jo_k_02_14 at left
hide jo_t_03_4 at right
with dis

if rec_points >= 3:
  jump mode_choice_gauken
else:
  jump mode_choice_fushigi

label mode_choice_fushigi:
play sound se_0173
scene white
pause .5
scene map_bg_joker_day with ImageDissolve("gui/grad_t.png", 2, ramplen=128, reverse=True)
show jo_k_02_8 at center
$ show_mes("frame_gen_chara")
voice jok_k0003
Black_Joker "「ああ？判定するまでもなく、原作に決まってんだろうが。\n
この俺様を待たせたんだ。たっぷり遊んでやるよ」"
play sound se_0199
hide jo_k_02_8
$ hi_mes()
pause 1
play sound se_0272
$ rec_points = 0
pause 1.5
stop music fadeout 1
jump setting_choice

label mode_choice_gauken:

play sound se_0173
scene white with Fade(.5, .5, .5, color="#ffffff")
scene bg_map_day with ImageDissolve("gui/grad_b.png", 2, ramplen=128, reverse=True)
pause .2
show jo_t_03_7 at center
$ show_mes("frame_gen_chara")
voice jok_k0002
White_Joker "「たまには違うことをしてみるのもいいと思うよ。\n
君なら魔法学校もきっと楽しめる。さあ、行っておいで」"
$ hi_mes()
play sound se_0199
hide jo_t_03_7
$ hi_mes()
pause 1
play sound se_0272
$ rec_points = 0
pause 1.5
stop music fadeout 1
jump setting_choice
