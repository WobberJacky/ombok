label gakuen_elliot5:
scene bg_map_day
with dis
$ clockanim()


scene bg_par15_rg_tow_day with Dissolve(1.2)

play music view_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後。\n
普段なら中庭にあるにんじん畑に向かっている時間だが、私は塔を見上げて溜息をついていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨夜の件について、授業が終わったら風紀に報告に行くようにと言われているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が悪いことをしたわけではなくとも、ようは事情聴取のようなもの。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれだけの馬鹿騒ぎでも、女子寮の窓を割るような行為がＮＧというルールはあったらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……早く、エリオットに会いたいのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットの、最後の言葉を思い出す。"


scene bg_par15_rg_tow_day_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0190
Elliot "「……悪い。\n
今晩のことは、ひとまず忘れてくれ」"


scene bg_par15_rg_tow_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "何を忘れろというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "結局あの後、駆けつけた使用人達に簡単に事情説明をして（と言っても、私に説明できることなど少ない）……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "医務室で治療を受けて戻ってきたときには部屋の窓も綺麗に修復されていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちなみに腕の傷も、綺麗に魔法で治癒してもらうことが出来た。\n
今はもう、傷一つ残ってはいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_3")
T "（ひとまずって言っていたけど……、いつまで？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……はあ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "憂鬱に溜息をついて、塔の中の風紀委員会室を目指す。"

play sound se_0774

scene bg_par20_re
with dis

scene bg25_rr_day
with dis
play sound se_0302
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0027
Julius "「開いている。\n
入れ」"

play sound se_0200

play music laboratory_day_p_wam

scene bg_par19_fi with stripe_l
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの声に迎えられて、中へと足を踏み入れた。そこは以前初日に訪れたような医務室とは違い、小さな会議室といった風の部屋だった。"


show yuri_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0028
Julius "「適当に座ってくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……うん」"

play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "勧められるままに、ロの字を描くようにして配置されたテーブルの、ユリウスの向かい側に腰を下ろす。"

hide yuri_m_01_12
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0029
Julius "「で……？\n
昨夜何かトラブルがあったと報告を受けている」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（なんだか、緊張するなあ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「……ええ。\n
理由は分からないんだけど……、窓ガラスを割られたの」"

hide yuri_m_03_9
show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice jul_g0030
Julius "「魔法でか？\n
被害は窓だけか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「割れた窓ガラスで腕を切ったけれど……、そっちは治療ずみよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_9")
T "「片付けをしてくれた使用人が言うには、石ころが投げ込まれたようだから物理的なものね」"

hide yuri_m_02_9
show yuri_m_03_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_9")
voice jul_g0031
Julius "「怪我をしたのか……。\n
……酷かったのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「いえ、軽症よ。\n
医務室で見てもらって、もう痕も残っていないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（ちょっと意外）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "仕事熱心、職務にしか興味がないといったような様子のユリウス。\n
その彼が、親身に心配してくれたというのが軽い驚きだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（あまりよくは知らないけど……、いい人なのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこで、またエリオットを思い出す。\n
彼も、見た目によらないところが多い。"

hide yuri_m_03_12
show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0032
Julius "「……そうか。\n
おまえ……、誰かに恨まれるような覚えは？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「恨み、って……、ないわよ。\n
そりゃあ、私だって誰にも反感を持たれずに生きているとは言い切れないけれど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「夜中にいきなり、窓ガラス割られるようなことをした覚えはないわ。\n
……ただの愉快犯かしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "イベントのあった夜だし、充分に有り得るような気がする。"

hide yuri_m_02_9
show yuri_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0033
Julius "「昨夜はストームだったからな。\n
興奮した愚か者が暴走した可能性もあるが……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふむ、とユリウスは顎に手をあてて考え込む。"

hide yuri_m_02_8
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0034
Julius "「使用人達はなんと言っていた？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「イベントに乗じた悪戯の可能性が高いけど、寮の窓ガラスは全面的に強化してくれた……って。以後こんなことがないように気を付ける、とも言ってくれたわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「なんだか、イベントに水を差したみたいでこっちのほうが恐縮しちゃう」"

hide yuri_m_03_9
show yuri_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice jul_g0035
Julius "「そうか……。\n
どうして帽子屋寮は、こうも問題ばかり起こすんだ」"

hide yuri_m_01_3
show yuri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice jul_g0036
Julius "「先日は赤薔薇寮と小競り合いがあったばかりだぞ。\n
おまえにも、問題を起こすなと私は言ったはずだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「知らないわよ、私が好きで起こしたわけじゃないもの。\n
……って、ちょっと待って」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その言葉が、どこか引っかかった。"

hide yuri_m_01_9
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0037
Julius "「なんだ？\n
どうした？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「……赤薔薇寮と小競り合い、って。\n
そういうのって、よくあることなの？」"

hide yuri_m_03_9
show yuri_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice jul_g0038
Julius "「ある意味においてよくあることで、ある意味においてはあまりないこと、だな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「なにそれ。\n
なぞなぞ？」"

hide yuri_m_02_10
show yuri_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice jul_g0039
Julius "「ふ。各寮の寮長共が悪ふざけの延長で、勝手にイベントを開催することがあるんだ。\n
たとえば、学生証狩り、だとかな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「……学生証狩り？\n
響きからして物騒ね」"

hide yuri_m_02_11
show yuri_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice jul_g0040
Julius "「敵対する寮の寮生から、学生証を奪い、その数を競い合うわけだ」"

hide yuri_m_03_8
show yuri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice jul_g0040_5
Julius "「が……、そういったイベントの場合、無許可ではあるが各寮長の間で話し合いはすんでいて、明確なルールが定まっている」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「つまり、勝手にイベントを開いてはいるけれど……。\n
あながちそれが悪いわけではないってこと？」"

hide yuri_m_01_9
show yuri_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0041
Julius "「もちろん悪いが、ルールがあり、均衡は保たれている。\n
風紀としては頭が痛い事態ではあるがな」"

hide yuri_m_03_4
show yuri_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0042
Julius "「そういった各寮の間の小競り合いは、いつものことだ。\n
しかし……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「その、前にあったというのは、勝手な喧嘩だったのね？\n
つまり各寮長のあずかり知らぬところで勝手に揉めていた……、というような」"

hide yuri_m_02_9
show yuri_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice jul_g0043
Julius "「そういうことだ。\n
校則はもちろん、各寮の自治ルールにも抵触する行為だ」"

hide yuri_m_02_10
show yuri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_15")
voice jul_g0044
Julius "「おそらくは、そちらの副寮長あたりからとっちめられたんじゃないか？\n
校則は守ろうとしない奴らだが、自分達の定めたルールには厳しい奴らだからな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "半ば呆れたように言うが、その口調の中には、信頼のようなものも見える。\n
立場的には敵対しているが、ある程度認めてもいるのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（そういえば……）"


play music gloomy_a_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨日の夜、ちらりと見た後姿。\n
闇の中に逃げ込むように走り去っていった背中を思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あれは……、あのときの生徒ではないだろうか。\n
壁に追い詰められ、勝手な行動をエリオットによって咎められていた、彼だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "両方の場面において、きちんと対面したわけではないので確証はないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（似ている、気はする）"

hide yuri_m_02_4
show yuri_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_15")
voice jul_g0045
Julius "「……心当たりがあるのか」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスの声が、低くなる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_14")
T "「確証はないの。\n
でも……、昨夜、私の部屋にはエリオットがいたわ」"

hide yuri_m_03_8
show yuri_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_14")
Julius "「……！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「だから、もしかしたら窓を割ったのは、彼に敵対する人かも……。\n
前に揉めていたのを見たこともあるの」"

hide yuri_m_03_11
show yuri_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice jul_g0046
Julius "「ああ、それはずいぶんと有力な証言だな。\n
……で、おまえらはいつからそんな関係になったんだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「そ、それは関係ないでしょう！\n
ともかく！私から言えることはこれぐらいよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "世俗のことなど興味はありません、といった堅物風でありながら、こうして真顔で聞いてくる彼は意地が悪い。"

hide yuri_m_02_4
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0047
Julius "「充分だ。\n
こちらでも犯人捜索を進めよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ありがとう。\n
助かるわ」"

hide yuri_m_03_9
show yuri_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice jul_g0048
Julius "「問題を起こした生徒の素行を調査するのは、風紀委員会の仕事だ。\n
おまえに礼を言われるようなことではない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……それでも、よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "以上、言葉通り、私には報告すべき内容はこれ以上ない。\n
席を立つと、部屋から出ようとする。"

hide yuri_m_03_4
show yuri_m_02_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0049
Julius "「[firstname]。\n
何か困ったことがあったら、いつでもこい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その背に、ユリウスが声をかけてきてくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと振り返った彼は、いつもの通りの仏頂面ではあるものの、彼なりにトラブルに巻き込まれた私のことを気にかけてはくれているらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「ええ。\n
遠慮なく頼ることにするわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう口にして、私は風紀委員会室を後にした。"

hide yuri_m_02_12
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_par03_nb_nn_day
with stripe_l_long

play music school_front_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔を出た後、まっすぐ帽子屋寮に戻り、中庭へと出る。\n
いつもならエリオットも畑にいる時間だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「……あ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、畑にエリオットの姿はなかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……忙しいのかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "女子寮とはいえ、自寮内で起こったトラブルとなれば、その後処理はエリオットの仕事だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それで、畑による時間を作れずにいるのかもしれない。"

play sound se_0496

show magic_b onlayer master with Dissolve(1.5)
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

play sound se_0138
show white onlayer master with expand
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぽうっと四隅のマジックアイテムが光る。"

play sound se_0741
hide white
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がマジックアイテムの発動を止めると、畑の頭上に立ち込めていた雨雲はあっという間に消えていった。それを確認してから、畑の中へと足を踏み入れる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にんじんの芽と間違えないようにしながら、雑草を抜いていく。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_14")
T "（少なくない……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "雑草の量が、いつもより少ない。\n
というか、ほとんどない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "毎日こまめに手入れしているが、それでもぽつぽつと顔をだす雑草はなかなか減らないのが常だ。それなのに、今日に限ってその雑草が見当たらない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「……エリオット？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットがやったのだ。\n
一人で、先に来て草むしりをして、去ったのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もうテラスのほうに移動したのだろうか。\n
私はマジックアイテムを再び起動させると、テラスへ移動することにした。"

with dis
$ hi_mes()

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_par12_hct_day
with stripe_l_long
play sound se_0200

play music garden_eve_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "扉をくぐって、テラスへと出る。\n
ティーテーブルでは、いつものようにブラッドが一人で紅茶を啜っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……一人で。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットがそこにいないことに、落胆する。\n
昨日あんなことがあったからこそ、会いたいと思うのに、タイミングが悪すぎる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（……そう、よね？\n
タイミングが悪いだけよね？）"


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脳裏に、また別れ際のエリオットの言葉がよみがえる。"


scene bg06_sk_h_day_s
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0190
Elliot "「……悪い。\n
今晩のことは、ひとまず忘れてくれ」"


scene bg06_sk_h_day
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_3")
T "（押し倒されて……、キスをして。\n
告白までしたのに、それを忘れろ……ってことじゃないでしょうね）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "タチの悪いからかい。\n
いや、そんなことはない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぐるぐると、暗いほうへ思考が傾く。\n
落ち込みそうに考えこむところに喉を鳴らして笑う声が聞こえ、顔をあげた。"


scene bg_par12_hct_day
with dis
##[rchara1 PAY ATTENTION="false"]
show bra_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0449
Blood "「やあ、お嬢さん。\n
昨夜は何か大変だったそうだな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「ええ……、色々とね」"

hide bra_m_02_5
show bra_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice blo_g0450
Blood "「ふむ？\n
どういう色々なのか、知りたいところではあるな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「寮長様には関わりのないところで、色々あるのよ。\n
嘆かわしいことね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「……仕事を押し付けているんだから、仕方ないことでもあると思うけど」"

hide bra_m_03_3
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_17")
voice blo_g0451
Blood "「おやおや、ふふ。\n
手厳しいことだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「……ねえ。\n
エリオットはいないの？」"

hide bra_m_03_2
show bra_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice blo_g0452
Blood "「お目当ては、あいつか……。\n
ふふ、火傷してしまいそうだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_12")
T "「からかわないで。\n
そのティーカップひっくり返して、物理的に火傷させてやるわよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（どこまで知っているのよ、この人は）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その場にいなかったくせに、何でも知っているという顔をする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのまま聞いてしまいそうになるが、それを言ってしまっては自ら何かあったことを認める形になってしまう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思えば、最初からブラッドは意味ありげなことばかり言っていた。"

hide bra_m_02_1
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0453
Blood "「苛立っているな。\n
うまい紅茶でも飲んで、落ち着いたらどうだ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「その前に、エリオットはどうしたのよ？」"

hide bra_m_03_15
show bra_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice blo_g0454
Blood "「紅茶が先、だ。至らぬ部下より、よほど重要なことさ。\n
ほら、こちらへ座りなさい」"

play sound se_0185
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドがひらりと手を揺らすのと同時に、私の目の前にあった椅子が勝手に動いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずずずっとまるで見えない誰かが椅子を引き、座るようにと促しているようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この男に逆らっても無駄だということは、まだそう長くもない付き合いの中からも充分すぎるほどに学んでいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "基本的に我侭なのだ。\n
我侭気まま、自分のしたいことを、したいようにする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そのための手段は選ばないし、そのための労力も惜しまない。私が席につくと、ブラッドはいつものように紅茶を手ずから用意して差し出してくれた。"

play sound se_0174
hide bra_m_03_9
show bra_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0455
Blood "「カモミールティーだ。\n
落ち着くぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_15")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……私がここに来ることを見越していたのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "カモミールは、心を落ち着ける効能を持つといわれているハーブだ。\n
ふー、っと息をふきかけるとふわりとリンゴのような甘酸っぱい香りが立ち上る。"

play sound se_0785 volume .7
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……いい匂い」"

hide bra_m_02_5
show bra_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice blo_g0456
Blood "「だろう？\n
そこに茶葉があるから、貰っていきなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_9")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり、私のために用意してくれたのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_10")
T "「……気を遣ってくれて、ありがとう」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（気遣い……って言っていいものか微妙だけど）"

hide bra_m_03_1
show bra_m_02_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice blo_g0457
Blood "「いいや？\n
それで、お嬢さんには、紅茶以上に気になることがあるようだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しれっと言って、ブラッドが自らもその紅茶を啜る。\n
つられたように、私もカップを傾けた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「別に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "砂糖をいれてはいないが、ほんのりと自然の甘みがちょうどいい。"

hide bra_m_02_16
show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0458
Blood "「……ふ。\n
エリオットなら、見回りに出掛けているぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……っ」"

hide bra_m_03_15
show bra_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_7")
voice blo_g0459
Blood "「昨日のことが、奴にとってもショックだったみたいだな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_10")
T "「……何を知っているの、あなた」"

hide bra_m_03_3
show bra_m_02_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_10")
voice blo_g0460
Blood "「たいしたことは知らないさ。\n
……君とエリオットが、互いに気になって仕方がないらしいということくらいかな」"

hide bra_m_02_16
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_10")
voice blo_g0461
Blood "「気になって……、つまらないことを気にし合っている。\n
柄にもなく、気遣いなどをして」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "肩がびくりと揺れてしまった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "動揺を見せたくなくて、わざと少し間を置いてから視線を持ち上げたのに、楽しげな笑みを含んだ蒼の双眸としっかり目が合う。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「…………」"

hide bra_m_03_2
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice blo_g0462
Blood "「……面倒ごととは無縁でいるのではなかったのかな、お嬢さん。\n
今の君は、まさにその渦中にあるようだが？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分のスタンスを崩すほど、エリオットのことを気にしている。\n
そう言いたいのだろう。"

menu:
    "気になっていると認める。":
        jump gakuen_elliot5_2a
    "意地を張ってみせる。":
        jump gakuen_elliot5_2b
label gakuen_elliot5_2a:
$ lovechara_elliot_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「悪い？\n
……エリオットのことが気になっているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_13")
T "「文句ある？\n
あなたこそ、柄でもなく、人のことを気遣って……」"

hide bra_m_03_4
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
Blood "「…………」"

hide bra_m_03_10
show bra_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_13")
voice blo_g0463
Blood "「……ふふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……何よ」"


play music blood_t_ali
hide bra_m_03_9
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice blo_g0464
Blood "「……っく。\n
はははは、君は本当に私を退屈させないな、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "開き直るように声を荒げた私に、ブラッドは楽しくて仕方がないというように声をあげて笑い出した。"

hide bra_m_02_8
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0465
Blood "「……私のは、気遣っているわけではなく、遊んでいるだけさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……でしょうね」"

hide bra_m_02_15
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice blo_g0466
Blood "「面倒ごとや厄介ごとも、人の身に降りかかるものなら、いい退屈しのぎになる。\n
……私なら御免だがね、ふふ」"

jump gakuen_elliot5_3
label gakuen_elliot5_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「……まさか。\n
エリオットのことは、見かけないから、どうしたのかしらと思っただけよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう言って、一拍挟んで紅茶を味わう。\n
ふうと一息ついてから、再び口を開いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（さりげなく、さりげなく）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「……で？\n
どうして、エリオットがショックを受けているの？」"

hide bra_m_03_4
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
Blood "「…………」"


play music blood_t_ali
hide bra_m_03_10
show bra_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice blo_g0464
Blood "「……っく。\n
はははは、君は本当に私を退屈させないな、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気にしていないふうを装おうと試みつつも、結局聞いてしまった私に、ブラッドは楽しくて仕方がないというように声をあげて笑い出した。"

jump gakuen_elliot5_3
label gakuen_elliot5_3:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……あなたには、私のことがずいぶんと滑稽に映るようね」"

hide bra_m_02_4
show bra_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice blo_g0467
Blood "「……ふ。\n
滑稽だなどとは……」"

hide bra_m_01_2
show bra_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice blo_g0468
Blood "「君とエリオットのことは……。\n
そうだな……、可愛いと思っているよ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざとらしく、目元に浮いた涙を拭うような動作つきだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（～～～～っ。\n
本当、腹立たしいというか、厭味というか……！）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おちょくられているような気分にさせるのがうまい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一口に「可愛い」といっても、私がエリオットに思うような可愛さでないことは明確だ。"

hide bra_m_01_3
show bra_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0469
Blood "「……逃げたり追いかけたりと、まるで物語のようじゃないか。\n
本を読んでいるようだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "読書家という点では、ブラッドと私は気が合う。\n
嫌な奴だと思いつつ、親近感はある。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「……やっぱり、私、避けられているの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私よりもずっと、ブラッドはエリオットを知っている。\n
やはりエリオットは私を避けているのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "去り際の「忘れてくれ」というのは……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（…………）"

hide bra_m_01_11
show bra_m_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice blo_g0470
Blood "「あいつは、見ての通り、動物的な男でね。\n
単純ながら、直感で動く」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_20")
T "「……どういうこと？」"

hide bra_m_03_16
show bra_m_03_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_20")
voice blo_g0471
Blood "「あいつは、昨日のことが自分のせいだということを理解している。\n
だから、お嬢さんに近づく資格がないと傷心なのさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_6")
T "「な……っ！\n
何よ、それ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_4")
T "（……なに、それ）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_9")
T "「そんな……っ！」"

hide bra_m_03_3
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_9")
voice blo_g0472
Blood "「ふふ、私に怒鳴らないでくれ。\n
私は、あいつの考えていることを代弁してやっているだけだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_13")
T "「なら、ついでに代理で怒鳴られておきなさいよ！」"

hide bra_m_02_15
show bra_m_02_17 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_13")
voice blo_g0473
Blood "「……無茶を言うな、お嬢さん」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしも、間にテーブルがなかったのならば、私はきっとブラッドの胸倉を掴んでいた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際エリオットがいたならば、その胸倉を掴んでがっくんがっくん揺さぶって、そしてひっこぬく勢いでその耳を引っ張っているところだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「……なんで、そんな発想になるのよ」"

hide bra_m_02_17
show bra_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
voice blo_g0474
Blood "「……さてね。\n
動物なりの気遣いなんだろう、私にはよく分からないがね」"


play music disquieting_a_wam
hide bra_m_02_1
show bra_m_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_14")
voice blo_g0475
Blood "「……で。\n
本当に、そうなのか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「……っ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "急に、空気が冷えたように感じた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが一瞬にしてその身にまとう空気を変えたのだ。ぞっとするような冷気を、つい先ほどまで私をからかって笑っていたはずの男から感じる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「な、何が、『そう』なの？」"

hide bra_m_03_16
show bra_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice blo_g0476
Blood "「エリオットのせいで、君にまでとばっちりが及んだのかと聞いているんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「だ、だとしても、エリオットのせいじゃないわよ！\n
怒ったりしないで」"

hide bra_m_01_5
show bra_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice blo_g0477
Blood "「エリオットに対して、怒っているわけじゃないさ。\n
君にまで危害が及ぶに至ったことについては甘いと言わざるを得ないが」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「…………」"

hide bra_m_01_13
show bra_m_01_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice blo_g0478
Blood "「……もちろん、君に対して怒っているのでもない」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_16")
T "「……じゃあ、なんで怒っているの？」"

hide bra_m_01_12
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_16")
voice blo_g0479
Blood "「いや、そもそも怒ってなどいないさ。\n
楽しんでいる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……そうは見えないけど」"

hide bra_m_03_2
show bra_m_03_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice blo_g0480
Blood "「……何にでも、ルールというものがあるんだよ、お嬢さん。\n
破った輩にはペナルティが課せられる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「それが楽しいの？\n
つまり……、仕返しが」"

hide bra_m_03_10
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_10")
voice blo_g0481
Blood "「……ふ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は、明言しない。\n
だが、当たりということなのだろう。"

hide bra_m_02_15
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0482
Blood "「……うちの寮はならず者の集まりだなどと言われているが、真っ当な人間も含まれている。\n
君のように……」"

hide bra_m_02_18
show bra_m_02_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0483
Blood "「……普通のお嬢さんを巻き込んだとあれば、それなりのペナルティはあってしかるべきだ。\n
ルールは守ってもらわなくては」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（……これが、ブラッド＝デュプレなのね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "日頃エリオットに仕事を丸投げしているように見えても、やはり彼がここのボス。\n
普段は感じないが……、格というか、リーダーだという雰囲気があった。"

hide bra_m_02_14
show bra_m_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0484
Blood "「そうするべき事態なんだろう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「……今、風紀委員長のユリウスも調べてくれているわ。\n
でも、その可能性が高いと思う」"

hide bra_m_03_16
show bra_m_03_19 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
Blood "「…………」"

hide bra_m_03_19
show bra_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice blo_g0485
Blood "「お嬢さん、君がそう言うということは……。\n
確証があるんだな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「確証というほどじゃないけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらりと見た後ろ姿が、あの日エリオットに押さえ込まれていた青年の姿に重なる。\n
背格好はよく似ていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「……いえ。\n
証拠がないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドに言えば、証拠などなくともその線で進めてしまいそうだ。"

hide bra_m_01_9
show bra_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0486
Blood "「証拠などなくても……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……だから、怖いんでしょ。\n
間違っていたらどうするの」"

hide bra_m_01_10
show bra_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice blo_g0487
Blood "「間違っていたら……、やり直せばいい。\n
間違った対象には詫びを言って、他を探すさ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_16")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_4")
T "（この人って……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "シンフォニアは名門校だ。\n
それゆえ、私はこの学校に入るまで素行不良の者なんていないと思っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際、一般の学校にいるようないわゆる不良はほとんどいない。\n
この学校の不良は……、なんというか……、不良といっても……。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……本物のやくざ者みたい）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "実際、ここを出たら本職になりそうな雰囲気がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_14")
T "（でも、ブラッドに任せたら……。\n
……そうしたら、この件はかたがつく？）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_7")
T "（いや……、つかなくてもつかせそうな……。\n
力技というか、もっとえげつない方法で）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "犯人を見つけて、罰してしまえば、事件としては収束するだろう。\n
任せれば、ブラッドはこの寮の寮長として適切以上のことをやってくれそうだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "事件が終わってしまえば、エリオットも態度を軟化させるかもしれない。\n
私を避けるようなことも……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_16")
T "「ブラッドのほうでも調べてくれるのなら……」"
if lovechara_elliot_points == 9:
    jump gakuen_elliot5_4b
jump gakuen_elliot5_4a
label gakuen_elliot5_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「……お願いしてしまってもいいかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私一人では、どうすることもできない。\n
いくら犯人のメドがついているとはいえ、何か出来ることもない。"

hide bra_m_01_7
show bra_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0488
Blood "「構わないとも。\n
私にとっても楽しみにつながることだ、喜んで」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドは私の声に満足げに頷いて、それからテーブルの上に両手を組み、その上に顎を乗せる形で身を乗り出した。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_7")
T "（う、わ……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "長めの前髪が影を落とす双眸が、ぎらりと物騒な色に瞬いたような気がした。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "頼んだ瞬間、後悔が始まる。\n
とんでもない人を頼ってしまったのではないだろうか。"

hide bra_m_03_9
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0489
Blood "「さあ、話を聞こうか」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "引き返せないところに、足を踏み出してしまった気がしつつも、私はゆっくりと口を開いた。"

hide bra_m_02_15
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg06_sk_h_day
with stripe_l_medium

scene bg06_sk_h_eve
with dis

scene bg06_sk_h_nig
with dis

scene bg06_sk_h_day
with dis

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_par12_hct_day
with stripe_l_long

play music high_day_p_wam
##[rchara1 PAY ATTENTION="false"]
show bra_m_02_14 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice blo_g0490
Blood "「あっけなかった。\n
……つまらない」"

hide bra_m_02_14
show bra_m_02_18 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
voice blo_g0491
Blood "「また面白いことがあったら教えてくれ。\n
面倒でないこと限定で」"

hide bra_m_02_18

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（面倒でなくて、あっけなくなくて、面白いこと、ね……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もちろん、私がそんなことを知るはずがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すべてのカタがついたと、ブラッドから連絡があったのはそのほんの数日後のことだった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その連絡を受けて訪れたテラスの茶会で、ブラッドの隣にはしょんぼりとした大きな影がある。\n
エリオットだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「……エリオット」"


show eri_m_03b_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice eri_g0192
Elliot "「っ……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "名前を呼んだだけでも、その声に篭る怒気は通じる。\n
びくっと、エリオットのしょんぼりと垂れていたウサギ耳が跳ねた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "怯えたように伏せたウサギ耳は、ちょっとどうにかなってしまいそうなほどに可愛らしいが、今はそれどころではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「エリオット！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ずかずかとティーテーブルに歩み寄る。"

hide eri_m_03b_13
show eri_m_03a_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0193
Elliot "「ご、ごめんな、俺、あんたに怪我させちまって……！！」"

hide eri_m_03a_4
show eri_m_03b_12 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0193_5
Elliot "「責任とってちゃんと犯人とっちめてやろうと思ったのに、手間取っちまってよ……！」"

hide eri_m_03b_12
show eri_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0194
Elliot "「結局あんたとブラッドの手を借りてしか、犯人の野郎を見つけられなかった……！！\n
不甲斐ないよな、すまねえ！！」"

play sound se_0052
hide eri_m_01_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がテーブル前に着くと同時に、エリオットはバネ仕掛けのおもちゃのように立ち上がってそう言った。すまねえと繰り返し、深く頭を下げられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "理想的な角度だ。\n
ほぼ直角に近い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、どういうふうに理想的かというと……、私の目の前にはエリオットの柔らかですべらかな毛並みの二本の耳が差し出されている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それはもう、さあどうぞ引っ張ってくださいと言わんばかりに、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（ふ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "額がテーブルについてしまいそうなほどに頭を下げているエリオットには、私の顔は見えていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらり、と私の顔を見てしまったらしきブラッドが、一瞬引いたような顔をして、すっと視線をそらした。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_15")
T "（……失礼ね）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（期待に応えてあげようっていうだけじゃない……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「いいのよ、エリオット」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "持ち上げた手で、くしゃりと彼の金髪へと触れる。\n
色鮮やかな金色の髪は、手触りもいい。"


show eri_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0195
Elliot "「っ！」"

hide eri_m_02_5
show eri_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0196
Elliot "「あんた……っ！\n
許してくれるのか！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_4")
T "「ええ、もちろん許すわ。\n
……{size=+20}そのお耳をくれたらね？{/size}」"

hide eri_m_01_5
show eri_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_4")
voice eri_g0197
Elliot "{size=+20}「え」{/size} "

hide eri_m_01_10
show eri_m_01_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_4")
voice eri_g0198
Elliot "「み、耳！？\n
耳が欲しいって、そんなグロ……、[firstname]！？」"

play sound se_0492
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットが顔を上げるより先に髪に触れていた手を素早く耳へと滑らせた。\n
逃げかけた彼は自爆する。"

play sound se_0055

show m_eri5_goodend1 onlayer master
with dis
hide eri_m_01_9

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0199
Elliot "「{size=+20}いっ！？{/size}\n
いってえええええええ！！！！」"


play music district_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0200
Elliot "「な！？何するんだよ、[firstname]！？ちょ、離せって……っ、{size=+20}いでででででで……！！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0201
Elliot "「耳は本当、弱いんだって……！！！\n
耳なんて、普通、欲しがったりしないだろ……っ！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_5")
T "{size=+20}「普通じゃない耳だもの」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "即答した。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_8")
T "「エリオット、あなた自分では分かっていないのね……？\n
本当に素晴らしいのよ、あなたの耳は」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相変わらず、エリオットの耳のさわり心地はその髪以上に素晴らしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ウサギの毛皮のマフラーは高級品だが、その理由が分かる気がする。\n
こんなにも柔らかで、すべらかで、そして暖かい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（……もふもふ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_14")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_1")
T "（はあ～～、気持ちいい……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "幸せだ。\n
私はこうしてエリオットに触れていると、こんなにも幸せになることが出来る。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それなのに、私から離れようなんて、彼は私のことをまったく分かっていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_17")
T "（そうよ、忘れろ、なんて……）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_6")
T "（……忘れられるはずがないじゃない。\n
このもふもふ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ああ、これは恋だ。\n
まごうことなき、恋。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はエリオットが大好きだ。\n
何もかも……、この耳も。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice eri_g0202
Elliot "「な、なあ……っ！！？\n
お願いだから放してくれって……！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_4")
T "「嫌よ。\n
あなたが私から逃げ回っていた分、堪能するの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_4")
voice eri_g0203
Elliot "「……っっ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さすがにここ数日、私を避けていたことに対しての罪悪感はあるのか、エリオットの抵抗がぴたりと止んだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_1")
T "（……可愛いウサギさん）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私のことを気遣い、私を守るために離れようとしたり（余計なお世話だが真剣に）、そうして離れたことを責められれば、私のされるがままにもなってくれる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_8")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_8")
voice eri_g0204
Elliot "「……っ！！！！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_8")
voice eri_g0205
Elliot "「い、今なんか……っ。\n
えっ、ええええっ！！？？？？？」"

hide m_eri5_goodend1
show m_eri5_goodend2 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "溢れんばかりの愛しさに突き動かされて、はむっとその耳の先っちょを咥えてみた。歯はたてないように、もふもふと甘噛みする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "痛くはないはずだ。\n
……ああ、私はどこかがおかしくなっているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼は可愛く、私はそんな彼を食べてしまいたいくらいだと思っている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_14")
T "（……若干、恨みもこもっているけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここまで惹かれるもふもふでも許されないほど、エリオットの仕打ちときたら酷かった。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
Elliot "「……っ、[firstname]！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……酷いわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice eri_g0206
Elliot "「……えっ、あ、ごめ……。\n
酷いよな、あんたに待ってもらって、そのくせ犯人を自力でどうとも出来なくて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（……そこじゃないのよ、酷いのは）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どうして分からないのか。\n
酷いのは、ちゃんと私に向き合ってくれなかったことだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "気持ちが通じ合ったのに、放り出された。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_9")
T "（酷い）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_9")
voice eri_g0207
Elliot "「……っ、な、酷いのは分かったから、やめてくれよ。\n
っ、こ、こんな……、わ、あ……！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_13")
T "（ちっとも分かっていない）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_4")
T "「……酷いから、報復しているの」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_4")
voice eri_g0208
Elliot "「～～～～っ！！！」"

play sound se_0155
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "紅茶に被害を出せば、隣のブラッドにもとっちめられると分かっているせいだろう。エリオットは控えめにテーブルをタップして、降参を示している。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くすぐったいのだろうか。\n
はむはむ、と唇で圧を加えるたびに、ふよふよとエリオットの耳は小刻みに震える。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらり、とブラッドを見た。"

hide m_eri5_goodend2
show m_eri5_goodend3 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0492
Blood "「……忠告しておこう。\n
それ以上見せつけるつもりならば、{size=+20}私も混ざるぞ？{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……エリオットいじめに？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice blo_g0493
Blood "「ふ、誰が。\n
私はウサギよりも、お嬢さんをいじめたいんだが」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_17")
T "「遠慮しておくわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_17")
voice blo_g0494
Blood "「……犯人探しと解決のお礼としてでもいいぞ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「お礼はお礼として言います。\n
ありがとう、寮長」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "格式ばって言うと、ブラッドは嫌そうな顔をした。\n
義務だろうと聞こえたのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0495
Blood "「……厭味か？\n
礼を言うなら、せめて見せつけるのをやめてくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「……そうね」"


play music transparent1_a_ali
hide m_eri5_goodend3
show m_eri5_goodend4 onlayer master
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice eri_g0209
Elliot "「へ？？？\n
見せつけ……って？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はようやくエリオットの耳から、手と唇を離す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "状況が飲み込めていないのか、エリオットは涙目のまま私とブラッドとを交互に見ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にっこり、と笑いかけてやれば、分かりやすくエリオットの頬に朱色がのぼった。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_1")
T "（……本当、可愛いんだから）"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_1")
voice blo_g0496
Blood "「見せつけるな、と私は言っているんだが」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「そんなつもりはないわよ？\n
ねえ、エリオット」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice eri_g0210
Elliot "「え？？？\n
いや、見せつけるって、どう見ても……いじめられてるだろ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice blo_g0497
Blood "「……さあな。\n
私は静かに紅茶が飲みたい……、恩義を感じているなら、そろそろ出て行ってくれ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice blo_g0498
Blood "「オレンジも御免だが、ピンク色の空気も耐え難いものがある……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドはげっそりと溜息をつく。\n
彼は、私に手を貸したことを後悔しているのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "でも、もう遅い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "引っ付いた暁には、見せつけだってするし……、もっと表に出てもらって、エリオットの仕事を減らすべく頑張ってもらわねば。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_2")
T "（これから、宜しくね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "エリオットにもだが、ブラッドに対しても思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これから、私達は親しくなっていくのだろう。\n
今回の、犯人がどうなったかなどの詳細を知れば、私はきっと後悔するはずだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドが、手助けしたこと以上に。\n
だが、後悔しても、付き合いをやめたりはしない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「ね、エリオット」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice eri_g0211
Elliot "「ん……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「どんな悪い面があっても、一度付き合うって決めた相手を放り出しちゃいけないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice eri_g0212
Elliot "「あ、あれは一時的に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「一時的にでも、よ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "少しも、離れたくない。\n
私達は、これから、そういう気持ちを持つことになるのだろうか。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "あるとしても、それはまだ、ずっと先の話。"

hide m_eri5_goodend4
hide ali_m_06_16
hide frame_par_togaki
with Dissolve(5)
scene black with Dissolve(5)
stop music
jump gakuen_b

label gakuen_elliot5_4b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_15")
T "（いえ、駄目よ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなのは、フェアじゃない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "たとえ、相手が恨みを持った相手の知人の女の部屋のガラスを割るような不届き者だったとしても、だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_03_16")
T "（……大体、当事者がいないし）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相手がアンフェアだからといって、自分までがそうなる必要はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は帽子屋寮を選んだが、だからといって、ならず者にならなければいけないわけでもないのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分で選べる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ありがとう、ブラッド。\n
でも、いいわ」"


show bra_m_03_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_18")
voice blo_g0499
Blood "「いい、とは？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "面白そうに、ブラッドは片眉をぴくんと跳ね上げる。\n
わざとらしさが、この男には妙にはまる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_1")
T "「気遣われなくても平気」"

hide bra_m_03_15
show bra_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_1")
voice blo_g0500
Blood "「ふふ。\n
それでは、まるで私が気遣いを忘れない、優しい男のようだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_15")
T "（優しいかどうかはともかく……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自分の寮の者や、部下の恋人候補にはそれなりに気遣ってくれる。\n
だが、そんなことを言えば、きっとへそを曲げるだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（……この人って、私と似ているところがあるのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "捻くれ者という点で、そっくりだ。"


play music secret_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「私が、自分でケリをつける」"

hide bra_m_03_9
show bra_m_03_16 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice blo_g0501
Blood "「ほう、お嬢さんが自分で？\n
ふふ、君はずいぶんとこの寮に染まったらしい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「違うわよ、元からこうだからこそ……。\n
ここを選んだの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だが、彼らの流儀通りには動かない。\n
まったく、捻くれている。"

hide bra_m_03_16
show bra_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0502
Blood "「……ふむ、それは頼もしい。\n
エリオットは果報者だな、くくっ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_4")
T "「……そうかしら。\n
その、当の相手には逃走されているようだけれど」"

hide bra_m_01_11
show bra_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice blo_g0503
Blood "「それはまあ……、あいつが悪い。\n
あいつは君を、守るべきか弱い淑女だと思っているからな」"

hide bra_m_01_13
show bra_m_03_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_4")
voice blo_g0504
Blood "「君は、あいつが思う以上にしたたかだ。\n
……私と浮気をしてみるつもりは？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_17")
T "（浮気も何も、本命と始まってさえいないんだけど）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ブラッドも、分かっていてからかっているのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「……それ、褒めている？\n
それに、残念ながら、あなたとはいい友人でいたいわ」"

hide bra_m_03_1
show bra_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_1")
voice blo_g0505
Blood "「……ふ。\n
あいつは馬鹿なウサギだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_7")
T "（それには、同意。\n
あなたは本当に馬鹿よ、エリオット）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私は、淑女なんかではない。\n
姉さんのように、まっすぐで清らかな女性ではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だから、そんなに一生懸命守ろうとしなくてもいいのだ。"

hide bra_m_03_2
show bra_m_02_15 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0506
Blood "「残念だよ。\n
だが、私と直接関わりのないところでも面白くしてくれるというなら歓迎しよう」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "互いに紅茶のカップを傾けながら、そんな会話をテンポよく交わす。\n
ブラッドは自分のせっかくの申し出を断られたというのに、上機嫌だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この距離感がいい。\n
エリオットとは違う意味で、私はこの寮長が好きになった。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「…………」"

play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "くうっとカップの中身を飲み干すと、ティーカップをソーサーの上に戻す。"

hide bra_m_02_15
show bra_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice blo_g0507
Blood "「おかわりはいかがかな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「ごめんなさい、悪いけど、急用を思い出したの。\n
……塔に話をつけてくるわ」"

hide bra_m_02_8
show bra_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_6")
voice blo_g0508
Blood "「ああ。必要だったら、私の名前を出しなさい。\n
好きに使うといい」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「……ありがとう、ブラッド。\n
茶葉も、ありがたくいただくわ」"

hide bra_m_03_4
show bra_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice blo_g0509
Blood "「ふふ。\n
どういたしまして」"

hide bra_m_01_11
show bra_m_01_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice blo_g0510
Blood "「……私は、面白ければ何だっていいんだよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "和やかに穏やかに会話を交わしながらも、その口元に浮かぶ笑みは不穏だ。\n
獲物をいかに解体するかを話す、肉食獣の穏やかさに似ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんなものがあるとしたら、の話だが。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……それが、心地いいだなんて）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_17")
T "「それじゃあ、行って来るわ」"

hide bra_m_01_7

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう告げて、再び塔に向かうためにテラスを後にした。"

with dis
$ hi_mes()

scene bg_par12_hct_day with Dissolve(.8)

scene bg_par15_rg_hat_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_par15_rg_tow_day
with stripe_l_medium

play music laboratory_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔へと戻る道すがら。通りすがりにでもエリオットの姿を見かけたりはしないだろうかと思うものの、やはり彼の姿を見つけることは出来なかった。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもならば、学園も広いのだから仕方がないと思うことができるのに。\n
今はまるでそれが避けられている証拠のようで腹立たしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……馬鹿エリオット。\n
馬鹿ウサギ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "心の中で毒づきながら、風紀委員会室の扉をノックする。"

play sound se_0303
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0050
Julius "「開いている。\n
入ってくれ……、っと、おまえか」"


scene bg_par19_fi with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスに促されて足を踏み入れた風紀委員会室には、二人の見知らぬ生徒の姿があった。\n
おそらくは風紀委員だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "邪魔をしては悪いと、一度廊下に退こうとするものの、ユリウスがそれを手で制した。"


show yuri_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0051
Julius "「おまえ達、少し下がっていてくれ。\n
また用事が出来たら呼ぶ」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice kaz_g0016
Fuuki "「はい、分かりました！\n
指示を待ちますね！」"

with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice ari_g0024
Fuuki "「分かりました！\n
廊下で待機しています！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "はきはきとした調子で答えた生徒達が、私とすれ違うような形で廊下へと出て行く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "追い出してしまうような形になるのが悪くて軽く頭を下げると、二人してにこやかに会釈を返してくれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人が完全に廊下に出るのを見届けてから、私はユリウスの傍らまで歩みを寄せた。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「よかったの？」"

hide yuri_m_02_10
show yuri_m_03_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice jul_g0052
Julius "「いや、むしろ、ちょうどよかったんだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「？」"

hide yuri_m_03_8
show yuri_m_01_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice jul_g0053
Julius "「昨夜の件についての指示を出していたところだ。\n
おまえから新たな情報が入るのならば、指示はその後のほうが合理的だ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_6")
T "「……確かに。\n
私にとっても、そのほうが都合がいいわ」"

hide yuri_m_01_4
show yuri_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_6")
voice jul_g0054
Julius "「どういうことだ？\n
……何を吹き込まれてきた」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスが嫌そうに眉根を寄せる。"

hide yuri_m_03_4
show yuri_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0055
Julius "「おまえの寮の連中ときたら……。\n
素行不良のくせに、やたら結束が固くてかなわん……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私がここを出た後、誰に会ったのか大体の見当がつくらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_13")
T "「先に、ちょっと確かめておきたいことがあるんだけど……。\n
いいかしら？」"

hide yuri_m_03_11
show yuri_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_13")
voice jul_g0056
Julius "「言ってみろ。\n
おまえは被害者だからな、答えられる範囲で答えてやる」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_14")
T "「ありがとう。\n
まず、ブリーズについてを聞きたいんだけれども」"

hide yuri_m_02_10
show yuri_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice jul_g0057
Julius "「ブリーズというのはストームの逆、女子が男子寮に攻め込むイベントだな。\n
ブリーズ、ストーム、どちらも馬鹿げたイベントではあるが、学校公認だ」"

hide yuri_m_03_9
show yuri_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_14")
voice jul_g0058
Julius "「他に……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_4")
T "「……公認なのね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "にたり、と私の口元に笑みが浮かぶ。\n
その笑みに、ユリウスは露骨に嫌そうな顔をした。"

hide yuri_m_03_2
show yuri_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0059
Julius "「なんだ、その顔は。\n
悪巧みをしている帽子屋のようだぞ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「あなたそれ、失礼よ」"

hide yuri_m_01_3
show yuri_m_01_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_12")
voice jul_g0060
Julius "「失礼なのはおまえだ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "即答で返した言葉に、それまた即答で返された。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……まあ、本当に悪巧みしているわけなんだけれども）"

hide yuri_m_01_11

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はどうやら、思っていた以上に帽子屋寮に染まってしまっているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寝食を共にすると、似てくる。\n
元から望んで入った場所、寮全体にいえることなのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスも言う通り、結束は固くて当然。"

with dis
$ hi_mes()

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg_map_day
with stripe_l_medium

scene bg_map_eve with Dissolve(1.2)
##endmemory
jump gakuen_elliot6
