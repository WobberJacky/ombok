label gakuen_common_breeze:
scene bg_map_nig
with dis

scene bg25_rr_nig
with dis

play music forest_thick_nig_p_wam

scene bg24_rj_nig_lon with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いよいよ、ブリーズの夜がやってきた。\n
そわそわと浮き足立つような空気は、ストームの夜を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あのときとは違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストームの夜は何も知らずに戸惑っていたが、こうして迎えたブリーズの夜は、何が起こるのかを把握した上で覚悟を決めている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は部屋の中で静かに待機していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（そろそろ……、かしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの開始は、それを伝える役目の生徒が各部屋の扉をノックして回ることで知らされるのだという。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "参加する気のある人間はその音を合図に行動を開始し、参加する気のない生徒はただその合図を聞き流すだけでいいらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は参加組なので、その合図を待つ。"

play sound se_0300

play music magic_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアが鳴った。\n
時間だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0008
Seito "「開始の合図だわ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0009
Seito "「ブリーズよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いよいよ、ブリーズが始まる。"

play sound se_0165

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は窓辺へと歩み寄ると、しゃっとカーテンを開け放った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓の外には、いつもと変わらない夜が広がっている。\n
しかし、それは見た目だけ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際には、ブリーズに参加する女子生徒たちが大勢、合図をきっかけに潜んでいるはずだ。"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"


##[cg time="1500"]
play sound se_0586
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も姿隠しの呪文を唱えると、窓を開けた。\n
さら、と吹き込む風が気持ちいい。"

if routechara == "Ace":
    jump gakuen_breeze_ace
if routechara == "Peter":
    jump gakuen_breeze_pet_gow_bor_pie_jul
if routechara == "Gowland":
    jump gakuen_breeze_pet_gow_bor_pie_jul
if routechara == "Boris":
    jump gakuen_breeze_pet_gow_bor_pie_jul
if routechara == "Pierce":
    jump gakuen_breeze_pet_gow_bor_pie_jul
if routechara == "Julius":
    jump gakuen_breeze_pet_gow_bor_pie_jul
label gakuen_breeze_ace:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ポケットの中に小瓶が入っているのを確かめてから、私は窓枠に足をかけると、トンと勢いをつけてそこから飛び降りる。"

play sound se_0216
pause .5
play sound se_0348

scene bg20_gd_nig
with dis
play sound se_0141
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

play sound se_0086
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "浮遊の呪文を唱え、ふわりと自由落下の速度を緩めて中庭へと着地した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲に人の姿はないが、それでもどこからか気配を感じる。\n
同じように、姿隠しの魔法を使って潜んでいる者がいるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（まずは状況を把握、と）"

if routechara == "Ace":
    jump gakuen_breeze_pet_ace_pie
label gakuen_breeze_pet_gow_bor_pie_jul:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は窓枠に足をかけると、トンと勢いをつけてそこから飛び降りる。"

play sound se_0216
pause .5
play sound se_0348

scene bg20_gd_nig
with dis
play sound se_0141
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

play sound se_0086
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "浮遊の呪文を唱えて、ふわりと自由落下の速度を緩めて中庭へと着地した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲に人の姿はないが、それでもどこからか気配を感じる。\n
同じように、姿隠しの魔法を使って潜んでいる者がいるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（まずは状況を把握、と）"

if routechara == "Peter":
    jump gakuen_breeze_pet_ace_pie
if routechara == "Gowland":
    jump gakuen_breeze_gow
if routechara == "Boris":
    jump gakuen_breeze_bor
if routechara == "Pierce":
    jump gakuen_breeze_pet_ace_pie
if routechara == "Julius":
    jump gakuen_breeze_jul1
label gakuen_breeze_pet_ace_pie:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズに参加すると決めてから、急遽情報収集を行ったのだ。"

if routechara == "Ace":
    jump gakuen_breeze_common2
if routechara == "Peter":
    jump gakuen_breeze_common2
if routechara == "Pierce":
    jump gakuen_breeze_common2
label gakuen_breeze_gow:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "恥を忍んで、事前に、ボリスへと協力を求めた甲斐があった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの基本情報や、どうやって男子寮に侵入したらいいのかなどのコツ。\n
すべて彼が教えてくれた。"
if routechara == "Gowland":
    jump gakuen_breeze_common2
label gakuen_breeze_bor:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このために、今朝彼女達に協力を求めたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの基本情報や、どうやって男子寮に侵入したらいいのかなどのコツ。\n
すべて彼女達が教えてくれた。"
if routechara == "Boris":
    jump gakuen_breeze_common2
label gakuen_breeze_jul1:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちゃんと事前に、カフェテリアで情報収集をした甲斐があった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの基本情報や、どうやって塔の男子側に渡ったらいいのかなどのコツ。\n
すべて先輩にあたる生徒達が教えてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の仕組みとして、男女共同区域より上の階は男女で左右に分かれている。\n
その間には渡り廊下があるが、侵入経路が限られている分、難易度が上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのため、一度窓から外に出て、男子側の窓から侵入しなおすのが一番手っ取り早いコースなのだそうだ。"

if routechara == "Julius":
    jump gakuen_breeze_common2
label gakuen_breeze_common2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "基本的にはストームとルールは変わらない。ある程度手加減した使用人達の目を盗み、無事に男子寮へと侵入することがブリーズの目的だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただストームと違うのは、男子達が説明力や侵入における魔法技能を試されたのとは違い、探索力を試されるという点だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何せ、取られたものを取り返しに行くというのがその目的なのだ。\n
誰の部屋でもいいわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あらかじめ目的の部屋の位置などを把握しておかなければ、目的をスムーズに達成することは出来ないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……よく出来ているわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただのお祭りイベントかと思いきや、互いの苦手分野を磨くようになっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一般的に、男子は空間・図形把握能力に優れ、女子は言語・コミュニケーション力に優れているといわれている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "このイベントでは、空間把握に優れている男子にコミュニケーション力が求められ、その逆で女子には空間把握能力が求められているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントとはいえ、学習も兼ねているらしい。"

play sound se_0010 volume .6
pause 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……動いた？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "風に木々が揺れる音に混じり、それ以外の音が微かに混じる。\n
皆が移動を始めたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、影を選んで静かに移動を開始する。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Servant "「…………」"

play sound se_0625
$ flash_color("yellow",.3)
if routechara == "Julius":
    jump gakuen_breeze_jul2
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっと私の傍を明かりが過ぎた。\n
女子寮と男子寮の間にある中庭のあちこちを、使用人やメイド達が見回っている。"

if routechara == "Peter":
    jump gakuen_breeze_common3
if routechara == "Ace":
    jump gakuen_breeze_common3
if routechara == "Gowland":
    jump gakuen_breeze_common3
if routechara == "Boris":
    jump gakuen_breeze_common3
if routechara == "Pierce":
    jump gakuen_breeze_common3
label gakuen_breeze_jul2:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっと私の傍を明かりが過ぎた。\n
塔を囲むように広がる庭のあちこちを、使用人やメイド達が見回っている。"
if routechara == "Julius":
    jump gakuen_breeze_common3
label gakuen_breeze_common3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いくら姿隠しの魔法を使っていても、質量が消えるわけではない。灯りが照らしている中を下手に動けば、不自然な草木の揺れでバレてしまいかねない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際見つかる女子生徒もいるようで……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tan_g0007
Servant "「こら、おとなしくしろ！\n
捕まったんだから、諦めて一度寮に戻るように！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0009
Seito "「姿隠しの魔法、もっと練習しておけばよかった～～！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0011
Maid "「あらあら、それで隠れているつもりなのかしら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0012
Maid "「そこのあなたも……。\n
ほ～ら、捕まえた！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice sam_g0010
Seito "「げっ！\n
なんで捕まったの～！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0013
Maid "「そりゃあ、いくら姿隠しの魔法を使っていても、ああ堂々と歩かれたら気付きます。もうちょっと、忍んでいただかないと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手加減しているとはいっても、その手加減の度合いは使用人達の間にもブレがあるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しぐらいの物音を見逃してくれる者もいれば、しっかり捕獲に乗り出す者もいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捕まっても一度寮に強制送還されて、いわゆる「振り出しに戻る」だけだということは分かっているのだけれども……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、緊張感に心臓がどきどきと高鳴る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（これって……、かくれんぼや鬼ごっこと同じ感覚よね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クセになりそうな緊張感だ。\n
少し進んでは動きを止めて様子を伺い、また少し進んでは……、と繰り返して着実に男子寮へとの距離を詰めていく。"

with dis
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "窓の鍵は、男子側のほうから開けてあるらしい。\n
先に侵入した人がいるのか、私が辿り着いたとき、すでに窓は開いていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"
if routechara == "Julius":
    jump gakuen_breeze_jul3
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりと窓から男子寮の中へと忍び込む。"
if routechara == "Peter":
    jump gakuen_breeze_common4
if routechara == "Ace":
    jump gakuen_breeze_common4
if routechara == "Gowland":
    jump gakuen_breeze_common4
if routechara == "Boris":
    jump gakuen_breeze_common4
if routechara == "Pierce":
    jump gakuen_breeze_common4
label gakuen_breeze_jul3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "するりと窓から塔の男子寮側へと忍び込む。"

if routechara == "Julius":
    jump gakuen_breeze_common4
label gakuen_breeze_common4:

play music corridor_nig_p_wam

scene bg25_rr_nig with stripe_l_medium
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……これで、第一関門は抜けたわね」"

play sound se_0741
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姿隠しの魔法を解き、ほう、と息を吐き出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "男子寮の中へ入ってしまえば、後は滅多なことで使用人に捕まるようなことはない。使用人達は中庭での妨害が、主な任務になっているらしい。"
if routechara == "Peter":
    jump gakuen_peter6_2
if routechara == "Ace":
    jump gakuen_ace6_2
if routechara == "Gowland":
    jump gakuen_gowland6_4
if routechara == "Boris":
    jump gakuen_boris6_4
if routechara == "Pierce":
    jump gakuen_pierce6_2
if routechara == "Julius":
    jump gakuen_julius6_2
