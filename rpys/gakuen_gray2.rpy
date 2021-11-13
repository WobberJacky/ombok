label gakuen_gray2:
scene bg_map_day
with dis
$ clockanim()


play music flower_day_p_wam

scene bg06_sk_h_day with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以来、ナイトメアを探すグレイを見かける度に、私は手伝いを申し出るようになっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、偶然に頼るのは最初の二、三回まで。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最終的に、放課後になるとナイトメアの医務室へと顔を出し、グレイに合流することが私の日常になった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアが見つかれば、医務室まで連行。\n
その場合、お礼として医務室でココアをご馳走してもらう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見つからなかった折には、二人で屋上へと向かう。\n
そこで、カフェテリアでテイクアウトしたココアとコーヒーで休憩するのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どちらに転んでも、私にとっては嬉しい事態だ。\n
普段は接することのない相手と、時間を過ごせる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "慣れてきた学園生活の中、刺激になっていた。\n
グレイは真面目な男性だが、私にとっては新鮮な面も多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、たまにナイトメアが真面目に仕事をしていると残念に思ってしまったりもする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "本末転倒だが、それではグレイと過ごせない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな毎日を過ごすうちに、ナイトメアから不満が出てきた。"


scene bg_par16_rs_tow_day
with stripe_l_long

play music nightmare_t_ali

show nai_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0256
Nightmare "「ずるい！\n
ずるいぞ、[firstname]！！」"

hide nai_m_03_2
show nai_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0257
Nightmare "「どうして君はグレイだけ手伝うんだ！\n
グレイを手伝うならば、私を手伝ってくれてもいいじゃないか！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「えー……？」"

menu:
    "ナイトメアを手伝う。":
        jump gakuen_gray2_2a
    "断る。":
        jump gakuen_gray2_2b
label gakuen_gray2_2a:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何度も来ているせいか、ナイトメアの医務室が居心地よくなってしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "話し相手として居座るよりも、何かしら手伝えることがあったほうが更に過ごしやすくなりそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「分かったわ、あなたの仕事も手伝ってあげる。\n
その代わり、真面目に仕事しなさいよね」"

hide nai_m_03_8
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice nig_g0262
Nightmare "「ふはははは、私はいつだって真面目だとも！！\n
よし、君は今日から特別執務官だ！」"

jump gakuen_gray2_3
label gakuen_gray2_2b:
$ lovechara_gray_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「あなた、手伝うほどの仕事をしていないでしょうに。\n
そういうことは、もっとまともに働いてから言いなさいよ」"

hide nai_m_02_4
show nai_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice nig_g0258
Nightmare "「むむ……。\n
痛いところをつくな、君は」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういう発言が出てくるあたり、己が仕事をグレイに押し付け気味であることに対する自覚はあったらしい。"

hide nai_m_02_9
show nai_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0259
Nightmare "「だが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にやりと、ナイトメアが悪役めいた笑みをその顔に浮かべた。"

hide nai_m_02_1
show nai_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0260
Nightmare "「私を手伝えば、グレイと過ごす時間は増えるぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それは魅力的だ。\n
グレイもそうだが、この医務室は居心地がいい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……変な誤解はしないでよ？\n
グレイは友人よ」"

hide nai_m_02_3
show nai_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nig_g0261
Nightmare "「ああ、だが、その友人と堂々と一緒にいられる場所がほしくはないか？\n
ここなら、誰に見られることなくのんびりできるぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こそこそとグレイ本人に聞こえないよう、小声で話し合う。\n
まるで、取引のようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………。\n
……分かったわ、手伝ってあげる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「その代わり、真面目に仕事しなさいよ？\n
サボりは許さないから」"

hide nai_m_03_1
show nai_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_12")
voice nig_g0262
Nightmare "「ふはははは、私はいつだって真面目だとも！！\n
よし、君は今日から特別執務官だ！」"

jump gakuen_gray2_3
label gakuen_gray2_3:
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "調子にのって高笑いをあげるナイトメアとは逆に、グレイはどこか呆れたような顔をしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私を責めるというほど強い調子ではないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（グレイは、私が医務室に入り浸ることを、あまりいいと思っていないのかしら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔というのは元々が職員寮だったこともあり、全体的な運営にも関わる場所だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "内部に、寮生とはいえ部外者が立ち入ることを好ましくないと考えているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……グレイ。\n
あなたは、私がナイトメアの手伝いをするの、反対？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、私が彼に対して確認を入れたことに関して、驚いたようだった。\n
沈黙を挟む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の上司である、ナイトメアの意向だ。\n
それに対して、部下である彼が反対しても仕方がないと思っているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、少なくとも私にとってグレイの反対というのは大問題だ。"

hide nai_m_02_4
show nai_m_02_4 at left
with dis

show gre_m_01_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0110
Gray "「そうだな、俺としては反対したいよ。\n
……君への負担が、大きすぎる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の口にした反対の理由は、私の予想とは異なっていた。"

hide gre_m_01_13
show gre_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0111
Gray "「君は、これまでにも充分すぎるほど俺を助けてくれていたのに……。\n
ナイトメア先生の手伝いまでするとなったら、負担が大きくないか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（なるほど、そっちか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイの反対の理由は、私の想像したようなものではなかった。\n
あくまで、私のことを心配してくれている。"

hide nai_m_02_4
show nai_m_02_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0263
Nightmare "「ああ、その辺は大丈夫だ。\n
私を手伝う権限は与えるが、義務とはしない」"

hide gre_m_01_11
show gre_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0112
Gray "「それなら俺も文句はありませんが……、頼りすぎないでくださいね？\n
彼女は多忙な学生ですから」"

hide nai_m_02_12
show nai_m_02_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0264
Nightmare "「それぐらい私だって承知しているさ。\n
だから、必要なら特別執務官でも何でも、役職名を作っても構わないが、どう思う？」"

hide gre_m_03_11
show gre_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0113
Gray "「名前を作ってしまうと、特権が出来る代わりに、義務も発生してしまうでしょう。\n
そうなると……」"

hide gre_m_01_11

hide nai_m_02_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "グレイとナイトメアは、なにやら私の扱いについてを話し合っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（そんな大層にしなくても……。\n
手伝えるときに手伝うっていうだけなんだから）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それに、私に手伝えることなど、たかが知れている。\n
なんとはなしに聞き流しながら、ふと気付く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどグレイは、こう言った。"


scene bg_par16_rs_tow_day_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0111
Gray "「君は、これまでにも充分すぎるほど俺を助けてくれていたのに……。\n
ナイトメア先生の手伝いまでするとなったら、負担が大きくないか？」"


scene bg_par16_rs_tow_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（俺の手伝いはもうしなくてもいい、とは言わないのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段の彼ならば、そういう言い方をしそうだなと思ったのだ。\n
そこが違和感で、引っ掛かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言わなかったということは、グレイなりに、私と一緒に過ごす時間を気に入ってくれているのだと受けとめてもいいだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じんわりと嬉しくなる。\n
グレイのような大人の男性に認められているというのは、それだけで嬉しいものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（普通なら得られないような、特別な友人だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クラスメイトや、知り合い。\n
そういったものにはなりにくい、年の離れた相手。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（グレイにとっては、どうなのかしら）"

with dis
$ hi_mes()

scene bg_par16_rs_tow_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg06_sk_h_day
with stripe_l_long

play music room2_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……と。\n
せっかく名目まで考えてもらったのに、私はなかなか医務室に顔を出すことが出来なくなってしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業が進むにつれ、ついていくのが精一杯になってきたのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初の頃、ゴーランドから言われたように、授業のレベル自体は今の私の状態と乖離しているわけではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "けれど、その形式が今まで私が受けてきた授業とは違うのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たとえば今までが、研究対象を渡されてレポートを作成するのだとしたら、シンフォニアで求められるのはその研究対象を自ら発見するところから始まる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "コツが掴めれば、きっとそんなに大変なものではないと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、今のところ私はまだシンフォニア流の授業の進め方に適応するのに必死なのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おかげで、放課後も先生の研究室を訪ねたり、図書館を訪ねることが増えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（今日も……、無理そうね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "宿題として出された課題のことを考えて、げんなりと息を吐く。\n
そろそろ、一度、二人に事情を打ち明けに行くべきかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（いきなり来なくなったから、気にしているかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "悪いほうにとられていなければいいなと思う。\n
一方、気にされていなければいないで、寂しいものがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早くも、あの場所は私にとって馴染みの場になっていた。"

with dis
$ hi_mes()

scene bg06_sk_h_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg25_rr_day
with stripe_l_long

play music drawingroom_day_p_wam
play sound se_0302
pause .15
play sound se_0397

scene bg_par16_rs_tow_day with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ドアを開けて迎えてくれたグレイは、そこに立つ私を見て一度驚いたように「ああ」と声をあげた。"


show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0114
Gray "「君か。\n
しばらくこちらに顔を出していなかったので、心配していた」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それから後ろを振り返り、ナイトメアへと声をかける。"

hide gre_m_02_2
show gre_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0115
Gray "「ナイトメア先生、彼女が来ましたよ。\n
よかったですね、嫌われたわけではなかったようです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「ええ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_7")
T "（嫌ってなんか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "想定外のことを言われてしまった。"

play sound se_0584
hide gre_m_02_3
show gre_m_02_3 at left
with dis

show nai_m_01_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0265
Nightmare "「[firstname]！君か！\n
ああよかった、もう遊びにきてもらえないんじゃないかと心配していたんだ……っ！」"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "騒々しい足音がして、すぐにナイトメアが入り口までやってきた。\n
その顔に浮かんでいるのは、分かりやすい安堵だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何がどうして、私が彼らを嫌っているだとか、もう遊びにこないなんて話になっていたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "助けを求めるようにグレイへと視線をやれば、彼はやれやれというふうに肩を竦めた。"

hide gre_m_02_3
show gre_m_03_6 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0116
Gray "「ナイトメア先生が君に手伝いを求めて以来、君がここに顔を出さなくなってしまっていただろう？」"

hide gre_m_03_6
show gre_m_02_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0116_5
Gray "「それで君に無理強いしたんじゃないかと、ずっと気に病んでいらっしゃったんだ」"

hide gre_m_02_11
show gre_m_03_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0117
Gray "「……俺はそんなことないですよ、と繰り返し申し上げていたんだが」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……グレイはナイトメアと意見が違うのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少し声音を落として、こそこそっと言われた言葉に私も小声で彼へと言葉を返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん、グレイのほうで正解だ。\n
だが、タイミング的には、ナイトメアの被害妄想も成立しないわけではない。"

hide gre_m_03_11
show gre_m_01_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0118
Gray "「君は、逃げ出すほど嫌なことは最初から引き受けないだろう？\n
それに、約束を破るような子でもない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……なるほど」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当たり前のように言われて、恥ずかしくなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その通りではある。\n
自分に出来ないことならば、最初から引き受けたりはしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しなくてはいけないことならばまだしも、しなくてもいいことならば。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな正面から、さらりと言われてしまっては謙遜するのも難しい。\n
何より彼自身が、褒めるつもりで口にしたわけではないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼の目に映る私の評価を、ごく自然に口に出しただけ、というような感じだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（くすぐったいな……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんなことをてらいなく言えるあたり、大人だと思う。\n
同年代では照れずに口に出せることではない。"

hide nai_m_01_1
show nai_m_02_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0266
Nightmare "「わ、私だって別に彼女が約束を破るような子だとは思っていなかったぞ！？」"

hide nai_m_02_8
show nai_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0266_5
Nightmare "「ただ……、その、私が我侭を押し付けてしまったのではないかとだな、心配していただけだ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……この人も、大人なはずなんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……気のまわしすぎよ、ナイトメア。\n
でも、心配させてごめんなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_11")
T "「もっと早く、ここに顔を出すべきだったわ。\n
そうしたら、そんな勘違いさせずにすんだのに」"

hide nai_m_01_4
show nai_m_02_10 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_11")
voice nig_g0267
Nightmare "「い、いや、私が何かしたわけじゃないなら構わないんだ。\n
君が来たいと思ったときに顔を出してくれれば……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（これは……、本当に心配させちゃったかな）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "申し訳ないという気持ちが膨らんでくる。"

hide gre_m_01_11
show gre_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0119
Gray "「いつ君が遊びにきてもいいように、と。\n
ナイトメア先生が医務室に居付くようになってくださったのは、正直ありがたい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "横合いから、真面目ぶった声でグレイが口を挟んだ。"

hide gre_m_01_3
show gre_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0120
Gray "「これからも気紛れで構わないから、是非遊びにきてくれ。\n
……俺のためにも」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（そんなふうに言われちゃうと……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とどめのようだ。\n
来ないと、という気持ちが固まってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「そ、そうね。\n
ナイトメアがまた逃亡癖を復活させない程度には、顔を出したいわ」"

hide gre_m_01_4
show gre_m_03_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_6")
voice gra_g0121
Gray "「んん？\n
ああ、それももちろんだが……」"

hide gre_m_03_9
show gre_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_6")
voice gra_g0122
Gray "「俺自身も、君が来てくれるのを楽しみにしている。\n
また、息抜きに付き合ってくれたら嬉しいと思っているよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……私も。\n
是非、息抜きがしたいわ」"


show m_gre1_3s onlayer master
with dis

play music memory1_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "瞼の裏に、あの見事な夕焼けが蘇る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の頂上から二人で眺めた景色。\n
それと一緒に思い出すのが、煙草を咥える彼の横顔だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仕草が、とても綺麗だった。"

hide m_gre1_3s with Dissolve(1.5)
hide nai_m_02_10
show nai_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0268
Nightmare "「むう……。\n
私だって息抜きしたいぞ」"

hide gre_m_03_4
show gre_m_03_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0123
Gray "「あなたは息抜きしすぎですよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「あんたは息抜きしすぎなのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ナイトメアへのつっこみがハモった。\n
あまりのユニゾン具合に笑みが零れる。"

hide gre_m_03_7
show gre_m_01_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0124
Gray "「ふ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「ふふ」"

hide nai_m_03_9
show nai_m_03_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice nig_g0269
Nightmare "「むむう……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最初は憮然としていたナイトメアだが、私達が笑っているのにつられたのか、最終的には三人分の笑いが重なった。"


play music drawingroom_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その笑いが収まる頃に、グレイが部屋の中へと視線を流して口を開く。"

hide gre_m_01_3
show gre_m_01_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0125
Gray "「ああ、それで、君は今日も予定があるのか？\n
よかったら、ココアだけでも飲んでいかないか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「う～ん……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ココアの誘惑に心が揺れた。\n
実は、今日もこれから課題で忙しい。"

menu:
    "ココアを断る。":
        jump gakuen_gray2_4a
    "誘惑に負ける。":
        jump gakuen_gray2_4b
label gakuen_gray2_4a:
$ lovechara_gray_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……が、我慢我慢）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……ごめんなさい。\n
ココアは、また次の機会にしておくわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "久しぶりに会った二人との会話だって、名残惜しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（でも、課題……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐらぐらと理性が欲望に負けてしまいそうになるが、ここが我慢のしどころだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただでさえ、気を遣わせている。\n
うっかり誘惑に負けてしまったとして、私の成績が悪かった場合、きっと二人は私以上に気にするだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "バレなければ……、と思わなくもないが、彼らだって学園関係者だ。\n
どこからか、そんな話が伝わってしまう可能性は充分にある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔の責任者ということで、塔に在籍する成績不良な生徒の情報などが報告されるということもあるかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分達のせいで……、なんていうふうに考えなくとも、知られるだけで恥ずかしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "身近な人達だからこそ、きちんとした姿を見てほしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（ちゃんと、本当の意味で息抜きが出来るようになってから顔を出そう）"

jump gakuen_gray2_5
label gakuen_gray2_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（ちょ、ちょっとぐらいなら……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「コ、ココアの一杯ぐらいなら、平気かしら……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "課題といっても、無理な量が出ているわけではない。\n
きちんとそれなりの時間を割けば、対応できるだけのものだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そして、その時間というのは、ココアの一杯も飲めないほど追い詰められるほどのものではない。"

hide nai_m_03_8
show nai_m_02_12 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0270
Nightmare "「そうだとも！\n
一杯ぐらい平気だとも！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（ああ……、でも……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "難儀な話だが、そう賛成されると悪いことをしている気分になる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ただでさえ、気を遣わせている。\n
うっかり誘惑に負けてしまったとして、私の成績が悪かった場合、きっと二人は私以上に気にするだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（大体、久しぶりなんだから……、一杯だけっていっても話し込んじゃうわよね）"

hide gre_m_01_4
show gre_m_01_12 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice gra_g0126
Gray "「……今日はやめておいたほうがいいかもしれないな。君がそうやって悩むということは、まずいかもしれないと思う部分があるんだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ええ」"

hide gre_m_01_12
show gre_m_01_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice gra_g0127
Gray "「それならば、無理はしないほうがいい。\n
ナイトメア先生が強引に誘って悪かったな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「……そうね。\n
今日は、我慢することにするわ」"

jump gakuen_gray2_5
label gakuen_gray2_5:
hide nai_m_02_12
show nai_m_01_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nig_g0271
Nightmare "「なんだ。\n
君、そんなに忙しいのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「授業が本格的に始まったでしょう？\n
予習復習だったり、宿題だったりでちょっと今大変なのよ」"

hide nai_m_01_2
show nai_m_01_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice nig_g0272
Nightmare "「ほう、そんなに大変なのか。\n
ちょっと休憩をとるのも無理なほど……？」"

hide nai_m_01_4
show nai_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice nig_g0273
Nightmare "「あ、いや……、断られたからというのではなくて……。\n
そんなに切羽詰っているのはよくないんじゃないか？」"

hide gre_m_01_13
show gre_m_03_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（そう、なのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ココアを一杯飲むくらいの時間も惜しいほどに追い詰められているのか、といえば答えはノーだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、居心地のいい医務室に足を踏み入れ、この二人と息抜きなどしてしまえば、そのままずるずると居座ってしまうのは目に見えている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（悪いのは、私の自制心のなさよね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ココア一杯ときっちり決めて、切り上げることが出来れば問題はないのだ。\n
そう出来る自信がないことこそが、問題。"

hide gre_m_03_9
show gre_m_02_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0128
Gray "「……そのココア一杯ぐらいというナイトメア先生が、一回のコーヒーブレイクでどれだけの時間を無駄にしているのかご存知ですか？」"

hide nai_m_02_7
show nai_m_03_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0274
Nightmare "「……っう。\n
そ、それは……、そう、だな……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思い当たる節があったのか、ナイトメアの言葉が急激にトーンダウンした。"


play music study_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「やっぱり、休憩といっても、話したりしちゃうしね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「そういうわけだから、今は我慢しておこうと思うの。\n
ココアは、課題が無事仕上がったときのご褒美にとっておいてもいいかしら」"

hide gre_m_02_3
show gre_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0129
Gray "「ああ。\n
美味しいココアを淹れられるように、俺も修行しておこう」"

hide nai_m_03_7
show nai_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice nig_g0275
Nightmare "「それなら私は、何か美味しいケーキでも取り寄せておくことにするよ。\n
……早く、一段落つくといいな」"

hide gre_m_02_2
show gre_m_02_13 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice gra_g0130
Gray "「ええ、そうですね。\n
……ですが、ナイトメア先生は、彼女の心配でなくご自分の仕事の進み具合も心配していただきたいものです」"

hide nai_m_03_11
show nai_m_03_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice nig_g0276
Nightmare "「ううっ。\n
な、なんだか具合が悪くなってきた……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「{size=+20}気のせいよ。{/size}\n
……それじゃあ、私も課題をやっつけてくるとするわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仮病なのか本気なのか。\n
体調の悪さを主張し始めたナイトメアを切り捨てて、私も自室に戻ることにした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（気持ちを切り替えて……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "課題のレポートを書くのに必要な文献はすでに図書館で手配済み。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここシンフォニアの図書館は、本の転送サービスがあるのだ。\n
おそらくもう部屋に届いていることだろう。"

hide nai_m_03_5
show nai_m_02_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nig_g0277
Nightmare "「頑張れよ。\n
最初は大変だろうが、慣れたら余裕も出来る」"

hide gre_m_02_13
show gre_m_02_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0131
Gray "「ああ、頑張ってくれ。\n
ほら、ナイトメア先生、あなたも彼女を見習って頑張ってください」"

hide nai_m_02_1

hide gre_m_02_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が足を引くと同時に、グレイはナイトメアを執務机へと追い立てていく。\n
それを見送って、私も踵を返そうとする。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……あ）"


show gre_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "最後扉が閉まる間際、グレイがナイトメアからは見えない角度でひらりと小さく手を振ってくれたのが分かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひら、と私も手を振り返す。"

hide gre_m_01_3
show gre_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Gray "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "浅く、顎を引く返事が帰ってきた。"

hide gre_m_02_2

play sound se_0399

scene bg25_rr_day with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（内緒話みたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何か伝えたい意味がお互いあったわけではない。\n
ちょっとしたコミュニケーションだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その後、すぐに扉は閉まってしまったが、なんだかとてもやる気がわいてきた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_1")
T "（……よしっ！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっさと課題を終わらせて、また医務室を訪ねよう。\n
グレイのココアとナイトメアのケーキで、ゆっくりと息抜きをしよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目標を作ると、やりがいもある。"

with dis
$ hi_mes()

scene bg25_rr_day with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg06_sk_h_day
with stripe_l_medium

scene bg06_sk_h_eve with Dissolve(1)

scene bg06_sk_h_nig with Dissolve(1)

scene bg24_rj_nig_lon
with stripe_l_long

play music high_nig_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……あー」"

play sound se_0160 volume .8
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呻いて、伸びをした。\n
そろそろ深夜にさしかかろうかという頃だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "机の上には、様々な資料とノートが広げられている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以前ナイトメアやグレイに応援してもらったレポートのほうは無事に締め切りまでに提出することが出来たのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "未だ私は医務室での憩いの時間を取り戻せずにいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "宿題や課題が出るのは、何もその一科目だけではないのだ。\n
次から次へと、きりがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（だんだんとスピードは上がってきているけど、まだ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（…………）"

play sound se_0018 volume .6
$ flash(.1)
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（うっ、腰が……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "伸びをしたとたんに、腰にぴきりと妙な痛みが走った。\n
ずっと同じ姿勢で書き物をしていたせいだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「いたたた……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゆっくりと息を吐きながら、伸ばしていた背を緩めていく。\n
少しずつ、強張った筋から力が抜けていくのが分かる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「ちょっと、ストレッチでもしようかな」"

play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "呟いて、立ち上がった。"

play sound se_0290
pause .3
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、そのタイミングでドアが鳴る。\n
もうだいぶ夜も遅い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こんな時間に訪ねてくる友人に心当たりはない。\n
もちろん、こんな時間に使用人に訪ねられる覚えもない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「はい……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返事に、警戒が滲む。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアの寮内に不審人物が侵入したり、その不審人物がわざわざドアをノックしたりするようなことはないと分かってはいるのだが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0107
Maid "「夜分遅くに失礼致します。\n
扉を開けていただけますか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "覗き穴から確認するが、そこにいるのは間違いなく塔のメイドだ。\n
だが、その訪問理由が分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（まさか、悪い知らせとか？）"

play sound se_0397 volume .8
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そろそろと、ドアを開けた。"


scene bg25_rr_nig
with dis

play music corridor_nig_p_wam

show maid_d_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0108
Maid "「こちらを、お届けするようにと言いつかって参りました。\n
お受け取りいただけますか？」"

show m_cut_gre2_1u onlayer master
with dis
hide maid_d_2

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……ココア？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女の手にしたお盆の上には、甘い香りを放つマグカップと、小さな二つ折のメモがのっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（……！）"

hide m_cut_gre2_1u

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はっとした。\n
周囲をきょろきょろと見やる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "廊下には誰もいない。\n
夜も遅いので当然だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そっと声を抑えて、彼女へと聞いてみる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……グレイから？」"


show maid_d_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice tad_g0109
Maid "「はい。\n
グレイ様からです」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女は、頷いてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声を潜めたのは、彼女なりの気遣いだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "万が一誰かに聞かれて騒がれでもした場合、私とグレイが困ることになるのを分かっているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ありがとう。\n
……同じ言葉を、伝えてくれる？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "誰に、とは言わない。\n
それでもその言葉の意味は正しく通じ、彼女は再び頷いてくれた。"

hide maid_d_3
show maid_d_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tad_g0110
Maid "「それでは、私は失礼させていただきますね。\n
おやすみなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ええ、おやすみなさい」"

play sound se_0774
hide maid_d_2

pause .15
play sound se_0399

scene bg24_rj_nig_lon
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "お盆を彼女から受け取って、その背を見送った。\n
戸締りをして机へと戻る。"


play music room3_p_wam

scene m_cut_gre2_1
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "机に座って、さっそく温かいココアを口に運んだ。\n
もう寒い時期は過ぎたとはいえ、夜の温かい飲み物は嬉しい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "甘さと共に、体の中で凝り固まった疲れが、じんわりと解けていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「……おいし」"

play sound se_0471 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "味わってから、メモへと手を伸ばした。\n
無造作に二つ折にされているのを、開く。"


scene white with expand_long
play sound se_0526

scene m_cut_gre2_2u with compress_long
pause .5
play sound se_0346 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まばゆい光が溢れたかと思ったら、メモはあっというまにその形を変えていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_10")
T "（……か、可愛い。\n
けど何だろう……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "とりあえず、丸い。\n
太りすぎのアザラシのようにも、まんまるの猫のようにも見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大きさは私の握りこぶしよりも小さい。\n
ピンポン玉ぐらいだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "手足のないスライムのような形状をしているが、液体っぽさはない。\n
謎の生き物だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_8")
T "（でも、可愛い）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何かのキャラクターなのだろうか。\n
つぶらな瞳が私を見上げている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「……えい」"

play sound se_0058
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちょいと、指先で突くと、くすぐったげにその生き物は身じろいで……。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0132
Nazo "「勉強は捗っているだろうか。\n
部屋の明かりがまだついているようだったから、ココアを届けさせた」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「！！！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "可愛らしい外見とは不釣合いに低い声。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "謎の生き物から響いて、ぎょっとした。\n
ココアの入ったマグカップを取り落としそうになってしまったほどだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、そんな私の動揺など無視して、その生き物は言葉を続ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0133
Nazo "「勉強熱心なのはいいことだが、あまり根を詰めすぎて体を壊さないようにな。\n
君が遊びに来てくれるのを、ナイトメア先生は楽しみにしている」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0134
Nazo "「……ごほん。\n
もちろん、俺もだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0135
Nazo "「休息も大事だ、そろそろ休むように。\n
……おやすみ」"


scene m_cut_gre2_2_gre3
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（グレイの声だわ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "吹き込まれていたのはそれだけなのか、お休みの挨拶の後は再び静かになる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "きっとこの生き物は、ボイスメッセンジャーの役割を果たすマジックアイテムなのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずいぶんと可愛らしいデザインなのは、私へ宛てたものだからだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女の子に送るものだからと、わざわざ可愛いグッズを探しているグレイの姿を想像する。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_9")
T "（大人なのに……、なんだか……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "煙草を我慢してカップを齧っていたときに感じた、くすぐったさ。\n
大人なのに、可愛らしくて……、抱きしめたくなるような。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「……ん？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボイスの内容を思い返して、ふと気付いた。"


scene bg24_rj_nig_s
with dis

play music starlit_sky_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gra_g0132
Nazo "「勉強は捗っているだろうか。\n
部屋の明かりがまだついているようだったから、ココアを届けさせた」"


scene bg24_rj_nig_lon
with dis
play sound se_0165

scene bg06_sk_h_nig
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "勢いよく立ち上がると、窓に向かった。\n
しゃっと音をたててカーテンを開く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……やっぱり」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見下ろした先に、ぽつりと大小の明かりが浮かんでいるのが見える。\n
おそらく、そこにグレイがいるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "大きめの灯りがランタンか何かで、小さいのは煙草の火だろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（見回りの途中だったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "生徒の中には、夜間こっそり抜け出そうとする不埒者もいるらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういった生徒を取り締まるために、使用人達が外を定期的に見回っているという話は聞いたことがあった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見下ろす先で、つうっと灯りが揺れる。\n
ゆらりっと手を振るような動きだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こちらから彼の姿は見えないが、部屋に明かりがついている今、彼の側からは私が見えるはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "影絵でも分かりやすいように、大きな動作でゆっくりと手を振る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "返事のように、また灯りが揺れた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_7")
T "「……もう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私に手話が出来たならば、ありがとうと伝えることが出来たかもしれない。\n
けれど、そんな特技があるわけでなし。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_19")
T "「ますます、早いところ課題に慣れなきゃ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぼやくように呟いた言葉には、自分でもはっきりと分かるほどに喜色が滲んでいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "早く、シンフォニアの授業に慣れよう。\n
そして彼に会いに行こう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_10")
T "（ありがとう、って、自分の口から伝えなきゃ）"

with dis
$ hi_mes()

scene bg_par15_rg_tow_nig
with stripe_l_medium

scene bg_map_nig
with stripe_l_medium
##endmemory
jump gakuen_gray3
