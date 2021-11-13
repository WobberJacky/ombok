jump fushigi_common2_castle
label fushigi_dad2_2:

scene map_bg_spring_day
with stripe_l_medium

scene charasel_bg_castle_day
with stripe_l_medium

scene hg_01
with stripe_l_long

play music castle_guestroom_p_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「暇だわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に用意された客室には明るい日差しが差し込んでいる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "窓の外に広がる庭には見事な薔薇が咲いているというのに、今の私には見て回ろうという気持ちになれない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうしても気になってしまうのは、飛び出してきたばかりの、この世界の家のこと。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（……あの子達があそこまで隠すようなことって、一体何なのかしら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子は子供の姿をしていても、マフィアの一員。\n
私よりもずっとずっと隠し事はうまいはず。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そんな彼らが隠し切れず、その上、ばれても更に隠そうとするようなこと。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（そもそもあの子達が休みやお金以外のことで、あそこまで熱意を持って臨むことって、今までにあったかしら？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "{size=+20}（ないわよね、やっぱり）{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "過去の行いを振り返ってみても、ディーやダムが積極的になることは休暇と給料だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "玩具や遊びについてならば、子供らしい熱心さを見せるが……、長続きしない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（いつもとは、何か違った気がするのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供は楽しいことが大好きだ。\n
そして、楽しみのためならば、少しの我慢もする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "我慢は苦手な彼らだが、その後にご褒美が待っていると分かっていれば、多少ならば耐えるはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（でも、我慢しきれていないというか、夢中になっちゃっているというか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今回の二人を見ていると、何故かそんな気がしてくる。\n
彼らはとても賢くて……、いや、狡賢いといってもいいほど、頭がいい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう簡単に掴ませない尻尾を何故今回に限ってちらちらと振ってくるのかが分からなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「うーん」"

play sound se_0275
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "誰が来たのだろうと思って振り返ると、白いウサギがそこに立っている。"


show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0291
Peter "「[firstname]、こんなところにいたんですね！\n
探しましたよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_15")
T "「ペーター？」"

hide per_t_03_1
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice pet_f0292
Peter "「あなたが来ているというのに、お相手が出来ずすみません！\n
寂しかったでしょう？」"

hide per_t_02_6
show per_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_15")
voice pet_f0293
Peter "「ああ、僕はあなたのためなら……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「仕事は放り出さないでね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "以前にも同じようなことを言って、本当に仕事を放り出したことのある友人に釘を刺す。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（居候の身で宰相の仕事を滞らせたりなんてしたら、皆に悪いもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "勿論、この場合の『皆』はメイドや兵といった、この城に詰める彼らのことだが。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "間違っても、仕事を放り出して逃走を図る女王様や、出たが最後鉄砲玉のように帰って来ない（が忘れた頃に戻ってくる）軍事責任者ではない。"

hide per_t_03_4
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0294
Peter "「仕事なんて……。\n
僕はあなたといることがすべてなんです！」"

hide per_t_02_5
show per_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0295
Peter "「あなたの微笑みを目にして、あなたの声を聞くだけで、僕は……！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_9")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "{size=+20}「でも、仕事はさぼらないで」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（迷惑をかけるんじゃないって言っているのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界のウサギさんの耳は、長いばかりで意図が通じないことが多いので、重ねて釘を刺しておく。"

hide per_t_02_12
show per_t_01_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0296
Peter "「分かっています、さぼったりしません。\n
あなたはきっと気にすると思いましたので、綺麗さっぱり片付けてきました」"

hide per_t_01_10
show per_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0297
Peter "「今回は本当に、ぴたっと仕事が終わっているんです。\n
この時間帯、僕は完全にあなたのものです」"

hide per_t_02_1
show per_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0298
Peter "「さあ、好きにしてください！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「…………」"

play sound se_0198
##special anime kirakira_center
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の真横に立ったペーターは、両手を広げ、きらきらとした目で私を見ている。\n
そう、きらきらとした目で。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「好きにしろって言ったって、何をどう……」"

hide per_t_03_11
show per_t_03_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice pet_f0299
Peter "「殴りませんか？\n
蹴ったりしてもいいんですけど……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「あんた、私を一体何だと言いたいわけ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人を欲求不満みたいに言わないでほしい。\n
思わず真上にある顔を睨むが、ペーターはむしろ意外そうに首を傾げた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気持ちを物語るように、ぴくぴくと白い耳が動く。"

hide per_t_03_8
show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0300
Peter "「だって……、[firstname]。\n
あなた、ずっとピリピリしていたでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（ピリピリ？）"

hide per_t_02_3
show per_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice pet_f0301
Peter "「ええ。\n
しばらくここにいたいと城を訪ねたときから、あなたはずっと……、怒って、そして落ち込んでいる」"

play sound se_0267
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自他共に認める潔癖症の白ウサギが、私の頬に触れてくる。\n
手袋越しの手は硬く、そして意外なほどに優しく撫でた。"

hide per_t_01_8
show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0302
Peter "「分かったでしょう、あんなマフィアの元にいることはないんです」"

hide per_t_02_10
show per_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0302_5
Peter "「あなたをあんなに怒らせた上に、怒らせたままでいるなんて、僕には耐えられません」"

hide per_t_02_9
show per_t_01_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0303
Peter "「あなたを傷つける元凶など、殺してしまいたい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "穏やかに微笑んでいたはずの目に、一瞬立ち上った殺意。\n
頬を撫でる手を裏切るような、冷たい感覚が肌を突き刺す。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「……ペーター」"

hide per_t_01_1
show per_t_02_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice pet_f0304
Peter "「でも、そんなことをしたら……。\n
あなたはかえって怒ってしまうでしょうし、僕にこんなことをさせてもくれなくなってしまう」"

play sound se_0361
hide per_t_02_4
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice pet_f0305
Peter "「それは嫌ですから、今は、耐えることにします」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "赤い殺意は霞のように消えて、残ったのは困ったように笑う目と、手を繋がれている安心感。"

hide per_t_02_8
show per_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0306
Peter "「せっかくあなたがここにいるんです。\n
僕とのゲームに付き合ってくれませんか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「ゲーム？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T "（ビバルディならともかく、ペーターがゲームを持ち出してくるのは珍しいわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "イライラしやすい女王様と違い、彼は私を部屋に招いたり、一緒にいるだけで楽しそうだったのに、どんな心境の変化だろうか。"

hide per_t_01_2
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0307
Peter "「ええ、顔なし……、いえ、城の兵士がこの前街で流行っていると話していたんです。あなたに少しでも楽しんでもらえればと思って準備していたんですが」"

hide per_t_02_8
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0308
Peter "「必要なものが、先ほど全部届きまして、これでようやくご招待できます」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_12")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_15")
T "（本当に、成長したわよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "初めて出会ったときには、頭にウサギ耳の生えたストーカーにしか見えなかったのに。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少しずつ接し方を覚えてくれているようで、それが嬉しい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_8")
T "（耐えるとか、最初の頃のペーターだったらあり得ないわよね）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「ありがとう、楽しみにしているわ」"

hide per_t_03_1
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice pet_f0309
Peter "「ええ、僕はあなたを幸せにしたいんです。\n
そのためなら、なんだってしますっ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T "「幸せって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_8")
T "（いちいち言うことが大袈裟なんだから）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう思っていても、笑って流せる程度には私も彼のことが気に入っている。"

hide per_t_02_5
show per_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0310
Peter "「ああ、でも、安心してくださいね、[firstname]。\n
僕はあなた思いのウサギですから、ちゃんとお返しはしておきました」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_6")
T "{size=+20}「お返し？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（何よ、その……、急に不穏な響きのある言葉は）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "何しろ、ここは銃弾飛び交うワンダーランド。\n
危険な『お返し』を彼が企んだとしても、おかしくない。"

hide per_t_01_3
show per_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0311
Peter "「だって、僕の愛しい人を怒らせるなんて、本当だったらすぐに～～～～～～して、～～～～～～した後に、更に～～～～～～～しなければ」"

hide per_t_01_9
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0312
Peter "「でも、そこまでするとあなたがきっと怒ると思いましたので、別のものでお返しを」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（別のもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この様子では少なくとも好意的なプレゼントではないことは間違いないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（むしろ、悪意に満ちているような）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「……何をしたのよ？」"

hide per_t_02_8
show per_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0313
Peter "「大したことはしていませんよ。\n
本当に、ささやかな贈り物です」"

hide per_t_02_2
show per_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0314
Peter "「怪我をするようなものではありませんから、安心してください」"

hide per_t_03_2
show per_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0314_5
Peter "「ああ、でも……、約一名、もとい、約一匹だけは歓迎してくれるでしょうね、きっと」"

hide per_t_03_3
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice pet_f0315
Peter "「他の人間にとっては嫌がらせ以外の何ものでもないでしょうけど、可愛いものですよね」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「変わっていない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（成長したと思ったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ストーカーウサギのすることは、相変わらず過激なもので満ちている。"

hide per_t_02_5

$ hi_mes()

scene hn_spr_01
with stripe_l_long

play music castle_garden_p_ali

show per_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice pet_f0316
Peter "「これです！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「これ？」"

hide per_t_01_2
show per_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice pet_f0317
Peter "「はい！\n
今、ハートの城の領土で人気の球技らしいんですよ！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「……ふうん」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターに案内されるままに連れてこられた場所は、城の中に設けられた小さな庭。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "周囲に設置されたものを物珍しそうに見る私に、彼は丁寧に説明をしてくれる。"

hide per_t_02_8
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0318
Peter "「ここの柱から、あの柱までボールを打ち合うゲームになります。\n
途中のフープを全部潜っていくんです」"

hide per_t_03_1
show per_t_02_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0319
Peter "「本来は二人で組を作り、チーム戦をするらしいんですが……、僕とあなたがいれば他の人間なんていりませんよね！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「いや、チーム戦がどうのこうのっていう以前に」"

play sound se_0353
hide per_t_02_1

$ hi_mes()

scene t_cut_twi2u with Dissolve(.5)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_9")
T "{size=+20}「何で、フラミンゴと、ハリネズミがいるのかが聞きたいんだけど？」{/size} "


scene t_cut_twi2
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（何で生きたフラミンゴがいるのよ？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（ハリネズミだって……、動いているし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "繋がれてもいないのに彼らはじっと柵の中で待っている。\n
見つめてくる眼差しはつぶらで、何が起きるのかなど考えてもいない顔だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "地面にいくつも配置されたフープはあるが、球技だというのに肝心の道具がないのが、すごく気になる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_5")
T "（……まさかとは思うけど）"


show per_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice pet_f0320
Peter "「ああ、フラミンゴとハリネズミのことですか？\n
あれはボールと、ボールを打つ槌です」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_13")
T "「待て」"

hide per_t_02_3
show per_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice pet_f0321
Peter "「街中で流行っているのは、ボールを木の槌で打ち合うようなんですが。\n
正式には、こうして生きたフラミンゴとハリネズミを使って行うと聞きました！」"

hide per_t_03_1
show per_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice pet_f0322
Peter "「僕としては、生きた鳥やネズミなんて触るだけでも雑菌がついて嫌なんですが……、愛しいあなたのためならばどんなことでもします！」"

play sound se_0433
hide per_t_03_5
show per_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_13")
voice pet_f0323
Peter "「さあ、[firstname]！\n
遠慮せず、ゲームを始めましょう！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "{size=+20}「出来るか！！」{/size} "

play sound se_0107
hide per_t_02_5 with Dissolve(.5)


camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "久しぶりに遠慮なく拳を固めて振り切った。\n
結構いい音がしたから、痛かっただろう。"

show per_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「～～～～っ！？」"

hide per_t_01_5
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0324
Peter "「な、何をするんですか、[firstname]！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私に殴られたペーターは驚いたように言うが、驚かされたのは私のほうだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「何をするんですじゃない！\n
私に動物虐待の趣味はないわよ！」"

hide per_t_02_6
show per_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_13")
voice pet_f0325
Peter "「……現に今、僕を殴っているじゃないですか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_13")
T "「あんたと人畜無害な動物を一緒にするな！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気に入らない相手には銃を向けて発砲するウサギと一緒にされては、フラミンゴやハリネズミがあまりに不憫だ。"

hide per_t_01_4
show per_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0326
Peter "「でも、これが一番正しいやり方だって言われたんですよ……」"

hide per_t_02_6
show per_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0326_5
Peter "「兵士達に、生きたままのフラミンゴを捕まえさせるのも、結構骨が折れたんですが」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「普通は生きた動物で球技なんかしないわよ。\n
誰よ、その間違いまくった知識を広めたのは……」"

hide per_t_02_9
show per_t_03_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice pet_f0327
Peter "「誰って……、それは」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_11")
voice ace_f0341
Ace "「俺だけど？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「…………」"

hide per_t_03_5
show per_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
Peter "「…………」"

hide per_t_03_7
show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_5")
voice pet_f0328
Peter "「エース君」"

play sound se_0609
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "唐突に、生け垣の上から声がした。\n
視線を向けると、ひらりと着地した赤い騎士が庭を眺めて感嘆の声をあげる。"

hide per_t_02_10
show per_t_02_10 at left
show ace_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0342
Ace "「うっわー、すごいなあ！\n
うちの城に戻ってきたつもりだったけど、動物園の間違いだったかな」"

hide ace_t_03_2
show ace_t_01_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0343
Ace "「フラミンゴに、ハリネズミ……。\n
ははは、その上、ウサギさんまでいる」"

hide ace_t_01_4
show ace_t_01_10 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0344
Ace "「陛下の趣味とは思えないし……。\n
これ、どうしたの、ペーターさん？」"

hide per_t_02_10
show per_t_03_2 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0329
Peter "「ふ、ふふ……、ちょうどいいところに出てきました。\n
エース君、君の言うところの城下で流行っているという球技ですが」"

hide ace_t_01_10
show ace_t_03_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0345
Ace "「うん、クロケーだろう？\n
あれ、そういえばこの庭にもクロケー用のフープが出来ているなあ」"

hide ace_t_03_2
show ace_t_03_7 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0346
Ace "「肝心の槌とボールがないけど……」"

hide ace_t_03_7
show ace_t_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice ace_f0347
Ace "「あ、ひょっとしてペーターさん、動物でやるって冗談で言ったのを、真に受けちゃった？ははは、俺の言葉をそんなに信用してくれていたなんて、感激だぜ」"

play sound se_0525
$ flash(.1)
play sound se_0500
$ flash(.1)
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "底抜けに明るい笑い声に、銃声が混じる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「ペーター」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "無言で時計を銃に変えたペーターを制止するよう名前を呼ぶが、返ってきたのは清々しい笑顔だった。"

hide per_t_03_2
show per_t_03_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0330
Peter "「すみません、[firstname]。\n
少しだけ待っていてくださいね」"

hide per_t_03_1
show per_t_02_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0331
Peter "「今、この～～～～な男を撃ち殺して、仕切り直しますから」"

hide per_t_02_5

hide ace_t_02_3


scene bg_gen_sky_spr_day
with dis
play sound se_0501
$ flash(.1)
play sound se_0500
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（気持ちは分かるけど）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice ace_f0348
Ace "「ははは、どうしてそんなに怒るんだよ、ペーターさん。\n
このゲームが流行っているのは本当だぜ」"

play sound se_0682
camera at hpunch
camera at vpunch
$ flash(.1)
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice ace_f0349
Ace "「ただ、ちょっと冗談も交えただけで」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice pet_f0332
Peter "「君の言うことなどに耳を貸した僕が愚かでしたよ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice pet_f0332_5
Peter "「とりあえず、そのよく回る口を塞いでしまえば、質の悪い冗談も言えなくなって清々すると思いませんか？」"

play sound se_0501
$ flash(.3)
play sound se_0682
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「緊張感がないというか、殺伐としているというべきか……」"

play sound se_0353
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "視界の隅では、何も知らないハリネズミがのんびりと眠りはじめている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_11")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（ああ、私もいっそ、何も知らずに寝てしまいたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この銃声と金属音が鳴り響く庭で、それは到底叶いそうもなかった。"

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music forest_town_square_p_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kaz_f0010
Clerk "「クロケー用のボールと、槌ですね。\n
ええ、在庫がありますからお持ち帰りになれますよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「そう、よかった」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice pet_f0333
Peter "「では、城まで運んでください。\n
それぐらいは何でもないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice kaz_f0011
Clerk "「かしこまりました。\n
二回時間帯が変わるまでには、お城にお届け致します」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice pet_f0334
Peter "「……分かりました」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice pet_f0335
Peter "「さあ、[firstname]。\n
行きましょう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「え？\n
もう行くの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あっさりと踵を返したペーターに引っ張られるように、店の出口へと連れて行かれてしまう。"

play sound se_0180
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kaz_f0012
Clerk "「ありがとうございました！\n
またどうぞご贔屓に」"

play sound se_0624

scene bg_gen03_hjm_spr_day
with stripe_l_long

show per_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0336
Peter "「ふん。\n
ああ、本当に不衛生な店ですよね」"

hide per_t_02_7
show per_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0337
Peter "「埃っぽくて、雑菌だらけで嫌になります」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T "「そうかしら？\n
私、ああいう雑貨のあるお店って結構好きよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T "（お店の雰囲気も悪くなかったし……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_14")
T "（また今度来てみようかな）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "結局エースの冗談により捕獲された動物は放してやり、通常の道具を買い求めに街へやってきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "張本人のエースは、のらりくらりと攻撃をかわし、気付けば姿を消していた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "おそらくまたどこかで迷子になりつつ、旅を続けているのだろう。"

hide per_t_01_9
show per_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0338
Peter "「な……、あ、あんな店が好きなんですか、[firstname]！？\n
駄目ですよ、あんなに散らかった雑然とした店なんて……！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T "「そう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「ディーとダムの部屋なんて、もっとすごいわよ。\n
刃物はごろごろしているし、天井からは斧がぶら下がって……」"

hide per_t_01_6
show per_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
Peter "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（あ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人の名前を出した途端に、ペーターの目が少し険しくなったことに気付く。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "失敗した。\n
勝手に帽子屋屋敷を出てきて居候させてもらって、甘えているのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（ペーター相手だと、つい気が緩んじゃう）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「ごめん、ペーター」"

hide per_t_02_10
show per_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice pet_f0339
Peter "「あなたが謝る必要は……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "耳障りな高い音が響いたのは、城へ戻ろうとした私達の背後からだった。"

play sound se_0216
$ flash(.4)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「！！」"


play music tension_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_6")
T "「な……」"


show dee_p2_02_8 at center
hide per_t_03_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice dad_f0113
Unknown "「町の中にウサギがいるなんて、変だよねえ。\n
さっさと森にでも追い払わないと……」"

hide dee_p2_02_8
show dee_p2_02_8 at left
show dam_p_02_2 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_6")
voice dad_f0114
Unknown "「そうだね。\n
ウサギなんて、森の中でにんじんでも囓っていればいいのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_7")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（この声は……）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「ディー、ダム？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T "「あれ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "多くの人が行き交うハートの城の城下町。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "人混みに紛れない、二つの影。\n
いつも鏡写しのように揃っていた影が、今は……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（大きさが違う？）"

hide dee_p2_02_8
show dee_p2_02_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice dad_f0115
Dee "「久しぶ……、じゃなかった。\n
こほん、どうかしたの、可愛いお嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T "「……お嬢さん？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T "（大人になったディー……、よね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大人の姿になっているときのディーは後ろ髪を少し長く伸ばして、リボンで留めている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今はリボンを付けていない私服姿だが、見間違えるはずがない。"

hide dam_p_02_2
show dam_p_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0116
Dam "「兄弟……と、今はそうじゃなかった。\n
父さん、先にあの変なウサギを狩っちゃおうよ」"

hide dee_p2_02_1
show dee_p2_02_10 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0118
Dee "「そうだね、兄弟……、じゃなかった、息子。\n
さっさと捕まえて、ウサギ料理好きの騎士にでも押し付けよう」"

play sound se_0084
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（一緒にいるのは、ダムよね？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（何で、あの子達、子供と大人の姿でいるのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "斧を構えた彼らが大人と子供の姿を気分で変えることは私も既に知っているが、姿を変えるときは二人一緒だったはずだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（それが、今回はどうして別々なのかしら？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（…………？）"


show per_t_01_1 at center
hide dee_p2_02_10

hide dam_p_02_11
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
voice pet_f0340
Peter "「ブラッド＝デュプレのところの門番ですか。\n
まったく、彼女を怒らせるだけでは飽きたらず、こんなところまで来るとは……」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "苦々しい口調で言うペーターに、ダムがあっかんべーと舌を突き出した。\n
ディーはディーで、斧を振り回しながら声を上げる。"

hide per_t_01_1

show t_twi2_1 onlayer master
with dis

play music battle_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0120
Dee "「違うよ、今の僕らは{size=+20}ただの通りすがりの親子。{/size}\n
人違いだよ、白いウサギさん！」"

play sound se_0672
##special anime kiseki02
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0341
Peter "「ちっ……。\n
そんな悪趣味な顔立ちの親子なんて、鬱陶しいことこの上ありません！」"

play sound se_0525
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0342
Peter "「ちょうどいい。\n
ここで始末をつけてあげます」"

play sound se_0023
$ flash(.2)
play sound se_0500
$ flash(.1)
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_6")
T "「！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「ペーター！」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T "（街中で何を平然と戦い始めているのよ、あんた達は！？）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice dad_f0121
Dee "「こっちに来ちゃ駄目だよ、危ないからね、お嬢さん」"

hide t_twi2_1


play music forest_town_square_p_ali

show dam_p_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice dad_f0122
Dam "「そうだよ、お姉さんはこっちだよ」"

play sound se_0492
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつの間にやってきたのか、制服でもない普通の服を着たダムが私の手を引いてくる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「ダム……。\n
これは一体どういうことよ？」"

hide dam_p_02_10
show dam_p_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice dad_f0123
Dam "「しー。僕達、今、内緒で来ているんだから……。\n
通りすがりの親子だって言ったでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T "「通りすがりって……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（だから、何なのよ、その無理な設定は）"

menu:
    "どう見ても、あんた達でしょう。":
        jump fushigi_dad2_3a
    "……また、内緒？":
        jump fushigi_dad2_3b

label fushigi_dad2_3a:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「通りすがりって言うけど……」"

play sound se_0501
$ flash(.1)
play sound se_0506
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

hide dam_p_02_8


show t_twi2_1 onlayer master
with dis

play music battle_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「これをただの通りすがりですませるのは、無理があると思うんだけど」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice dad_f0124
Dam "「お姉さんは気にしすぎだよ。\n
ここではこれぐらいいつものことじゃない」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（いつものことと言えばそうだけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "住人が平然と銃を持って闊歩する世界。\n
それが当たり前の不思議な国。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（でも、ハートの城の宰相に堂々と斬りかかる通りすがりの親子なんて、普通いないでしょう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "役持ちだから出来る暴挙だ。\n
役を持たない他の人間だったら、間髪入れずに銃で撃たれている。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0125
Dee "「本当に、しつこいウサギだね。\n
だいたい、ウサギの分際でお姉さん……、じゃなかった、お嬢さんを連れて歩くなんて、何様だよ！」"

play sound se_0507
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0343
Peter "「君達こそ、見え透いた言い分でこちらの領土にまで乗り込んできたんです。\n
覚悟は出来ているんでしょうね？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0344
Peter "「僕は彼女ほど優しくもなければ、遠慮もしません」"

play sound se_0500
$ flash(.1)
$ flash(.1)
hide t_twi2_1


play music forest_town_square_p_ali
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃と斧で物騒な音を奏でながら、彼らは睨み合って一歩も引かない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_5")
T "「…………」"


show dam_p_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0126
Dam "「ねえ、お姉さん。\n
そんなことよりも、そろそろ屋敷に帰ってきてよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しょんぼりと肩を落としたダムは、じっと私を見上げてきている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "大きな赤い目。\n
どんな姿でも変わらない、怖さも、愛しさも感じさせる目だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもの私なら流されていたかもしれないが、今は違う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（隠しごとを最初にしたのは、そっちじゃない）"

jump fushigi_dad2_4
label fushigi_dad2_3b:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「それに……。\n
内緒で来ているって、どういうことよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「また、仕事をさぼってきたの？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らは帽子屋屋敷のサボりの常習犯だ。\n
気が向くままに休暇と称して他領土に遊びに行くことも珍しくない。"

play sound se_0501
$ flash(.1)
play sound se_0506
$ flash(.1)

play music battle_ali

show t_twi2_1 onlayer master
with dis
hide dam_p_02_9

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0128
Dee "「ち、違うよ！\n
誤解だってば、お嬢さん！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「ディー、その呼び方はやめて」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（誰かさんにそっくりだから）"

play sound se_0503
$ flash(.1)
play sound se_0508
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ペーターと撃ち合いながら声をかけてくるディーの口調は、彼らのボスを連想させた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0129
Dee "「だ……、だって、他人の振りをするならそれなりの呼び方を考えなくちゃと思って。……って、しつこいよ、この～～～～～～～～ウサギ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0345
Peter "「ふん、身体ばかりが大きくなったところで、やることに大差はありませんね。\n
そんなだから、彼女に呆れられるんです」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0346
Peter "「そんな不誠実な子供に、彼女を預けられるはずがないでしょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃口をディーに向けながら、ペーターは感情のこもらない声でそんなことを言う。\n
しかし、それを受けるディーに物怖じした様子はない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0130
Dee "「……ふうん、やる気？\n
僕も、動物なんかにお姉さんを貸しておくのは嫌だったし、ちょうどいいや」"


play music forest_town_square_p_ali
hide t_twi2_1


show dam_p_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0131
Dam "「兄弟、兄弟。\n
呼び方が戻っているよ」"

hide dam_p_02_9
show dam_p_02_9 at left
show dee_p2_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0132
Dee "「それを言ったら、兄弟だって戻っているよ」"

hide dee_p2_02_8
show dee_p2_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0132_5
Dee "「今回の僕達の設定は、通りすがりの親子なんだから、兄弟って呼ぶのは正しくない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（ややこしいなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らが大人になるときは大抵一緒に大人になっているし、子供のときもそれは変わらない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "違う姿でいるのだから、兄弟という呼び名ではなくともおかしくはないのだろうが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（何だか、落ち着かない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らが気分次第で大人の姿になったり、子供に戻るのはいつものことだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "子供のときは瓜二つだが、大人のときは髪型や装飾品で違いを分かりやすくしてくれている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人にとっては、見分けがつこうがそうでなかろうが、問題はない。\n
だが、違いが分かると私が喜ぶので、そうしてくれている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（その気遣いが、嬉しかったはずなのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "今は姿そのものが違うせいで、間違えようがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "区別がつくことはいいことだと思うのに、同じではない二人を見ると、落ち着かない。"

jump fushigi_dad2_4
label fushigi_dad2_4:
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_12")
T "「ところで、二人とも。\n
なんで、そんな姿でわざわざハートの城の領土に来たわけ？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（いつも城に遊びに来るときでも、あの制服なのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らは帽子屋屋敷に属しているが、ハートの城の領土に遊びに来るときでも、服を変えたりしない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "むしろ、その名前を示すような制服を着て、兵士を挑発して物騒な遊びに巻き込むような子供達だ。"

hide dam_p_02_9
show dam_p_02_9 at left
hide dee_p2_02_12
show dee_p2_02_13 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0133
Dee "「なんでって……、お姉さんが、お城のウサギと仲よくしているって聞いたからに決まっているじゃない」"

hide dee_p2_02_13
show dee_p2_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0134
Dee "「でも、ひよこウサギににお姉さんを迎えに行くなら、ファミリーの看板を下げていくんじゃなくて、ちゃんと自分達だけで解決して来いって言われたから」"

play sound se_0506
$ flash(.1)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "きんと甲高い音を立てて、銃弾を弾いたディーもまた私のほうへと駆け寄ってくる。"

hide dam_p_02_9
show dam_p_02_10 at left
hide dee_p2_02_12
show dee_p2_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0136
Dam "「でも、普通に迎えに来たら大騒ぎになるから、ちゃんと変装したんだよ。\n
僕達、ここではちょっと有名な子供だからさ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（変装）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "じっと今は子供と大人の姿の双子を見つめて、首を傾げる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_11")
T "（これって、変装……？）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_11")
T "（単に、仕事着から私服に着替えただけのような気がする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、変装の当初の目的は、まったく果たされていない。"

hide dam_p_02_10

hide dee_p2_02_5

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0028
Woman "「あれは、ハートの城の……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0016
Man "「斧を振り回しているのは、帽子屋のところの門番じゃ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0029
Woman "「ブラッディ・ツインズ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（結局大騒ぎになるのは避けられていないわよ）"

play sound se_0055

show dee_p2_02_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice dad_f0137
Dee "「お姉さん」"

hide dee_p2_02_11
show dee_p2_02_11 at left
show dam_p_02_11 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice dad_f0138
Dam "「ねえ、聞いて」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "周囲の囁き声など気にしていない二人は、私の手をそれぞれとってくる。\n
エリオットの言うところの説得を始めるつもりらしく、目は真剣そのものだ。"

hide dee_p2_02_11
show dee_p2_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0140
Dee "「どうしたら、お姉さんは帰ってきてくれる？」"

hide dee_p2_02_8
show dee_p2_02_5 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0140_5
Dee "「僕、お姉さんが帰ってきてくれるのなら、休暇を全部お姉さんのために使ってあげる」"

hide dam_p_02_11
show dam_p_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0141
Dam "「僕達、とっても反省したんだ。\n
お姉さんがいなくて、寂しくて寂しくて」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「私は……」"

play sound se_0501
$ flash(.2)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "頷くつもりだったの、首を横に振るつもりだったのか。\n
自分でもわからなかった答えは、銃声によってかき消された。"

hide dee_p2_02_5
show dee_p2_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
Dee "「！」"

play sound se_0508
$ flash(.2)
hide dee_p2_02_3
show dee_p2_02_13 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice dad_f0143
Dee "「危ないなあ、僕らがいたからいいけど、もしお姉さんに当たっていたら、その耳じゃ釣り合わないからな！」"


show per_t_03_9 at center
hide dee_p2_02_13
hide dam_p_02_8
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice pet_f0347
Peter "「無駄な心配ですね。\n
彼女に当たるような失敗を僕がするはずがないでしょう」"

hide per_t_03_9
show per_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice pet_f0348
Peter "「次は、逃がしません。\n
いずれ消える汚れとはいえ、君達の血で僕の愛しい人が汚れるような事態にさせたいんですか？」"

play sound se_0023
$ flash(.3)
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "銃を構えたペーターは本気だ。\n
先ほど許せないといっていた言葉どおり、二人を撃ち殺しかねない雰囲気を漂わせている。"

hide per_t_03_10


show dam_p_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「…………」"

hide dam_p_02_12
show dam_p_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0144
Dam "「……僕達だってお姉さんを汚すのは嫌だから、返り血なんか浴びずに片付けてあげる」"

play sound se_0084
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "腰に差していた小さな銃が一瞬にして大きな斧へと姿を変える。"

play sound se_0672
##special anime kiseki01
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "自分の得物を一振りしたダムもまた戦闘態勢に入っていた。\n
今にも飛び出しそうな二人の背中に、私は声をかける。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「ところで、あなた達」"

hide dam_p_02_13
show dam_p_02_13 at left
show dee_p2_02_4 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
voice dad_f0145
Dee "「何、お姉さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T "「私が帽子屋屋敷を飛び出した理由を、忘れていないわよね？」"

hide dam_p_02_13
show dam_p_02_4 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_16")
voice dad_f0146
Dam "「勿論だよ。\n
僕達は賢くていい子だもの、ちゃんと覚えているよ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "打てば響くような反応のよさで返答がある。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「だったら、いい加減、屋敷の皆が私に何を隠していたのかを話してくれるのよね？」"

hide dee_p2_02_4
show dee_p2_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
Dee "「！」"

hide dee_p2_02_8
show dee_p2_02_5 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice dad_f0148
Dee "「僕達、お姉さんに隠しごとなんて何もしていないよ。\n
そうだよね、兄弟！？」"

hide dam_p_02_4
show dam_p_02_7 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice dad_f0149
Dam "「そ、そうだよ。\n
気のせいだよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T "（やっぱり、まだ仲間外れにするんじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らにその意図はないのだろうが、好意を持っていると知っている人からされる爪弾きなんて、かえって残酷なだけだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_5")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T "「話してくれる気はないのね？」"

hide dee_p2_02_5
show dee_p2_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
Dee "「…………」"

hide dam_p_02_7
show dam_p_02_8 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_15")
Dam "「…………」"

play sound se_0056
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもなら同じ高さにある目が、斜めに視線を結ぶ。\n
言葉を交わさなくとも、心が読めなくとも、彼らは簡単に意思疎通が出来る。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_5")
T "（私には入り込めない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いくらその目を覗き込んでも、言葉がなければ私は彼らの気持ちを知ることも出来ないままだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "双子という、他人にはどうしようもない繋がりのある二人の間に、私は割り込むことさえ許してもらえない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_3")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「分かったわ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「ペーター！」"


show per_t_02_8 at center
hide dee_p2_02_8
hide dam_p_02_8
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_9")
voice pet_f0349
Peter "「はい、何でしょう、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「私、城に帰るわ。\n
一緒に帰りましょう」"

play sound se_0103
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "二人を押しのけて、帽子屋とは反対側の道へ向かう。"


show dee_p2_02_7 at center
hide per_t_02_8
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0150
Dee "「え……、ええ！？\n
どうして、どうしてそんなことを言うの、お姉さん！？」"

hide dee_p2_02_7
show dee_p2_02_7 at left
show dam_p_02_3 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0151
Dam "「そうだよ、あんなウサギとじゃなくて、僕達と一緒に」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_3")
T "「この前も言ったでしょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "駆け寄ってきたペーターの手を取って、私は二人ににっこりと微笑んだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「あなた達が教えてくれる気になるまで家出中なの。\n
ああ、こうとも言ったわよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "伸ばしてくる二人の手を払いのけ、更に私は続けた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_12")
T "（こうなったら、根比べよ）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T "「{size=+20}ついてきても、口も聞かない{/size}って……、ね」"

hide dee_p2_02_7
show dee_p2_02_12 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
Dee "「…………」"

hide dam_p_02_3
show dam_p_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
Dam "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_4")
T "「じゃあ、さようなら！\n
通りすがりさん」"

play sound se_0624
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "気まずい表情を浮かべている双子に告げると、見せつけるようにペーターの手を引いて歩き始めた。"


show per_t_02_3 at center
hide dee_p2_02_12

hide dam_p_02_9
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Peter "「！！！」"

hide per_t_02_3
show per_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pet_f0350
Peter "「[firstname]、あなたが僕の手を引いて歩いてくれるなんて……。\n
ああ、なんて素晴らしい」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T "（大袈裟ね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "これぐらいのことで、いちいち感動しないでほしい。"


show dee_p2_02_9 at center
hide per_t_02_13
with dis

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dee "「……[firstname]」"

hide dee_p2_02_9
show dee_p2_02_9 at left
show dam_p_02_8 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Dam "「[firstname]……？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_12")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_3")
T "（そんなふうに呼ばないでよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "怒らせたのは、彼ら。\n
隠しごとをいつまでも引き摺って、教えてくれないのも彼ら。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "しかし、背後から聞こえた哀しそうな声が背中から離れない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "呼ばれる名前を聞こえないふりをするだけでも、今の私には多大な努力が必要だった。"

hide dee_p2_02_9

hide dam_p_02_8

$ hi_mes()

scene charasel_bg_castle_day
with stripe_l_medium

scene map_bg_spring_day
with stripe_l_long
##endmemory
jump fushigi_common3_castle
