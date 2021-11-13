label gakuen_nightmare6:
scene bg06_sk_h_day
with dis
$ clockanim()


scene bg06_sk_h_eve
with dis

play music forest_thick_nig_p_wam

scene bg06_sk_h_nig with Dissolve(1.2)
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


scene bg24_rj_nig
with dis
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

play sound se_0302
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……っ！」"


scene bg06_sk_h_nig
with dis
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
T "いよいよ、ブリーズが始まる。\n
私は少し待ってから、ドアを開けて外に出た。"

play sound se_0397

scene bg25_rr_nig
with dis

play music magic_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の仕組みとして、男女共同区域より上の階は男女で左右に分かれていた。\n
その間には渡り廊下があるが、侵入経路が限られている分、難易度が上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それ故、普通は一度窓から外に出て、男子側の窓から潜り込んでいくのだそうだ。\n
だが私の場合、目指すは頂上だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外に出るよりも、中から階段で目指したほうが人目につかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の生徒が外から攻める分、渡り廊下以外の内部の守りは手薄になるのではないだろうか。"

play sound se_0496

show magic_b onlayer master with Dissolve(1.5)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

play sound se_0731
hide magic_b with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "姿隠しの呪文を唱えると、するりと廊下へと出た。\n
すでにドアをノックして、ブリーズの開始を告げた誰かの姿はない。"

play sound se_0141
show magic_g onlayer master with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

hide magic_g with Dissolve(1.5)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の周囲に風の結界を張り、音が漏れないようにした。\n
姿隠しをしても、足音でバレるというのはよくあることだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はしんっと静まり返った廊下をそろそろと移動する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（まずは状況を把握、と）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズに参加すると決めてから、急遽、情報収集を行ったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "基本的にはストームとシステムは変わらない。ある程度手加減した使用人達の目を盗み、無事に男子寮へと侵入することがブリーズの目的だ。"

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
T "このイベントでは、空間把握に優れている男子にコミュニケーション力が求められ、その逆の女子に空間把握能力が求められているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントとはいえ、学習も兼ねているらしい。"

play sound se_0556

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……外は賑やかね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "遠くから楽しそうな声が響く。"
$ renpy.sound.register_channel("sound2", mixer=Sound, loop=True)
$ renpy.sound.play("se_0776", loop=True)
play sound se_0776
pause .3
play sound2 se_0776

scene bg25_rr_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "人の気配がした。\n
姿を隠しているし、消音の魔法もかけているとはいえ、物陰へと隠れる。"


show siyounin_a2_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0064
Servant "「今回のブリーズも、何事も問題なく終わるといいですね……」"

hide siyounin_a2_8
show siyounin_a2_8 at left
with dis

show maid_d_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0116
Maid "「そのために私達がサポートするのよ。\n
怪我人は出さないようにね」"

hide siyounin_a2_8
show siyounin_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kat_g0065
Servant "「そうですね。\n
気を引き締めていきましょう」"

stop sound2 fadeout .5
pause .3
stop sound fadeout .5
hide siyounin_a2_3

hide maid_d_8

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "使用人達の足音と気配とが、私の傍らを足早に過ぎていく。\n
私の存在には気付かなかったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ほうっと息をついて、再び行動を開始する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が階段に辿り着き、登り始めたときには外はさらに賑やかになっているようだった。"


scene bg06_sk_h_nig
with dis
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

play sound se_0794 volume .65
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "外では捕まった生徒も出ているようだ。\n
何でも捕まった女子生徒は一度女子寮へと戻され、再スタートとなるのだそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らが派手に外でブリーズを展開してくれているおかげで、私はこうしてこっそりと動くことができる。"



scene bg25_rr_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……行こう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、早足で階段を登り始めた。"

with dis
$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "途中で力尽きるというナイトメアの気持ちも理解できそうになってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "へとへとになりながら、それでもなんとか最上階へと辿り着くことが出来た。\n
最上階にはナイトメアの部屋しかないため、迷う心配はない。"

if lovechara_nightmare_points == 8:
    jump gakuen_nightmare6_2a
label gakuen_nightmare6_1_5:
menu:
    "ノックをする。":
        jump gakuen_nightmare6_2a
    "部屋へ入る。":
        jump gakuen_nightmare6_2b
label gakuen_nightmare6_2a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアの前で姿隠しなどの魔法を解除した。\n
それから、ドアへと手を伸ばす。"

play sound se_0300
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドキドキとする胸を抑え、ノックした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（な、なんで、こんなにドキドキしているの、私……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_7")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（ナイトメアはどんな顔で迎えてくれるのかしら……）"

play sound se_0397
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し間があいてから、ドアが開く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "{size=+20}「っ！！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……グレイ？」"


play music stream_day_p_wam

show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこか申し訳なさそうな顔でドアを開けたのは、ナイトメアではなくグレイだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慌てて場所を確認するが、間違いなくここが最上階だ。\n
ここより上となると、残されているのは屋上だけになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「え……っ、なんで？\n
どうして、グレイがここに？」"

hide gre_m_03_3
show gre_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは沈鬱な表情で視線を伏せる。\n
とてもとても、申し訳なさそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かがあったから、彼がこんな顔をしなくてはいけないのだろう。\n
そもそもナイトメアはどうしたというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（来ることは伝えておいたし……。\n
仕事じゃないんだから、逃げ出したとも思えない）"

hide gre_m_01_6
show gre_m_01_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice gra_g0008
Gray "「イベントを楽しみにここまで来た君に、こんなことを言うのは俺も辛いんだが……。\n
……ナイトメア先生が体調を崩された」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（ナイトメアが体調を崩した？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃から不健康そうな、いや、不健康極まりないナイトメアである。\n
いつ本格的に体調を崩したとしてもおかしくはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、逆にいつそうなってもおかしくない状態で常に持ちこたえていたこともあり、そのナイトメアが体調を崩したということが信じられなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「た、大変……ね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段から大変そうなので、なんとも……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「それで、大丈夫なの？」"

hide gre_m_01_14
show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice gra_g0009
Gray "「ああ、ようやく落ち着いてきたところだ。\n
……だが、ブリーズは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「あ、いいのよ、そんなことは。\n
ナイトメアが無事ならよかったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（普段の様子じゃ、体調を崩してそのままポックリ……、なんてことも充分にありそうだもの）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりとグレイ越しにナイトメアの部屋を覗く。\n
ベッドの上にこんもり丸く盛り上がった人影が見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呼吸するたびの上下の触れ幅が、通常より大きく見えるのは息が荒いせいなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（何か、してあげられたらいいんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここには介護のプロ（？）であるグレイも控えている。\n
私に出来ることは何もない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ナイトメアに、お大事にって伝えてくれる？\n
あと……、そうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「元気になったら、また遊びましょうって」"

hide gre_m_03_3
show gre_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice gra_g0010
Gray "「ああ、分かった。\n
ちゃんと伝えておく」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がそれほど分かりやすく気落ちしなかったことに、グレイは安堵したようだった。眉間に寄っていた深い皺が、ゆるりと伸びる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを見届けて、自室に戻ることにした。"

hide gre_m_02_8


scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかくのブリーズだが……。\n
どうやら失敗のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "敗因は、想像以上に病弱だったナイトメアというところだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（しかし、グレイに知られてしまっていたとは……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントは失敗したというのに、妙に照れる。"

with dis
$ hi_mes()

scene bg06_sk_h_nig with Dissolve(.8)

scene bg06_sk_h_day with Dissolve(1)

scene bg06_sk_h_eve with Dissolve(1)

scene bg06_sk_h_nig with Dissolve(.8)

scene bg06_sk_h_day with Dissolve(1)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg25_rr_day
with stripe_l_long

play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから数日が過ぎた。\n
いつものように朝、カフェテリアに向って歩いているところでグレイに呼び止められた。"


show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0011
Gray "「ああ、[firstname]。\n
ちょうどいいところで会えた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「なあに？\n
私に何か用かしら」"

hide gre_m_02_2
show gre_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice gra_g0012
Gray "「いや、ナイトメア先生の熱が下がってな。後は安静にしていれば治ると思うんだが、どうもあの人は退屈が我慢ならないらしいんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……困った患者よね。\n
医者の癖に」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どんな患者が一番困るかなどを承知しているはずなのに、どうして彼自身がその困った患者になりきってしまうのか。"

hide gre_m_02_11
show gre_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0013
Gray "「君が見舞いにでも訪れたら、きっとおとなしく寝ていてくださると思うんだが……。\n
どうだろう、行ってあげてくれないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え？\n
いいの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズやストームというイベントでもないのに、ナイトメアの私室を訪ねたりなどしてもいいのだろうか。"

hide gre_m_03_3
show gre_m_01_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0014
Gray "「補佐をしている俺が頼んだのだから、超法規的処置ということにしておいてくれ」"

hide gre_m_01_14
show gre_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0014_5
Gray "「ここで安静にしていてもらわないと、あの人はまた倒れるからな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふっとグレイの視線が遠くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……苦労しているのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "優秀な彼だけに、同情してしまう。"

hide gre_m_01_10
show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0015
Gray "「使用人達にも話は通しておく。\n
ああ、でも他の生徒の目にはつかないようにしてくれるとありがたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「了解。\n
授業が終わった放課後に、お見舞いに行かせてもらうわね」"

hide gre_m_01_4
show gre_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gra_g0016
Gray "「分かった。\n
……それじゃあ、それまではゆっくり休んでいてもらおう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……力づくで？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな不穏さを、彼の言葉に感じてしまった。\n
グレイの声音に滲む疲れた響きのせいだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（こんな優秀な補佐を思い詰めさせて……。\n
医者のくせに、困った患者ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中でつっこみつつ、私はグレイに見送られてカフェテリアへと向かった。"

hide gre_m_01_1

$ hi_mes()

scene bg25_rr_day
with dis

scene bg_par15_rg_tow_day
with dis

scene bg25_rr_day
with dis
play sound se_0383
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後になって、グレイに言われた通り、人目につかないようにこっそりとナイトメアの部屋のある最上階を目指す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……これを毎日繰り返していたら、痩せる上に体力もつきそうだ。\n
メイドや使用人が引き締まった身体をしている理由が分かってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの部屋へと近付くにつれ、言い争う声が聞こえてきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0129
Nightmare "「い、嫌だ……！！\n
私は逃げるぞ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0017
Gray "「何言っているんですか、そんな身体で！\n
彼女は、あなたのためにお見舞いに来てくれるんですよ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0130
Nightmare "「あ、会いたくない……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "{size=+20}（なぬ？）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶちっと、どこかで何かが切れる音を聞いたような気がした。\n
いつのまに、こんなに沸点の低い人間になってしまったのか。"

play sound se_0291
camera at hpunch
camera at vpunch

scene bg_par24_rht_day with Dissolve(.5)
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次の瞬間には、私はほとんどナイトメアの部屋の扉を蹴り開けるようにして闖入していた。"


play music nightmare_t_ali
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「誰に会いたくないですって……！？」"


show nai_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
Nightmare "{size=+20}「！！！！！」{/size} "

hide nai_m_03_3
show nai_m_03_3 at left
with dis

show gre_m_01_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは窓枠に片足をかけ、今にも飛び出そうとしている。\n
そしてグレイは、その腰にしっかりと腕を回して逃がすものかと捕まえている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "傍から見ると、自殺志願者とそれを止める図といったようだ。\n
滑稽な場面なのに、私は笑えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「どういう意味なのか、きっちり説明してもらいましょうか。\n
……ねえ、ナイトメア？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脅しつけるよう低い声で名前を呼べば、ナイトメアの背中がびくりと跳ねた。\n
とりあえず、逃亡の意志を折ることには成功したらしい。"

play sound se_0587
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は渋々ながらも窓枠から足を下ろすと私へと向き直る。\n
そそくさとグレイが窓を閉めて、飛び降り防止に鍵をかけた。"

play sound se_0452
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これで一応、逃げ場は塞いだ形だろうか。"

hide nai_m_03_3
show nai_m_02_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0131
Nightmare "「……会えないだろう。\n
私は君が楽しみにしていたブリーズを台無しにしてしまった」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは眉尻を下げて、悲しげだ。\n
いつか見た、諦念の滲んだ笑い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何もかもを達観しきっているかのような、そんな顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……いやいや。\n
熱出して倒れた程度で、そんな大層な）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

hide gre_m_01_6
show gre_m_02_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイへとちらりと視線を投げかける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "アイコンタクトはばっちり。\n
意味はすなわち、どうしてこいつこんなに馬鹿なの、だ。"

play sound se_0098
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、ずんずんとナイトメアへと距離を削ると、その胸倉を鷲掴む。"

play sound se_0492
hide nai_m_02_8
show nai_m_02_10 at center
with dis
hide gre_m_02_11

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0132
Nightmare "「っ、本当にすまなかった……！\n
君に合わせる顔がない……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「あるわよっ！！」"

play sound se_0637 #
#special anime hit center
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思いっきり頭を引いて、頭突きという形で顔を合わせてやった。"

hide nai_m_02_10
show nai_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0133
Nightmare "「……{size=+20}っ！？{/size}」"

play sound se_0553
play sound se_0327
hide nai_m_03_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふらりっと容易くナイトメアの足元が危うくなる。それをそのまま無理矢理引っ張って、ぐるんと遠心力を利用してベッドに向かって押し倒した。"

show m_naigoodend1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0134
Nightmare "「あ、頭が割れそうに痛い……っ！！\n
しかも、くるくる回って……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「それは、あんたの熱がまだ下がっていないからよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が頭突きしてぶん回した影響も{size=+20}少々{/size}あるかもしれない。\n
ぶつけた額がじんわりと熱い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私より少し熱いといったような体温だが、日頃低体温なナイトメアにとっては、発熱といっていい状態だろう。"

play sound se_0232
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま無理矢理、ベッドの中に押し込んでしまう。"

hide m_naigoodend1


show gre_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0018
Gray "「……驚いた。\n
俺より力技だな、君は」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「ナイトメアが馬鹿だから、仕方ないのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "病み上がりともいえない回復状態なのに逃げ出そうとするとは、馬鹿としか言いようがない。"

hide gre_m_03_1
show gre_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0019
Gray "「我が上司ながら、否定できないのが残念だ。\n
……手間のかかる人なんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「知っているわ。\n
……うんざりするほどね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しみじみと傍らのグレイと言葉を交し合う。\n
ナイトメアが面倒で、手間のかかる男であることぐらい、私だって知っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "微妙に張り合ってしまうのは、ナイトメアの一番近いところにいるのがグレイだと分かっているからだろうか。"


show nai_m_02_9 at center
with dis
hide gre_m_03_6

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0135
Nightmare "「うう……。\n
二人とも……、酷いぞ」"

hide nai_m_02_9
show nai_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0136
Nightmare "「…………。\n
……怒っているんだろう、[firstname]？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……どうして、そう思うの？」"

hide nai_m_03_6
show nai_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice nig_g0137
Nightmare "「どうして、って……。\n
ブリーズが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_2")
T "「あのね、ナイトメア。\n
私が楽しみにしていたのは、ただのブリーズじゃないの」"

hide nai_m_03_9
show nai_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_2")
voice nig_g0138
Nightmare "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「あなたからリボンを取り返すための、ブリーズよ。\n
そこのところ、分かっているの？」"

hide nai_m_02_7
show nai_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice nig_g0139
Nightmare "「だ、だから……。\n
それを私が駄目に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通じていない。\n
もっと直接的な言葉でなければ、ナイトメアには通じないのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「いい？\n
どんなイベントでも、一緒に過ごす相手があってのものでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「体調を崩したなら、無理をしてもらっても仕方ないわ。\n
駄目にしたなんて思っていない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はあの後、おとなしく自室に戻ったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "取り返す相手がいなくとも、お祭り騒ぎに加わることくらい出来ただろう。\n
だが、そうしなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうしなかったということは……、そういうことなのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアがいなくてはと思ったし、苦しんでいる彼を放って騒ぐ気にもなれなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん、私がまっすぐに寮に戻ったことなんてナイトメアには分からないことだろうが……。"


play music flower_eve_p_wam

show m_naigoodend2 onlayer master
with dis
hide nai_m_02_10

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「[firstname]……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと伸びてきた手が、ベッドサイドに屈みこんでいた私の頬へと触れた。\n
熱っぽい手だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gray "「…………」"

play sound se_0284 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイが、そっと離れていくのを視界の端に認めた。\n
気を利かせてくれたのか、ドアを開閉する音が背後で一度響く。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0140
Nightmare "「……私が元気になったら、ブリーズをやり直させてくれないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……ずいぶんと遠そうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（元気になったら、なんて）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが健康になれることなんて、この先あるのだろうか。\n
それに、次のブリーズは一年後だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ずいぶんと、先の話ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice nig_g0141
Nightmare "「君が待っていると思えば、薬も飲めそうだ。\n
……だから、頼むよ」"

hide m_naigoodend2
show m_naigoodend3 onlayer master
with dis

scene black ##instant]
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「そうね。\n
あなたが元気になったら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice nig_g0142
Nightmare "「ふふ。\n
一年後の予約だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "嬉しそうに目を細める彼に、私まで笑みが口元に浮かんでしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……でも、一年先まで他にイベントがないわけじゃないんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズはまだ先。\n
だが、もっと近くにだって、機会はあるはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "渡すことの出来なかったラブレター。\n
あれほど明確な想いではなくとも、育てることも、渡す機会も……、彼となら。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（早く、元気になってね）"

hide m_naigoodend3 with Dissolve(5)
hide frame_par_monologue
hide ali_m_01_9
with Dissolve(5)

stop music
##endmemory
jump gakuen_b
label gakuen_nightmare6_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっとドアのノブへと手をかけた。\n
音をたてないように回してみる。"

play sound se_0277 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あ、開いている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "鍵はかかっていなかった。\n
するりと部屋の中へと忍び込む。"


play music quiet_a_wam

scene bg_par24_rht_nig with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの部屋は、私の部屋よりもだいぶ広いようだった。\n
やはり、職員ということだけあって優遇されているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その広い部屋の窓際に、綺麗にセットされたテーブルが用意されていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シックな色合いでまとめられたテーブルクロス。\n
その中央には華やかな花が飾られている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の主から想像していたよりも、大人っぽい内装だ。\n
窓辺には、銀色のワインクーラーがさりげなく置かれていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（……っ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気恥ずかしくなってしまうほどに、歓待の準備が整ってしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "奪われたものを奪い返すというような野性味溢れるイベントの趣旨はどこへ行ってしまったのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（ナイトメアは……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きょろりと視線をめぐらせれば、鏡の前で身嗜みをチェックしている彼の姿を見つけてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タイの具合を確認してみたり、角度でポーズをつけてみたりと余念がない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「～～～……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "格好をつけようとしているナイトメア。\n
本人が真剣なのが分かってしまう分、余計におかしくなってしまった。"

menu:
    "姿を現す。":
        jump gakuen_nightmare6_3a
    "そっと外に出る。":
        jump gakuen_nightmare6_3b
label gakuen_nightmare6_3a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はここで姿を現すことにした。\n
ナイトメアの背後へと回る。"

play sound se_0526
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そしてそこで姿隠しの魔法と、音を消すための魔法を解除した。"


show nai_s_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0143
Nightmare "「……んっ、わああああ！！？\n
き、きききっ、君！いつのまに入ってきたんだ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まるで幽霊のようにすうっと背後へ現れた私に、ナイトメアは予想通りのリアクションを返してくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "驚き半分、見られた羞恥半分というところだろうか。"

hide nai_s_03_3
show nai_s_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0144
Nightmare "「ぶ、舞台裏を覗くなんて、マナー違反だぞ！！？\n
ううう、なんという辱めだ……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「だって、鍵が開いていたんだもの。\n
それに……、その、あなたがそんなにも私を迎えるために準備していてくれたのが嬉しいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか私まで恥ずかしくなってきてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "訪れた先で一生懸命準備してくれたのを知り、嫌な気分になる者はいない。\n
一方で、それを嬉しく思ってしまうことに照れる。"

hide nai_s_02_10
show nai_s_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0145
Nightmare "「……ふふ。\n
君がそんな顔をしてくれるなら、こうして準備した甲斐があったな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやらナイトメアの機嫌は戻ったようだ。\n
すっと慣れた所作で、テーブルへとエスコートされる。"

jump gakuen_nightmare6_4
label gakuen_nightmare6_3b:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、そっともう一度外に出ることにした。\n
こんなにも一生懸命、用意してくれているのだ。"


scene bg25_rr_nig with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと、私を迎えるところからいろいろとシミュレートしているのだろう。\n
音を立てないようにドアを閉めて、廊下にて自身にかけていた魔法を解いた。"

play sound se_0300
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それからノックをする。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "部屋の中から、ナイトメアの緊張した気配が伝わってきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……馬鹿。\n
私まで緊張してくるじゃないのっ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の緊張が私にまで移りそうで、そわそわとしてきてしまう。"

play sound se_0397
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やがて……、ドアが開く。"

hide nai_s_01_13
show nai_s_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0146
Nightmare "「……やあ、[firstname]。\n
いらっしゃい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "精一杯に気取った声音だ。\n
いろいろ耐えかねてふき出してしまいそうになるが、そこは堪える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここで笑い出してしまっては、ナイトメアの心に取り返しのつかない深い傷をつけてしまいかねない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "年上の男性なのに、思春期の男の子のようなナイーブさがありそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（私のほうが年下なのに……、こんなふうに気を回すのって変かしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……ありがとう。\n
失礼するわね」"

hide nai_s_02_2


scene bg_par24_rht_nig with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから私も、なるべく澄ました声でそう言って彼の部屋へと足を踏み入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実は二度目になるのだが、そんなことはおくびにも出さず、物珍しげに周囲へと視線を向けてみる。"


show nai_s_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0147
Nightmare "「こちらに、テーブルを用意してあるんだ。\n
こっちだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すいっと手馴れた所作で窓際のテーブルまでエスコートされた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（ああ、でもこういうところは……、大人だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "マナーなどは、完璧だ。\n
さらっとした様子で導かれる。"

jump gakuen_nightmare6_4
label gakuen_nightmare6_4:
play sound se_0161 volume .6
show m_nai6_1 onlayer master
with dis
hide nai_s_01_11


play music luxurious_room_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "かたりと椅子を引かれて、腰掛けた。\n
ナイトメアの私室であるはずなのに、高級なレストランにでも足を踏み入れてしまったような気がしてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が制服姿なのが残念だ。\n
ナイトメアのスーツ姿に合わせ、それなりにお洒落した格好で来ていたならばもっと絵になっただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう思うと少し残念だ。\n
彼が私の向かいへと腰を下ろす。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……慣れているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0148
Nightmare "「何がだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「女性の扱い方。\n
こういった準備だったり……、今の椅子の引き方だったり……、慣れているようだったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女たらしだとかそういった意味ではない。\n
マナー的なことで、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意図はナイトメアにも伝わったようで、彼も動揺せず答えてくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0149
Nightmare "「ああ、そうだな。\n
慣れている……、といえば慣れている」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0150
Nightmare "「幼い頃より夜会に連れ出されていれば、自然と身につくさ。\n
私の家はそれなりに名家なんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「そういえば……、大層な家名だったわね。\n
ゴットシャルク、だっけ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice nig_g0151
Nightmare "「ああ、そうだとも。\n
私の名前は、ナイトメア＝ゴットシャルクだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice nig_g0152
Nightmare "「これでも、省略されているんだよ。\n
ナイトメアとゴットシャルクの間には、４～５の名前がつく」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……私には聞いたことがない名前だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仕方のない話だ。\n
私の家は裕福なほうではあるが、名のある家ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぶっちゃけた言い方をすると、いわゆる成金の部類だ。\n
旧家ではなく、ここ数代で成功してきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこの娘である私も、権力者や貴族といったような人々の名前や、交流関係には疎い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "父に野心があり名誉欲に走れば、姉や私はきっとその夜会に送り込まれていたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが実際のところ、父にその気はなかった。父は仕事がうまくいくだけで満足しており、名誉だとか栄誉といったものにはあまり拘っていなかったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（そのことには、感謝しているけど、こうして身近に身分の高い人がいると多少は交流を持っておくべきだったかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紋章学なんて授業が歴史の中に含まれていたので、王族や、有名な名家の家紋や家の名前は覚えさせられたこともある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が……、今ではもう諳んじてみろといわれてもすっかり記憶の彼方だ。"

hide m_nai6_1
show m_nai6_2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0153
Nightmare "「君のほうこそ、エスコートされ慣れているようだ。\n
……彼に、してもらっていたのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっと顔を上げて、ナイトメアを睨みつける。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0154
Nightmare "「いや、そうだな。\n
君は彼とそんな関係にはなかった」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（そこまで見たの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「……悪趣味よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは私の夢を知っている。\n
夢の中に現れて、悪夢を遠ざけてくれた代わりに、その中身をナイトメアは知ってしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……憎たらしい）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「知っているくせに。\n
私は彼に、ラブレターすら渡し損ねたのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんらかの行動に出る前に、すべて終わってしまった初恋だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0155
Nightmare "「……もう、想いは吹っ切ったのか？\n
彼は、君にとって過去の人か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「……あなたには関係ないでしょう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（そう……、私にとっても、もう関係ない人なんだわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "柔らかな傷口にそっと触れてくるような彼の問いかけに体が強張る。\n
だが、思ったほどその問いは痛くなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もっと生々しく、血を流していると思っていたのに。\n
夢で追い詰められたより、今は傷が浅くなっているようだ。"

hide m_nai6_2
show m_nai6_3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0156
Nightmare "「関係あるとも。\n
私は君のことが好きだし、今から口説こうとしているわけだからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……は？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エスコートしたときのように、さらりと。\n
スマートに、言われてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（え……？\n
今なんて……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice nig_g0157
Nightmare "「聞こえなかったか？\n
私は君が好きで、今から口説こうとしている、と言ったんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「っ、あなたねえ！\n
ここまで用意を整えて、そんなさりげなく言う！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな完璧なセットを用意しておきながら、まさかの段取り無視だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "軽い食事と、アルコールと、楽しいおしゃべりと。\n
そして最後に告白なんて想像していたのが、ガラガラと音を立てて崩れていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（やけに軽く……。\n
……ＯＫされるって、自信があるから？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まあ、もちろん、こういうシチュエーションだ。これで好意を持っていなかったらおかしいし、そこに入ってきた私にだって気持ちはある。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0158
Nightmare "「……ふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは、私が動揺しているようなのに満足げに隻眼を細める。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0159
Nightmare "「普通に告白しても、面白くないから却下、ぐらいは言われそうだからな。\n
先制攻撃だよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……先制って」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういったことは、格闘技ではない。\n
だが、その威力は絶大。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "座っている傍から足元が宙に浮きそうだ。\n
頭の中も同じく、ふわふわしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……浮かれている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼といると、浮ついている自分を自覚できた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0160
Nightmare "「夕食は、もうすませているだろうから……。\n
フルーツと……、シャンパンでもどうだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……いただくわ」"

play sound se_0468
pause .7
play sound se_0783
hide m_nai6_3
show m_nai6_4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが指を鳴らすと同時に、机の上に季節のフルーツの盛り合わせが現れる。\n
艶々とみずみずしいさくらんぼだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "光を受けて輝く様は、まるで小さな宝石。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは一般的な魔法は使えないはずではなかっただろうか。\n
机の上に現れたさくらんぼの盛り合わせと、ナイトメアとを見比べる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0161
Nightmare "「ふ、この特殊な体質との付き合いも長いんだ。\n
色々と、インチキは心得ているよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（そういえば……、空間移動もインチキって言っていたわよね？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世間一般の空間移動魔法とは違い、ナイトメアの空間移動は夢を仲介して移動するのだと言っていた。\n
もしかして、今のもそうなのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「夢に、準備していたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0162
Nightmare "「……それは、企業秘密だ。\n
種明かししてしまうと面白くないだろう？」"

hide m_nai6_4

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「当たっているかどうかは、教えてくれたっていいじゃない」"


show nai_s_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice nig_g0163
Nightmare "「舞台裏を覗いては面白くないよ。\n
第一、私だって格好がつかない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょいと肩を竦めて、ナイトメアが立ち上がる。\n
ぱさりとハンカチを広げ、ワインクーラーにさしてあったシャンパンを引き抜く。"

play sound se_0666
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "冷たい氷水に浸してあったのか、ボトルを引き抜く際に氷がぶつかる涼しげな音がした。"

hide nai_s_01_1
show nai_s_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0164
Nightmare "「ふっふっふ。\n
さて……、これの出番だ」"

play sound se_0674

show m_nai6_5 onlayer master
with dis
hide nai_s_02_4

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「え……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが取り出したのは、小型の鉈ぐらいの大きさはありそうなナイフだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、形状としては包丁といったほうがいいのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0165
Nightmare "「これはシャンパン・サーベルと呼ばれるものでね。\n
見ていてごらん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアは自信満々だが、こちらとしてはハラハラするばかり。\n
彼に刃物なんて、いかにも自分の手を切る前兆のようにしか思えない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（指、切らないでよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice nig_g0166
Nightmare "「切らないよ。\n
心配ない」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……っ、読まれた）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「人の心を、勝手に読まないでよ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこまで読まれているのだろう。\n
さすがに全部は読んでほしくない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0167
Nightmare "「私が読もうとしなくとも、あんまりにも強い思考は漏れてくるんだよ。\n
見せておきながら見るなというのは、対処のしようがないとは思わないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「そ、それでも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "強い思考なんて言われてしまうと、ますます困る。\n
それではまるで、私がナイトメアをとても心配したかのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……しているわけだけども）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本当に、手を切りそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0168
Nightmare "「それじゃあ、いくぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し、ナイトメアの声にも緊張が混じる。\n
私の緊張まで伝わっているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

play sound se_0126
hide m_nai6_5
show m_nai6_6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シャンパンのグラスを左手で捧げ持ち、右手のサーベルを一閃した。"

play sound se_0234
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの振るったサーベルは、狙い違わず見事にシャンパンボトルの首を飛ばした。"

play sound se_0235
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっぱりと切断された切り口からはしゅわしゅわと炭酸が溢れ、飛んだボトルが空中で花火のように弾けて光が踊る。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……わあ！\n
綺麗……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice nig_g0169
Nightmare "「ふふ、そうだろうそうだろう。\n
君が喜んでくれてよかったよ」"

hide m_nai6_6

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がそんな光に見蕩れている間にも、ナイトメアは零れたシャンパンの始末をソツなくこなしてしまっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（おお……、すごいじゃない。\n
手も切らず、失敗もなし）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "感動するより、しみじみと感心してしまう。\n
普段が情けないと、成功すること自体が感心の対象だ。"

play sound se_0575 volume .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前のグラスに、シャンパンが注がれた。\n
薄く黄金色に色づいたシャンパンの中では、小さな気泡がたくさん弾けている。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが席につくのを待って、グラスを持ち上げた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「乾杯しましょうよ」"


show nai_s_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nig_g0170
Nightmare "「そうだな。\n
……君の瞳に？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_8")
T "「……っ、{size=+20}笑い殺す気？{/size}」"

hide nai_s_02_1
show nai_s_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_8")
voice nig_g0171
Nightmare "「それじゃあ……。\n
二人の出会いと、これからに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……それだって、充分恥ずかしいわよ」"

hide nai_s_03_10
show nai_s_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice nig_g0172
Nightmare "「君が嫌なら、別の言葉を探すべきか。\n
もっと恥ずかしい言葉を言ってしまうかもしれないが……、どうする？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……いえ、もう充分だってば。\n
それでいい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここが自分のテリトリーだからか、やけにナイトメアは強気だ。\n
押し負けてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういったシチュエーションの男女としては正しい図かもしれないが、どこか悔しい。"


play music residence_p_wam

show m_nai6_7 onlayer master
with dis
hide nai_s_03_1

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0173
Nightmare "「それでは、二人の出会いとこれからに。\n
……乾杯」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「これからに……。\n
乾杯」"

play sound se_0359
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人、軽くグラスを持ち上げて乾杯の文句を言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グラスをぶつけるタイプの乾杯は、本来正式のものではない。\n
だが、学生同士という感じでもなくて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（マナーだけじゃなくて、崩し方も知っている人なんだな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "雰囲気に流されたか、妙に評価も上がってしまう。"

hide m_nai6_7

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口に運んだシャンパンは、甘すぎず爽やかだ。怒涛のようなロマンチックな演出に、ドギマギとらしくもなく緊張していたのがようやく落ち着く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（……ふう）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「あなた、意外とロマンチストなのね。\n
……あ、意外でもないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（普段から、子供っぽい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "子供っぽさが浪漫に直結するかといったら違うかもしれないが、遊び心や格好つけたがりといったところでは近いものがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……背伸びしたいっていうのは分かるけど」"


show nai_s_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0174
Nightmare "「む……。\n
背伸びなんかでは……、私は大人の男で……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「……悪い意味じゃないわよ。\n
たまになら、こういう肩の凝るような演出もいいわね、ってこと」"

hide nai_s_02_7
show nai_s_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_15")
voice nig_g0175
Nightmare "「むむ……。\n
肩が凝るとは……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……あなただって、でしょう？\n
いつもなら、ちょっと疲れる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_1")
T "「だけど、たまになら……」"

hide nai_s_02_10
show nai_s_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_1")
voice nig_g0176
Nightmare "「今夜は……、特別だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「……うん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひょいと手を伸ばしてさくらんぼを口に運ぶ。\n
甘く、ジューシーな果肉が口の中に広がった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「……美味しい。\n
やっぱり果物は季節のものが一番ね」"

hide nai_s_01_11
show nai_s_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice nig_g0177
Nightmare "「魔法が発達したおかげで、季節を無視して手に入るものも増えたが……。\n
やはり季節のものを季節のときに食べるのが、一番美味だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そういえば……。\n
さくらんぼのへたを口の中で結べる人はキスがうまいって言うわよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「昔そういうの流行って、無意味に試したりしたことない？\n
私、試したことあるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "へたをつまんでぶら下げたさくらんぼ、ちょいと揺らして言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれは、まだ小さい頃のことだ。\n
それがどうしてキスがうまいということになるのかも分からないままに、きゃっきゃとはしゃいで試していた。"

hide nai_s_01_6
show nai_s_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0178
Nightmare "「それで、君は出来たのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「いいえ。\n
あれ、出来る人なんて本当にいるのかしら」"

hide nai_s_01_2
show nai_s_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice nig_g0179
Nightmare "「よし。\n
私も試してみるぞっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もごりと早速ナイトメアが口の中にへたを入れる。"

hide nai_s_02_12
show nai_s_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もごもご。"

hide nai_s_02_7
show nai_s_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もごもごもご。"

hide nai_s_02_9
show nai_s_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もごもごもごもご。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……意地にならなくてもいいと思うわ。\n
たぶん、一種の都市伝説よ」"

hide nai_s_03_5
show nai_s_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice nig_g0180
Nightmare "「……ぬう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しばらく挑戦はしていたものの、やはり、うまくいかなかったらしい。\n
ナイトメアは諦めたように、さくらんぼのへたを吐き出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「別にさくらんぼのへたが結べなかったからキスが下手、なんてことないわよ」"

hide nai_s_02_10
show nai_s_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
Nightmare "「…………」"

play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "次のさくらんぼへと手を伸ばしたところで、ナイトメアの手が私の顎先を掬った。"

hide nai_s_02_7
show nai_s_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0181
Nightmare "「それなら……、試してみてくれ。\n
私が、上手かどうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……それ、口説き文句？」"

hide nai_s_02_2
show nai_s_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0182
Nightmare "「……充分に恥ずかしい、な。\n
ベタかもしれないが、私だって恥ずかしいんだぞ？」"

hide nai_s_01_5
show nai_s_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0183
Nightmare "「背伸びだって……、したくもなるさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか格好がつかないような気もするが、そういう肝心なところで本音を打ち明ける感じがなんともナイトメアらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（背伸びをしても……、最後まではしきれない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな不充分なところが好きだ。\n
充分に恥ずかしい、そういう不充分さが。"


play music starlit_sky_a_wam

show m_nai6_8 onlayer master
with dis
hide nai_s_01_13

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分からもそっと身を乗り出して、らしくもないと思いながらキスを待つように瞼を下ろした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（私……、浮かれている）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "空気にも、シャンパンにも。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頭の芯がふわふわとする。\n
ちゅ、と唇が触れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シャンパンの匂いがする。\n
それから少し思い切ったように、キスをした。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "甘酸っぱい、さくらんぼの味のするキスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_8")
T "（なんて……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ロマンチックなようでいて、まったく締まらない。\n
可愛らしすぎて笑ってしまうような甘い味。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、呼吸があがる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "閉じた瞼の裏でチカチカと光が瞬く。\n
夢から覚めるときの刺激のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0184
Nightmare "「……っは。\n
ど……、どう、だ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……ん。\n
……まだ、分からないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice nig_g0185
Nightmare "「そ、そうか……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_3")
T "「うん、分からないから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_3")
voice nig_g0186
Nightmare "「ん……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「分かるまでしたら、続けてみたらいいんじゃないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice nig_g0187
Nightmare "「そ……、それは名案だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「……ん」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_19")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_19")
Nightmare "「…………」"

hide m_nai6_8


show nai_s_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_19")
voice nig_g0188
Nightmare "「……あ。\n
[firstname]、君が好きだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思い出したように、間抜けた告白。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "キスと同じ。\n
締まらないのに、その瞳は真剣で。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "疑いようもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（……私もよ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "強く思えば伝わるというのならば、きっと届く。\n
思うだけで、伝わる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアにならば、ラブレターなんて必要ない。"

hide nai_s_01_5

$ hi_mes()

scene bg_par15_rg_tow_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_long
##endmemory
jump gakuen_nightmare_end
