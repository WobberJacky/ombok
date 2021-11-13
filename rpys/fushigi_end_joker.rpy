label fushigi_end_joker:
scene map_bg_joker_day
with dis
$ clockanim()


scene md_01
with dis
play sound se_0562 volume .1

play music forest2_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大荷物を運んできた子供達は荷台に載せると団長を振り返った。"

show j-boy_a_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0041
Danin "「ジョーカー、大きな荷物はこれで最後みたい」"

hide j-boy_a_3
show j-boy_a_3 at left
show j-girl_a_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0037
W "「テントも畳んだし、あとはこれを積めばおしまいよ」"

hide j-boy_a_3
show jo_t_03_14 at center
hide j-girl_a_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0306
White_Joker "「うん、ご苦労様。\n
いやあ、思ったよりも早く片付いたな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「本当よね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "最後の公演でもあれだけボールや機材を使っていたはずなのに、今回の撤収作業は嘘のように早かった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（あれだけの時間帯、ずっと片付けていたのに……。\n
どうして、今回はこんなに早かったのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界の時間の流れが滅茶苦茶でも、理不尽だと思う程度には大きな差があるように思ったのだが、そう感じているのは私だけらしい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0307
Mask "「あー、やっと、しまいだ、しまい。\n
せいせいするぜ」"

hide jo_t_03_14
show jo_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0308
White_Joker "「ふふふ。お疲れ様、[firstname]。\n
君も手伝ってくれてありがとう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「いいわよ。\n
お世話になったのは私だもの」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T "（そういえば……。\n
どうやって、移動するつもりかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らの荷物の多くは車に乗せられている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まさかこれらを引きずりながら移動していくわけではないだろうが……。"

hide jo_t_01_5
show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0309
White_Joker "「じゃあ、忘れ物もなさそうだし……。\n
開けようか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言って、ジョーカーが近付いたのは、森の中にある一つのドア。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（ああ、なるほど。\n
ここにはドアがあったわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その人が一番望む場所、あるいはその人にとって最良の場所。\n
ここのドアは、勝手に目的地へと繋げてくれる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ドア……、か）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ジョーカーは迷うことなく、ドアノブに手を伸ばす。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "未だに私には開ける勇気も、ノブに触れようと思う気持ちもわかないのに。\n
ジョーカーだとこんなに簡単。"

play sound se_0285

show door7 onlayer master
with dis
hide jo_t_03_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0310
White_Joker "「はい、次の場所はここだよ。\n
荷物を運ぶとしよう」"

play sound se_0468
pause .5
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice mat_f0042
Danin "「うん、分かったよ」"

play sound se_0047
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice nos_f0038
W "「落とさないように気を付けなくちゃね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どういう仕掛けになっているのか、車は子供達が乗り込むと同時にゆっくりとドアのほうへと移動していく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一台、また一台。\n
まるで隊列を組むように、自分から進んでいく。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T "（おもちゃの車みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見えないレールに従うように車はドアを抜ける。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（消えていく）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ドアを抜けた先は、私にはよく見えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "明るすぎて見えないのか。\n
それとも、暗すぎて届かないのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも分からない。"

hide door7
show t_jo_end1 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
White_Joker "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ジョーカー」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先ほどまで団員達を指揮していた男はいつのまにか、私の真横に立っていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "箱のような帽子を外して、一礼してくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0311
White_Joker "「ねえ、[firstname]。\n
今度のサーカスは楽しめたかな？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0312
White_Joker "「エイプリル・シーズンのサーカスは、今ひとつ楽しめなかったようだからね。\n
今回はどうだった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（楽しかった？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かめるような言葉が、まるで私の中から聞こえてくるようだった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「楽しかったわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T "「今回のサーカスだけじゃないわ。\n
あなたのサーカスは、いつも、とても楽しかった」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "色とりどりの闇色のサーカス。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "光だけではなく、あの闇も混じった世界は、遠くから見つめるだけでは終われない魅力があった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の答えは、ジョーカーにとっても満足いくものだったらしい。\n
満面の笑みが返ってきた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0313
White_Joker "「それはよかった。\n
君も一緒に行くんだし、その楽しさを知っておいてもらうに越したことはないからね」"

hide t_jo_end1
show door7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_8")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（一緒に行く？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（誰が？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何度か彼にサーカスへ誘われたことは事実だが、私は一度も承諾していない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何よりも、私には帰る家がある。"

hide door7 with Dissolve(2)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「何で、そんな話になっているのよ。\n
私はサーカスについていくなんて、そんなこと……」"


show jo_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice jok_f0314
Black_Joker "「俺は反対だぜ。\n
こんな鈍くさいのを連れていくなんて、冗談じゃねえ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（よく出てくるわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラックさんは、ぶすっとした顔で現れると、犬でも追い払うように私に向かって手を振る。"

hide jo_t_02_8
show jo_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0315
Black_Joker "「ほら、とっとと帰れよ」"

hide jo_t_03_10
show jo_t_03_10 at left
show jo_t_01_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0316
White_Joker "「ジョーカーは素直じゃないなあ。\n
俺は彼女に来てほしいと思っているんだから、君だって同じだろうに」"

hide jo_t_01_1
show jo_t_03_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
White_Joker "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言葉を一度切って、ジョーカーは私の名を呼んだ。\n
見上げる先には、二つの顔。"

hide jo_t_03_14
show jo_t_03_15 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0317
White_Joker "「君が君の居場所を出てきてから、もうそれなりの間ここで過ごしてきたのは事実だろう。\n
もう少し、延長してみる気はない？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（延長なんて、そんなこと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然の提案に私は息を飲む。"

hide jo_t_03_10
show j-boy_a_2 at center
hide jo_t_03_15
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice mat_f0043
Danin "「そうだよ、一緒に行こうよ。\n
もっと楽しいことがあるよ」"

hide j-boy_a_2
show j-boy_a_2 at left
show j-girl_a_14 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice nos_f0039
W "「あなたにとっていい場所よ。\n
もう少しだけならいいじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "熱心に口説こうとする子供達の声にエコーがかかって聞こえた気がした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（何か、これって……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何度も何度も聞いた、あの声を思い出す。"

hide j-boy_a_2

hide j-girl_a_14

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sat_f0010
T "「開けて」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0039
T "「扉を開けて、別の世界に行こう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（ドアは今、何も言っていないはずなのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供達の声が、ドアの声に重なる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、ドアと子供達との決定的な違いが一つある。\n
ドアは囁くだけで、手を伸ばして引き込むことはないが、彼らは違う。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "現に彼らは両手を引っ張って、私を連れて行こうとする。"


show j-boy_a_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Danin "「[firstname]」"

hide j-boy_a_3
show j-boy_a_3 at left
show j-girl_a_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
W "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（この子達に引き込まれてしまいそう）"

hide j-boy_a_3
show jo_t_03_14 at center
hide j-girl_a_3
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jok_f0318
White_Joker "「ずっとじゃないさ。\n
一時的なものだよ、いつでも戻れる」"

hide jo_t_03_14
show jo_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice jok_f0319
White_Joker "「君さえ望めば、いつでもどんな場所にでも戻れる。\n
俺達が行こうとしているのは、そういう場所だ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつの間にか私の背後に回ったホワイトさんが、耳元で囁いてくる。"

hide jo_t_03_7
show jo_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jok_f0320
White_Joker "「一緒に行こう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

label fushigi_end_read_white:
if renpy.seen_label("fushigi_end_read_white") == True:
  jump fushigi_end_root_blood
else:
  jump fushigi_end_joker_black


label fushigi_end_read_black:
if renpy.seen_label("fushigi_end_read_black") == True:
  jump fushigi_end_root_blood
else:
  jump fushigi_end_joker_nochoice


label fushigi_end_root_blood:
if renpy.seen_label("fushigi_end_root_blood") == True:
  jump fushigi_end_read_blood_j
else:
  jump fushigi_end_read_other1

label fushigi_end_read_blood_j:
if renpy.seen_label("fushigi_end_root_blood") == True:
  jump fushigi_end_read_hatter
else:
  jump fushigi_end_joker_nochoice

label fushigi_end_read_hatter:
if renpy.seen_label("fushigi_end_elliot") == True:
  if renpy.seen_label("fushigi_end_dad") == True:
    jump fushigi_end_read_other1
else:
  jump fushigi_end_read_other2

label fushigi_end_read_other1:
if renpy.seen_label("fushigi_end_peter") == True:
  if renpy.seen_label("fushigi_end_boris") == True:
    if renpy.seen_label("fushigi_end_nightmare") == True:
      jump fushigi_end_bad_hatter_recheck
else:
  jump fushigi_end_joker_badchoice

label fushigi_end_bad_hatter_recheck:
  if renpy.seen_label("fushigi_end_bad_hatter_recheck") == True:
    jump fushigi_end_joker_allchoice
  else:
    jump fushigi_end_joker_homechoice

label fushigi_end_read_other2:
  if renpy.seen_label("fushigi_end_peter") == True:
    if renpy.seen_label("fushigi_end_boris") == True:
      if renpy.seen_label("fushigi_end_nightmare") == True:
        jump fushigi_end_joker_homechoice
  else:
    jump fushigi_end_joker_nochoice

label fushigi_end_joker_allchoice:
menu:
  "行っても、いいの？":
    jump fushigi_end_joker_nochoice_2
  "うちに帰らなくちゃ。":
    jump fushigi_end_home1
  "そうね……、少しだけなら。":
    jump fushigi_end_bad_hatter1
label fushigi_end_joker_badchoice:
menu:
  "行っても、いいの？":
    jump fushigi_end_joker_nochoice_2
  "そうね……、少しだけなら。":
    jump fushigi_end_bad_hatter1

label fushigi_end_joker_homechoice:
menu:
  "行っても、いいの？":
    jump fushigi_end_joker_nochoice_2
  "うちに帰らなくちゃ。":
    jump fushigi_end_home1
label fushigi_end_joker_nochoice:
label fushigi_end_joker_nochoice_2:
    if fushigi_joker4_2b_seen == True:
        jump fushigi_end_joker_white
    else:
        jump fushigi_end_joker_black
