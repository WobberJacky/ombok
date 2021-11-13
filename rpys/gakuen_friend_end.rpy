label gakuen_friend_end:
if place_of_stay == "Castle":
    jump gakuen_friend_end_castle0
if place_of_stay == "Hatter":
    jump gakuen_friend_end_hatter0
if place_of_stay == "Amuse":
    jump gakuen_friend_end_amuse0
if place_of_stay == "Tower":
    jump gakuen_friend_end_tower0
label gakuen_friend_end_castle0:
with dis
$ hi_mes()

scene bg_map_eve
with stripe_l_medium

scene bg_par15_rg_ros_eve
with stripe_l_medium
jump gakuen_friend_end0
label gakuen_friend_end_hatter0:
with dis
$ hi_mes()

scene bg_map_eve
with stripe_l_medium

scene bg_par15_rg_hat_eve
with stripe_l_medium
jump gakuen_friend_end0
label gakuen_friend_end_amuse0:
with dis
$ hi_mes()

scene bg_map_eve
with stripe_l_medium

scene bg_par15_rg_amu_eve
with stripe_l_medium
jump gakuen_friend_end0
label gakuen_friend_end_tower0:
with dis
$ hi_mes()

scene bg_map_eve
with stripe_l_medium

scene bg_par15_rg_tow_eve
with stripe_l_medium
jump gakuen_friend_end0
label gakuen_friend_end0:

scene bg06_sk_h_eve
with dis

play music evening_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "書類を届けにいっただけのはずなのに、結構な長居をしてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（……楽しかったな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いろいろトラブルもあったが、そういったことも全部ひっくるめて楽しかった。\n
帰る頃になると、なんだか少し寂しい気までしてしまったぐらいだ。"


scene bg25_rr_eve
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一抹の名残惜しさを振り切って、夕焼けの差す道を歩き、自寮を目指す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そしてエントランスをくぐって、自室へと向かおうとしたところで声をかけられた。"


show girl_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0018
Seito "「あ、おかえりなさい。\n
今日は、遅くまで外にいたのね」"

hide girl_a2_3
show girl_a2_3 at left
with dis

show girl_b1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0125
Seito "「おかえり、[firstname]。\n
図書館の帰り？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たまたまそこにいた女子生徒二人に、「おかえりなさい」と迎えられて驚いた。\n
いや、驚いたというのはおかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までにももう何度も、同じ会話を交わしている。\n
私だって、当たり前のように挨拶を返していたはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それがあんまりにも自然だったもので、今まで意識していなかっただけ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういった挨拶が当たり前のように馴染んでいるということに、改めて気付かされた。"

if place_of_stay == "Castle":
    jump gakuen_friend_end_castle1
if place_of_stay == "Hatter":
    jump gakuen_friend_end_hatter1
if place_of_stay == "Amuse":
    jump gakuen_friend_end_amuse1
if place_of_stay == "Tower":
    jump gakuen_friend_end_tower1
label gakuen_friend_end_castle1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ただいま。\n
今日は図書館じゃなくて、ビバルディに頼まれてちょっとお遣いに行っていたのよ」"

hide girl_a2_3
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice may_g0019
Seito "「寮長に……？\n
気に入られているみたいだけど、大変ね」"

hide girl_a2_1
show girl_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice may_g0021
Seito "「それでこんなに遅くなるなんて、大変なお遣いだったの？\n
お疲れ様」"

hide girl_b1_8
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice tak_g0126
Seito "「お疲れ様！\n
夕食の時間までに帰ってこられてよかったわね」"
if gakuen_friend_castle_seen == True:
    jump gakuen_friend_end_go_castle1
if gakuen_friend_hatter_seen== True:
    jump gakuen_friend_end_go_hatter1
if gakuen_friend_amuse_seen == True:
    jump gakuen_friend_end_go_amuse1
if gakuen_friend_tower_seen == True:
    jump gakuen_friend_end_go_tower1
label gakuen_friend_end_hatter1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ただいま。\n
今日は図書館じゃなくて、ブラッドに頼まれてちょっとお遣いに行っていたのよ」"

hide girl_a2_8
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice may_g0019
Seito "「寮長に……？\n
気に入られているみたいだけど、大変ね」"

hide girl_a2_1
show girl_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice may_g0021
Seito "「それでこんなに遅くなるなんて、大変なお遣いだったの？\n
お疲れ様」"

hide girl_b1_3
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice tak_g0126
Seito "「お疲れ様！\n
夕食の時間までに帰ってこられてよかったわね」"
if gakuen_friend_castle_seen == True:
    jump gakuen_friend_end_go_castle1
if gakuen_friend_hatter_seen== True:
    jump gakuen_friend_end_go_hatter1
if gakuen_friend_amuse_seen == True:
    jump gakuen_friend_end_go_amuse1
if gakuen_friend_tower_seen == True:
    jump gakuen_friend_end_go_tower1
label gakuen_friend_end_amuse1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ただいま。\n
今日は図書館じゃなくて、ゴーランドに頼まれてちょっとお遣いに行っていたのよ」"

hide girl_a2_8
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice may_g0020
Seito "「ゴーランド先生に……？\n
気に入られているみたいだけど、大変ね」"

hide girl_a2_1
show girl_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice may_g0021
Seito "「それでこんなに遅くなるなんて、大変なお遣いだったの？\n
お疲れ様」"

hide girl_b1_3
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice tak_g0126
Seito "「お疲れ様！\n
夕食の時間までに帰ってこられてよかったわね」"
if gakuen_friend_castle_seen == True:
    jump gakuen_friend_end_go_castle1
if gakuen_friend_hatter_seen== True:
    jump gakuen_friend_end_go_hatter1
if gakuen_friend_amuse_seen == True:
    jump gakuen_friend_end_go_amuse1
if gakuen_friend_tower_seen == True:
    jump gakuen_friend_end_go_tower1
label gakuen_friend_end_tower1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ただいま。\n
今日は図書館じゃなくて、ユリウスに頼まれてちょっとお遣いに行っていたのよ」"

hide girl_a2_8
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice may_g0019
Seito "「寮長に……？\n
気に入られているみたいだけど、大変ね」"

hide girl_a2_1
show girl_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice may_g0021
Seito "「それでこんなに遅くなるなんて、大変なお遣いだったの？\n
お疲れ様」"

hide girl_b1_3
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice tak_g0126
Seito "「お疲れ様！\n
夕食の時間までに帰ってこられてよかったわね」"
if gakuen_friend_castle_seen == True:
    jump gakuen_friend_end_go_castle1
if gakuen_friend_hatter_seen== True:
    jump gakuen_friend_end_go_hatter1
if gakuen_friend_amuse_seen == True:
    jump gakuen_friend_end_go_amuse1
if gakuen_friend_tower_seen == True:
    jump gakuen_friend_end_go_tower1
label gakuen_friend_end_go_castle1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「お遣いの内容自体は、書類を届けるだけだったんだけどね。\n
行き先が赤薔薇寮の自治会室だったのよ」"

hide girl_a2_8
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice may_g0022
Seito "「ああ……。\n
あそこの副寮長、あなたに対してすごいらしいものね……」"

hide girl_b1_3
show girl_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice tak_g0127
Seito "「幼馴染って、皆あんな感じなの？\n
私、幼馴染とかいないからよく分からないんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達も、私に対してのペーターのストーカーぶりについては見聞きしているらしい。"

hide girl_a2_1
show girl_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0023
Seito "「あなたがいないときの様子を知っているだけに、ギャップが……」"

hide girl_b1_9
show girl_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0128
Seito "「ええ、変な感じよね……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……普段、どんな感じなのかしら）"

hide girl_a2_5
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice may_g0024
Seito "「無理矢理、引き止められたりはしなかった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ああ、それは大丈夫」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターは私に構いたがるが、乱暴なことはしない。\n
その点だけは誤解してほしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「いろいろあったけど、美味しい紅茶を振る舞ってもらったし……、そうね、楽しかったって言えるんじゃないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからこそ、帰り際に名残惜しさを覚えたのだ。\n
けれど今、その気持ちはもうない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達が言ってくれた「おかえりなさい」の言葉に、そんな気持ちはすっかりなくなってしまった。"
if place_of_stay == "Castle":
    jump gakuen_friend_end_castle2
if place_of_stay == "Hatter":
    jump gakuen_friend_end_hatter2
if place_of_stay == "Amuse":
    jump gakuen_friend_end_amuse2
if place_of_stay == "Tower":
    jump gakuen_friend_end_tower2
label gakuen_friend_end_go_hatter1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「お遣い自体は書類を届けるだけの簡単な内容だったんだけどね？\n
宛先が……、帽子屋寮寮長のブラッド宛だったのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「それで、内容が、双子とエリオットについての苦情だったりしたものだから……。\n
もう、分かるでしょう？」"

hide girl_a2_1
show girl_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
Seito "「…………」"

hide girl_b1_5
show girl_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
Seito "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、察してくれたらしい。\n
そっと気の毒そうな顔で目を伏せている。"

hide girl_a2_9
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0025
Seito "「それは本当に……、お疲れ様ね。\n
それで大丈夫だったの？」"

hide girl_b1_9
show girl_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0129
Seito "「帽子屋寮ってほら、いろいろ危ない噂もあるじゃない？\n
そんな知らせを運んで……、あなた自身は危ない目にあわなかった？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ああ、それは大丈夫」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは、無意味に乱暴なことはしない。\n
その点だけは誤解してほしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「いろいろあったけど、美味しい紅茶を振る舞ってもらったし……、そうね、楽しかったって言えるんじゃないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからこそ、帰り際に名残惜しさを覚えたのだ。\n
けれど今、その気持ちはもうない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達が言ってくれた「おかえりなさい」の言葉に、そんな気持ちはすっかりなくなってしまった。"
if place_of_stay == "Castle":
    jump gakuen_friend_end_castle2
if place_of_stay == "Hatter":
    jump gakuen_friend_end_hatter2
if place_of_stay == "Amuse":
    jump gakuen_friend_end_amuse2
if place_of_stay == "Tower":
    jump gakuen_friend_end_tower2
label gakuen_friend_end_go_amuse1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「お遣い自体は書類を届けるだけの簡単な内容だったんだけどね？\n
宛先が……、遊園地寮の代表者だったのよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「そこで、道案内をピアスに頼んじゃったものだから……。\n
もう遊園地寮の罠に片っ端からひっかかっちゃって」"

hide girl_a2_1
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice may_g0026
Seito "「そ、それは災難だったわね……。\n
私も、遊園地寮のトラップについては聞いたことあるわ」"

hide girl_b1_1
show girl_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice tak_g0130
Seito "「私は実際に体験したことがあるわ……。\n
遊園地寮にいる友達のところに遊びにいったときにね、酷い目にあったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんと、彼女達の一人は、経験者だったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人して遊園地寮のトラップについてを思い巡らせているのか、うんうんと頷きあっている。"

hide girl_a2_1
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0027
Seito "「よく無事に帰ってこられたわよね……。\n
怪我しなかった？」"

hide girl_b1_1
show girl_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0131
Seito "「トラップの中には、結構危ないものもあったでしょう？\n
ちゃんとボリスやゴーランド先生には会えたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「どうにかこうにか、ね。\n
最終的には、遊園地寮のカフェテリアでいろいろご馳走になってきちゃった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "災難ではあったが、嫌だったわけではない。\n
その点だけは誤解してほしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「いろいろあったけど……、楽しかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからこそ、帰り際に名残惜しさを覚えたのだ。\n
けれど今、その気持ちはもうない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達が言ってくれた「おかえりなさい」の言葉に、そんな気持ちはすっかりなくなってしまった。"
if place_of_stay == "Castle":
    jump gakuen_friend_end_castle2
if place_of_stay == "Hatter":
    jump gakuen_friend_end_hatter2
if place_of_stay == "Amuse":
    jump gakuen_friend_end_amuse2
if place_of_stay == "Tower":
    jump gakuen_friend_end_tower2
label gakuen_friend_end_go_tower1:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「お遣い自体は書類を届けるだけの簡単な内容だったのよ。\n
宛先だって、塔のユリウス宛だったし」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「だけど……、途中でナイトメアの脱走と捕獲劇に巻き込まれちゃって。\n
捕まっても仕事はしたくないって駄々こねるしで大変だったの」"

hide girl_a2_1
show girl_a2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice may_g0028
Seito "「まあ、もうあれは塔の名物みたいなものだしねえ。\n
グレイ執務長がいつも頑張っているのを見かけるわ」"

hide girl_b1_1
show girl_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice tak_g0132
Seito "「どうしてあんなに、仕事を嫌がるのかしらね。\n
書類に目を通して、サインをするだけでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その「書類に目を通してサインをするだけ」の仕事をしてもらえないから、グレイは困り果てているのだ。それに気付いて、私達三人の視線が泳いだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアに入学できるくらいだから、生徒は基本真面目な者が多い。\n
ナイトメアのさぼり癖は、理解できないものがある。"

hide girl_a2_9
show girl_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0029
Seito "「そ、それはともかく。\n
ナイトメア先生は無事に捕まったの？」"

hide girl_b1_9
show girl_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0133
Seito "「ユリウス風紀委員長に書類を届けるだけならすぐだろうけど……。\n
結局、最後まで付き合っちゃったんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「ええ、そうなのよ。\n
捕獲どころか、その後のコーヒーブレイクにまで付き合っちゃったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「いろいろあったけど、ちゃっかり楽しんできちゃった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だからこそ、帰り際に名残惜しさを覚えたのだ。\n
けれど今、その気持ちはもうない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達が言ってくれた「おかえりなさい」の言葉に、そんな気持ちはすっかりなくなってしまった。"
if place_of_stay == "Castle":
    jump gakuen_friend_end_castle2
if place_of_stay == "Hatter":
    jump gakuen_friend_end_hatter2
if place_of_stay == "Amuse":
    jump gakuen_friend_end_amuse2
if place_of_stay == "Tower":
    jump gakuen_friend_end_tower2
label gakuen_friend_end_castle2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の帰る場所はここ、赤薔薇寮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「いってらっしゃい」と見送られて、「おかえりなさい」と迎えられる。\n
それは、まるで家のようで。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（いつのまにか……、自然になっていたな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私自身、気付かないくらい自然に、ここに馴染んでいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他寮にはまだ知らないものがたくさんあって、そういったものと触れ合うことは楽しい。目新しいものは新鮮で、どうしたって興味をひかれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "でもそれ以上に、こうして赤薔薇寮に帰ってきて、緊張が緩むのを感じている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「変ね。\n
さっきまで緊張しているなんて思っていなかったのに、こうして帰ってきてほっとしているみたい」"

hide girl_a2_1
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice may_g0030
Seito "「ふふ、そりゃそうよ。\n
寮は、あなたの家みたいなものなんだから」"

hide girl_b1_5
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice tak_g0134
Seito "「帰ってきて落ち着くほどに、あなたがここに馴染んでくれたんだと思うと嬉しいわ。\n
さ、一緒に夕食を食べにでもいかない？」"
if gakuen_friend_castle_seen == True:
    jump gakuen_friend_end_go_castle2
if gakuen_friend_hatter_seen== True:
    jump gakuen_friend_end_go_hatter2
if gakuen_friend_amuse_seen == True:
    jump gakuen_friend_end_go_amuse2
if gakuen_friend_tower_seen == True:
    jump gakuen_friend_end_go_tower2
label gakuen_friend_end_hatter2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の帰る場所はここ、帽子屋寮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「いってらっしゃい」と見送られて、「おかえりなさい」と迎えられる。\n
それは、まるで家のようで。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（いつのまにか……、自然になっていたな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私自身、気付かないくらい自然に、ここに馴染んでいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他寮にはまだ知らないものがたくさんあって、そういったものと触れ合うことは楽しい。目新しいものは新鮮で、どうしたって興味をひかれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "でもそれ以上に、こうして帽子屋寮に帰ってきて、緊張が緩むのを感じている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「変ね。\n
さっきまで緊張しているなんて思っていなかったのに、こうして帰ってきてほっとしているみたい」"

hide girl_a2_3
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice may_g0030
Seito "「ふふ、そりゃそうよ。\n
寮は、あなたの家みたいなものなんだから」"

hide girl_b1_3
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice tak_g0134
Seito "「帰ってきて落ち着くほどに、あなたがここに馴染んでくれたんだと思うと嬉しいわ。\n
さ、一緒に夕食を食べにでもいかない？」"
if gakuen_friend_castle_seen == True:
    jump gakuen_friend_end_go_castle2
if gakuen_friend_hatter_seen== True:
    jump gakuen_friend_end_go_hatter2
if gakuen_friend_amuse_seen == True:
    jump gakuen_friend_end_go_amuse2
if gakuen_friend_tower_seen == True:
    jump gakuen_friend_end_go_tower2
label gakuen_friend_end_amuse2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の帰る場所はここ、遊園地寮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「いってらっしゃい」と見送られて、「おかえりなさい」と迎えられる。\n
それは、まるで家のようで。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（いつのまにか……、自然になっていたな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私自身、気付かないくらい自然に、ここに馴染んでいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他寮にはまだ知らないものがたくさんあって、そういったものと触れ合うことは楽しい。目新しいものは新鮮で、どうしたって興味をひかれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "でもそれ以上に、こうして遊園地寮に帰ってきて、緊張が緩むのを感じている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「変ね。\n
さっきまで緊張しているなんて思っていなかったのに、こうして帰ってきてほっとしているみたい」"

hide girl_a2_3
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice may_g0030
Seito "「ふふ、そりゃそうよ。\n
寮は、あなたの家みたいなものなんだから」"

hide girl_b1_3
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice tak_g0134
Seito "「帰ってきて落ち着くほどに、あなたがここに馴染んでくれたんだと思うと嬉しいわ。\n
さ、一緒に夕食を食べにでもいかない？」"
if gakuen_friend_castle_seen == True:
    jump gakuen_friend_end_go_castle2
if gakuen_friend_hatter_seen== True:
    jump gakuen_friend_end_go_hatter2
if gakuen_friend_amuse_seen == True:
    jump gakuen_friend_end_go_amuse2
if gakuen_friend_tower_seen == True:
    jump gakuen_friend_end_go_tower2
label gakuen_friend_end_tower2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の帰る場所はここ、塔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "「いってらっしゃい」と見送られて、「おかえりなさい」と迎えられる。\n
それは、まるで家のようで。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（いつのまにか……、自然になっていたな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私自身、気付かないくらい自然に、ここに馴染んでいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他寮にはまだ知らないものがたくさんあって、そういったものと触れ合うことは楽しい。目新しいものは新鮮で、どうしたって興味をひかれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "でもそれ以上に、こうして塔に帰ってきて、緊張が緩むのを感じている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_13")
T "「変ね。\n
さっきまで緊張しているなんて思っていなかったのに、こうして帰ってきてほっとしているみたい」"

hide girl_a2_3
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice may_g0030
Seito "「ふふ、そりゃそうよ。\n
寮は、あなたの家みたいなものなんだから」"

hide girl_b1_3
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_13")
voice tak_g0134
Seito "「帰ってきて落ち着くほどに、あなたがここに馴染んでくれたんだと思うと嬉しいわ。\n
さ、一緒に夕食を食べにでもいかない？」"
if gakuen_friend_castle_seen == True:
    jump gakuen_friend_end_go_castle2
if gakuen_friend_hatter_seen== True:
    jump gakuen_friend_end_go_hatter2
if gakuen_friend_amuse_seen == True:
    jump gakuen_friend_end_go_amuse2
if gakuen_friend_tower_seen == True:
    jump gakuen_friend_end_go_tower2
label gakuen_friend_end_go_castle2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「そうね……。\n
お茶会じゃ、おなかは膨らまないもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "赤薔薇寮で供された茶菓子はどれも一流で、紅茶も美味だったが、さすがに夕食の代わりになるほど食べてきたわけではない。"

jump gakuen_friend_end2
label gakuen_friend_end_go_hatter2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_14")
T "「そうね……。\n
お茶会じゃ、おなかは膨らまないもの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "帽子屋寮で供された茶菓子はどれも一流で、紅茶も美味だったが、さすがに夕食の代わりになるほど食べてきたわけではない。"

jump gakuen_friend_end2
label gakuen_friend_end_go_amuse2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「そうね……。\n
……チーズと魚料理以外のものを」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……頭が破裂するような音楽の聞こえない場所で食べたいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しみじみと口にしたリクエストに、二人は気の毒そうな顔をした。\n
ぽんと肩に彼女達の手が乗る。"

jump gakuen_friend_end2
label gakuen_friend_end_go_tower2:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「そうね……。\n
コーヒーブレイクにはケーキもついてきたんだけども、さすがにそれじゃ夕飯の代わりにはならないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あくまであれはおやつだと考えるべきだろう。\n
夕食は夕食でしっかり食べたい。"

jump gakuen_friend_end2
label gakuen_friend_end2:
hide girl_a2_3
show girl_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0031
Seito "「それじゃあ、行きましょうか。\n
今日は、何が食べられるかしらね」"

hide girl_b1_3
show girl_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0135
Seito "「無難にいくか、新規開拓に挑戦するか……。\n
悩ましいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_5")
T "「……私は、ちょっと冒険してみようかしら。\n
なんだか、今ならいける気がするのよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの食堂は頭の中に描いたイメージにより近い料理が自動的に提供される魔法が仕掛けてある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大勢の生徒の要望に対応するための工夫だ。だが、描いたイメージにブレがあると、当然出てくるメニューも、想定外のものになってくる。"

hide girl_a2_2
show girl_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0032
Seito "「冒険かあ……。\n
料理で冒険はしたくないけど……、気分を変えたくなるときってあるわよね」"

hide girl_b1_2
show girl_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0136
Seito "「分かったわ、そんなあなたのチャレンジ精神に敬意を払って。\n
何かとんでもないものが出てきたら、消費するの手伝うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_2")
T "「……意外と、すごく美味しいものが出てくるかもしれないわよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（珍しいものは、美味しく見える）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わいわいと、同寮の友人と話に花を咲かせながら食堂へと向かう。"
if place_of_stay == "Castle":
    jump gakuen_friend_end_castle3
if place_of_stay == "Hatter":
    jump gakuen_friend_end_hatter3
if place_of_stay == "Amuse":
    jump gakuen_friend_end_amuse3
if place_of_stay == "Tower":
    jump gakuen_friend_end_tower3
label gakuen_friend_end_castle3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな他愛のない日常がある赤薔薇寮こそが、今の私の帰る場所なのだ。"

hide girl_a2_8
show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0033
Seito "「でも、定番の料理が一番よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（……そうね。\n
その通り）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただいま、と。\n
もう一度、心の中で呟いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに、私の「定番」は決まっている。"

hide girl_a2_3

hide girl_b1_3
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_ros_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_long
##endmemory
if routechara == "Vivaldi":
    jump gakuen_vivaldi2
if routechara == "Peter":
    jump gakuen_peter2
if routechara == "Ace":
    jump gakuen_ace2
label gakuen_friend_end_hatter3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな他愛のない日常がある帽子屋寮こそが、今の私の帰る場所なのだ。"


show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0033
Seito "「でも、定番の料理が一番よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（……そうね。\n
その通り）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただいま、と。\n
もう一度、心の中で呟いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに、私の「定番」は決まっている。"

hide girl_a2_3

##[rchara2 PAY ATTENTION="false"]
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_hat_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_long
##endmemory
if routechara == "Blood":
    jump gakuen_blood2
if routechara == "Elliot":
    jump gakuen_elliot2
if routechara == "Deedam":
    jump gakuen_dad2
label gakuen_friend_end_amuse3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな他愛のない日常がある遊園地寮こそが、今の私の帰る場所なのだ。"


show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0033
Seito "「でも、定番の料理が一番よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（……そうね。\n
その通り）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただいま、と。\n
もう一度、心の中で呟いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに、私の「定番」は決まっている。"

hide girl_a2_3

##[rchara2 PAY ATTENTION="false"]
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_amu_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_long
##endmemory
if routechara == "Gowland":
    jump gakuen_gowland2
if routechara == "Boris":
    jump gakuen_boris2
if routechara == "Pierce":
    jump gakuen_pierce2
label gakuen_friend_end_tower3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな他愛のない日常がある塔こそが、今の私の帰る場所なのだ。"


show girl_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0033
Seito "「でも、定番の料理が一番よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（……そうね。\n
その通り）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただいま、と。\n
もう一度、心の中で呟いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すでに、私の「定番」は決まっている。"

hide girl_a2_3

##rchara2 PAY ATTENTION="false"]
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_tow_eve
with stripe_l_medium

scene bg_map_eve
with stripe_l_long
##endmemory
if routechara == "Nightmare":
    jump gakuen_nightmare2
if routechara == "Gray":
    jump gakuen_gray2
if routechara == "Julius":
    jump gakuen_julius2
if routechara == "Joker":
    jump gakuen_joker2
