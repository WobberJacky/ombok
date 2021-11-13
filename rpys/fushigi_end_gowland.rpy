
scene map_bg_summer_day
with dis
label fushigi_end_gowland1:
$ hi_mes()
$ clockanim()


scene map_bg_summer_day
with dis

scene yum_sum_01_1
with dis

scene bg_gen11_yuy_sum_day
with dis

play music gowland_t_ali

scene go_01
with Dissolve(1.2)
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「ねえ、そういえば……。\n
結局、新しいアトラクションって決まったの？」"


show go_t_01_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0282
Gowland " 「いや、全然だな。\n
どいつもこいつも、二番煎じだったり、迫力不足だったり……」"

hide go_t_01_7
show go_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0283
Gowland " 「どうにもこうにも、最後の一押しが足らなくて、全部没になった」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「ふうん」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_15")
T " （でも、一応考えたものがあるんだ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 久しぶりに入った、ゴーランドの私室には書類がいっぱい積まれていた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 喧嘩の原因にもなった企画書の山だ。\n
その中の何枚かに目を落としてみる。"

play sound se_0469
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「これは結構面白そうだけど……。\n
これも没になったの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （比較的、うちにはしてはまともなアトラクションっぽい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 見た目はジェットコースターだが、椅子がスプリング式になっていて、ぼよんぼよんと揺れる仕組みになっているらしい。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " しかし、ゴーランドの首は縦には振れなかった。"

hide go_t_03_2
show go_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0284
Gowland " 「駄目だ駄目だ。\n
そんなのじゃ、最近の客は呼べねえよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「……そうかしら？\n
私だったら、ちょっと来てみたくなるけどなあ」"

hide go_t_01_11
show go_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gor_f0285
Gowland " 「そんな柔らかいものを座席に使ったって、急スピードで動いたらあんまり関係ねえからな。\n
もう少しひねりがないと駄目だ」"

hide go_t_03_1
show go_t_02_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_14")
voice gor_f0286
Gowland " 「うーん……。\n
さて、何を作るか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （やっぱり、こっちのほうがいいな）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_2")
T " （ゴーランドって感じがする）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 黄色いジャケット。\n
顎を縁取る無精髭と、眼鏡。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ワンポイントの三つ編みも、いつも通り。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T " （変な格好だとは思うけど）"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T " 「……見ていて、落ち着くわ」"

hide go_t_02_10
show go_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice gor_f0287
Gowland " 「……なんだよ、[firstname]。\n
俺のスーツ姿はそんなに変だったのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_5")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 書類を両手にとって、机で忙しく仕事をしているゴーランド。\n
その正面から相手を見て、はっきり頷く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「うん、変だった」"

play sound se_0431

show gaaan1 onlayer master with Dissolve (.5)
hide go_t_02_13
show go_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0288
Gowland " 「……え？\n
マジかよ……、従業員にはそんなに評判悪くなかったのに」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_12")
T " 「だって、ゴーランドらしくないんだもの。\n
いつも変だけど、あのときはもっと変だったわ」"

play sound se_0431
show gaaan2 onlayer master with Dissolve(.5)
hide gaaan1
hide go_t_03_3
show go_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
Gowland " 「…………」"

hide gaaan2 with Dissolve(1.2)
hide go_t_03_7
show go_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_12")
voice gor_f0289
Gowland " 「なあ、[firstname]。\n
あんた、まだ怒っているのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 机に書類を放って、肘をついたゴーランドが上目に窺ってくる。\n
子供の機嫌を取りかねているみたいで、少しおかしい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_16")
T " 「怒ってなんかいないわよ。\n
ただ、どうやったらあんなに甘い匂いが染みつくのかと思っただけ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " あのときのぱりっとしたゴーランドには、甘ったるい香りだけが不似合いだった。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_10")
T " （あからさまに、女の人の影がちらついて見えるみたいだったものね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " どうしてゴーランドがあの匂いに気付かなかったのか、不思議でならない。"

hide go_t_02_5
show go_t_03_7 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0290
Gowland " 「だから、別に後ろめたいことはなんにもしてねえって。\n
そんなに睨まないでくれよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_10")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T " （どうだか）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 少なくともあの路地で密着していたことは間違いない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T " （だいたい、取引がある相手って言っていたけど誰だったんだろう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドはただの遊園地のオーナーというだけではなく、勢力争いに加わるだけの実力がある。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " こうしているとただの気のいい人だが、裏に抱えるものはけして軽くはないだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 何しろ、敵対する勢力は、マフィア、城。\n
分かりやすい権力者とその名を並べる以上、暗くて、重いものがないはずがない。"

hide go_t_03_7
show go_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0291
Gowland " 「あ、まだ疑っているだろう、あんた。\n
本当にただ取引先のお嬢さんっていうだけだって」"

hide go_t_01_11
show go_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0292
Gowland " 「指一本触れていない……、とまでは言わねえけど、あんたが見た以上のものは、俺も知らねえよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_9")
T " 「ふうん……。\n
ちなみに、どこのお嬢さんだったかは、聞いてもいいのかしら？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " もし、知らないほうがいい相手だったら、適当に誤魔化してくれるはずだ。\n
ゴーランドがそう判断したことに私が口を挟むまでもない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T " （それに、遊園地で会うことはなさそうだし）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " オーナーにビンタして帰るぐらいだ、彼女が自らここにやってくることはないだろう。"

hide go_t_03_1
show go_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0293
Gowland " 「どこって……。\n
あの通りだぜ」"

hide go_t_02_3
show go_t_02_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0294
Gowland " 「バニラアイスのメーカーだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_16")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「…………」"


play music gag2_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「は？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " もっと深刻なものや、複雑な関係を想像していただけに拍子抜けだ。"

hide go_t_02_13
show go_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0295
Gowland " 「だから、アイスだよ、アイス。\n
うちにアイスを卸している、でっかい会社のお嬢さん」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T " 「…………」"

hide go_t_03_4
show go_t_02_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice gor_f0296
Gowland " 「あのお嬢さんはその社長の娘だか何だか……、まあそういう位置付けってわけだ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T " （アイス）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T " （アイスの会社の令嬢）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 確かにあれだけのバニラの香りはなかなか付くことがないとは思うが、それにしても……。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_1")
T " 「…………」"

play sound se_0431
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_13")
T " {size=+20}（私は、アイスの香りにヤキモチを焼いていたわけ！？）{/size}"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 知らなければよかった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " しかし、後悔しても遅い。\n
後悔なんて、いつだってした後にこそ訪れるものだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T " （せめて香水とかだったら、よかったのに）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 苛ついていた自分が、本当に馬鹿らしくなってくる。"

hide go_t_02_12
show go_t_03_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0297
Gowland " 「おい、[firstname]？\n
大丈夫か？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T " 「……なんで」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_10")
Gowland " 「？？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_14")
T " 「アイス作っているからって、自分もあんな甘い匂いなんて付けないでしょう！\n
どうしてそんなことをしているのよ！？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_9")
T " （営業なの！？\n
社長令嬢自らが回らなくちゃいないような状況なの、その会社はっ！？）"

play sound se_0395
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " バンッと机を叩いて訴えると、ゴーランドは軽く笑いながら返す。"

hide go_t_03_3
show go_t_01_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0298
Gowland " 「見上げた営業精神だろ。\n
あの熱心さだけは俺も見習わないとな」"

hide go_t_01_8
show go_t_03_1 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0299
Gowland " 「まあ、そんなわけで……、前々からどうしても会ってくれってしつこくてよ。\n
俺もあんたがいない状況で会う気にはなれないって断ったんだが……」"

hide go_t_03_1
show go_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0300
Gowland " 「とうとう向こうさんのほうが痺れをきらせて、押しかけてきちまったんだ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「それって……、私が一度戻ってきたとき？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドは頷かなかったが、表情が是と物語っていた。"

hide go_t_02_5
show go_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0301
Gowland " 「いくらなんでも不躾だからな。\n
ちょっとばかり荒っぽくても、さっさと帰ってもらうつもりだったんだけどなあ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「…………？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " そこで一度言葉を切ると、じいっと彼は私を見つめた。\n
思い出すような、懐かしむような、そんな目だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T " （でも、何だか視線がうまく噛み合わないような）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 視線の先がよく分からない。\n
彼は一体どこを見ているのだろう。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_2")
T " 「ゴーランド？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 名前を呼ぶと、ゴーランドの手がそっと伸びてきて私の髪に触れた。\n
確かめるような、困っているような眼差しで。"


play music transparent1_a_ali
hide go_t_03_12
show go_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0302
Gowland " 「あんたの髪と同じ色していただろ、あのお嬢さん？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_5")
T " （髪の毛？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 首を傾げると、ゴーランドは毛先を掴みじっと見つめる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T " （……確かに近い色はしていたと思うけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 私の髪は長いが、別に珍しくも何ともない色だ。\n
ボリスの蛍光ピンクの髪の色に比べれば、平凡すぎるし、ありふれている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_11")
T " 「髪の毛だけでしょう？\n
他に共通点なんて、なかったわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 顔の見えにくい役を持たない人。\n
彼女もまたその一人だった。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " だが、その顔を意識しようと思えば、見えないことはない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T " （顔はまったく似ていなかったもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 比べるのもおこがましい。\n
社長令嬢と言われれば、納得してしまう程度に……、落ち着いた顔立ちと、上品な笑顔。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 彼女にもっと似ている人を、私は知っている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T " （姉さんにちょっと似ていたのかも、雰囲気が）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_6")
T " （…………）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T " （まあ、髪型は私に近かったといえば近かったけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ただ、それだけ。\n
私との共通項なんて、髪だけだ。"

hide go_t_03_13
show go_t_02_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0303
Gowland " 「そうなんだ、髪ぐらいしか連想するところがないっていうのに。\n
あんたを思い出したら、冷たくしにくくてな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「え？」"

hide go_t_02_2
show go_t_02_5 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0304
Gowland " 「自分でも思うぜ、情けねえ話だって。\n
でもよ……、あんたがいないのは思った以上に堪えていたみたいでよ」"

hide go_t_02_5
show go_t_03_2 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0305
Gowland " 「そんなちゃちな共通点に縋ろうなんて……、さ。\n
俺らしくもない、感傷だろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " くるりと手の中で髪の毛を弄びながら、苦笑を浮かべる。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T " （会いたいと、思っていてくれていた？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 髪を掴んでいた手がそっと離れる。\n
それを、無意識に追い掛けて、捕まえていた。"

hide go_t_03_2
show go_t_01_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T " 「ゴーランド」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 逆の手は彼の髪の毛に差し入れて、編まれた髪を掴む。\n
あのときには、なかった一房。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 触れていると、とても安心する。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T " （どんな格好をしていても、ゴーランドはゴーランドだけど）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_10")
T " （やっぱり、今のゴーランドがいい）"

show t_go_end1 onlayer master
with dis
hide go_t_01_11
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 上半身を倒し、相手の唇に、自分の唇を重ねる。\n
触れるだけのキスをして、離れた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0306
Gowland " 「……っ、は、あんた。\n
いきなり、それは……、ねえだろ」"

hide t_go_end1 with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 焦ったような声がおかしくて、嬉しい。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「……嫌だった？」"


show go_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gor_f0307
Gowland " 「まさか。\n
ただ、不意打ちされてばかりじゃ、悪いだろう？」"

play sound se_0251
camera at hpunch
camera at vpunch
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " スッと立ち上がったかと思えば、腕をとられて引っ張られる。\n
反対の腕で腰を支えられて、抱き上げられたまま、イスに座った。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 膝の上に乗せられて、瞬きを繰り返す。"


show t_go_end2 onlayer master
with dis
hide go_t_01_3
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T " 「あ……。\n
んっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 今度は相手から唇が触れて、熱が広がる。\n
不思議な感覚。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 心地よく、熱い。\n
あれほどじりじりと焦げるようだった感情が、今は凪いでいるのが分かる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T " （今、この人に触れているのは、私）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_8")
T " （今、この人に触れられているのは、私）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " そう思うだけで、胸の中で心臓が跳ねそうだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「[firstname]……」"

hide t_go_end2
show t_go_end3 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_4")
T " 「あ、ちょ、ちょっと待って」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 続きをせがむような声を遮って、手を動かすとゴーランドは不思議そうに首を傾げた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0308
Gowland " 「ん？\n
嫌なら、無理にとは言わねえけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_7")
T " 「そうじゃないけど……。\n
先に話しておこうと思って」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_7")
Gowland " 「？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T " 「クローバーの塔に居候していたときに、新しいアトラクションを思いついたから」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_6")
T " 「もし、まだ新しいのが決まっていないのなら、少し考えてもらえないかなって」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_6")
Gowland " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「もちろん、ゴーランドが没って言う可能性もあるし、あくまで案としてなんだけど……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_7")
T " （な、なんで、そんなに驚いた顔で固まっているの？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 横抱きで腕の中に納まったまま、相手を窺う。\n
ぽかーんとしたままのゴーランドは、私の顔を見たまま動かない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0309
Gowland " 「あんた、塔でも、うちの遊園地のことを考えてくれていたのか」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T " 「……だって、手ぶらで帰るのも嫌だったし。\n
いきなり休んだから、皆にも迷惑かけたでしょう」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 書類を駄目にされたことはまだ思うところがあるが、仕事に穴を開けたことは間違いない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T " （穴埋めになるかはわからないけど……、筋を通さないと）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 彼女からの平手打ちを真っ向から受け止めたことがゴーランドのけじめだというのなら、これが私の誠意。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " そう思っての言葉だったのだが、彼は私の予想した以上に真剣な顔で頷いた。"

hide t_go_end3
show t_go_end4 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0310
Gowland " 「分かった、次のアトラクションはあんたの案で行く。予算もどっかーんと使って構わねえから、好きな場所に、思い通りものを作ってくれ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0311
Gowland " 「いらないものがあったらどかすし、必要なものがあれば、どんなものでも取り寄せてやる」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「……え？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「ええ！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T " 「だって、まだ何も言っていないじゃない。\n
ゴーランドから見たら大したものじゃないかもしれないわよっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " こと、遊園地にかける情熱でゴーランドを越える存在を私は知らない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " でたらめなアトラクションが並んでいても、不思議とバランスが取れているのは、すべて彼の絶妙な采配があってだ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0312
Gowland " 「最初に立ててくれたやつを駄目にしちまったしな。\n
あんたの視点なら、いいものが出来る気がするから、安心して任せられるぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T " 「……いや、それはどうかと。\n
だいたい、設計とかはどうするのよっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_11")
voice gor_f0313
Gowland " 「設計なんか気にするな。\n
面白くて、楽しめるものならなんでもいいさ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " からっと彼は言うが、恐ろしいことだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T " （まさか……、この調子でいつも新しいアトラクションを増やしているんじゃないでしょうね？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 思わず浮かんだ想像を否定する材料がないことを哀しむべきか、喜ぶべきか。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0314
Gowland " 「仕事の話は、とりあえずこれぐらいでいいだろう？\n
あんた、働きすぎだ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0315
Gowland " 「嬉しいけどな。\n
少しぐらい、休めよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_13")
T " 「……休ませてくれるの？」"

hide t_go_end4
show t_go_end5 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_13")
voice gor_f0316
Gowland " 「仕事なら、休みをやる。\n
だけど、こっちは……、また別物だろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 吐息がかかるほど、相手の顔が近くにある。\n
昼が似合う遊園地のオーナーの顔が、隠れた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " この瞬間を知っているのは、私だけならいいと思う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_17")
T " （もう、あの匂いもない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " あのとき嫌で堪らなかったバニラの香りは、もう消えている。\n
そんな当たり前のことにほっとした。"

$ hi_mes()
hide t_go_end5

scene go_01 with Dissolve(.8)

scene yum_sum_01_1
with stripe_l_medium

scene map_bg_summer_day
with stripe_l_medium

scene map_bg_winter_day with Dissolve(1)

scene charasel_bg_tower_day
with stripe_l_medium

scene ts_01
with stripe_l_long

play music tower_room2_p_ali

show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice jul_f0154
Julius " 「……断る」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_17")
T " 「そんなこと言わないでよ。\n
ちゃんとお仕事としてお願いするから」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T " （……と言っても、私にユリウスの仕事の相場なんて知らないけど）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " しかし、仮に彼にふっかけられたところで、予算については限度なしと既にオーナーからＯＫが出ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 手にした書類を持ったまま私は、難攻不落の仕事人間に食い下がった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「ほら、ずっと仕事ずくめだとユリウスの身体にも悪いし。\n
知恵の輪の代わりに気分転換すると思って……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T " 「ね、ユリウス。\n
私から受けるのがあなたの仕事としてまずいなら、ゴーランドの名義として受けてほしいの」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_9")
T " 「お願い！」"

play sound se_0121
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 拝むように手を合わせると、呆れたため息が落ちてくる。"

hide yuri_t_02_8
show yuri_t_03_12 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0155
Julius " 「私の仕事は時計の修理だ。\n
便利屋ではない」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T " 「だって、ユリウス以上に設計とか得意そうな人に当てがないんだもの」"

hide yuri_t_03_12
show yuri_t_02_8 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_6")
Julius " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 一時は居候していたクローバーの塔。\n
そこから繋がる、時計塔の一室に私は来ている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 予想以上に苦い顔をしているユリウスに、設計図の依頼をするために。"

hide yuri_t_02_8
show yuri_t_03_10 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0156
Julius " 「おまえのためなら、いくらでも協力する奴がいるだろう。\n
そいつらのところに行けばいい」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_7")
T " 「……あなた以上に器用な人を紹介してくれたら、考えるけど」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T " （そんな人いないと思うんだけどなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 子供がちょっと乗って遊べるような玩具ではないのだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 正確な設計が出来るような技術を持った相手など、私にはユリウスしか思い浮かばなかった。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_15")
T " 「とはいっても、ジェットコースターみたいに複雑なやつじゃないから……。\n
乗りかかった船だと思って、協力してくれない？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「一応、大まかなラインだけは作ってみたのよ、ほら」"

play sound se_0469
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 言葉通りだと示すように、ゴーランドが持っていた資料を集めて、色々と書き込んだ書類を見せる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T " （資料はあくまで参考にしかならないんだもの。\n
実際に作ってみないと不確定要素が多すぎるわ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 企画から設計まで一連の流れを任せてもらったのは、遊園地に来てから初めてのことだ。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " だからこそ、少しでも確かなものを作りたい。\n
そう思っていた。"

hide yuri_t_03_10
show yuri_t_02_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0157
Julius " 「[firstname]。\n
……おまえ、すっかりいつもの調子に戻ったな」"

hide yuri_t_02_3
show yuri_t_03_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0158
Julius " 「図々しさまで戻ったのは、予定外だったが。\n
殊勝すぎるおまえというのも気持ち悪いか」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ユリウスはそう言いながら、私の手にした設計図に目を走らせると、早速渋い顔をした。"

hide yuri_t_03_4
show yuri_t_03_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Julius " 「…………」"

hide yuri_t_03_13
show yuri_t_01_3 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0159
Julius "{size=+20} 「……これか？」{/size}"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T " 「うん、なかなか楽しそうでいいでしょう？」"

hide yuri_t_01_3
show yuri_t_01_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_2")
voice jul_f0160
Julius " 「おまえが作るものを、遊園地の連中は知っているのか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_1")
T " 「教えていないわよ。\n
ゴーランドが完成するまでは、内緒にしておけって言ったから、知っているのはあなたと私だけ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " なんでも、遊園地の従業員にもサプライズは必要だとか何とか言っていた。"

hide yuri_t_01_9
show yuri_t_03_11 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0161
Julius " 「…………。\n
どうなっても、私は責任を取らないからな」"

play sound se_0470
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 溜息をつきながらも、彼は私の手にした資料に定規で線を引いていく。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T " 「ありがとう、ユリウス！」"

hide yuri_t_03_11
show yuri_t_02_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_10")
voice jul_f0162
Julius " 「おまえが落ち込んで鬱陶しいよりは、図々しいほうがマシだ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_9")
T " （心配してくれていたのよね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 何気ない言葉にも、気遣いを感じる。"

play sound se_0333
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_16")
T " （それにしても、上手いなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 予想以上の手付きに思わず見とれてしまう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ユリウスの手は、まるで魔法じかけのようだ。\n
何気なく引いた線の一本一本まで、洗練されているように見える。"

hide yuri_t_02_9
show yuri_t_03_9 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice jul_f0163
Julius " 「おい、見ている暇があれば、先に計算しておけ。\n
こことここで、強度の算出が必要になるだろう」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「あ、うん、分かったわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " てきぱき。\n
いつも時計を直しているときとはまた違った正確さ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_2")
T " （でも……）"

hide yuri_t_03_9
show yuri_t_01_13 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice jul_f0164
Julius " 「まったく、こんなものを作りたがるおまえの神経は、私には理解できん」"

play sound se_0333
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ぶつぶつと文句を言いながらも、ユリウスの手は止まっていない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （それに……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_03_14")
T " （何だか、ちょっと楽しそう）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 本人に伝えたら、きっと顔を顰められるだろうから言わない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " しかし、設計図を仕上げていく彼の顔は、どこか穏やかに見えた。"

hide yuri_t_01_13
$ hi_mes()

scene ts_01 with Dissolve(.8)

scene charasel_bg_tower_day
with stripe_l_medium

scene map_bg_winter_day
with stripe_l_medium

scene map_bg_summer_day with Dissolve(1)

scene yum_sum_01_1
with stripe_l_medium

scene yun_sum_01
with stripe_l_medium

play music amuse_inside_p_ali
play sound se_0402 volume .6

show bg_gen_sky_sum_day onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
voice tan_f0020
Employee " 「すごーーーーい、高いですねーーっ！\n
ほら、オーナー、見てくださいよ、すっごいですよっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice may_f0037
Employee " 「ほんと、ほんと！！\n
だって、観覧車よりも高いですよ、すごいっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
Gowland " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice kaz_f0013
Employee " 「オーナー！\n
何を黙っているんですかっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice chi_f0030
Employee " 「完成を一番楽しみにしていたのは、オーナーだったじゃないですか。\n
ほら、すっごいですよーっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
Gowland " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0317
Gowland " 「……そうだな、すげえ高さだな。\n
それでだ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「なに？」"


play music gag1_a_ali
hide bg_gen_sky_sum_day
show t_go_end6 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gor_f0318
Gowland "{size=+20}「どうして俺は、足をぐるぐる巻きにされて、こんな長いゴムを付けられているんだ？」{/size}"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_1")
T " 「あら、決まっているじゃない。\n
栄えある実験台一号は、やっぱりオーナーが務めないとね」"

play sound se_0729
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_6")
T " （高いせいかしら。\n
結構風が強いわね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 風になびく髪を押さえ付けながら告げると、ゴーランドはげっそりした顔で首を横に振った。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0319
Gowland " 「いや、そもそも俺もまだあんたから新しいアトラクションの正体を聞いてないんだが……」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0319_5
Gowland " 「いや、もうだいたい想像は付いているんだが、決定打がほしいような、ほしくないような」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0182
Boris " 「あれ、なに、おっさん、びびっているの？\n
だったら無理しないほうがいいんじゃない？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0183
Boris " 「無理した挙げ句に～～～～で、～～～～～～な姿なんて晒したら、次の時間帯から外歩けなくなっちゃうかもよ？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " アトラクションの上までついてきたボリスが、ゴーランドの様子を見て茶化している。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0320
Gowland " 「だ、誰が～～～～で、～～～～～～なんてするかっ！\n
おまえこそ、なんでこういうときにばっかりしゃしゃり出てくるんだっ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0321
Gowland " 「大体こういうのはいかにもおまえ向きだろうが！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0184
Boris " 「何を言っているんだよ。\n
実験に付き合わせるのなら、猫よりネズミだろう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0185
Boris " 「……あれ、そういえばピアスは？\n
先刻までその辺をちょろちょろしていた気がしたんだけど」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「ピアスなら、もう下りているわよ。\n
ほら、あそこ」"

hide t_go_end6
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 地面を指差せば、小さな影がちょろちょろと動き回っているのが見えた。"
show pia_t_02_6 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0124
Pierce " 「わわわ、わわわ。\n
猫とあんな高いところに行くなんて、信じられないよ」"

hide pia_t_02_6
show pia_t_01_4 at center
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice pie_f0125
Pierce " 「どこにも逃げ場はないし……、ううう、絶対に嫌だっ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_17")
T " （何を言っているのか、正確に聞き取れないけど……。\n
まあだいたい予想が付くわよね）"


show t_go_end6 onlayer master
with dis
hide pia_t_01_4
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice gor_f0322
Gowland " 「ピアスがいないなら、ボリスだっていいだろう」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_17")
voice gor_f0322_5
Gowland " 「これ、二人までは一緒に飛び込める設計になっているみたいだしな、[firstname]？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_6")
T " 「そうだけど……。\n
でも、まずは一人が落ちたときの反動とかを確かめないと、二人は無理じゃないの？」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_5")
T " （まあ、一応、砂袋で実験はしているけどね）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドのように思い切りよく、すぐさま人で実験する勇気など、私にはない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " それ以前に仮にも恋人に当たる人を、こんな高さから飛び降りさせるのに安全を確認しないはずがない。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 普段の彼ならそこまで想像が付くはずだが。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_7")
T " （多分、そこまで思い当たらないんだろうなあ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 砂袋での実験が終わると同時に、園内を歩いていたゴーランドを呼び付けて、一気にこの高台まで上らせたのだから、当然といえば当然だ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_04_17")
T " 「それとも、私の発案が気に入らないの、ゴーランド？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_17")
voice gor_f0323
Gowland " 「そ、そういうわけじゃねえけど。\n
さすがにこの高さは、ちょっと……、なあ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_17")
voice bor_f0186
Boris " 「ふうん、おっさん。\n
他でもない、ご指名なのに……、びびって逃げ出すんだ？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_17")
voice gor_f0324
Gowland " 「だ、誰が逃げ出したりなんか……」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T " 「じゃあ、何も問題ないわよね？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 両側から同じような表情で肯定を求めると、さすがのゴーランドも反論しにくいらしく、口を噤む。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_17")
T " 「ゴーランド？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice tan_f0021
Employee " 「オーナー！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice may_f0038
Employee " 「ここで逃げたら男が廃りますよ！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice kaz_f0014
Employee " 「ほらほら、オーナー！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice chi_f0031
Employee " 「オーナー、早く早くっ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 傍にいる従業員の檄が次々に飛ぶ。"


play music falling1_a_ali
hide t_go_end6
show t_go_end7 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0325
Gowland " 「だああっ、分かった、分かった！\n
俺がやればいいんだろう！？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_10")
T " 「だって、あなたがここのオーナーだもの。\n
率先して試してもらわなくちゃ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 諦めた相手に、ふふっと笑う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T " （あなたが楽しめないようなものを、作ったらまずいでしょう？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " だから誰よりも最初に彼の感想が欲しい。\n
駄目なら駄目だと、良作なら良作だと、結果があれば納得できる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （だって、これが原因で飛び出したんだもの）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 一時は知恵の輪のように捻れてしまった関係を、本来の形に戻すのなら、原因から正したかった。"

$ hi_mes()

hide t_go_end7 with dis
scene bg_gen_sky_sum_day

$ time_effect()

play music cheerful_a_ali
$ hi_mes()
$ show_mes("frame_gen_chara")
voice kaz_f0015
Employee " 「じゃあ、３・２・１で行きますよ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
voice gor_f0326
Gowland " 「ああ、分かった。\n
俺もここのオーナーだ、どんときやがれ」"

show t_go_end8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 先端の板の上に立ったゴーランドは、吹っ切れたのか、妙に清々しい顔をしている。"

hide t_go_end8
show t_go_end8 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 彼の周りにいる従業員はいつも通りだから、余計に浮いて見えた。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_4")
T " （いや、あれはやけっていうのかもしれないけど）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_4")
voice bor_f0187
Boris " 「ふうん、ちょっとどきどきするね」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 彼らから少し離れた場所で一緒に見ていたボリスは、楽しげだ。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_11")
T " 「私は……、ちょっとどころじゃないわ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 自分がけしかけたにせよ、いざ本番となると緊張してくる。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_1")
T " （ゴムの具合も何度も確かめたし、下には何段かに分けてネットも敷いてあるし……）"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_11")
T " （何も心配することなんて、ないはず）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " そう思っていても、初めてのことだ。\n
不安と期待が混じり合って、何ともいえない気持ちになる。"

hide t_go_end8
with dis
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice chi_f0032
Employee " 「３！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0022
Employee " 「２！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「…………」"

play sound se_0055
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドの手が胸の前でしっかりと組まれた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0039
Employee " 「１！！！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0327
Gowland "{size=+20} 「だあああっ！！！！」{/size}"

play sound se_0348
$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_4")
T " （…………！）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ジャケットが台の上から、消える。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_7")
T " 「ゴーランドっ」"

play sound se_0692
pause .20
play sound se_0268
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
Gowland " 「！！？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_7")
voice gor_f0328
Gowland " 「おお、すげえっ！\n
こういうのは、なかなかねえな！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " びよよんと縦に揺れていた顔が、こちらを見上げてくる。\n
その顔は、飛び降りる前とは打って変わった、楽しげな表情だった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「[firstname]！！」"

play sound se_0268
pause .3
play sound se_0268
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 風の音に遮られていても、彼の声だけはここまできちんと聞こえてくる。\n
それが何よりも嬉しかった。"

play sound se_0693 volume .7

show t_go_end9 onlayer master
with dis
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_13")
T " （よかった、楽しんでくれているみたい）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 飛び込む瞬間よりも遊園地を見下ろしていることを楽しんでいるあたり、当初の予定とちょっと違っているが、それぐらい構わない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0188
Boris " 「へえ……、何だか楽しそうだね。\n
俺も次やってみようかな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0189
Boris " 「ほら、[firstname]、あんたも行こうぜ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「あ、待って、ボリス！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 先に走り出したボリスを追いかけるように手を伸ばしたときだ。"

hide t_go_end9
with dis
play sound se_0611
camera at vpunch
camera at hpunch
pause .6
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T " 「！！？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ごうっという風が巻き起こって、視界を揺らした。\n
いや、違う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_8")
T " （揺れているのは……、私？）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 台から身体が風で押し出されているのだ。\n
慌ててバランスを立て直そうとしたが、傾いた身体は戻らない。"

play sound se_0348

play music tension_a_ali
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_6")
T " {size=+20} 「きゃああっ！！！！」{/size}"

play sound se_0402

show white onlayer master with spread_extrashort
hide white with spread_extrashort
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 足下に感じていた固い感触がなくなると同時に、私は空に投げ出されていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Boris " 「[firstname]！！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 台から手を伸ばしているボリスがぐんぐんと遠退いていく。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 届かない。\n
どんなに手を伸ばしても、あの場所に私の手は戻れない。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_8")
T " 「～～～～っ」"

play sound se_0402

show black onlayer master with spread_short
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴーランドのようにゴムが付いているわけではないのだ。\n
ネットのある場所に落ちきるまで、止まるわけがない。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_10")
T " （ネットがあるし死なないとは思うけど……、ものすごく痛そう！！）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_04_9")
voice pie_f0126
Pierce " 「ぴっ！？\n
[firstname]、ぎゃああ、危ない、危ないよおおおっ」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ピアスの悲鳴が近くに聞こえる。\n
落下していく感触は、曖昧で感覚が狂う。"


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 酷くゆっくりにも、一瞬のようにも思う。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T " （もう、そんなに下まで落ちたの……？）"

play sound se_0052
camera at hpunch
camera at vpunch
camera at hpunch
camera at vpunch
pause .6
$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_01_12")
voice gor_f0329
Gowland " 「大丈夫だ。\n
[firstname]、平気だろ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_10")
T " 「…………」"


play music moon_night1_a_ali
hide black with open
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_7")
T " 「ゴ、ゴーランド……？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_05_7")
voice gor_f0330
Gowland " 「それにしても、あっぶねえな……。\n
ボリス、おまえ、近くにいながら何してんだ！」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ガクンッと衝動があって、ゴーランドの声に目を開けた。"


$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ゴムが動く音が聞こえ、代わりに全身を包み込んでいた風の流れが途切れている。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " どうやらゴーランドは逆さまにぶら下がったまま、落下してくる私を受け止めたらしい。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice bor_f0190
Boris " 「悪い、ここの風がこんなに強いとは思わなかったんだよ。\n
[firstname]、大丈夫？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 台の方から声をかけてくるボリスに、何とか手を挙げて無事だと伝える。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_04_9")
T " （た、助かったのよね……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 折角作ったアトラクションを、発案者の事故で台無しにはしたくない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0331
Gowland " 「まったく、仕方ねえな。\n
大丈夫じゃなかったら、ここから銃弾ぶっぱなしていたぜ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice tan_f0023
Employee " 「さっすがオーナー！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice may_f0040
Employee " 「やるときはやりますね！」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0332
Gowland " 「やれやれ……。\n
[firstname]、ほら、目を開けてみろよ」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_5")
T " 「……む、無理言わないでよ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_01_12")
T " （だって、ここ、すごく高いのよ）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 足場がしっかりしていた台ならともかく、彼の腕だけが頼りの状況でこれ以上目を開けたらパニックを起こして、落ちてしまいそうだ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_3")
T " （特に高所恐怖症っていうわけじゃないけど……）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 現状、薄目を開けるのが精一杯だった。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0333
Gowland " 「大丈夫だって。\n
ほら、目、開けてみろよ、いいものが見られるぜ？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_12")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " だんだんと私を受け止めた衝撃も落ち着いてきたのか、揺れる回数も減ってきた。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 振動が収まれば、下で控えている従業員がゴーランドの命綱を外してくれることだろう。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0334
Gowland " 「今しか見られないぜ、こんな風景」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_16")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_16")
voice gor_f0335
Gowland " 「俺に掴まっていれば大丈夫だ。\n
ゆっくり、目を開けてみな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_3")
T " 「……ゴーランド？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " そこまで言われては、恐怖心よりも好奇心が勝つ。\n
しっかりとゴーランドの服に縋り付いたまま、ゆっくり目を開けてみた。"


play music happy_a_ali
show t_go_end10 onlayer master with open_long
hide black
$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_15")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_03_10")
T " 「わあ」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_20")
T " （遊園地をこうやって見渡せるなんて、思わなかった）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 視界の下に広がっているのは、よくできた模型のようだった。\n
点のように見えるが、動いているのはすべて生きている人。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " アトラクションの稼働状況も、あちこちから聞こえてくる歓声と絶叫も、全部が全部、ここに集約されている。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_14")
T " 「観覧車から見たことは何度もあったけど……」"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_05_14")
T " （ガラスも何も通さずに、こんな風景が見られるなんて）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 高台に上ったときも、見晴らしはいいと思っていた。\n
しかし、今はまるで遊園地の上を飛んでいるような気分だ。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T " （気持ちいい……）"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_17")
voice gor_f0336
Gowland " 「な？\n
これはここからじゃないと、なかなか見られないだろう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 私の身体をしっかりと支えながら、ゴーランドが自信に溢れた顔で言う。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0337
Gowland " 「この景色はあんたにも見てもらいたかったが……。\n
出来ればもう少し穏便な方法にしてやりたかったな」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_18")
T " 「うん。\n
でも、ゴーランド、一つだけいいことがあったわ」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_18")
voice gor_f0338
Gowland " 「いいこと？\n
なんかいい落とし物でも見つけたのか？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " きょろきょろと下を見渡すゴーランドの顔に唇を近付けて、囁く。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_05_8")
T " 「だって、一緒に落ちない限り……。\n
こうやって、遊園地を見ることなんて出来ないでしょう？」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 同じ位置、同じ姿勢。\n
誰かとまったく同じものを見ることなんて、ほとんどないだろう。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （ここなら、遊園地と、ゴーランドしか、見えない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " そして恐らく、彼には遊園地と、私しか見えていない。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
Gowland " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0339
Gowland " 「はははっ、そりゃ違いねえ。\n
確かに、こうでもしねえとあんたと一緒には見られなかったから、不幸中の幸いってやつだな」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 豪快な声を上げてひとしきり笑ったあと、ゴーランドはふと表情を変えて、地面を見下ろした。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 遊園地のオーナーでも、侯爵でもない、静かな、物思いに耽るような顔だ。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0340
Gowland " 「あのさ、[firstname]。\n
俺は、あんたには、覚えていてほしいな」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0341
Gowland " 「この景色を、俺と一緒に見たことを」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_02_2")
T " 「……ゴーランド？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0342
Gowland " 「……な～んてな。\n
ははは、どうだ、少しはぐっときただろう？」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_02_2")
voice gor_f0343
Gowland " 「な？\n
惚れ直したか？」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_5")
T " 「…………」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 一瞬、彼の声のトーンが僅かに下がったような気がしたのは、気のせいだったのか。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 振動は収まってきていて、高台では従業員達が私達を下ろす準備をしている。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_02_17")
T " （覚えていてほしいって……？\n
忘れるはずがないじゃない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ここが私の生活する場所。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " でたらめなアトラクションに、銃を携帯する従業員。\n
猫やネズミが追いかけっこを繰り返し、おかしな侯爵が経営する遊園地。"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_01_9")
T " 「覚えているし、忘れたりしないわ。\n
だって、私の家はここだもの」"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 自分でも不思議なほど自然に、答えていた。"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0344
Gowland " 「ああ……、そうだな。\n
あんたはここにいる」"

$ hi_mes()
$ show_mes("frame_gen_chara")
$ face("ali_t_06_16")
voice gor_f0345
Gowland " 「すげえアトラクションも考えてくれる、俺の最高のパートナーだ。\n
これからも、頼むぜ、[firstname]」"

$ hi_mes()
$ show_mes("frame_gen_heroine")
$ face("ali_t_06_2")
T " 「ええ」"

play sound se_0551
$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 頷くと、顔を寄せられた。\n
私を抱きとめているせいで、手が使えないからだろう。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 髭のちくちくした感触が、くすぐったい。"

$ hi_mes()
$ show_mes("frame_gen_monologue")
$ face("ali_t_06_15")
T " （忘れるはずがない）"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " 真下に広がる、私の暮らしていく滞在地の風景。\n
おもちゃのように見えても、そこに感じる愛情は本物だから。"

$ hi_mes()
$ show_mes("frame_gen_togaki")
$ face("ali_t_06_16")
T " ずっとずっと大切にして、胸の中に仕舞っておきたい宝物だ。"


hide frame_gen_togaki
hide ali_t_06_16
with Dissolve(2)

show white onlayer master
with compress_extralong
hide t_go_end10 with dis

hide white with compress_extraextralong
pause 1

$ renpy.movie_cutscene("endroll_a.mpg")
#return
