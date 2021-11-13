jump fushigi_common2_castle
label fushigi_blood2_2:

scene hm_spr_01
with stripe_l_medium

scene bg_gen23_hkt
with stripe_l_long

play music castle_guestroom_p_ali

show viv_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0249
Vivaldi "「おお、[firstname]。\n
こんなところにおったのか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ビバルディ？」"

hide viv_t_02_10
show viv_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0250
Vivaldi "「姿が見えぬと思ったら、何をしておるのじゃ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ああ、これ？\n
せっかくお邪魔させてもらっているから、お料理でも習っていこうかと思って」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "帽子屋屋敷は基本的に個人主義だ。\n
食べ物の趣味も人それぞれだから、一度にたくさんの料理を作ることは多くない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まあ、誰かさんみたいに一人で大量のにんじん料理を消費することはあるけど、あれはかなり特殊な例だし……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、ハートの城は逆だ。\n
舞踏会も然り、大勢を一度にもてなす機会も多い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰か一人のためではなく、大勢の人の口に合うものを作ることがもっとも肝心なこと。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（万人受けする料理って基本に忠実なものが多いから、いくら習っておいても悪くないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "城に滞在している今の私はあくまで客人だ。\n
まさかここのメイドさんに混じって仕事をするわけにもいかない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手持ち無沙汰もあって、厨房のシェフの手が開いているときにはこうして料理を習っていた。"

hide viv_t_01_5
show viv_t_01_5 at left
show chef_a_1 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0012
Chef "「ええ、お嬢さんならいい腕になりますよ。\n
教え甲斐もありますしね」"

hide viv_t_01_5
show viv_t_03_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

hide viv_t_03_9
show viv_t_03_7 at center
hide chef_a_1
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0251
Vivaldi "「おまえの手料理は悪くないが、わらわはつまらぬ。\n
せっかくいいことを思いついたのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "不満そうに口を尖らせたビバルディの言葉に、聞き返す。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「いいこと？」"

hide viv_t_03_7
show viv_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0252
Vivaldi "「ああ、とても楽しいことじゃ。\n
おまえもきっと楽しめると思う」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "まわりの目があるせいか、ビバルディは具体的に話そうとしない。\n
だが、その目はきらきらと輝いていて楽しみにしていることが窺える。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（ビバルディの楽しいこと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "斬首が口癖の女王だが、ぬいぐるみを好む可愛らしい面も持っている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "他の人間に知られないようにしたいということは、そちらの趣味なのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（それに首を刎ねるのもいつものことだから、今更新しい楽しみとは言わないわよね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_18")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（違う、違う。\n
そうじゃないって！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に慣れてきても、越えてはいけない一線というものが存在する。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここは私の住むと決めた世界。\n
だが、すべてに頷かなければいけない世界ではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "受け入れられないものは、そう伝えなければどんどん流されるばかりだ。"

hide viv_t_03_1
show viv_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「[firstname]？」"

hide viv_t_03_11
show viv_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0253
Vivaldi "「どうしたのじゃ？\n
ぶつぶつ申して」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「何でもないわ。\n
じゃあ、料理も一段落したところだし、一緒に行きましょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「あなたも、付き合わせてごめんなさい。\n
ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "付けていたエプロンを外して、シェフにお礼を込めて会釈する。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（片付けがまだ残っているけど、このままビバルディを待たせるわけにもいかないものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "料理を教えてくれた恩人に八つ当たりをされるのは、忍びない。"

hide viv_t_01_11


show chef_a_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Chef "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の言いたいことを察してくれたのか、彼は頷いて早く行くように視線で促してくれた。"

hide chef_a_4


show viv_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0254
Vivaldi "「うむ、よい返事じゃ。\n
では、ついておいで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "満足げに頷くビバルディは、女王と言うよりも、女友達の顔をしていた。"

hide viv_t_01_6

$ hi_mes()

scene hm_spr_01
with stripe_l_medium

play music vivaldi_t_ali

scene v_01
with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「どうしたの、これ？」"


show viv_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0255
Vivaldi "「うむ、今回新しく取り寄せたのじゃ。\n
やはりこういう小道具にも拘りが必要であろう？」"

hide viv_t_02_10
show viv_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0256
Vivaldi "「遊びは本気でやらねばつまらぬからのう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「それにしても……、すごい量ね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの部屋に運び込まれているのは、大量の服だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハンガーに掛けられている分だけでもかなりの数があるが、床の上に積まれたものも少なくない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あら」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（でも、サイズが全部小さいわ……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人形遊びが好きなビバルディだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "服が置かれているのを見て、てっきり今回は私を人形に見立てて着替えをさせるつもりなのかと思ったが、この大きさでは私はとても着られない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_14")
T "（子供用？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ましてやビバルディに着せるのは、論外だ。\n
身長も、女性としての骨格も、この服には収まるはずがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（何か人形に着せるのかとも思ったけど、新しい人形もないみたいだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この部屋には相変わらずたくさんの人形が置かれているが、動物の形を模したものが多い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "服はどう見ても体の小さな子供か人形用の形をしていて、動物用にしては根本的に形が違いすぎる。"

hide viv_t_02_5
show viv_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0257
Vivaldi "「素材も色々と選んでおいたぞ。\n
絹に麻、綿……、他に手織りの生地もある」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……ええと、色々な種類があるのは分かったけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「これ、誰が着るの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（まさか、ピアスの持っている小さくなる薬を飲むとか言わないわよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女王ならば眠りネズミの薬ぐらい簡単に調達出来るだろうが、あれは大きさの調整が難しい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さくなりすぎたらとても着せ替えをするどころではないだろう。"

hide viv_t_01_3
show viv_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0258
Vivaldi "「わらわに決まっておろう。\n
おかしなことを言うのう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "{size=+20}「ええっ！？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ビバルディがこれを着るの！？」"

hide viv_t_01_5
show viv_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_4")
voice viv_f0259
Vivaldi "「……何じゃ、その反応は。\n
まあおまえが着たいと言うのなら、話は別じゃが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「いやだって……、サイズが大分合わないし」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（それに、ビバルディが着るには、デザインが可愛い系よね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディは目鼻立ちがはっきりしているので、けして似合わなくはないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、彼女の美しさが引き立つのは、もっと別の服だ。\n
まさに今着ている赤のドレスなど、その最たるもの。"

play sound se_0490
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "物言いたげな私の視線が気に入らなかったのか、彼女は苛立ったように杖で自分の手の平を打った。"

hide viv_t_03_11
show viv_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0260
Vivaldi "「……何じゃ、おまえ、まさかわらわが太いとでも言うつもりか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「っ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「滅相もございません……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（こ、怖い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "女性に体型を匂わす言葉は禁句だということは言うまでもない。"

hide viv_t_01_8
show viv_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0261
Vivaldi "「じゃが、確かにおまえの言うとおりでもある。\n
今のわらわにこれは着れぬ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「？\n
だったら、どうして……」"

hide viv_t_03_12
show viv_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice viv_f0262
Vivaldi "「ふっ……、簡単なこと。\n
服が小さいならば、わらわもそれに合わせればよい」"

play sound se_0466
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤いドレスが小さくなったと思ったときには、そこには小さな美少女がいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが顔に残るほくろも、あどけなさが残りつつも整った顔立ちも、私の知っているひとに似ていた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「！！」"

hide viv_t_03_2


scene hm_spr_01 with stripe_l_long
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「え……」"

scene map_bg_spring_day with stripe_l_short

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "{size=+20}「ええええっ！？」{/size} "


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "間違いなく、この時間帯で最大の悲鳴を上げて、今度こそ私はのけぞった。"


scene v_01 with stripe_l_long
play music cheerful_a_ali



show viv_chil01_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0263
Vivaldi "「……騒々しいぞ、[firstname]。\n
帽子屋のところの門番もよくやっているではないか」"

hide viv_chil01_16
show viv_chil01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0264
Vivaldi "「わらわが子供の姿になったぐらいで騒ぐものではない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「いや、それはそうなんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ディーとダムが子供の姿になったり、大人の姿になったりするのは、私ももう驚かない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一言で言ってしまえば慣れたということだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、大人の姿から子供へと姿を変えたのは、彼女が初めてだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それが許される世界だとは知っていたが、実際に目の当たりにするとどうしても驚かずにはいられない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（この世界にもずいぶん慣れたと思っていたけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、私の反応をビバルディは別のものとして取ったらしい。\n
したり顔で頷いてくる。"

hide viv_chil01_10
show viv_chil01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0265
Vivaldi "「ふ、そうか。\n
幼いわらわの可憐さに驚いておるのだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「え、ええ……。\n
そうね、驚いているわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "適当な相槌を打ちながら、私は目をビバルディから離せずにいる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……私、そういう趣味はないはずなんだけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（可愛い）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（反則的に可愛い、どうしたらいいのって言うぐらいに可愛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの子供姿は、大人の彼女とはまったく趣が違っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T "（いつもは切れ長の目が、今は大きくてくりくりだし……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_8")
T "（顔の輪郭も柔らかくて、本当に人形みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの女王としてのビバルディは、欠伸姿さえ威厳のある、完璧な女王様だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この少女が大きくなってあのビバルディになるのだと言われても、すぐに納得するのは難しいぐらいに可憐な顔立ちだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_1")
T "（口調がいつものビバルディそのままっていうのがまた可愛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さな子供が一生懸命大人の真似をしているような、そんな印象を受ける。"

hide viv_chil01_2
show viv_chil01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0266
Vivaldi "「そうじゃろう、そうじゃろう」"

hide viv_chil01_7
show viv_chil01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0267
Vivaldi "「では、早速始めようか、[firstname]。\n
ドレスを選ぶのだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手にした金色の杖（こちらもいつもよりも短くなっている）を振りかざして、小さな女王様は私に命じた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「いいわよ、その服はビバルディが着るために集めたんでしょう？\n
せっかくだから、着たいものを着ればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんなに可愛らしい女の子だ。\n
どんな服を着ても似合うに決まっている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（私がわざわざ選ぶ必要はないと思うんだけど）"

hide viv_chil01_2
show viv_chil01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice viv_f0268
Vivaldi "「何を言うかと思えば……。\n
おまえがわらわのドレスを選ばなくてどうするのだ」"

hide viv_chil01_15
show viv_chil01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice viv_f0269
Vivaldi "「自分から服を選ぶ人形などおらぬぞ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（私が選ぶ？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（人形？）"

play sound se_0361
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "焦れたように私の服を引っ張った子供は、急かす。"

hide viv_chil01_14
show viv_chil01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0270
Vivaldi "「ほら、早く選ばぬか。\n
子供をいつまでも待たせるものではない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ええと……。\n
本当に、私が選んでいいの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確認すると、ビバルディは可愛らしい顔を顰めた。\n
とはいえ、それでも十分すぎるほど可愛らしさは変わらない。"

hide viv_chil01_15
show viv_chil01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0271
Vivaldi "「当たり前じゃ。\n
おまえ以外が選んだものなど、誰が着るか」"

hide viv_chil01_13
show viv_chil01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0272
Vivaldi "「ほら、早く選ぶのじゃ。\n
おまえが選ばなければ遊びにならぬだろう」"

play sound se_0695
hide viv_chil01_14

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「あ、ま、待ってよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言うが早いか、ビバルディは服の森の中に潜り込んでしまった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（ビバルディが着るドレスを私が選んで、楽しいのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず首を傾げた。"

play sound se_0126

show viv_chil01_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもより高い声が癇癪を混ぜて私のことを呼ぶ。\n
女王様の叱責なら身が縮む思いだが、今はそれさえもどこか愛らしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「わ、分かったわ。\n
すぐ決めるからっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "とはいえ、これだけの衣装からわけも分からず選べと言うのは無茶な話だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（……全部見るだけでも、何時間帯かかるか分からないわ）"

hide viv_chil01_16
show viv_chil01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice viv_f0273
Vivaldi "「わらわは早く遊びたいのじゃ、早く選んでおくれ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口調は厳しくとも私を呼ぶその声は、いつものように柔らかい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（……まあいいか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "玩具のような杖と王冠を被った、小さな女友達の姿を見ながら笑みが零れた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（可愛い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どんなに傲慢に振る舞っても許されてしまうほど、今のビバルディは可愛かった。"

hide viv_chil01_8

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "布の洪水に四苦八苦しながら、ようやく一着を決めてビバルディの体に合わせてみた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「どうかしら？」"


show viv_chil01_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice viv_f0274
Vivaldi "「……いやじゃ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え？\n
だって、ビバルディは赤が好きでしょう？」"

hide viv_chil01_16
show viv_chil01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice viv_f0275
Vivaldi "「ああ、好きじゃ。\n
わらわは赤が一番好き」"

hide viv_chil01_13
show viv_chil01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice viv_f0276
Vivaldi "「なにものをも偽らぬ、偽れぬ色だからのう。\n
子供の姿になっても、赤が好きじゃ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（ええ。\n
そう思ったから、とりわけ鮮やかな赤いドレスを探してきたのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、身体に当てたドレスを見て、ビバルディは不満そうに口を尖らせている。"

hide viv_chil01_14
show viv_chil01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0277
Vivaldi "「今のわらわは子供なのじゃ。\n
だから、違うドレスがよい。いつも同じではマンネリだからな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

hide viv_chil01_8
show viv_chil01_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0278
Vivaldi "「……文句があるのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つんとすました表情で睨んでくるビバルディ。\n
眼光は鋭いのに、その様子はどこか微笑ましい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（私にも、妹はいるけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（そういえば、イーディスとこんな会話をしたことはなかったわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "年の離れた妹がいたら、こんな感じだろうか。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（姉さんも、こんな気持ちで私を見ていたのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "手がかかる。\n
だが、その手間さえも愛おしい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（姉さんにそう思われていたのならいいけど、私の場合ビバルディみたいな可愛げはなかったものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何でも許されてしまう可愛らしさ。\n
それは持って生まれた天性のものだ。"

hide viv_chil01_15
show viv_chil01_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「あ、ごめんなさい。\n
じゃあ、次のドレスを探してくるわね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（姉さんも、イーディスも、ここにはいない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薄情なのは私なのに、寂しいと思うのはずるい。\n
ここを選んだのは、他でもない私自身なのに。"

hide viv_chil01_14
show viv_chil01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0279
Vivaldi "「うむうむ、その調子じゃ。\n
早く選んでおくれ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T "「ええ。\n
かしこまりました、小さな女王様」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "綺麗で可愛い女王様との遊びは、小さかった頃に置き忘れてきたものを思い出すような……、そんな気分にしてくれる。"

hide viv_chil01_2

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

show viv_chil02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0280
Vivaldi "「ふむ、まあこんなところか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの赤いドレスから、デザインも色も違うドレスに着替えたビバルディは、ようやく納得がいったのか、鏡の前でくるりと回って見せた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "見た目は相変わらずの可愛らしさだが、私にはそれを楽しむだけのゆとりはない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_15")
T "「そ、そう。\n
ようやく及第点がもらえたのね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（永遠に終わらないかと思ったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここに行き着くまでに試着した服は十点を超える。\n
そして、試着されることなく却下された服は、その倍以上だ。"

hide viv_chil02_2
show viv_chil02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0281
Vivaldi "「何だ、疲れた顔をして。\n
もうくたびれたのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「くたびれたというよりも、気持ちが折れそうだったというか……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T "（まさか、ビバルディの服選びがこんなに大変だったとは思わなかったわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女が取り寄せたというだけあって、服はどれも一級品なのだが、女王様の好みは実に厳しかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "デザインが気に入らないと言われるのならまだ探しようがあるが、「好かぬ」とだけコメントされてしまうと、完全にお手上げである。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_13")
T "「ところで、どうしてドレス選びなんて言い出したの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「メイドさんもいないし……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの部屋には彼女のお気に入りのメイドと、私ぐらいしか立ち入れない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "着替えをするのなら、当然彼女達の手も必要だと思うのだが、結局二人だけで進めてしまった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0282
Vivaldi "「当然であろう。\n
人形遊びに余計なものはいらぬ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「そうよ、そもそも人形遊びっていう意味が分からなかったんだけど……」"

hide viv_chil02_13
show viv_chil02_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice viv_f0283
Vivaldi "「何だと？」"

hide viv_chil02_14
show viv_chil02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
voice viv_f0284
Vivaldi "「おまえ、目の前にこんな立派な人形がいて、気付かなかったというのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（ビバルディが人形？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "予想しなかった言葉に目を剥いたが、納得もした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何種類もの服から似合うものを選んで着せる。\n
人形遊びの大道といえなくはない。"

hide viv_chil02_13
show viv_chil02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0285
Vivaldi "「……わらわが人形では不満か？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「そ、そういうわけじゃないけど……。\n
ビバルディが自分から人形だなんていうから、びっくりしちゃって」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもならば私が彼女のお人形だ。\n
好きなように着替えさせられたり、買い物に付き合ったり。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（その割には、今回もビバルディのほうに主導権があったけど。\n
まあ、子供なら仕方ないわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "家出してきた屋敷の双子を見ていても、それは仕方ないと思ってしまう。"

hide viv_chil02_10
show viv_chil02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0286
Vivaldi "「何だ、慰め甲斐のない子だこと。\n
わらわがおまえのために一肌脱いでやったというのに」"

play sound se_0148

play music happy_a_ali
show t_bra2_1 onlayer master
with dis
hide viv_chil02_15

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぽんと新しいドレスを着たままビバルディは私の膝の上に座ってくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふわふわのドレスを着た彼女は、なるほど、確かに人形と言ってもいいぐらいに可愛い。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「私のため？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice viv_f0287
Vivaldi "「ああ、おまえ、帽子屋のところを出てきてから随分と落ち込んでおっただろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「落ち込んでいたわけじゃないわよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "心配してくれた人に言う言葉ではない。\n
しかし、辛うじて口を出た声は、そんな可愛くないこと。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（強がったって無駄だろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "間近で見つめてくるこの眼差しは、すべてお見通しのような気がする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界での同性の貴重な友人である彼女はいつだって私のことをよく見ているのだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0288
Vivaldi "「そうか？\n
ならば、きっとわらわの勘違いだろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0289
Vivaldi "「今のわらわは子供だからな。\n
間違えることもある」"

play sound se_0551
hide t_bra2_1
show t_bra2_2 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「……[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "名前を呼ばれたと思うと、更に深く体を預けられた。\n
今は子供である小さな体から、いつもの薔薇の香りが漂ってくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0290
Vivaldi "「わらわは人形で遊ぶのが好きじゃ。\n
可愛いものならなおよい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ええ、知っているわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0291
Vivaldi "「うむ、だからこんな可愛い人形がおまえのすぐ傍にあるのだ」"

hide t_bra2_2
show t_bra2_3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0292
Vivaldi "「このわらわが、おまえだけの人形になってあげる。\n
抱き締めてもよいぞ、無礼を許す」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小さな手が、私の頬に触れた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもよりも高い体温。\n
暖かくて、気持ちがいい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「っふ、はははは。\n
ビバルディったら」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_8")
T "「ありがとう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_8")
voice viv_f0293
Vivaldi "「わらわのありがたみがよく分かったであろう？\n
感謝せよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T "（ええ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人形だといっても、彼女の頭部に乗った王冠の重みは変わらない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（最高に偉くて、最高に怖くて、そして可愛い女王様）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今は、その気持ちが嬉しいから。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「次は、ビバルディ好みのドレスをすぐに選んでみせるわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice viv_f0294
Vivaldi "「む……、それは嬉しいが、何だかすぐに決められてしまうのもつまらぬのう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「先刻は、あんなに急かしていたのに」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice viv_f0295
Vivaldi "「子供は気紛れなものなのじゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "くすくすと笑いあうだけで、どうしてこんなにも楽しいのか。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_11")
T "（……ああ、そういえば、私といるときの姉さんも、いつも笑っていたわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今は遠い場所にいるあの人にも、同じ感覚があったのだろうか。\n
離れてしまった私には、確かめることも出来ない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T "（でも、こんな気持ちを持っていてくれたなら、いいのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ただただ願うばかりの気持ちは、一体どこに行くのだろう。"

hide t_bra2_3

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play sound se_0303

play music vivaldi_t_ali

show siro_t_01_01 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice hei_f0023
Maid "「陛下、失礼致します。\n
陛下への謁見を希望している者がおります」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "メイドの声に、寛いでいたビバルディが細い眉を上げた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつの間にか、ドレスを決めてから時間帯が変わっている。"


show viv_chil02_16 at center
hide siro_t_01_01
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0296
Vivaldi "「……何じゃ、誰も通すなと命じておいたであろう」"


show siro_t_01_02 at center
hide viv_chil02_16
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0012
Maid "「ですが、陛下への謁見は、正式なものであれば、お目通りだけでも果たすのがルールですから」"


show viv_chil02_10 at center
hide siro_t_01_02
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0297
Vivaldi "「ちっ、面倒な」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供姿に似合わない盛大な舌打ちを漏らしたビバルディだが、ルールというのなら仕方ないと思ったらしい。"

play sound se_0052
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の膝から立ち上がると、そのまま私の手を掴んで歩き出した。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「？\n
ビバルディ？どうしたの？」"

hide viv_chil02_10
show viv_chil02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice viv_f0298
Vivaldi "「まだ遊びは終わっておらぬからのう。\n
おまえも一緒に来るのだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「え？\n
私も？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（いや、それ以前に……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「その格好で行くの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼女はまだ体を小さくしたままだ。\n
女王への謁見なのに、問題はないのだろうか。"

hide viv_chil02_2
show viv_chil02_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0299
Vivaldi "「なんだ、何か問題でもあるのか？\n
わらわの愛らしさについては、おまえも共感したところであろう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "確かに小さなビバルディは可愛い。\n
それこそ、膝の上にずっと座らせておきたいほどだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（女王としてのビバルディに会いにきた人に、この姿で会うのは……、いいの！？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供の姿であっても彼女が誰か分からないということはないだろうが。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「だって、いつもの姿のほうがいいんじゃないかと思って……」"

hide viv_chil02_16
show viv_chil02_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice viv_f0300
Vivaldi "「構わん、くだらぬルールなのだ。\n
拝謁を許してやるだけでもありがたく思えばよい」"

play sound se_0774

play music castle_corridor_p_ali

scene hr_01
with dis
play sound se_0774
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呼びに来たメイドを後ろに従えて、ビバルディは廊下を歩く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（いつもだと真っ赤な廊下に、真っ赤なドレスだから混ざり合っているけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（この中に水色のドレスって、浮くのね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤以外がいいと言ったビバルディが最後に選んだのは、淡い水色のドレスだった。\n
私の服と合わせてくれたのかと思うと、確証もないのに嬉しくなってしまう。"

hide viv_chil02_14
show viv_chil02_14 at left

show siro_t_02_08 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0024
Maid "「陛下、ですがその……」"

hide viv_chil02_14

hide siro_t_02_08
show siro_t_02_08 at left
show siro_t_01_04 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0013
Maid "「見えたお客様なのですが……。\n
今、ホワイト卿と……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "小声で話しかけてくるメイド達の様子から察するに、何か問題が起こっているらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ペーター？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（あの潔癖症が誰かと会うなんて珍しいわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "宰相自らが相手をするほどの来客。\n
それも、女王への謁見を希望できるだけの人間とは一体誰なのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_3")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（まさか……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬思い浮かべた相手の姿を慌てて消し去る。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "来るはずがない。\n
彼にとってここは敵の領土だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "余程の理由がない限り、領主自ら敵地に乗り込んでくるはずがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（……考えすぎよ）"


show viv_chil02_10 at center
hide siro_t_02_08

hide siro_t_01_04
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
Vivaldi "「…………」"

hide viv_chil02_10
show viv_chil02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice viv_f0301
Vivaldi "「顔も見ておらぬのに、部屋に戻りたくなってきたわ。\n
ああ、頭が痛い」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "溜息混じりにいった彼女の言葉は、何故か他人事には聞こえなかった。"

hide viv_chil02_8

$ hi_mes()

scene he_01
with stripe_l_long

play music castle_audience_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "メイド達が戦々恐々と見守る中、辿り着いたホールにはいくつかの影があった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "腕を組んで来客と対面しているのは、白く長い耳を持った宰相だ。"


show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Peter "「…………」"

hide per_t_02_10
show per_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0257
Peter "「よくもまあ、堂々と顔を出せますね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice blo_f0037
Unknown "「堂々もなにも、一介の商人が門を潜ってこないほうがおかしいでしょう。\n
陰からこそこそと入り込むなんて、まるで盗賊の振る舞いだ」"

hide per_t_02_2
show per_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0258
Peter "「白々しい……」"

play sound se_0023
hide per_t_01_4
show per_t_01_4 at left
show king_t_02_08 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kin_f0010
King "「ホ、ホワイト、落ち着け。\n
確かにぼ……、ではなかった、この男の言うとおり、ルールは破られておらぬ」"

hide per_t_01_4
show per_t_01_9 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0259
Peter "「……ふん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "広い謁見の間で、宰相と王を相手取りながら、少しも畏まる気配のない男がそこにいた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（ペーター相手に、よくあんな態度がとれるものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ハートの城の宰相の冷酷さを知らないのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "やがて背中しか見せていなかったその客は、私達が来たことを察したらしく、振り返った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「え……？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！！！」"


show viv_chil02_16 at center
hide per_t_01_9

hide king_t_02_08
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_7")
voice viv_f0302
Vivaldi "「……ああ、部屋に戻りたい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頭を振ったビバルディの言葉は、私の心情そのものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "（……何であんたがここにいるのよ）"


show bra_d_01_2 at center
hide viv_chil02_16
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_15")
voice blo_f0038
Blood "「おや、どうやらお出まし……、じゃない。\n
お見えになったらしい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "形ばかりは丁寧だが、慇懃無礼な態度を崩そうとしない、ふてぶてしさ。\n
斬首が口癖の女王を前にしてこんな口が叩ける人間は限られている。"

hide bra_d_01_2
show bra_d_01_2 at left
show viv_chil02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0303
Vivaldi "「女王を呼び付けるとは、いい身分じゃな。\n
商人にしては、図々しい男じゃ」"

hide bra_d_01_2
show bra_d_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0039
Blood "「これは失礼。\n
面の皮が厚くないとやっていられない商売なものでして」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "眼鏡ぐらいでは、変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "変装とはとても言えないレベルの変装だが、ブラッドは物怖じした様子もなく立っていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（服が替わっても消えない胡散臭さは、もう国宝ものだけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……一人で、来たの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらちらと周囲の様子を見るが、あの目立つ三人の姿はおろか、構成員の影も形も見えない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（ここは敵地でしょう！？\n
何を考えているのよ、あんたは！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディと繋いでいた手の平に、冷や汗が滲んでいた。\n
堂々と正面から城に入ってきた馬鹿なひとは、本当に一人で来ているらしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディとブラッドはじっと睨み合ったまま動かない。"

hide bra_d_01_11
show bra_d_01_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0040
Blood "「おや、私の顔に見覚えでも？」"

hide viv_chil02_8
show viv_chil02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0304
Vivaldi "「そうじゃな、わらわが一番首を刎ねてやりたい男に、よく似ておる。\n
無礼なところもそっくりじゃ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（ここで首を刎ねろなんて言ったら……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドは常にだるそうな男だが、強い。\n
そうでなければ、マフィアのトップなど出来るはずもない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、役を持たない兵士と城の役持ちに総攻撃されたら……、ただではすまないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人の本当の関係を知っているのは、この場では私だけ。\n
しかし、ここは薔薇の香る帽子屋領の庭園ではない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（殺し合い、奪い合うのがこの人達のゲーム）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのためならば情報を駆使し、出し抜き、隙あらば息の根を止める。\n
殺し合い、奪い合う危険なゲームなのだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（……やめてよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薔薇園以外で顔を合わせるときには、ただの敵同士であっても、私にとって二人はそれぞれ大切な人だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の不安に気付いていないブラッドは、いけしゃあしゃあと言葉を続けた。"

hide bra_d_01_12
show bra_d_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0041
Blood "「ははは、何しろ無頼者なので、口の利き方を知らなくて申し訳ない。\n
無礼があっても、その器量で受け流してもらいたいものですな、女王陛下」"

hide bra_d_01_11
show bra_d_01_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0042
Blood "「珍しい品が入ったので、ぜひご覧頂こうと思って立ち寄ったんですよ。\n
いかがですか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が言うように背後には大きな荷物が積まれている。\n
それぞれ小分けにされた荷物は布に覆われていてよく見えない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（一体何を持ってきたのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "さすがにここで爆薬が出てきたり、ましてやエリオット達が中に入っていましたというのでは、洒落にならない。"

hide viv_chil02_13
show viv_chil02_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Vivaldi "「…………」"

hide viv_chil02_10
show viv_chil02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0305
Vivaldi "「ふん、よかろう。\n
そこまで言うのだ、くだらぬ品だったら、即刻首を刎ね飛ばしてやるぞ」"

hide bra_d_01_2
show bra_d_01_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0043
Blood "「……ご随意に」"

hide bra_d_01_12
show bra_d_01_11 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恭しく礼を取った男が、ちらりと私を見た気がした。\n
しかし言葉を交わすことなく、彼は背後の荷物へと手を伸ばした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視線が外れた途端、ビバルディは口を尖らせている。"

hide viv_chil02_13
show viv_chil02_14 at center
hide bra_d_01_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0306
Vivaldi "「ふん、ほんに図々しい男」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「ビバルディ……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "張り詰めていた緊張感は、たとえ身体が小さくとも、常と何ら変わらない。\n
彼女が、気付いていないはずがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（……本当に、首を刎ねる気じゃないわよね）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（もし、ブラッドとビバルディが本気で殺し合ったら、私は……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "嫌な予感に唇を噛み締めていると、宥めるように小さな声がかけられた。"

hide viv_chil02_14
show viv_chil02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0307
Vivaldi "「役割から外れたことをしようとする愚か者など、首を刎ねるまでもない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_15")
T "「？」"

hide viv_chil02_15
show viv_chil02_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice viv_f0308
Vivaldi "「うちの馬鹿と同じじゃ。\n
別の役割を装ったところで何も変わらぬ」"

hide viv_chil02_16
show viv_chil02_14 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice viv_f0309
Vivaldi "「あの愚かな男がそう振る舞うのなら、遊んでやるまでじゃ。\n
つまらなければ、放っておけばよい」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きっぱりと言いきる彼女の顔は、やはり、赤い城の女王だった。"

hide viv_chil02_14

$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME

show viv_chil02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0310
Vivaldi "「……ほう、言うだけあって、それなりのものは用意してきたようじゃな」"

hide viv_chil02_12
show viv_chil02_12 at left
show bra_d_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice blo_f0044
Blood "「ええ、このあたりなども珍しい織物ですね。\n
模様も色々あって」"

hide viv_chil02_12
show viv_chil02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice viv_f0311
Vivaldi "「ふむ。\n
存外、悪くない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（意外だわ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T "（ブラッドとビバルディが、{size=+20}普通に{/size}\n
{size=+20}会話しているなんて{/size}）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お互い、相手が誰かは分かりきっているのに、今のところ二人は穏やかに布を見ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう、ブラッドが持ってきたのは、大量の布だった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（一応、変装でお咎めなしってことなんだろうけど……、この世界の基準ってよく分からないわ）"

hide bra_d_01_2
show bra_d_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice blo_f0045
Blood "「販売だけではなく、オーダーメイドで色々と作り歩いていましてね。\n
予算も、装飾も、依頼者に合わせております」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんなことをさらりと言った彼は、専門用語を織り交ぜつつ布を選んでいる。"


show siro_t_01_05 at center
hide viv_chil02_2

hide bra_d_01_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0014
Maid "「あら、陛下。\n
こちらも可愛らしいですわ」"

hide siro_t_01_05
show siro_t_01_05 at left
show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0014
Maid "「ええ、この花柄も華やかでよろしいですし」"

hide siro_t_01_05

hide siro_t_02_01
show siro_t_02_01 at left
show siro_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0025
Maid "「目移りしてしまいますわね」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（いつのまにか、メイドさんまで混じっているし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "口が達者な男は、周囲のメイドとも親しげに会話を成り立たせている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "正体を知らなければ、本職といっても過言ではない専門知識まで披露していた。"


show per_t_03_9 at center
hide siro_t_02_01

hide siro_t_01_02
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0260
Peter "「ああ、早く帰ってくれませんかね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「……ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の隣に立った白いウサギは不快そうに顔を顰めた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その赤い目は適当な変装をした男を睨んでいる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「あなたは見なくていいの？」"

hide per_t_03_9
show per_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice pet_f0261
Peter "「あんな男の持ってきたものになど触りたくもありません。\n
雑菌だらけじゃないですか」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T "（ペーターらしい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "絶対にお断りと顔に大きく書いた彼は、私と同じく彼らから少し離れたところにいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディがこっちに掛かり切りになっているため、キングは代行で仕事を押し付けられ、ここにはもういない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "賑やかな一団から離れてその様子を見ているのは、私とペーターだけだった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「いいの？\n
ビバルディのすぐ傍に……、あの人を行かせて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "刺客を送り付け合う間柄でも、彼にとって彼女は主だ。\n
その敵の一人がすぐ隣にいるというのに、ペーターには止める気もないらしい。"

hide per_t_01_7
show per_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0262
Peter "「あの陛下ですからね、自衛ぐらい出来ます。\n
それに寝首を掻かれるぐらいなら、その程度の器ということでしょう」"

hide per_t_02_9
show per_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0263
Peter "「……ですが、残念ながら、そこまで陛下は腑抜けてはいないようです。\n
あの男もそこまで馬鹿じゃない」"

hide per_t_02_4
show per_t_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0264
Peter "「僕としては、あの男が手を出してここで消えてくれれば言うことはないんですがね。\n
残念です」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（そうね、今のところはそつなく商人ぶっているものね）"


show bra_d_01_2 at center
hide per_t_02_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice blo_f0046
Blood "「この布などいかがですか？\n
きっと、よく似合います」"


show viv_chil02_14 at center
hide bra_d_01_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
voice viv_f0312
Vivaldi "「……そうじゃな、その色が似合わぬとは誰にも言わせぬよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう言ってブラッドが宛がったのは、鮮やかな赤だ。\n
普段の彼女が身に纏う色そのもの。"

hide viv_chil02_14
show viv_chil02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0313
Vivaldi "「ふむ……、[firstname]、おまえはいつまでそこにおるのだ。\n
こっちへおいで」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "突然名指しされて、間の抜けた声が出てしまう。\n
ビバルディは小さな身体を伸ばして、私を呼び付けた。"

hide viv_chil02_13
show viv_chil02_15 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0314
Vivaldi "「わらわの服を選ぶのはおまえの役目であろう。\n
この男に任せていないで、手伝わぬか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "乱暴に手招きをされて、慌てて立ち上がる。\n
そして、幻のように広がる色の海へと足を踏み入れた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「うわー」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（近くで見ると、ますますすごいわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "濃淡様々な布が広がっている。"


show siro_t_01_02 at center
hide viv_chil02_15
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0026
Maid "「どうぞ」"

hide siro_t_01_02
show siro_t_01_02 at left
show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0015
Maid "「こちらもとてもいい品ですわ」"


show bra_d_01_11 at center
hide siro_t_01_02

hide siro_t_02_01
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0047
Blood "「ふっ、どうぞお嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（この人、私が怒って飛び出したのを忘れたわけじゃないでしょうね？）"

menu:
    "仕方ないから混ざる。":
        jump fushigi_blood2_3a
    "断る。":
        jump fushigi_blood2_3b

label fushigi_blood2_3a:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（まあ、ビバルディも楽しんでいるみたいだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ここで私が水を差すのも悪いだろう。\n
伊達に彼らとの付き合いも浅くない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一定の緊張感を保ちつつも、これも一つのゲームと割り切っているのか、ビバルディもブラッドも険悪な雰囲気を持ち出すことはなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「それじゃあ、見せてもらおうかしら」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "布を踏みつけないように注意しながら腰を下ろすと、すぐに布が押し当てられた。"

hide bra_d_01_11
show bra_d_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0048
Blood "「ああ、やはりお嬢さんは色が白いから、こういう色がお似合いだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「……少し派手じゃない？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が手にしているのは、強い赤だ。\n
ビバルディがいつも着ているドレスに通じるほどの真っ赤。"

hide bra_d_01_1
show bra_d_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0049
Blood "「いや、飾り付け次第でしょう。\n
そうは思いませんか、女王陛下」"


show viv_chil02_3 at center
hide bra_d_01_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0315
Vivaldi "「そうじゃな。\n
おお、そうだ、ならばわらわとお揃いで着ればよい」"

hide viv_chil02_3
show viv_chil02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0316
Vivaldi "「だったら、おまえも安心して着られるだろう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ビ、ビバルディとお揃いで、この色を着るの！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "こんなに自己主張の強い色など今までも着たことはない。\n
今着ているエプロンドレスにしても、姉の好みに合わせたものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（似合う似合わない以前の問題よ）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……色だけじゃなくて、見劣りしちゃう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それも、誰よりも赤が似合う人の隣に並べられれば、お粗末なのは簡単に想像がつく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、自分の思いつきが気に入ったのか、ビバルディは手を叩いて喜んでいた。"

play sound se_0121
hide viv_chil02_2
show viv_chil02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0317
Vivaldi "「うむ、そうしよう。\n
よくあるではないか、人形と同じ服を着る遊びが」"

hide viv_chil02_2
show viv_chil02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0318
Vivaldi "「おまえと同じ服ならば、わらわにも異存はない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「いやいや、ちょっと待って！\n
だって、ビバルディの服選びだったんでしょう、これは！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうしていつの間にか、私の服を選ぶような流れに変わっているのか。"

hide viv_chil02_7
show viv_chil02_7 at left
show bra_d_01_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0050
Blood "「ふっ、いいじゃないか。\n
私だって、{size=+20}年甲斐もなく若作り……{/size}」"

hide bra_d_01_2
show bra_d_01_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0051
Blood "「……こほん、違った。\n
いや、普段着飾らないお嬢さんのほうが、飾り立て甲斐がある」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（この男は……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "せっかく平穏無事に終わるかと思ったところに、爆弾を投下しないでほしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の横では耳聡い小さな女王が視線を険悪なものに転じていた。"

hide viv_chil02_7
show viv_chil02_16 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0319
Vivaldi "「……何か、不穏な発言が聞こえた気がするが。\n
気のせいか、商人？」"

hide bra_d_01_3
show bra_d_01_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0052
Blood "「ええ、私の耳には何も聞こえておりませんよ、女王陛下。\n
きっと幻聴でしょう」"

hide bra_d_01_11
show bra_d_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0053
Blood "「そんなにお若いんです。\n
まさか、難聴ということはありますまい？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（く、空気が重い……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "先刻まで弾んだ様子で布を選んでいたはずなのに、彼ら以外の人間は凍りついたように二人を見ている。"

hide viv_chil02_16
show viv_chil02_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0320
Vivaldi "「ふ、ふふふふふふふ」"

hide bra_d_01_10
show bra_d_01_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0054
Blood "「ははははは」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（大人げない姉弟）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一瞬溢れた殺気にメイドさんが顔を強ばらせたが、それを流すようにブラッドが一枚の布を手に取った。"

hide bra_d_01_7
show bra_d_01_2 at center
hide viv_chil02_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0055
Blood "「では、採寸してみましょうか。\n
部屋をお借りしますよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「採寸……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（一体誰の採寸だろう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自称商人の言葉の意味が分からずにいると、彼は立ち上がりながら私の腕を取った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「え……。\n
わ、私の採寸をするの！？」"

hide bra_d_01_2
show bra_d_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_6")
voice blo_f0056
Blood "「おや、衆人環視の中で採寸がご希望ですか？\n
なら……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

play sound se_0062
camera at hpunch
camera at vpunch
hide bra_d_01_10
show bra_d_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_2")
voice blo_f0057
Blood "「ぐっ。\n
あ、足癖の悪いお嬢さんだな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "腕を取られているので、代わりに足で蹴り飛ばす。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「ふん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（見た目はちょっと変わっても、中身はやっぱりブラッドのままよね）"

jump fushigi_blood2_4
label fushigi_blood2_3b:
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_17")
T "（怒らせた挙げ句に、殴られても顔色を変えなかった張本人が、いけしゃあしゃあと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "図々しい男なのは知っているが、あまりに軽く扱われているようで、頭にきた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「……いいえ、結構よ」"

hide bra_d_01_5
show bra_d_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_1")
voice blo_f0058
Blood "「おや、女王陛下のお呼び出しを無視するのかな？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「……あんたねえ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（こういうときだけ利用するんじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少し離れているぐらいでは、何も変わらない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_12")
T "（私が怒って飛び出したぐらいじゃ、気にもしないってことかしら？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ああ、自分で考えて落ち込む）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドに好かれているという自覚は私にもある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "同じように、私が彼のことを少なからず好ましいと感じていることも、否定しようがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（私だったら、好きな人に叩かれて、飛び出されたら……、落ち込むけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（まあ殊勝なブラッドというのも想像出来ないか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつでも余裕ぶって、何が起きても顔色一つ変えない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だから、そんな彼が私を追いかけてきてくれたのかもしれないと思って、勝手に浮かれた私が悪いのだろうか。"


show per_t_02_5 at center
hide bra_d_01_10
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0265
Peter "「ああ、[firstname]！\n
そうですよね、あなたもこんな男の持ってきたどこの何とも知れないものなんて嫌ですよねっ」"

play sound se_0051
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「ペ、ペーターっ！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今まで黙って見ていたペーターに、突然抱きつかれた。"

hide per_t_02_5
show per_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0266
Peter "「あなたがこんな人達に付き合うことはありません、[firstname]。\n
そうです、僕とデートしましょうっ」"


show viv_chil02_8 at center
hide per_t_01_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0321
Vivaldi "「馬鹿げたことを言うな、ホワイト。\n
この子はわらわと遊んでおるのだ、邪魔をするなら引っ込んでおれ」"


show per_t_01_8 at center
hide viv_chil02_8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0267
Peter "「陛下を使っての人形遊びなんて……、～～～～～～な趣味、あなたにはありませんよね」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0267_5
Peter "「あなたは、僕のほうが好きですよね、[firstname]！」"

$ flash(.2)
$ flash(.2)
play sound se_0332 volume .5

show white onlayer master ##instant
hide per_t_01_8
show usape_1 at center
hide white with compress_long
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私よりも大きかった身体が一瞬でサイズを変える。\n
白く長い耳はそのままで、ふさふさの毛並みと愛らしい目。"

hide usape_1
show usape_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0268
Peter "「ほら、あなたの大好きな可愛いウサギですよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T "「うっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "つぶらな眼差しが、じっと私を見上げてくる。\n
だが、その隣にあるビバルディの目線もまた鋭い。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_7")
T "（中身はいつもの二人だって分かっているのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_8")
T "（どうしてこんなに可愛いんだろう）"


show bra_d_01_12 at center
hide usape_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_8")
Blood "「…………」"

hide bra_d_01_12
show bra_d_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_8")
voice blo_f0059
Blood "「申し訳がないが、ウサギの毛を使った布の取り扱いはないのでね」"

play sound se_0134
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ブラッドがウサギの姿をしたペーターの首根っこを掴んだ。"

hide bra_d_01_11
show bra_d_01_11 at left
show usape_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0269
Peter "「な、何をするんですか、触らないでください！\n
雑菌が移るじゃありませんかっ」"

hide bra_d_01_11
show bra_d_01_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0060
Blood "「ああ、そうだな。\n
私も動物の毛にまみれるのは遠慮したいので……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言いながらブラッドは壁際の窓に向かって歩いて行く。\n
ペーターはじたばたと抵抗をしているが、ブラッドは涼しい顔で無視を決め込む。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（まさか、ね）"

hide bra_d_01_10

hide usape_5

play sound se_0585

play music castle_garden_p_ali

scene bg_gen_sky_spr_day
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうするつもりかと思っていると、彼はいきなり窓を開けた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_10")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が何をするつもりか気付いた私が慌てて駆け寄ったが、間に合わない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0061
Blood "「ウサギはウサギらしく、庭を駆けていてもらいましょうか、宰相ウサギ殿」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「！！？」"

play sound se_0703
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのまま、何の躊躇いもなく、ブラッドはペーターを窓から投げ捨ててしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「ペーター！\n
何をするのよ、ブラ……！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "思わず名前を呼びそうになった私を押さえ込んで、彼はしっと言うように唇に手を押し当ててくる。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0062
Blood "「おっと、危ないよ、お嬢さん。そんなに心配しなくても大丈夫。\n
動物の反射神経を甘く見るものじゃない」"

play sound se_0502
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "するとその言葉が聞こえたかのように、窓の外で銃声が響いた。\n
窓の縁から下を見れば、白いウサギが地面に着地したところだった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "空中で人型に戻ったらしいペーターは、遠目にもわかるほど殺気立っている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0270
Peter "「絶対に、絶対に殺して差し上げます。\n
この～～～～～～～～！」"

play sound se_0502
$ flash(.2)

play music castle_audience_p_ali

scene he_01
with dis

show bra_d_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0063
Blood "「……この通り、というわけです。\n
では、お嬢さんにはどんな布がいいかな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「だ、誰が選んでなんて頼んだのよっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "放り投げたペーターのことなど忘れたかのように、布を選ぼうとするブラッドに、思わず声を荒らげた。"

hide bra_d_01_1
show bra_d_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0064
Blood "「おや、私の腕に飛び込んできたのは君だろう？\n
てっきりそういうつもりかと思ったのだが」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（何を勝手に決めつけてくるのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私を抱き止めたブラッドの顔を見ていると、ここまで全部段取りを組んでいたのではないかと邪推をしてしまう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（いや、この男なら十分有り得る）"


show viv_chil02_2 at center
hide bra_d_01_2
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice viv_f0322
Vivaldi "「その男の言うことにも一理あるぞ。\n
[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ビ、ビバルディ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の足下に来たビバルディがこくこくと頷きながら続ける。"

hide viv_chil02_2
show viv_chil02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0323
Vivaldi "「おまえに似合いそうな色もあるのだ。\n
わらわも一緒に見立ててやろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「いや、いいってば！\n
私、元々居候させてもらっている身だし、そこまで甘えるわけには……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディだけならまだしも、ブラッドと彼女に協力されたら、何をされるかわかったものではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "慌てて逃げだそうとした私の退路を塞ぐように、いつの間にか集まってきていたメイド達が取り囲んでいる。"

hide viv_chil02_3
show viv_chil02_3 at left
show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice hei_f0027
Maid "「まあ、でしたらこちらの色がよろしいですわ」"

hide viv_chil02_3

hide siro_t_02_01
show siro_t_02_01 at left
show siro_t_01_02 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice sam_f0016
Maid "「レースはこれがいいかしら。\n
どれもよく似合いそうですわよね」"

hide siro_t_02_01

hide siro_t_01_02
show siro_t_01_02 at left
show siro_t_02_01 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ari_f0015
Maid "「では、まずは採寸から始めないと」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「ちょっと、あなた達！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の抗議など何処吹く風。\n
サイズをというメイドとの声に気付いた様子で、ブラッドは私の腕を掴んで歩き出した。"

show bra_d_01_10 at center
hide siro_t_01_02
hide siro_t_02_01
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0065
Blood "「そういうわけだ。\n
観念するんだな、お嬢さん」"

jump fushigi_blood2_4
label fushigi_blood2_4:
hide bra_d_01_10

$ hi_mes()
$ time_effect()##PLEASE MANUALLY ADJUST ME
show t_bra2_4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice blo_f0066
Blood "「そんなに緊張することはないだろう。\n
採寸をするだけだよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_11")
voice blo_f0067
Blood "「痛くも痒くもないさ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T "（～～～～～～～～）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディの衣装部屋の一つだという小部屋に押し込まれて、背後からブラッドにサイズを測られている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（あなた、私の身体のサイズなんてもう知っているじゃないっ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "言っていいものならそう言ってしまいたいが、それは出来ない。\n
ここで彼が商人から帽子屋の顔に戻ろうものなら、ただではすまないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "着せ替え遊びどころではなくなってしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……はあ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice blo_f0068
Blood "「お嬢さんは綺麗な肌をしているから、どんなものも似合いそうだな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_1")
T "「ありがとう、でも褒めても何も出ないわよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_1")
voice blo_f0069
Blood "「ふふ、つれないな」"

play sound se_0267
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "身体のあちこちに定規や巻き取り式のメジャーを当てられる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼もやると決めたら徹底的にと決めているのか、採寸するブラッドの手付きは上手かった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（マフィアをやめても他の仕事でいくらでもつぶしが利きそうね）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
Blood "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_15")
voice blo_f0070
Blood "「少し痩せたんじゃないか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「勘違いでしょう。\n
根拠もないことを言わないで」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_2")
T "（あなたとはここで初めて会ったっていうのが前提なんでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ふっといつもの彼を思わせることを言わないでほしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これはあくまでビバルディとの遊びの延長なのだ、だったら最後まで遊びを貫けばいい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（そうじゃなかったら、私が馬鹿みたいだわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "仲間外れにされたと怒って、飛び出したのに。\n
あのときの感情まで蔑ろにされてしまうようで、嫌だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0071
Blood "「そうか、では痩せたというのは撤回しよう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0072
Blood "「だが、忘れてもらっては困るな。\n
私以上に君の身体を飾り立てたいと思っている男はいないよ、お嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0073
Blood "「いや、[firstname]」"


play music secret_a_ali
hide t_bra2_4
show t_bra2_5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "薄い下着から出ている肌に、顔を寄せられる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「やだ、何をして……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぞくっと背筋を震わせる感覚。\n
離れてから、いや、彼らが私に隠しごとをしてから縁遠かった刺激に、声が上がりそうだった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0074
Blood "「確かめているんだ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（だから、何を？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_12")
voice blo_f0075
Blood "「君の肌が私の見たとおりなのか。\n
触って、確かめないと……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「……っ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "声が出そうになる度に唇を噛み締める。\n
薄く開いた視界に鏡の中の自分が映っていて、ぞっとした。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（なんて顔をしているんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私だけではない。\n
ブラッドまで、同じように熱を含んだ目で鏡に映り込んでいた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "鏡は目の前にあるというのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（私達が、まるで鏡みたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "顔立ちも、浮かべる表情にも共通部分なんてどこにもない私達。\n
だというのに、瞳に宿る熱だけはどうしてこうも同じなのだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（……眩暈がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "映し合う私達は、一体どちらが本物なのか。\n
そして、どちらが鏡像なのか。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice blo_f0076
Blood "「この唇も、肌も。\n
全部、私の選んだ色に染めてあげよう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "囁かれる声に酔わされて、身動きが取れなくなる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（この手から飛び出したつもりだったのに）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T "（引き戻されるみたい）"

$ hi_mes()
hide t_bra2_5


scene hm_spr_01
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_medium

scene map_bg_spring_eve with Dissolve(1.6)

scene hm_spr_02 with ImageDissolve("gui/stripe_l.png", 1.6, ramplen=128, reverse=True)

scene v_02 with ImageDissolve("gui/stripe_l.png", 1.6, ramplen=128, reverse=True)

play music vivaldi_t_ali

show viv_chil01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Vivaldi "「[firstname]」"

hide viv_chil01_13
show viv_chil01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
Vivaldi "「[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「あ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「ご、ごめんなさい。\n
ビバルディ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_13")
T "「ええと、なんの話をしていたんだっけ？」"

hide viv_chil01_4
show viv_chil01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_13")
Vivaldi "「…………」"

hide viv_chil01_11
show viv_chil01_16 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_13")
voice viv_f0324
Vivaldi "「まったく、惚けた顔をしおって。\n
あれのどこがそんなにいいのか、わらわには分からぬわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呆れたように頬杖をついているビバルディは、絵本の続きを待っていたらしい。\n
私が手にした本を指先で突きながら溜息をついている。"

hide viv_chil01_16
show viv_chil01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice viv_f0325
Vivaldi "「……わらわと遊んでいるときには、他の奴のことを考えないでおくれ。\n
イライラして、首を刎ねたくなってしまう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「そうね、気を付けるわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ビバルディはいつもの赤いドレスを着ていた。\n
そう、彼が私に合わせようとしたドレスと同じ色だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……はあ」"

hide viv_chil01_5

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（重症だわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "様子を見に来たのか、それとも嫌がらせをしたかっただけなのか分からない。\n
いや、そもそも彼の思考を私が理解出来るはずもない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "なのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（なのに、どんな形にしろ、顔が見られてよかったと思っているあたり、負けているわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "向こうの思惑も分からないままなのに。\n
すっかりと思惑に乗せられてしまっていることが悔しい。"

$ hi_mes()

scene hm_spr_02
with stripe_l_medium

scene map_bg_spring_eve
with stripe_l_long
##endmemory
jump fushigi_common3_castle
