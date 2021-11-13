
scene map_bg_autumn_day
with dis

scene charasel_bg_hatter_day
with dis
label fushigi_elliot1:
hide screen hatter_man_choice
$ clockanim()

$ hi_mes()

scene b_aut_01
with dis

play music hatter_corridor_p_ali

scene br_01 with Dissolve(1.2)

show situji_t_01_06 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kat_f0015
Servant "「あれ～、エリオット様にご用ですか？\n
先刻、キッチンにいましたから……、まだ戻ってないと思いますよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットの部屋のドアをノックしようとしたところで、通りがかった使用人からそんなことを言われた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T "「キッチン？\n
あれ、今って、食事の予定だったかしら？」"

hide situji_t_01_06
show situji_t_01_02 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice kat_f0016
Servant "「いいえ、違います。\n
ですが、何だか、真剣な顔でシェフに相談されていました」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T "「……シェフに？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この屋敷のシェフは、食べ物にうるさい主の元で仕事を受けるだけあって、いい腕をしている。\n
そして、エリオットと、仲がいい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（密かにブラッドが断っても……、いまだに新作にんじん料理を作るのはやめないものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ある意味、ブラッド以上に厨房に顔が利くエリオットなら、キッチンにいてもおかしくない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ひょっとしたら、また新しいオレンジ色のメニューを考えているところかもしれないが……、多忙な彼はいつ屋敷を離れてしまうか分からない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T "（この機会を逃すと、またはぐらかされそうだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "追及するのなら、今が一番いいだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_2")
T "「分かったわ、ちょっと行ってみる」"

hide situji_t_01_02

play sound se_0776
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "教えてくれた使用人にお礼を言って、そのまま方向を変え、キッチンへと向かった。"

$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME

play music elliot_t_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice eri_f0042
Elliot "「だから、それじゃ駄目だって。\n
いや、これもうまいんだけど……、もっともっとうまいものを作ってやりたいんだ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "多くの人間が生活する帽子屋屋敷のキッチンは、広い。\n
エリオットの声は、そこから確かに聞こえてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屋敷の広さに負けないくらいの大声は、聞き慣れたもの。\n
ここに彼がいるのは間違いないらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そして、漂う甘い香り。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（お菓子でも作っているのかしら？）"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "物陰からこっそりと覗くと、茶色い耳を動かしながら力説する彼の姿が見えた。"


scene bg_gen23_bkt
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0017
Chef "「ですが、エリオット様……。\n
もっとうまいものと言われても……、具体的には、どんなものを考えていらっしゃるんです？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0043
Elliot "「だからうまいものだよ、うまいもの！\n
こう……、食べたら幸せっていうか……、嬉しくなるやつ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice kat_f0018
Chef "「うーん……、ですから、もう少し具体的に」"


scene t_cut_eri1u
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "案の定（というべきか）、キッチンにはオレンジ色の食材を使った食べ物が所狭しと並んでいる。\n
甘い香りが、部屋の中に充満していた。"

$ flash_orange(.15)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_7")
T "（にんじんケーキ、にんじんドーナッツ、にんじんマカロン……）"

$ flash_orange(.15)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（……にんじんトリュフ、にんじんクッキー、にんじんまんじゅう。\n
にんじんジュースに、にんじんムース、にんじんタルト）"

$ flash_orange(.15)
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（にんじん羊羹、にんじん蒸しパン。\n
にんじん、にんじん……、どこまでもにんじん）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "圧倒的なまでの、オレンジ色の洪水。"


scene t_cut_eri1
with dis
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T "（…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（目が痛い）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_15")
T "{size=+20}（ブラッドじゃなくても、にんじんが嫌いになれそう）{/size} "

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この異常な空間に耐えられる人間なんて、にんじん好きのウサギと、その料理の制作者だけだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お菓子の香りにまでオレンジ色が染み込んでいるような気がする。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「お腹が空いていたのかしら、エリオット」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は屋敷外で仕事をすることも多い。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "屋敷の中にいたとしても、自室でじっとしているなんてことは稀だ。\n
大抵は部下と一緒に計画の準備をしていたりと忙しく過ごしているのだが……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（……これは、仕事には見えないわよね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "少なくとも、日頃彼のにんじん責めに辟易している主ならば、絶対に出すはずのない命令だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この様子では小腹が空いて何か作ってもらったという雰囲気でもない。\n
今のエリオットは食べることよりも、新メニューを熱望しているのが、分かる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（それにしても、すごい量ね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "お腹を満たすことが目的で、これだけのお菓子を食べに来たといわれたとしても、奇妙である。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼は元々体格に見合うだけ食べるが、さすがにこれは多すぎる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "にんじんレストランでもオープンする気なのかと突っ込みたくなった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T "「まあ……、どちらかというとスイーツ専門店って感じよね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "客が定着するのかどうか、疑問は山ほどあるが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T "（少なくとも、ここの家主は絶対に近づかない）"


scene bg_gen23_bkt
with dis

show eri_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0044
Elliot "「何かねえかな……。\n
一度も食ったことのないような、それでいてうまいもの……、ん？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "首を傾げたエリオットが、こちらを振り返る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "「……{size=+20}え？{/size}」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "振り返ったその姿に予想していなかったものを見つけて、私は思わず目を見張る。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T "「エ、エリオット……？」"

hide eri_t_02_7
show eri_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_8")
voice eri_f0045
Elliot "「な……！\n
[firstname]、あんた、どうしてここに！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T "「それは私の台詞よ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "キッチンにいるのはいい。\n
シェフと料理談義をするのも、彼の自由だ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "メニューがたとえオレンジ色のものだろうが、そんなことは些末なことである。\n
この屋敷ではいつものことなので、呆れはしても、驚くほどのことではない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "その程度には、私だって彼のことをよく知っている。\n
しかし……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T "{size=+20}「何で、エプロンまで着けているの？」{/size} "

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice kat_f0019
Chef "「ああ、これは……」"

hide eri_t_01_5
show eri_t_01_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice eri_f0046
Elliot "「……黙れ。\n
余計なこと言ったら、殺すぞ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
Chef "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "のんびりとにんじん料理語りをしていたときとは打って変わった、冷たい声。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "一言でシェフを黙らせたあと、エリオットは慌ててエプロンを外しながら、私に向き直った。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「エリオット、またそんな物騒なことを言わないで。\n
あなたがそんな格好をしている理由を聞いただけじゃない」"

hide eri_t_01_6
show eri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice eri_f0047
Elliot "「な、何でもないんだって。\n
これは、その……、そう、そうだ！」"

hide eri_t_01_9
show eri_t_03a_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice eri_f0048
Elliot "{size=+20}「ブラッドに新しいにんじん料理を作ってくれって、頼まれたんだよ！」{/size} "

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "よりにもよって使う名前がそれとは……。\n
いや、ブラッド命のエリオットを動かす理由には、これ以上ないのだろうが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T "（本人にばれたら、名誉毀損でマシンガンを連射しかねない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あるいは、全力疾走でその場から逃亡を図るか……。\n
どちらだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T "（試してみるもの面白そう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "悪戯心が疼くが、マフィアのボスに喧嘩を売る勇気はない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そのあとに待っている報復を考えると、敵に回すにはブラッドは恐ろしい相手だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_10")
T "（……ねちねち、ねちねち。\n
しつこく根に持ちそう）"

hide eri_t_03a_3
show eri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0049
Elliot "「も、もちろん、あんたにも分けてやる予定だったんだぜ？\n
ほら、これなんか、結構うまく焼けただろう？」"

play sound se_0313
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼が差し出したのは、端が少し欠けたクッキーだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T "（プロが作ったにしては形が不揃いだから……、多分エリオットの手作りなんだろうけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ちらりと後ろに立つシェフと視線をあわせる。\n
彼はこくこくと頷いて、合図を送ってきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "恐らく受け取ってやってくれと言いたいのだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この大きな手で小さなクッキーを作っていたと思うと、それはそれで可愛らしい気もする。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、その感想を無に帰してしまうほど、心がざわついていた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_16")
T "（どうして……、誤魔化すの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "下手な嘘。\n
もっとうまく誤魔化すことだって、彼には出来るはずなのに。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_15")
T "（何で今更、遠ざけるのよ？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "あからさまに距離を置かれて、寂しくなる。\n
ファミリーの一員としてみてもらっていると思っていたから、余計だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（私は武器を扱えたりしないけど……。\n
抗争に向かうことも、止めたりはしなくなったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "彼らが生きていくためだから、仕事がうまくいってほしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "そう感じるようにすらなってしまったのに……、今更突き放されるのは嫌だと思う。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_12")
T "「クッキーはとりあえず、置いておいていいから」"

hide eri_t_01_9
show eri_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_12")
voice eri_f0050
Elliot "「ん……、何だ？\n
クッキーじゃないほうがよかったのなら……」"

play sound se_0546
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "受け取らなかった理由を彼は勘違いをしているのだろうか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いや、あるいは、意図的に話を逸らそうとしているのかもしれない。"

play sound se_0544
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ごそごそと他のオレンジ色の食べ物を渡そうとするエリオットに顔を近付けて、止めた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T "（甘い匂い）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "いつもなら美味しそうだと思う香りが、今はそう思えない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「そうじゃなくて。\n
私に嘘までついて、一体何をしようとしているの？」"

hide eri_t_02_12
show eri_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
Elliot "「！」"

hide eri_t_02_5
show eri_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice eri_f0051
Elliot "「だ、だから、何のことだって？\n
俺、あんたに隠しごとなんてしていない……、とは言わないけど」"

hide eri_t_02_6
show eri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_12")
voice eri_f0052
Elliot "「嘘なんてつくほど器用じゃねえよ。\n
ほら、こんなにうまいものがたくさんあるんだ、食って行けって」"

play sound se_0546
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T "「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T "（ふうん、まだしらを切るのね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "隠しごとをしていないとは言わなかった。\n
だがやはり、本当に隠さなければならないことだけ隠しているようには見えない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（だったら、私にだって考えがあるわよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "差し出されたクッキーには指一本触れないまま。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "表面上はわざとらしいほど上品に微笑んで、納得した声で応えた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「分かったわ、何を隠しているかについてはもう聞かない。\n
あなたを困らせるつもりはないから」"

hide eri_t_01_9
show eri_t_02_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_14")
Elliot "「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ほっとしたエリオットの顔から力が抜けた。\n
つられるように耳がへにゃっと垂れ下がり……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「追及しない代わりに、エリオットと一緒ににんじん料理も食べない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "冷たく言い放った私の言葉に、長い耳は再びぴんと立ち上がった。"

hide eri_t_02_7
show eri_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0053
Elliot "「え？は？\n
な、何だよ、それ……、どういうことだ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「どうもこうもないわよ。\n
ここから出ていけば、一緒に食べることもなくなるでしょう」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（そこまで隠すなら、教えてほしいなんて絶対に言ってあげない）"

hide eri_t_02_6
show eri_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_03_9")
voice eri_f0054
Elliot "「こ、ここから出て行く？？？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「ええ、そうよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「あなたが隠していることは、私には教えられないことなんでしょう？\n
それなら私が帽子屋屋敷にいないほうが、都合がいいじゃない」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "受け入れてくれたと思っていた。\n
見せないほうがいいと思うことだけ、隠しているのだと信じてもいた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、こんなあからさまに見せ隠しをされては、怒るなというほうが無理だ。"

hide eri_t_01_5
show eri_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice eri_f0055
Elliot "「おいおい、冗談だろ！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T "「冗談なんかじゃないわ。\n
今までお世話になりましたっ！！」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T "{size=+20}「嘘つきなんて、大嫌い！！」{/size} "

hide eri_t_02_5
show eri_t_01_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_6")
Elliot "「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_6")
Chef "「…………」"

hide eri_t_01_12
show eri_t_01_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_6")
voice eri_f0056
Elliot "「う、嘘つきって……、おい、[firstname]！？\n
ちょっと待てって！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "背中から追い掛けてくるエリオットを突き放すように、叩き付けるようにドアを閉める。"

play sound se_0319
camera at hpunch
camera at vpunch

scene br_01
with dis
hide eri_t_01_5
show eri_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Elliot "「～～～～っ！！！？」"

hide eri_t_02_5

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "かなり痛そうな音がしたが、今回ばかりは可哀想と思えない。\n
最初に悪趣味なことをしたのは、彼らのほうだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_2")
T "（エリオットならちゃんと話してくれると思っていたのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "期待していた私が、悪かったのかもしれない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T "（邪魔なんてしないのに……、信用されていないみたいで嫌なのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットならきっと話してくれる。\n
あるいは知らなくていいことなら、はっきりそう言ってくれる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "それだけの関係を築いていると思ったのは、自惚れだったのだろうか。"

$ hi_mes()

scene bm_aut_01_1
with stripe_l_long
play sound se_0584

play music hatter_gate_p_ali

show dee_t_01_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice dad_f0051
Dee "「あ、あれ、お姉さん？\n
そんなに急いで、どこに行くの？」"

play sound se_0465
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "珍しく仕事をしていた二人は、早足でやってきた私が通り抜けるや否や、近付いてくる。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "エリオットとのやりとりを知らなくとも、ただならぬ雰囲気というのは察したのか、気遣うように見上げられた。"

hide dee_t_01_2
show dee_t_01_2 at left
show dam_t_02_9 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0052
Dam "「何だか、すごく機嫌悪そうだけど……。\n
嫌なことでもあった？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_14")
T "「あんた達には関係ないわよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T "（隠しごとをしているくせに……。\n
信頼してくれていないんでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうしても口調が尖ってしまう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_12")
T "「それに、私がどこに行こうと、勝手でしょう。\n
邪魔しないで」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "ぴしゃりと言うと、二人は驚いたように目を白黒させた。\n
この屋敷で暮らして、今までにも小さな喧嘩のようなことは何度もしている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "だが、それはせいぜい口喧嘩の延長程度。\n
ここまで彼らを振り払ったことはなかった。"

hide dee_t_01_2
show dee_t_02_6 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0053
Dee "「え？ええ？\n
なにをそんなに怒っているの、お姉さん？」"

hide dam_t_02_9
show dam_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice dad_f0054
Dam "「誰かがお姉さんをいじめたの？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_13")
T "「…………」"

hide dee_t_02_6
show dee_t_02_3 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_13")
voice dad_f0055
Dee "「そんな酷い奴らは、僕らがちょん切ってきてあげるよ！\n
休憩時間返上で頑張ってもいいから」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "私の本気を察してか、双子はいつも以上に熱心に提案してくる。\n
しかし……。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_9")
T "（私をいじめたのだとしたら）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "イライラとした気持ちが、声を更に刺々しくさせた。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T "「……あんた達全員よ！\n
{size=+20}大っ嫌い！！{/size}」"

hide dee_t_02_3
show dee_t_01_1 at left
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_9")
Dee "「…………」"

hide dam_t_02_12
show dam_t_02_12 at right
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_9")
Dam "「…………」"

play sound se_0417
hide dee_t_01_1

hide dam_t_02_12

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "どうして怒られているのか分からない二人に背を向けて、私は帽子屋屋敷から離れていった。"

$ hi_mes()

scene bg_gen_sky_aut_day
with stripe_l_medium

scene charasel_bg_hatter_day
with stripe_l_long
##endmemory

scene bg_gen_sky_aut_day
with dis

play music map_autumn_jok
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T "「さて、どこに行こうかしら」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T "この世界に住む友人は何人もいるが、しばらく滞在させてもらうことを考えると……。"

$ routechara = "Elliot"

$ show_mes("frame_gen_togaki")
T "Where do I want to visit?"
$ hi_mes()
show screen fushigi_map1
$ ui.interact()
