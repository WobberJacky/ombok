label gakuen_gowland5:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_amu_day
with dis

play music dining_day_p_wam

scene bg_par02_ct_amu_day with Dissolve(1.2)
play sound se_0617
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "翌朝、いつものように制服に着替え、身だしなみを整えてからカフェテリアへと向かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜まで使っていたリボンはゴーランドに取られてしまったが、予備はある。"

jump gakuen_storm_gow_nig_gra_jok1
label gakuen_gowland5_3:

show girl_b2_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice hei_g0028
Seito "「[firstname]、おはよう。\n
席、こっちが空いているわよ」"

hide girl_b2_2
show girl_b2_2 at left
with dis

show girl_c1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice chi_g0046
Seito "「おはよう、[firstname]。\n
一緒に朝食をとらない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "声をかけられて、その声の主達を探す。\n
すぐ近くの席で、クラスメイトの女の子二人が手を振って合図していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ありがとう。\n
空いている席を探していたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人の言葉に甘えて、そちらへと移動する。空いている席へと座り、ふうと一息ついてから、自分が判断を間違えたことに気づいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（……まずい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は、いかにも興味津々といった目で私を見ている。\n
爛々と輝いているその目は獲物を探している獣といっても過言ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、それだけ、ハングリーだということだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思えば、クラスに新入生は私しかいない。\n
クラスメイト達が、私の初ストーム体験を聞きたがるのは当然のことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当然、なのだが……。\n
私のストーム体験はあんまりに変則的すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "クラスメイトに話せるわけがない。\n
ストーム時に会っていた相手が担任であるゴーランドだなんて……、バレるわけにはいかないのだ。"

hide girl_b2_2
show girl_b2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0044
Seito "「ねえねえ、[firstname]、あなたのところにも男子が来たでしょう？\n
ふふ、驚いた？」"

hide girl_c1_2
show girl_c1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0026
Seito "「初めてのストーム、びっくりしたでしょう。\n
どうだったの？」"

hide girl_b2_3
show girl_b2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0045
Seito "「本当は、説明してあげたかったけど、元から交流のあるクラスメイトがしゃしゃり出ていっちゃイベント趣旨に反しちゃうものね」"

hide girl_c1_3
show girl_c1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0027
Seito "「後から感想を聞こうって決めていたのよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "案の定、二人は弾んだ声で問い掛けてくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（ええっと……）"

menu:
    "誰もこなかったと嘘をつく。":
        jump gakuen_gowland5_4a
    "部屋に入れなかったと嘘をつく。":
        jump gakuen_gowland5_4b
label gakuen_gowland5_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「実は……、誰も来なくて……」"

hide girl_b2_2
show girl_b2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice nos_g0046
Seito "「……え」"

hide girl_c1_2
show girl_c1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice ari_g0028
Seito "「……本当に？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「え、ええ……。\n
本当よ」"

hide girl_c1_1
show girl_c1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Seito "「…………」"

hide girl_b2_1
show girl_b2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Seito "「…………」"

hide girl_b2_5
show girl_b2_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice nos_g0047
Seito "「それが本当なら……、ちょっとボリスを問い詰めなきゃ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「え！？\n
なんで、ボリス！？」"

hide girl_b2_7
show girl_b2_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nos_g0048
Seito "「男子寮の責任者は、そんなふうにイベントに参加できない子が出ないように調整しないといけないのよ」"

hide girl_c1_5
show girl_c1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice ari_g0029
Seito "「あなた、特に新入生だもの。\n
新入生の子がイベントに参加できなかったなんて、ちょっと酷いミスだわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「！！！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言い訳しようとして、状況を悪くしてしまった。\n
これで責められたら、無実のボリスが可哀想だ。"

jump gakuen_gowland5_5
label gakuen_gowland5_4b:
$ lovechara_gowland_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「私、まさか男子がくるなんて思っていなくてね……？\n
それで……、その、部屋に入れなかったの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「イベントだって知っていたら、もっとちゃんと反応したと思うんだけど……。\n
知らなかったものだから」"

hide girl_b2_7
show girl_b2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Seito "「…………」"

hide girl_c1_7
show girl_c1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
Seito "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがに、部屋に誰も来なかったというのは嘘くさくなりすぎる。\n
先ほど聞いた話を参考に、失敗談にしてみた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、二人の反応は芳しくない。\n
顔を見合わせて、訝しげに首を傾げている。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……な、なに？」"

hide girl_b2_5
show girl_b2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nos_g0049
Seito "「……おかしいなあ、と思って。\n
ね、おかしいわよね？」"

hide girl_c1_5
show girl_c1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice ari_g0030
Seito "「ええ、おかしいわ。\n
そんな失敗談、まだ聞いていないもの」"

hide girl_b2_9
show girl_b2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nos_g0050
Seito "「大体、途中で上級生の助けが入るはずなのよ」"

hide girl_c1_9
show girl_c1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice ari_g0031
Seito "「そうそう。\n
男性生徒側でも解決できないときは、女子生徒の先輩が出てきて……」"

hide girl_b2_9
show girl_b2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice nos_g0051
Seito "「男子生徒は、戦利品を持って帰らないといけないから必死なはずだし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "{size=+20}（げげ）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考えてみればそのとおりだ。\n
肝試しと同義であるストームを成功させた証拠として、彼らは戦利品を持ち帰る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "証拠というのは、証明するために使う。\n
その中で、失敗した者がいれば、すぐさま話題にもなるだろう。"

jump gakuen_gowland5_5
label gakuen_gowland5_5:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（う、うわあ。\n
どうしよう……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "安易に言い訳に走ったことを後悔する。\n
もはや、どう誤魔化したらいいのか分からない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いっそ最初から、よく知らない誰かが来たとか適当にでっちあげてしまっていればよかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今からだと、そういう無難な話にもっていっても遅い。\n
じゃあどうして最初に嘘ついたの、ということになってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……う」"

hide girl_b2_9
show girl_b2_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
Seito "「……？」"

hide girl_c1_9
show girl_c1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
Seito "「……[firstname]？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "じいっと二人に見つめられ、私はたじたじだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうしよう。\n
逃げたい。"


play music secret_nig_p_wam

show bor_m_02_8 at center
with dis
hide girl_b2_9

hide girl_c1_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0116
Boris "「こらこら、新入生をいじめるなよ。\n
[firstname]、あんたも正直に白状したらいいのに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……え？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスの声だと思ったときには、肩にその手が乗っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（う？\n
あああああ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "朝のカフェテリアなので、ボリスがいたとしてもおかしくはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、今ここで出てこられるのはとてもマズイ。\n
とてもとても、マズイ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリス＝エレイはピンクの猫。\n
そして、遊園地寮の寮長だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（寮長が出てきたら……。\n
確実に嘘がバレる）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、白状するというのは何のことだ。\n
彼は事情まで知っているのだろうか。"

hide bor_m_02_8
show bor_m_02_8 at left
with dis

show girl_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice nos_g0052
Seito "「おはよ、ボリス。\n
白状って、どういうこと？」"

hide bor_m_02_8
show bor_m_02_8 at left_center
hide girl_b1_5
show girl_b1_5 at center
with dis

show girl_c1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0032
Seito "「おはよう、ボリス。\n
別にいじめてなんかないわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐるぐる混乱している間にも、二人はボリスへと声をかけている。\n
私の疑問を、そのままボリスへぶつけていく。"

hide bor_m_02_8
show bor_m_03_12 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0117
Boris "「ああ、昨日さ、ちょっといろいろあって。\n
俺がこの子の部屋に行ったんだよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（……え？）"

hide girl_b1_5
show girl_b1_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice nos_g0053
Seito "「ええ？\n
ボリスが？」"

hide bor_m_03_12
show bor_m_01_10 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0118
Boris "「うんうん。\n
最初、うちの新入生が行ったみたいなんだけど、留守でさ」"

hide bor_m_01_10
show bor_m_02_1 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice bor_g0119
Boris "「それで、俺が行こうと思ってた部屋と交換したわけ。\n
で、結局、時間ぎりぎりまで戻ってこなかったんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ねっと念を押されるようにボリスに話をふられて、私はこくこくと必死に頷く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "溺れているものは藁でも掴む。\n
私はこの際、猫でも掴む。"

hide bor_m_02_1
show bor_m_02_3 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0120
Boris "「だから、参加は出来たものの、あんまり要領も分からなかったんだよな、[firstname]」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……う、うん」"

hide bor_m_02_3
show bor_m_01_12 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice bor_g0121
Boris "「どっきりってのも、考え物だと思うぜ。\n
あやうく、イベントを逃しかけたんだから」"

hide girl_b1_4
show girl_b1_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice nos_g0054
Seito "「う～ん、そうよね。\n
イベントがあるって分かっていないと、部屋にいない可能性もあるのよね」"

hide girl_c1_5
show girl_c1_5 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice ari_g0033
Seito "「確かにそれはあるわね。\n
外出できなくても、寮の中だと出歩けるもの」"

hide girl_b1_5
show girl_b1_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice nos_g0055
Seito "「大体は、何かあるって雰囲気で部屋にいるけど……」"

hide girl_c1_5
show girl_c1_9 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice ari_g0034
Seito "「気になって、逆に外へ出ちゃうってことも有り得るか……」"

hide bor_m_01_12
show bor_m_03_10 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice bor_g0122
Boris "「そういうこと。\n
だから、あんまり追及しないであげてよ」"

hide girl_b1_9
show girl_b1_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice nos_g0056
Seito "「そうね……。\n
ごめん、[firstname]、変なふうに追及しちゃって」"

hide girl_c1_9
show girl_c1_1 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice ari_g0035
Seito "「ええ、本当にごめんなさい。\n
あなたが何か、とびっきりのネタでも隠しているんじゃないかって思っちゃって……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "うろり、と泳ぎそうになる視線を堪えて、彼女たちを見返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「ううん、私こそ言いよどんじゃってごめんなさい。\n
まさか、そんな面白いイベントをスルーしたなんて言い出しにくくて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "申し訳なさそうに謝ってくれる彼女達に、心の中では罪悪感を覚える。\n
だが、まさか本当のことを言うわけにもいかない。"

hide bor_m_03_10
show bor_m_01_10 at left_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0123
Boris "「ま、土壇場で、色々とサプライズにもなったしね？\n
ストームの気分は味わえただろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「え、ええ。\n
もっと、ちゃんと参加したかったわ」"

hide girl_b1_1
show girl_b1_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice nos_g0057
Seito "「ふふ、ボリスってばさすが寮長ね。\n
ナイスフォローよ」"

hide girl_c1_1
show girl_c1_2 at right_center
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice ari_g0036
Seito "「ブリーズで挽回したらいいのよ。\n
いっぱい楽しむといいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……本当に、ナイスフォロー）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達の言葉に曖昧に微笑みながら頷き、ちらりとボリスを見上げる。"

hide bor_m_01_10
show bor_m_02_2 at center
with dis
hide girl_b1_3

hide girl_c1_2

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "意味ありげなウィンクが寄こされた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（……うう）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（どこまで知っているの？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "助けられたものの、結局、追及は避けられない気がする。\n
……追及する相手が変わっただけで。"

hide bor_m_02_2

##[clearmessage PAY ATTENTION="false"]

scene bg_par02_ct_amu_day with Dissolve(.8)

scene bg_par15_rg_amu_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg10_sb_day
with stripe_l_medium

scene bg01_cr_day
with stripe_l_long

play music classroom_day_p_wam
play sound se_0425
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その後、ストームとは関係ない話題で盛り上がって、朝食を終えた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……はあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こっそりと溜息をつく。\n
正直、いつボリスから話を切り出されるのかとびくびくしているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "せっかくの授業も、右から左へと抜けていく感がある。"


show go_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0153
Gowland "「……おいおい、[firstname]。\n
ぼんやりしているが大丈夫か？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「……え？」"

hide go_m_02_3
show go_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice gor_g0154
Gowland "「今日は召喚の実践をやるわけだが……。\n
現代魔法における召喚の分類は幾つだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いきなり、ぽんと指名されて硬直する。\n
質問すら聞いていなかった。"

hide go_m_03_10
show go_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0155
Gowland "「こら、聞いていなかったのか？\n
召喚の分類の数だよ」"

hide go_m_03_2
show go_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0156
Gowland "「召喚魔法についての説明は昨日までの授業でやってあったな？\n
それで、答えられるか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「えっと……。\n
現代魔法における召喚の種類は、二つです」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つい昨日やった内容だ。\n
質問さえきちんと聞いていれば、その答えを記憶の中から引っ張り出すことに苦労はしなかった。"

hide go_m_01_11
show go_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0157
Gowland "「よしよし。\n
じゃあその隣、その二種のうちの一つ、どっちでもいいから説明をよろしく」"

hide go_m_03_12
show go_m_03_12 at left
with dis

show boy_a1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0026
Seito "「げ……っ！？\n
ええっと……」"

hide boy_a1_4
show boy_a1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0027
Seito "「召喚第一種は、幻獣とか悪魔とか女神とか……、そういった存在と契約し、その契約を元にこちらの世界に呼び出すやつです」"

hide go_m_03_12
show go_m_02_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0158
Gowland "「なんだかえらく曖昧な答え方だが……、正解だ。\n
こっちの第一種の召喚が、世間一般でイメージされる有名な召喚だな」"

hide go_m_02_11
show go_m_03_1 at center
with dis
hide boy_a1_5

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0159
Gowland "「それじゃあ、もう一つのほうを、ピアス。\n
……あんまり期待はしていないが」"

hide go_m_03_1
show go_m_03_1 at left
with dis

show pia_m_03_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pie_g0019
Pierce "「えっと召喚っていうのは呼ぶことだよ！\n
友達を呼んで、助けてって言うことだよねっ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスの説明は、とんでもなく大雑把だった。\n
曖昧どころの話ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでは、遠くにいる友達の名前を呼んで、仕事を手伝ってもらうことすら召喚ということになってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（ああ、でもピアスの感覚だとそうなのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ピアスのお友達召喚は、その感覚に限りなく近そうだ。"

hide pia_m_03_11
show pia_m_03_11 at right
with dis
hide go_m_03_1
show go_m_01_11 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0160
Gowland "「その回答じゃ、花丸はつけてやれねえなあ。\n
それじゃあ、ピアスの隣、説明を補足してやってくれ」"

hide pia_m_03_11

hide go_m_01_11
show go_m_01_11 at left
with dis

show girl_a1_8 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0039
Seito "「第二種の召喚は、契約を必要としない召喚で……。\n
形のない魔力そのものを、意志の力で成型して操るタイプ、です」"

hide go_m_01_11
show go_m_03_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0161
Gowland "「よっし、正解。\n
これで皆、召喚魔法の種類については大丈夫だな？」"

hide girl_a1_8
show girl_a1_3 at center
with dis
hide go_m_03_4

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice mat_g0040
Seito "「はーい……」"

hide girl_a1_3
show girl_a1_3 at left
with dis

show boy_a1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice oni_g0028
Seito "「多分……」"

hide girl_a1_3

hide boy_a1_5


show go_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0162
Gowland "「……多分、とか言うなよ」"

hide go_m_03_11
show go_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0163
Gowland "「今日授業で試してもらうのは、第二種のほうだ。\n
第一種については、また次回だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "第一種、第二種と名前がついていながら、第二種の実習から始まるのは難易度の問題だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世間一般でイメージするような魔法生物の召喚は、他者との契約が必要な分、難易度も高い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たとえば、悪魔との契約なんて、シンフォニアの教授や卒業生の中にも成功者がいるかどうか。成功したとしても代償の伴う、非常に危険なものだ。"

play sound se_0122
hide go_m_02_12
show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0164
Gowland "「それじゃあ、準備を始めてくれ。\n
何か分からないところ、困ったことがあったら声をかけるんだぞ？」"

hide go_m_02_8

play sound se_0497

play music test_sp_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドの声を合図に、皆それぞれテーブルに向かった。\n
まずは己の魔力を形ある物体へと形成し始める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見える形、触れる形、へとイメージを固めていくのだ。\n
机の上に手をかざし、イメージを集約させていく。"

play sound se_0496
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……粘土みたいな、ゼリーみたいな）"

play sound se_0724

show white onlayer master with expand_long

scene m_cut_go5_au ##instant]
hide white with compress_long

pause 1

scene m_cut_go5_a
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ここまでは簡単なのよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "魔力を見える形に変換すること自体は、難しいことではない。\n
問題はここから先だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この透明な粘土状の魔力の塊に、定義と、形とを与えていかなくてはいけない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何をするために、どんな形をしているのかというのを明確にイメージする必要があるのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しでもイメージに齟齬があると、全然違う形に仕上がってしまう。"


scene bg01_cr_day
with dis

show girl_d2_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0013
Seito "「あれ～？おかしいわ。\n
鳥の形にうまく成型できたはずなのに、どうして飛ばないのかしら」"

hide girl_d2_5
show girl_d2_5 at left
with dis

show go_m_02_13 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0165
Gowland "「ふむふむ、ああ、見た目は鳥っぽくできているが……。\n
鳥の翼の仕組みを、ちゃんと細部までイメージしてあるか？」"

hide girl_d2_5
show girl_d2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0014
Seito "「あ……、そこまで考えていなかった。\n
そうよね、どうやって飛ぶのかまでイメージしなきゃ飛べるわけがないわ」"

hide go_m_02_13
show go_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0166
Gowland "「ああ。\n
だが、魔法で空を飛ぶイメージを付加してみたらどうだ？」"

play sound se_0337
show white onlayer master with expand
hide white with compress

pause .5
play sound se_0613
hide girl_d2_8
show girl_d2_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice may_g0015
Seito "「あ、飛んだ……！！\n
ふふ、見た目だけなら本物の鳥っぽい」"

hide go_m_03_9
show go_m_03_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0167
Gowland "「今、その鳥が小さくなったのは、体を構成していた分の魔力を飛ぶことに回したからだな」"

hide go_m_03_4
show go_m_01_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0167_5
Gowland "「こういうふうに、外見、定義を補うために魔力で機能を付加することも可能だ」"

play sound se_0497
hide go_m_01_3

hide girl_d2_2

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドは教室のあちこち見てまわりながら、生徒達にアドバイスをしている。\n
それを聞きながら、私も魔力の成型を続ける。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうやらクラスメイト達は、実際によく見知った動物を真似ているようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……そのほうがイメージしやすいものね）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「よし」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の中でも、イメージが固まる。\n
かざした手の下で、透明なゼリーのようだった魔力の塊がぷるんっと波打って形を変えていく。"

play sound se_0724
show white onlayer master with expand_long

scene m_cut_go5_bu ##instant]
hide white with compress_long

pause .4
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_1")
T "「……ふふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小さな猫。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昔、実家で飼っていた猫をイメージしたのだ。\n
可愛がっていただけあって、イメージも正確。"

play sound se_0647

scene m_cut_go5_b
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "サイズ自体はネズミほどしかないが、それでも見た目は立派な猫。\n
彼女はテーブルの上でくるくると顔を洗う動作をすると、毛繕いを始める。"


show go_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice gor_g0168
Gowland "「お、なかなかよく出来ているな。\n
あんた、猫好きだったんだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ。\n
昔、家で飼っていたの」"

hide go_m_02_8
show go_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice gor_g0169
Gowland "「……ほう、そうかそうか。\n
うん、よく出来ているな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_2")
T "（……？）"

hide go_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "変な間があった。\n
猫から顔を上げるが、すでにゴーランドは別の生徒の下へと歩いていってしまっていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その代わりといったように、傍らにすすすっと寄ってきたのはボリスだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_8")
T "（……っ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それだけで動揺してしまう。\n
何を言われることやらと構えた。"


scene m_cut_go5_cu
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0124
Boris "「ふふ～ん♪\n
見て見て、これ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……これ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何気なく、私の隣にやってきたボリスの手の上にいるのは、手のひらサイズの小さなネズミ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこかの誰かさんを彷彿とする色の毛並みをしている。"


scene m_cut_go5_c
with dis

show bor_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0125
Boris "「食べたくなるぐらい、可愛いだろ？\n
俺、ネズミって大好きなんだよね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ひらりと手をひっくり返して、猫の傍らにネズミを落とす。\n
大好きというだけあって、ディティールまでうまく再現されている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見れば見るほど、誰かさんによく似ている。\n
同じサイズの猫とネズミが並ぶなんて、シュールな光景だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「私、ネズミを見て、おいしそうだと思う趣味はないわ」"

hide bor_m_01_6
show bor_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice bor_g0126
Boris "「それは残念。\n
……あんたの猫、ネズミ追いかけたりしないんだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "言われてみれば、白い猫はネズミの傍らでも優雅に毛繕いを続行している。\n
サイズがサイズなだけに、相手をネズミと認識していないのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、私のイメージに欠陥があってネズミを追いかける習性まではコピー出来ていないのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ネズミはネズミで、次第に眠たげに目が細くなっていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……ピアスにそっくり）"


play music boris_t_ali

scene bg01_cr_day
with dis
hide bor_m_02_7
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
Boris "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ん？\n
何？」"

hide bor_m_01_11
show bor_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice bor_g0127
Boris "「いや……、ちょっと聞きたいことが」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_4")
T "{size=+20}（！）{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一度周囲の様子を伺って、誰もこちらに注意を払っていないのを確かめてからボリスが口を開いた。"

hide bor_m_02_10
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0128
Boris "「……で？\n
あんた、昨日はどこにいたの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "{size=+20}「う」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小声で呻いて、隣のボリスを見やる。\n
とてもとても楽しそうだ。"


with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "緊張のせいか、周囲のざわめきが遠くなったような気がした。"

menu:
    "寮内で出掛けていたと答える。":
        jump gakuen_gowland5_6a
    "黙秘する。":
        jump gakuen_gowland5_6b
label gakuen_gowland5_6a:
$ lovechara_gowland_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……あなたの言ったとおり、寮内で出掛けていたのよ。\n
悪かったわね、部屋にいなくて」"

hide bor_m_01_10
show bor_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice bor_g0129
Boris "「ふうん？\n
出掛けていたって、誰と？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「ど、どうして誰かと一緒だと思うの？\n
私一人よ」"

hide bor_m_03_2
show bor_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice bor_g0130
Boris "「嘘だね」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は吟味する素振りすら見せずに、却下した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「…………。\n
……どうして、断言できるのよ」"

jump gakuen_gowland5_7
label gakuen_gowland5_6b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こうなったらもう黙るしかない。\n
何を言っても、ボリスにはバレてしまうような気がする。"

hide bor_m_01_12
show bor_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0131
Boris "「あんた、部屋にいなかったよな？\n
でも、いくらストームだからって、寮の外には出られないわけだし……」"

hide bor_m_03_12
show bor_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0132
Boris "「寮内には、いたわけだろ。\n
そっちは、確実」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "肯定も否定もしない。\n
出来る限りの鉄面皮で、ただひたすらに黙秘する。"

hide bor_m_03_2
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0133
Boris "「でも、一人じゃなかったよな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔に出すまいと思っていたのに、きっぱりと断言されたのには動揺を露にしてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……そんなことないわ。\n
どうして、断言できるのよ」"

jump gakuen_gowland5_7
label gakuen_gowland5_7:
hide bor_m_01_10
show bor_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice bor_g0134
Boris "「勘、かな」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_10")
T "（勘、ときたか）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "根拠がない分、覆しようもない。"

hide bor_m_02_4
show bor_m_02_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0135
Boris "「もうさ～。\n
無駄なんだから、白状したほうがいいぜ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "確信するに足る理由があるのか、それとも単にカマをかけているだけなのか。\n
判断が、私にはつかない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、猫の勘ときたら、強力そうだ。"

hide bor_m_02_2
show bor_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0136
Boris "「……いくらあんたが気紛れを起こして、部屋から出て共用エリアに行ったとしてもさ」"

hide bor_m_01_11
show bor_m_03_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0137
Boris "「人がいないことを変に思うだろ、普通。\n
で、様子を伺えばあちこちで男子が忍び込んでの騒動が起きている」"

hide bor_m_03_7
show bor_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0138
Boris "「イベント終わるまで気付かずに、部屋に戻らなかったなんてありえないよ。\n
……だろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスの説明は、嫌になるほどに論理だっていた。\n
ぐうの音も出ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際、私は昨夜音楽室に向かう道すがら、肌で異常を感じていた。\n
あの空気や喧騒の中、それに一切気づかないで過ごすというのは不自然だ。"

hide bor_m_03_4
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0139
Boris "「多分……、てか、間違いないと思うんだけど。\n
……あんた、おっさんと一緒にいただろ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "{size=+20}「！！！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これがカマかけだったのなら、私は完璧にボロを出した。\n
そう言わざるを得ない勢いで、反応してしまった。"

play sound se_0121
$ flash(.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あんまりに動揺しすぎたせいか、白い猫がシャボン玉のようにぱちんとはじけてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のコントロールから外れた魔力が、その形を留めておけなくなってしまったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "が、今はそれどころではない。\n
目を瞠って、ボリスへと向き直る。"

hide bor_m_01_10
show bor_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0140
Boris "「はは、やっぱりなあ。\n
あんたの相手が生徒なら、ストームに参加すればいいだけなんだよ」"

hide bor_m_02_3
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0141
Boris "「それなのに、あんたをストームの舞台から攫う必要がある相手って言ったらさ。\n
教師ぐらいしかいないだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……ボリス、あなた魔法使いやめて探偵にでもなったら？」"

hide bor_m_01_10
show bor_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice bor_g0142
Boris "「はははは！\n
ってことは当たりか、やっぱり」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私も、これ以上誤魔化すことは諦めて、こっくりと頷いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そうよ。\n
音楽室でゴーランドと会っていたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……ほら、認めたわよ。\n
これで満足？」"

hide bor_m_02_6
show bor_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice bor_g0143
Boris "「まあね。\n
……でも、あんたがおっさんとねえ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くふふっと笑みの滲んだ声でボリスが私を見る。\n
にやにやとしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "授業中でなければ、目潰しでもしてやるところだ。"

hide bor_m_01_10
show bor_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0144
Boris "「ま、別にいいけどね？\n
俺、あんたもおっさんも、結構好きだし」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「…………。\n
……追及しないの？」"

hide bor_m_03_10
show bor_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice bor_g0145
Boris "「もう、しただろ？\n
これ以上何か出せるネタあるの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「ないないないない」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これ以上追及されたって、何も出せやしない。\n
ただ、教師と生徒で……、だとか言われるのかと思ったのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ボリスがそういったことに言及しないことがありがたい。"

hide bor_m_03_2
show bor_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0146
Boris "「邪魔するつもりはないよ？\n
好きって言ったろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "特別な意味ではない。\n
友人としての「好き」なのに、焦ってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（好きにも色々あるのに……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_12")
T "（……そうよ、色々）"

hide bor_m_01_5
show bor_m_01_5 at left
with dis

show go_m_03_6 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_12")
voice gor_g0170
Gowland "「こらこら。\n
おまえら仲がいいのは構わねえが、ちゃんと授業には参加しろよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_4")
T "「……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タイミングよくゴーランドが戻ってきたのに、息を飲んだ。\n
面白がるような気配が隣から伝わってくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……ボリスめ）"

hide go_m_03_6
show go_m_01_11 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice gor_g0171
Gowland "「あれ？\n
[firstname]、あんたさっきの猫はどうしたんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……ちょっと手違いで。\n
すぐに新しく召喚しなおすわ」"

hide go_m_01_11
show go_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice gor_g0172
Gowland "「おう、そうか？\n
それじゃあ、続けてくれ」"

hide bor_m_01_5

hide go_m_03_9

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ゴーランドはそれだけを言うと、また他の生徒達のほうへと歩いていく。\n
私はそれを見送ると、再び机の上に手をかざし、魔力の精製から始める。"


play music test_wam
play sound se_0497
pause 1
play sound se_0724
show white onlayer master with expand_medlong
hide white
show m_go5_6 onlayer master with compress_medlong

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "続いて、形成だ。\n
もうイメージするものは決めている。"

play sound se_0138
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先ほどと同じく猫だが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_13")
T "（ネズミを食べる、ネズミを食べる……）"

play sound se_0724
hide m_go5_6
show white onlayer master with expand_medlong

scene m_cut_go5_bu ##instant]
hide white
show m_go5_7 onlayer master with compress_medlong

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今度の猫はショッキングピンクの毛並みをしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "物言いたげな視線でボリスが私を見ているが、気にしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「ゴー！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "小声でけしかけると同時に、ショッキングピンクの豆猫は、半ば眠りかけていたネズミへと襲い掛かっていった。"

play sound se_0297
pause .4
play sound se_0309 volume .7
camera at hpunch
camera at vpunch
hide m_go5_7
show m_go5_8 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Boris "「……！！？」"

play sound se_0256 volume .6
pause 1
play sound se_0257 volume .6
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "サイズ自体は変わらないものの、私のイメージがネズミに対してアグレッシブな猫であったせいか、ちっとも負けていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "がじがじとネズミの尻尾を齧り、猫パンチを繰り出す。\n
そうやって私の出した猫はネズミの形を形成するボリスの魔力を削っていき……。"

play sound se_0121
$ flash(.2)

scene bg01_cr_day with dis##instantPAY ATTENTION="true"]
hide m_go5_8

$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちんっ、と。\n
攻撃に耐えかねたようにボリスの召喚したネズミが弾けて消えた。"


show bor_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice bor_g0147
Boris "「なにこの、どこにぶつけていいか分からないモヤモヤ。\n
猫が、ネズミをやっつけるのは当たり前だけど……っっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……ふん）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しばかり仕返しができたようで、すっきりした。"

hide bor_m_01_3

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一段落ついて、ゴーランドを見る。\n
彼は、他の生徒を指導していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "先生を見る、生徒の私。\n
他の生徒を見る、先生。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（……好きにも、色々）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか、自信がなくなってきてしまう。"

with dis
$ hi_mes()

scene bg10_sb_day
with stripe_l_medium

scene bg_map_day
with stripe_l_long
##endmemory
jump gakuen_gowland6
