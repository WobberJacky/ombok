label gakuen_gray_end:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_tow_day
with dis

play music room1_p_wam

scene bg24_rj_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズの翌日の朝、私は静かにパニックに陥っていた。\n
矛盾しているが、言葉の通りだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "行きはナイトメアが空間を渡らせてくれたから問題なかったし、帰りもグレイが姿隠しの魔法をかけてくれたので、無事に自室に戻ることは出来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "甘ったるく別れのキスをして……、そこまではよかったのだ。\n
部屋に戻って、軽くシャワーを浴びて、制服に着替えて……。"


show m_gre_end1 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_11")
T "（で。\n
どうするのよ、これ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "コレ、とは、首筋にくっきりと残った歯型だ。\n
赤く浮いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "制服に着替えてシャツのボタンをきっちり閉めてみたものの、少しでも動くと見えてしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "虫刺されといって誤魔化せるようなものでもなければ、絆創膏で隠せるようなものでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（グレイったら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうなることが分かっていて痕をつけたのだとしたら、彼も相当な意地悪だ。\n
見せつけることが前提になっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして何より頭が痛いのは、これだけ困っていながらこの痕を魔法で消してしまおうとは思えない私自身。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらく回復魔法を使えば、傷として認識されてこの噛み痕も消えるだろうに。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（……もったいない）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな考えに至る、自分ときたら。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「…………」"

hide m_gre_end1

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「ああ……、もうっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアではないが、逃げ出したくなる。\n
彼と違って、対象がグレイではないのが厄介だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（……むしろ、向かっていっちゃいそう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もう一度シャツを脱いで、試行錯誤することにする。"

with dis
$ hi_mes()

scene bg24_rj_day with Dissolve(.8)
scene bg25_rr_day
with stripe_l_medium

scene bg_par02_ct_tow_day
with stripe_l_long

play music dining_day_p_wam
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カフェテリアに着いたのは、いつもより少し遅い時間。\n
きょろきょろと周囲を見渡すが、空いている席を見つけるのは難しそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "時間が遅くなってしまった分、人が多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（テイクアウトで、教室で食べるしかないかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、以前にグレイがして見せてくれたようにうまく出来るかどうか、\n
試してみようとしたところ、聞き覚えのある声が届いた。"


show tower_a2_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0067
Seito "「[firstname]、こっちこっち！\n
席一つ、空いているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔見知りの女子生徒が、手を振って合図してくれている。\n
見れば、その言葉通り、席が一つ空いている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「そこいいの？」"

hide tower_a2_3
show tower_a2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice hei_g0068
Seito "「よくなかったら、声をかけていないわよ。\n
ほら、どうぞ」"

play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ありがとう。\n
助かったわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "がたんと椅子を引いて、その席へと座る。\n
時間もそうあるわけでもないので、さっそく朝食を呼び出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "定番なのに変わりはない。\n
こんな朝こそ、いつも通りが一番だ。"

hide tower_a2_2
show tower_a2_2 at left
with dis

show tower_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0087
Seito "「おはよう、[firstname]。\n
今日は遅かったのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「おはよう。\n
今日はちょっと、寝坊しちゃったのよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼやく口調で言いながら、トーストを齧る。"

hide tower_a2_2
show tower_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0069
Seito "「ああ、昨日はブリーズだったものね。\n
それで興奮して眠れなかったの？」"

hide tower_b1_3
show tower_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0088
Seito "「……あら？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜のブリーズについてを私が答える前に、向かいに座っていた女子生徒が小さく声をあげた。\n
私の首筋に向かって、指をさしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（……来たっ）"

hide tower_b1_9
show tower_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice chi_g0089
Seito "「どうしたの、それ。\n
……暑くない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（うん、暑い）"

hide tower_a2_8
show tower_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice hei_g0070
Seito "「なになに？\n
あら、あなた、シャツの下にハイネックを着ているの？」"

hide tower_a1_5
show tower_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice hei_g0071
Seito "「変なの……。\n
暑いでしょうに」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（そうそう。\n
変よね、不審よね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "首筋にある歯型を見せて歩くわけにもいかないし、だからといって消してしまうのも惜しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこで最終手段として、シャツの下にもう一枚薄手のハイネックを着ているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寒さの厳しい冬には珍しくもない格好だが、もう春も半ばを過ぎている。\n
よほどの寒がりでもなければ、こんな格好はしていないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怪訝そうな二人へと、私はがっくりと肩を落として見せた。\n
演技は、大袈裟なほうがいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「昨日ね、ブリーズの始まる前にナイトメアの釣りに付き合ったら酷い目にあったのよ。\n
もう全身ぐっちょぐちょ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「寮に戻ってから、寒気はするし頭は痛いわで……。\n
暖かくなってきたからって、油断ならないわよね」"

hide tower_a1_1
show tower_a1_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice hei_g0072
Seito "「そ、それは災難だったわね。\n
ああ、それで今日、厚着をしているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_9")
T "「ええ、そういうこと。\n
寒気がするのよ」"

hide tower_a1_4
show tower_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_9")
voice hei_g0073
Seito "「休まなくて平気？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「ええ、授業を休むほど熱があるわけでも、具合が悪いわけでもないから。\n
でも、悪化させると、まずいじゃない？」"

hide tower_b1_4
show tower_b2_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice chi_g0090
Seito "「そうね、暖かくするのは大事だわ。\n
それじゃあもしかして……、あなた、昨日のブリーズは？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……残念ながら不参加よ。\n
ベッドで、ナイトメアを呪っていたわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "冗談交じりに、愚痴っぽく言う。\n
実際ナイトメアの釣りに巻き込まれ、びちょびちょにされたのは事実なので、すべてが嘘というわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_6")
T "（なんだっけ……。\n
嘘をつくときは真実を混ぜろ、だっけ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一から十まですべてを嘘で固めるよりも、二割から三割の真実を混ぜるとバレにくいという説がある。\n
この場合もそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "体調不良や、シャツの下のハイネック着用の理由については嘘だが、ナイトメアの釣りに付き合って酷い目にあったというのは真実。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達にとって特に追及しなくてはいけないという範囲でない嘘ならば、この程度でも充分に誤魔化されてくれるはず。"

hide tower_b2_8
show tower_b2_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0091
Seito "「ストームのときといい、あなたって、ついていないわねえ……」"

hide tower_a1_5
show tower_a2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0074
Seito "「でも、よかったじゃない！\n
風邪を引いたのがストームじゃなくてブリーズだっただけ、よかったと思うわ！」"

hide tower_b2_1
show tower_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0092
Seito "「ああ、そうかもね、ストームはタイミングが命ですもの。\n
参加しそびれると、とても寂しいことになるわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あ、確かに」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "サラダを口に運びながら彼女達に同意する。\n
ストームは、新入生の女子生徒に対する不意打ちのサプライズイベントだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それを新入生で経験しないまま進級してしまうと、もはやサプライズではなくなってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これから先、私がシンフォニアに在籍している限り、ストームとブリーズは毎年やってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、ストームのサプライズが楽しめるのは、何も知らない新入生のときだけ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「私のブリーズは、気長に来年やり返すことにするわ」"

hide tower_b2_3
show tower_b2_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice chi_g0093
Seito "「前向きなのはいいことよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（うん。\n
来年は、自力で抜け出せるようになっていたらいいわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「そうね、前向きに考えているの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言えないことは多いが、会話は成立している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアの手を借りず、自力でトラップを抜けることが出来るようになっていたらいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな不穏な希望を抱きつつ、朝食を食べ進めた。"

hide tower_a2_2

hide tower_b2_2

with dis
$ hi_mes()

scene bg_par02_ct_tow_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_par16_rs_tow_day
with stripe_l_long

play music drawingroom_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブリーズが終わったことで、グレイにとって多忙な期間も無事に終了したようだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "元々、ブリーズの寸前には、例の密栽培の件もどうにか片付いていたらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなわけで、ようやく戻ってきた穏やかな放課後。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつものように顔を出した医務室では、以前と同じように、グレイがナイトメアを缶詰にしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"


scene m_cut_gre_end1u
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今までと違うのは、机の上に積みあがった書類の量が未だかつて見たことのないような量に達している点だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……新記録だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "書類の向こうからナイトメアの呻き声が聞こえるものの、書類の山に遮られているせいで、紙の束が泣いているようにも見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「どうしたの、その量。\n
……なんだか、すごいわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここまでくると、壮観だ。\n
呆れるを通り越す。"


scene m_cut_gre_end1
with dis

show gre_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0218
Gray "「ああ、俺が医務室に寄れないでいる間、ナイトメア先生は随分と羽を伸ばされたようだからな。その埋め合わせをしていただいているところだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（さては、隠していたわね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイを見習ってビシバシと仕事をやらせてきたつもりではあったが、どうやらナイトメアは未処理の書類をこっそり隠していたようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうでなければ、ここまで溜まる前に、私だって手を打った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……ごめんなさい。\n
グレイがいない分、私が仕事させようとはしたんだけど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見抜けなかったのは、私のミスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "申し訳程度に仕上げた書類も幾つかあるわけだが、今こうして山になっている未処理の束に比べると微々たる量。"

hide gre_m_01_5
show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0219
Gray "「ああ、それでこちらに処理済の書類があったのか。\n
ありがとう、[firstname]」"

hide gre_m_01_4
show gre_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0220
Gray "「ナイトメア先生に仕事をしていただくのは大変だっただろう？\n
俺が忙しい間、君がナイトメア先生の面倒をみてくれていたんだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0351
Nightmare "「こらグレイっ！\n
おまえ、上司に対して留守中のペットのような言い方をするんじゃない！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「そうね、ペットじゃなくて、子供のお守りでもいいかもね」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0352
Nightmare "「むむむ！\n
君まで、そんなことを言って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「反論できるの？\n
こんなに溜め込んでおいて」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段勉強を見てくれる親がいないすきに遊びまわり、結果として宿題を溜めて苦しむ子供のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰でも一度は経験のある、長期休み終了前の一夜漬けを思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も昔一度経験して、もう二度とあんなギリギリな体験はすまいと学んだ記憶があった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういった溜め込んだ宿題で一番大変だったのは、簡単なイメージのある日記だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "通常の日記ですら何十日分かをまとめると辛いというのに、魔法植物の観察日記ときたら……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……っと、脱線した。\n
さすがに、書類仕事に日記は含まれないわよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_1")
voice nig_g0353
Nightmare "「ううう。\n
日誌なんて、書かなくてもいいと思わないか……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……{size=+20}含まれるの？{/size}）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日記ではなく、日誌のようだが。\n
似たようなものだろう。"

hide gre_m_03_11
show gre_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0221
Gray "「駄目ですよ。\n
ちゃんと書く癖を普段からつけておかないから、こうやって俺がいないだけで白紙が続くんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0354
Nightmare "「そもそも、日誌なんて誰かに提出するものでもないだろう！？\n
見るのはおまえだけだ！」"

hide gre_m_01_9
show gre_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0222
Gray "「チェックしないと、書いてくださらないからですよ。本当は俺だってチェックなんてしたくありませんし、自主的に習慣化していただきたいんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0355
Nightmare "「習慣というのは、日常においてこそ許されるものだろう！？\n
今は特例！」"

play sound se_0529
play sound se_0527
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0356
Nightmare "「私が自分で言う言葉じゃないかもしれないが、未処理の書類の山がこれだけあるんだっ！\n
日誌は眼を瞑るべきじゃないか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……本当に、あなたの言っていい言葉じゃないわね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、間違えてはいない。\n
日誌がグレイへの連絡事項をメインにするものであるのなら、それは後回しにしてもいいものではないだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（珍しい……。\n
そういう、やらなくてもいい仕事とやらなくてはいけない仕事の優先順位を、グレイが見誤るだなんて）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まず、何から手をつけなくてはいけないのか。\n
どういう順番に処理していけば効率よく仕事が終わるのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "作業計画を作るのはグレイの仕事だ。\n
……それが、本来の執務長の仕事であるのかどうかはさておくとして。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0357
Nightmare "「いいか、[firstname]！\n
こいつはな、私に対して怒っているんだ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0358
Nightmare "「こいつが仕事で忙しく動けないでいる間、私が君と遊んでいたから！\n
やきもちを妬いているんだぞ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そんな、グレイに限って……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は大人だ。\n
確かにやきもち妬きな部分もあるが、だからといってそれを仕事に持ち込むようなことはないはず。"

hide gre_m_01_13
show gre_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0223
Gray "「ははは、そんなことはないですとも。\n
俺はただ、やるべきことをきちんとやり遂げることの大事さを理解していただきたいだけですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ほら」"


scene bg_par16_rs_tow_day
with dis
hide gre_m_03_4
show gre_m_03_4 at left
with dis

show nai_m_02_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice nig_g0359
Nightmare "「こんなあからさまな芝居に騙されるな、[firstname]！\n
ふん、こいつのことだ、君にも何か……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが、書類の山の脇から顔を出す。\n
私が医務室を訪れて、初めてナイトメアと目が合った。"

hide nai_m_02_5
show nai_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Nightmare "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「…………」"

hide nai_m_01_2
show nai_m_01_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice nig_g0360
Nightmare "「……暑くないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、シャツの下に着たハイネックの存在に気付かれてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の生徒に対しては、ナイトメアと水遊びしたせいで風邪を引いたという話で通してきたわけだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがにその片棒を担いだことになっている彼本人にその言い訳は通用しない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、ここにはその犯人たるグレイ張本人がいるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "助けを求めるように視線を投げかけると、涼やかな表情でしれっと微笑みかけられて終わった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（グ、グレイのせいなのにっ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイが、歯を立てて噛み付いたりなんかするから悪いのだ。\n
私の首筋に顔を寄せて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（～～～っ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "連想的に昨夜のことを思い出してしまいそうになって、頬が火照る。\n
そんな私の恥ずかしい回想を止めたのは、ナイトメアの盛大に苦しむ声だった。"

hide nai_m_01_12
show nai_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0361
Nightmare "「～～～うっ！！\n
グレイ、おまえ……っ、なんて破廉恥な……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔を上げると、ナイトメアが顔を真っ赤にして机に突っ伏している。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（どうしたの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か、ナイトメアが赤くなるような要素がどこかにあっただろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "口には出していない。\n
考えただけで、独り言も言っていないはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "状況が分かっていないのは、どうやら私だけらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイとナイトメアはお互いしっかり通じ合っているのか、私を置き去りに会話が進んでいく。"

hide gre_m_03_4
show gre_m_03_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0224
Gray "「おやおや、ナイトメア先生、どうしたんですか？\n
いけませんよ、覗き見なんて悪趣味です」"

hide gre_m_03_1
show gre_m_02_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0225
Gray "「覗き見は癖になるといいますからね。\n
癖になる前に、徹底的に叩き直しておくべきでしょうか」"

hide nai_m_02_10
show nai_m_03_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0362
Nightmare "「だから！\n
おまえは目が笑ってないんだ！！」"

hide nai_m_03_3
show nai_m_03_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0363
Nightmare "「……っ、なんだ、そんなに私が彼女と釣りをしたりなんだりと、おまえがいない時間を満喫したのが不満か！？」"

hide nai_m_03_8
show nai_m_02_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0364
Nightmare "「ああ、そうだろう、そうだろう！\n
不満で堪らないんだな！？おとなげない！」"

hide gre_m_02_1
show gre_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0226
Gray "「いえいえ？\n
俺は心の広い大人の男ですから」"

hide gre_m_03_4
show gre_m_01_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0227
Gray "「そんなことはないですよ？\n
俺がいない間、あなたに構ってくれていた彼女に感謝しているぐらいです」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つらつらと語るグレイだが、私にはその背中しか見えない。\n
彼が、目の前にいるナイトメアに対してどんな顔をしているのかは分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "分からないが……、赤から青に変わっていくナイトメアの顔色に、だいたいの想像はつく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……何が、どうなっているの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気になるが、それを聞いてしまうと、私も藪から蛇を出してしまいそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "主従というのは心で繋がっているものらしいので、きっとそういうことなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういうことにしておいたほうが、きっと平和だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（放っておこう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "積み上げられた書類の中から、私が手伝えそうなものを探すことにした。"

hide gre_m_01_1

hide nai_m_02_6

with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

scene bg_par16_rs_tow_eve
with dis

play music drawingroom_nig_p_wam

scene m_cut_gre_end2
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局、その日のうちで、あれだけ山になっていた書類が片付くわけもなく。\n
どうするのかと思っていれば、グレイは満足げに処理済の書類の束を手にとった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "未処理の書類の量で脅しをかけて仕事をさせたものの、そう差し迫ったものは多くないということだったようだ。"


show gre_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0228
Gray "「今日一日でこれだけ片付けば、まあ、充分でしょう。\n
明日もこの調子でお願いしますね、ナイトメア先生？」"

hide gre_m_02_1
show gre_m_02_1 at left
with dis

show nai_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0365
Nightmare "「……無理だー。\n
死んでしまうー」"

hide gre_m_02_1
show gre_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0229
Gray "「まだ死んでいないので大丈夫ですよ。\n
……さあ、[firstname]、女子寮の方まで送っていこう」"

menu:
    "お願いする。":
        jump gakuen_gray_end2a
    "断る。":
        jump gakuen_gray_end2b
label gakuen_gray_end2a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ありがとう、お願いするわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の申し出を素直に受ける。\n
目の前のナイトメアが少し驚いたように瞬くのが分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨日までの私だったら、もっと意地をはって「一人で大丈夫だ」とグレイの申し出を断っていたと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あるいは従うにも言い訳を作っただろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "主に仕事をしたのはナイトメアだが、その監督や、下準備の段階で彼も疲れているはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、これまでだったら「グレイも疲れているんだから休んだほうがいいわ。私も一人で帰れるから」だとか言ってしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、彼のその親切な申し出がただの親切でないことを私はもう知っている。\n
送ろうという申し出は、二人の時間を捻出したいという彼なりの要望だ。"

jump gakuen_gray_end3
label gakuen_gray_end2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「大丈夫よ？\n
あなただって疲れているんだから、休んだほうがいいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "主に仕事をしたのはナイトメアだが、その監督や、下準備の段階で彼も疲れているはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もうそろそろ夕食の時間というだけあって、外ではもう夕闇が迫りつつある時間。\n
だが、女子寮までの移動はあくまで塔の中で、何も危ないことなどない。"

hide gre_m_03_4
show gre_m_02_14 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0230
Gray "「俺が送りたいんだ。\n
……君といたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストレートに打ち明けられて、頬が熱くなった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_19")
T "（……そっか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜互いに話して、すれ違いがあったことに気付いたばかりだったのに、また同じことをしてしまうところだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「そうね。\n
それなら、お願いするわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私だって、彼と一緒にいたいと思う気持ちは同じだ。"

jump gakuen_gray_end3
label gakuen_gray_end3:
hide gre_m_02_14
show gre_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0231
Gray "「ありがとう。\n
それでは、行こうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ええ」"

hide gre_m_02_2

hide nai_m_01_4

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……おかしな感じ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "送っていこうとの親切な申し出を受けただけなのに、お礼を言われてしまう。\n
促されて、私はドアへと向かった。"


show nai_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0366
Nightmare "「部下にいじめられ、こき使われ……。\n
あげく、イチャイチャっぷりを見せつけられる私……、なんて不幸なんだー……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐったりと机にのびたナイトメアが呻く。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（こき使われないよう、仕事を溜めなければいいと思うんだけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアには貸しもあったが、借りもある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（次は、もっと手伝ってあげよう）"

with dis
$ hi_mes()
hide nai_m_03_2


scene bg_par16_rs_tow_eve with Dissolve(.8)

play music evening_a_wam

scene bg25_rr_eve
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイは、女子寮側の入り口まで送ってくれた。\n
それまで、他愛のない話をする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ありがとう、グレイ。\n
また明日ね」"


show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0232
Gray "「ああ、そうだ。\n
もう一度、改めて外出に誘わせてもらってもいいだろうか」"

hide gre_m_01_4
show gre_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0233
Gray "「前回駄目になってしまってから、俺も街には出掛けられていないんだ。\n
君さえよければ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この誘いに関しては、考えるまでもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「行くわ。\n
是非、ご一緒させて？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "即答で返事を返すと、彼も嬉しそうにしてくれる。\n
一度駄目になってしまったからこそ、思い入れもあった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「次の休みでいいのかしら。\n
外出の申請をしておかないと」"

hide gre_m_01_8
show gre_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice gra_g0234
Gray "「そちらは俺がしておくよ。\n
どのみち、許可を出すのは俺だからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……あ。\n
そういえばそうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒の外出許可などの管理をするのも、彼の仕事だ。\n
その彼と一緒に出かけるのだから、許可の心配をする必要はなかった。"

hide gre_m_03_9
show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0235
Gray "「前回の罪滅ぼしに、いろいろと面白いところを案内しよう。\n
楽しみにしていてくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「もちろん、楽しみにしているわ。\n
……今度は邪魔が入らないよう、祈っておくわね」"

hide gre_m_02_2
show gre_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_8")
voice gra_g0236
Gray "「……すごいタイミングだったからな、前回は。\n
さすがに続いたら、俺も仕事を放り出しそうだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_4")
T "「……ナイトメアみたいに？」"

hide gre_m_02_3
show gre_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_4")
voice gra_g0237
Gray "「……叱れなくなるから、秘密にしておいてくれ」"

with dis
$ hi_mes()
hide gre_m_02_8


scene bg25_rr_eve with Dissolve(.8)

scene bg_par15_rg_tow_eve
with stripe_l_medium

scene bg06_sk_h_eve with stripe_l_medlong

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1)

play music view_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "約束の日、私は先週と同じように少し大人っぽいワンピースに着替えた。\n
そして約束の時間十分前につくように部屋を出る。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_12")
T "（……ドキドキするなあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "前回が直前でのキャンセルに終わってしまったこともあり、頭のどこかで万が一の可能性を覚悟はしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "また今回も何かあるのではないかという不安と、楽しみとで半々だ。\n
そうして階段を下りてエントランスに向かい……、その半分は霧散した。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "約束の時間の十分前、そこにはもうグレイが待っていてくれたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_13")
T "（やっぱり……、十分前行動の人だったんだ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "あの日、わくわくしながら待ち合わせに向かった。\n
そのときの想像通り。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_2")
T "「グレイ！」"

show m_gre_end2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_2")
Gray "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "早足に駆け寄った私に、グレイが息を飲む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "普段の制服姿とは違う。\n
こうした私服姿が、彼の目にも新鮮に映ってくれるといい。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0238
Gray "「……よく似合っているよ、[firstname]。\n
前回も、こんなふうに服を選んでくれたのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_1")
T "「もちろん。\n
今回は前回用意しておいた分、悩まないですんだけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "ひょいと肩をすくめ、冗談めかして言う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "お互い前回のことをあまり気にしないようになっている。\n
こうして、気軽に口に出せるようになってよかった。"

hide m_gre_end2
show m_gre_end3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0239
Gray "「ああ、でも……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "すっと伸ばされたグレイの指先が、私の首筋に触れる。\n
つい先日まで、噛み痕が残っていた箇所だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "ぎりぎり間に合って消えてくれたおかげで、私はこうして少し胸元のあいたデザインのワンピースを着ることが出来た。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "もし間に合っていなければ、また何を着るべきかと一から悩んでいたことだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0240
Gray "「その服が着れるように傷が癒えてよかった……、と言わなければいけないところなんだろうが」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0240_5
Gray "「それを残念に思う俺は、やっぱりろくでもないんだろうな」"


scene bg_par15_rg_tow_day
with dis
hide m_gre_end3

play sound se_0384
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "本気ではそう思っていないような口調で言って、グレイがゆっくりと歩き出した。\n
その隣を、私も歩く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "こうしてエントランスで堂々と待ち合わせなどしたら目立ってしまうかとも心配したが、杞憂だったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "私は、放課後になるとナイトメアの医務室に入り浸り、その仕事を手伝っている。\n
そのことはすでに、塔の生徒の間で周知の事実になっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "だからこうしてグレイと並んで歩いていても、仕事絡みだと判断してくれるのだ。\n
今回も、きっと外から見たならば、買出しのお手伝いといったところだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_6")
T "（よかったような、物足りないような……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_06_11")
T "（……買出しっていうのは当たっているし）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "完全な休日というわけではなく、公用も含んでいる。\n
それでも、私達にとって、これは間違いなくデートだ。"


scene bg25_rr_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_05_5")
T "（……あれ？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_2")
T "「ねえ、街まではどうやって移動するの？\n
箒じゃないの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "グレイの歩く先。\n
外に向かうのではなく、エントランスから使用人達が待機するのに使う部屋に向かっているのに気付いて声をかけた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "今まで、休日になると箒に跨り出掛けていく生徒の姿を見ていたこともあり、きっと箒だろうと思っていたのだ。"


show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0241
Gray "「最近、街のほうにある店とうまく交渉が成立して、移動用の魔法陣を置かせてもらえることになったんだ。\n
今日はそれを使おう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_14")
T "「へえ！\n
そんなものがあるのね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_04_12")
T "「でも、それって……、私も使っていいの？」"

hide gre_m_02_2
show gre_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_04_12")
voice gra_g0242
Gray "「……特権ということで」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_7")
T "「……本当に、ナイトメアのことを叱れなくなっちゃうわね」"

play sound se_0285
hide gre_m_02_9


scene bg_par26_sr_kn
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "移動専用の部屋なのか、中に家具などは置かれていない。\n
ただ部屋の中央に、結構な大きさの魔法陣が描かれている。"


show gre_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0243
Gray "「さ、魔法陣の中に入ってくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_15")
T "「は～い」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "促されて、魔法陣の中へと足を踏み入れた。"

play sound se_0496

show magic_g onlayer master with Dissolve(1.5)
hide gre_m_03_10
show gre_m_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
Gray "「…………」"

hide magic_g with Dissolve(1.5)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "低く、呪文を詠唱する声が響く。"

hide gre_m_01_13

play sound se_0742
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "そうして魔力が通されると同時に、魔法陣が光を放ち、足元で風が渦を巻く。"

play sound se_0730

scene white with Dissolve(2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "真白な光が溢れて、目を開けていられない。\n
足元から吹き上がる風がごうっと強くなって……。"

pause .20



play music study_taught_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0245
Gray "「……着いたぞ。\n
大丈夫か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_2")
T "「……え？」"


scene bg_par26_sr_ka with open_m
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "すぐ傍から声をかけられて、目を開けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_4")
T "「わ……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "目を開いて飛び込んできたのは、先ほどまでいた小部屋とは違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "足元に魔法陣が描かれているのは同じだが、周囲には様々なマジックアイテムが陳列されている。"


show gre_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0246
Gray "「さあ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_05_7")
T "「？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "先に魔法陣から出たグレイに手を差し伸べられて、戸惑った。\n
別に、足場が悪いわけではない。"

hide gre_m_01_4
show gre_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0247
Gray "「学校では、あまりこういうことは出来ないだろう？\n
せめてデートのときぐらいは、な」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_9")
T "「……今日は、特例ばかりね。\n
でも、そうね、デートだし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "学校では、あくまで、忙しい執務長とそれを手伝う女子生徒といった関係だ。\n
だが、こうして学校の外に出た今ならば、堂々と恋人らしく振る舞える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "差し出されたグレイの手をとると、腕へと誘導された。\n
彼の腕に手を絡め、魔法陣の外へと足を踏み出す。"

with dis
$ hi_mes()
hide gre_m_01_7


scene bg_par26_sr_ka with Dissolve(.8)

scene bg_par22_mi
with stripe_l_long

play music district_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "地下室のような場所から階段を上り、ドアを開ける。\n
なんと、店に直結していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "どうやらここは、マジックアイテムを専門に扱う店らしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "魔法学校に通っているのだから、当然、マジックアイテムには馴染みがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "しかし、ここには、普段の学校生活では見ることがないようなものも一緒に陳列されていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_06_5")
T "（……何に使うのかしら）"


show gre_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_5")
voice gra_g0248
Gray "「まず、先に学校の用事を終わらせてしまってもいいか？\n
そうしたら、後は自由だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_10")
T "「そうね……。\n
用事から、先に終わらせてしまいましょうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "グレイが懐からメモを取り出し、買出しに必要なものを読み上げる。\n
私は、それを一緒になって探す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "こうやって学校の仕事を一緒にしているだけでも、場所が校外であるだけで充分にデートらしい。\n
腕を組んで、寄り添って歩く。"

with dis
$ hi_mes()
hide gre_m_02_9


scene bg_par22_mi with Dissolve(.8)

play music flower_day_p_wam

scene bg11_ct_day
with stripe_l_long
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "マジックアイテムの店を出て、他にも何軒か。\n
そうこうして、ふとグレイが足を止めたのは小さな雑貨屋だった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_15")
T "「？\n
ここでも、何か買うものがあるの？」"


show gre_m_02_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_15")
voice gra_g0249
Gray "「ああ、ここは俺のお気に入りの店なんだ。\n
……可愛いものが、たくさん置いてある」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_2")
T "「……え？」"

play sound se_0198
##special anime"kirakira_center"loop="false"time="1000"]
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "聞き間違えかと思って見上げた先、グレイは目をきらきらと輝かせて店先を覗いている。"

##[anime]
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "彼は迷いなく、その店の中へと足を踏み入れていった。"

play sound se_0774
hide gre_m_02_14

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_6")
T "（……可愛いもの？）"


scene bg_gen22_zk_day
with dis

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "疑問に思うものの、一緒になって店内を見てまわる。"


play music forest_town_square_p_ali
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_13")
T "（なるほど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "可愛いものがたくさん置いてあるという言葉は、すぐに実感として理解できた。\n
ここは、女性向けのマジックアイテムの専門店なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "女性限定というわけではないが、客には女性が多い。\n
それが明らかな品揃え。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "普通だったら、シンプルな形をしていることの多いマジックアイテムに、いろいろとデザイン性を持たせている。\n
……主に、可愛いデザインに。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "効果を読めばよく知るものも、ここでは知らないマジックアイテムのように見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "とにかく、何もかもがファンシーなアレンジを加えてあるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "物珍しくてきょろきょろとしているところで、グレイに声をかけられた。"

show m_gre_end4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0250
Gray "「[firstname]、君は猫と小鳥だとどちらが好きだ？\n
俺としては猫がいいかとも思ったんだが、小鳥も捨てがたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "振り返れば、彼はなにやら眉間に皺を寄せ、真剣な顔で二つのアイテムの間で悩んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "どちらも、何の変哲もないレターセットに見えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "何の変哲もないが……、やたらとファンシーな……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_05_5")
T "（……あ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "思い出す。\n
私が多忙にしていた間、グレイはいつもココアとメッセージとを届けてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "そのメッセージを再生してくれた、可愛らしい謎の生物。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_02_17")
T "（あれ、グレイの趣味だったんだ……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "女子生徒に宛ててということで、わざわざ可愛らしいマジックアイテムを選んでくれたのだとばかり思っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "もちろん、それもあるはずだ。\n
相手が私だからこそ、グレイも躊躇いなくああいったアイテムを使えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "さすがに、あのレターセットで、他の使用人や他寮の寮長に宛てたメッセージは飛ばせまい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_1")
T "「……ふふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "小さく笑ってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "私のためだと思っていたことが、彼自身の趣味だった。\n
だが、残念に思うどころか嬉しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "彼は気遣いのできる優しい大人の男性だが、それだけではないことが嬉しいのだ。\n
そういった面も見せてくれることが。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_18")
T "「……どっちにしようか、迷っているのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_02_18")
voice gra_g0251
Gray "「ああ、決められない。\n
俺はどちらも可愛く思うが……、君はどちらが好きだ？」"

menu:
    "小鳥が好き。":
        jump gakuen_gray_end4a
    "猫のほうが好き。":
        jump gakuen_gray_end4b
label gakuen_gray_end4a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_03_15")
T "「そうね……。\n
私は、小鳥がいいと思うわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_1")
T "「いかにもメッセージを届けてくれたっていう感じがするじゃない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "イメージ映像として展示されている図も、ふっくらとしたすずめのようで、とても可愛らしい。"

jump gakuen_gray_end5
label gakuen_gray_end4b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_1")
T "「私は、猫がいいわ。\n
実家で飼っているの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "馴染みがあるだけに、猫に惹かれた。\n
可愛い動物の代表格でもある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "傍に展示されていたイメージ映像も、まんまるな黒猫で、とても可愛らしい。"

jump gakuen_gray_end5
label gakuen_gray_end5:
hide m_gre_end4
show m_gre_end5 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0252
Gray "「そうだな。\n
それじゃあ、君が選んでくれたほうにするとしよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "あれだけ悩んでいたはずなのに、グレイはあっさりと私が選んだほうを手にとった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "そんなにあっさりと同意されてしまうと、こちらのほうが選択を迷い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_2")
T "「いいの？\n
もう一つのほうも、どちらも選べないから悩んでいたんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_02_2")
voice gra_g0253
Gray "「はは、君に送るラブレターだ。\n
君に選んでもらったものなら、はずれはしない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_05_7")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_02_3")
T "（ラブレター）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "頭の中に、以前渡すことが出来ないままに終わってしまったラブレターのことが蘇る。\n
好きだった彼のこと、姉のこと……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "私は、あの渡せなかったラブレターをどう処理したのだったか。\n
思い出すことも出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "今、思い浮かべることが出来るラブレターのイメージは、夜のココア。\n
見下ろす、煙草の灯り。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "以前とは、まるで違う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_15")
T "「ねえ、グレイ。\n
もう一つのほう、私が買ってもいいかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_15")
voice gra_g0254
Gray "「ああ、気に入ったのか？\n
それならば一緒に……」"

hide m_gre_end5
show m_gre_end6 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_2")
T "「駄目よ。\n
これは私が買うの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "一緒に会計をすませてしまおうと手をのばしてきたグレイから、さっともう一つ残っていたほうのレターセットを攫った。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "グレイが、少しだけ傷ついたような顔をする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_01_1")
T "（そんな顔をしても駄目）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "この人は、隙さえあれば私を甘やかしてしまおうとしているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "だが、これは譲れない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "大人になりたいだとか、自分の欲しいものは自分で買うのが自立の証だとか、そういった意地っぱりなことではなくて……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "私もまた、ラブレターを書いてみようと思ったのだ。\n
そのためのレターセットは、自分で買わなくては。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_02_18")
T "「私も、あなたに手紙を書きたいの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "そして、手渡しで送りたい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "あのときと違って、機を逃したりしない。\n
迷わず、渡せる。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0255
Gray "「君は、本当に俺を嬉しくさせるのが上手だな。\n
……俺に、ガキみたいな真似をさせるのも」"


play music flower_eve_p_wam
hide m_gre_end6
show m_gre_end7 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_05_5")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "その言葉の意味を捉えかねて、隣を見るのと同じタイミングで、ちゅっと小さな音がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "唇に掠めるように触れた柔らかな感触と、苦味を帯びた香りが残る。"

hide m_gre_end7
show m_gre_end8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_06_7")
T "「～～～……！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "慌てて周囲を見た。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "運がいいことに、他のお客さん達もそれぞれ自分達の手元にあるマジックアイテムに夢中になっていて、誰もこちらの様子に注意を払ってはいなかったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_01_8")
T "「ひ、人前よ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "ただでさえ、私達は普通の恋人ではない。\n
知られてはまずい立場にある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "このデートでさえ、リスキーなもの。\n
とても大人がやるようなことではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_06_16")
voice gra_g0256
Gray "「人前で、こういうことがしたくなるぐらいには嬉しかったんだ。\n
ガキみたいだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_s_05_10")
T "「お、大人のくせに……」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_s_05_10")
voice gra_g0257
Gray "「そうだな、大人だから、図々しいんだ。\n
……さ、レジへ行こうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "何事もなかったように背を軽く押され、二人並んでレジに向かう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_s_02_7")
T "（子供みたいなことをしても……、やっぱり大人）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "私には、何食わぬ顔など出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_s_06_16")
T "おそらくは、受け取ってもらえると知ったラブレターを渡す、そのときでさえ。"


##[bgimage ##instant]
hide frame_par_togaki
hide ali_s_06_16
with Dissolve(2)
##[clearmessage time="2000"PAY ATTENTION="false"]
hide m_gre_end8
show white onlayer master
with compress_extralong
hide white with compress_extraextralong
pause 1
stop music

##endmemory
jump gakuen_a
