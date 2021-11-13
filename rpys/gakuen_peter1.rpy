
scene bg25_rr_day
with dis
label gakuen_peter1:
$ clockanim()


play music corridor_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "考えてみたら、日頃よく訪ねている自治会室だが、その周辺にどんな部屋があるのかよく分かっていない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自治会室に行けば、ビバルディ、エース、ペーターの誰かが相手をしてくれるもので、ついそこで足を止めてしまいがちなのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日は、もうちょっと周辺探索に重きを置いてもいいかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_13")
T "（……いつもの定番っていうことで、自治会室から覗いてみようかしら）"

menu:
    "そうする。":
        jump gakuen_peter1_2a
    "仕事の邪魔をしては悪い。":
        jump gakuen_peter1_2b
label gakuen_peter1_2a:
$ lovechara_peter_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "周囲の探索ついでに、自治会室へと足を向けてみよう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつも行っている場所では探索にならない。\n
そう分かっていても、慣れた場所へと足は向かう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ちらっと覗いてみて、忙しそうだったら帰ればいい。\n
そうでなければ、顔を出して雑談に混ぜてもらおう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ビバルディの用意してくれる紅茶はいつだって美味で、エースとペーターの掛け合いは賑やかを通りこしてうるさいぐらいだが、見ている分には面白い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普段、私自身はペーターに押され気味な部分があるので、そのペーターが誰かにいじられているという状況は新鮮だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（いや、もう新鮮ってほどでもないけど……）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見慣れてきたのに惹かれるのは、馴染んできたからか。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_14")
T "（……うん、自治会室のほうへ行こう）"

jump gakuen_peter1_3
label gakuen_peter1_2b:
with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（でも、仕事をするからこその、自治会室、なのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "自治会という部署が具体的にどういう仕事をしているのかはよく分からないが……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これだけの生徒がいるシンフォニアの自治会を、彼らは三人だけで切り盛りしているのだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私達生徒全員が自治会員であり、彼らの部下にあたるようなものとはいえ、仕事は忙しくて当たり前だろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼らは私が遊びに行くと快く迎えてくれるが、それに甘えてしまうのはよくないかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "探索目的なのに、慣れた場所へ行こうとするのが甘えの証拠だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（おとなしく、周辺探索にしておこう）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（……って、結局、自治会室のほうへ行くわけだけど）"

jump gakuen_peter1_3
label gakuen_peter1_3:
play sound se_0158
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いつもなら通り過ぎてしまう自治会室周辺の部屋を、一つ一つ覗きながら歩く。\n
たまに鍵がかかっている部屋があるのだが、これは何なのだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "噂にもなっている、シンフォニアの秘宝が隠された部屋か。\n
期待は募るものの、そんなわけがない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通に歩いていて目に付くような、無造作な造りでは設置されていないだろう。\n
そうして自治会室が近くなったところで、私の名前を呼ぶ声が聞こえた。"



play music peter_t_ali

show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0020
Peter "「[firstname]！！！！\n
僕に会いに来てくれたんですか！？」"

hide per_m_02_5
show per_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0021
Peter "「ああっ、僕は幸せです！！！！\n
同じ寮にあなたがいるだけでも嬉しいのに、会いに来てくれるなんて……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「……いつも、幸せそうで何よりだわ」"

hide per_m_03_11
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice pet_g0022
Peter "「ええ！何よりです！何よりですとも！\n
あなたと会える以上の幸せはありません！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "相変わらずのテンションだ。\n
ペーターにとっての私は薬物にでも等しいのか、私の登場一つでペーターのテンションは恐ろしいほどに上昇する。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴょんっと跳ねるように私のもとへとやってくる動作が、本物のウサギのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「別にあなたに会いに来たわけじゃないわよ。\n
男女共同区域を探索していたの」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これ以上、ペーターのテンションが上がってしまっても困る。\n
あっさりと私はペーターが目的なのではないと告げたのだが、彼は聞いていない。"

hide per_m_02_13
show per_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0023
Peter "「なんと！！！\n
会おうと思っていないのに出会ってしまうなんて、これはまさに運命！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……{size=+20}世間一般では、そういうのをただの偶然というのよ{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……これは、会話が成立しているのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "聞いていて、捻じ曲げて理解しているのだから、ただ聞いていないだけよりもタチが悪いような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「あんたって、いつも……。\n
……はあ」"

hide per_m_01_2
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice pet_g0024
Peter "「どうしたんです？\n
溜息なんかついて」"

hide per_m_02_3
show per_m_01_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice pet_g0025
Peter "「ああっ、まさか、女子寮のほうで苛められているんじゃ……！？\n
誰ですか、あなたを苛める不届きな輩は！」"

hide per_m_01_6
show per_m_01_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_3")
voice pet_g0026
Peter "「安心してください、[firstname]！\n
僕が今すぐ成敗……っ！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_9")
T "{size=+20}「勝手に人を苛められっこにしないで頂戴」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_17")
T "「……本っ当に、あんたって昔から人の話を聞かないわよね。\n
私は誰にも苛められたりしていないし、皆親切にしてくれているわ」"

hide per_m_01_1
show per_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice pet_g0027
Peter "「あなたに親切なのは当然です。\n
万人がそうあるべきなんですよ」"

hide per_m_02_11
show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_03_17")
voice pet_g0028
Peter "「そう、それは当然として……。\n
いいですか、[firstname]、もしも気に入らないヤツがいたら、すぐに教えてくださいね？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「聞いて、どうするの？」"

hide per_m_02_8
show per_m_03_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0029
Peter "「もちろん、シンフォニアにいられなくするに決まっているじゃないですか。\n
僕は、あなたのために、この地位にいるんです！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ふふふ、とペーターは夢見るように赤い双眸を潤ませて笑う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見た目が美形な分、そんな様は麗しいといっていいようなものだが、口にしている内容はどこまでも危うい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私の望む望まないに関係なく暴走しがちなこの幼馴染のためにも、迂闊なことは出来ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "下手なことを言えば、とんちんかんな方向にペーターは行動を起こすに決まっている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "これまでの付き合いから、それぐらいは理解している。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「はいはい、分かっているわ。\n
でも、私のためを思うなら、何もしないでね？」"

hide per_m_03_2
show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_11")
voice pet_g0030
Peter "「はいっ、僕はいつもあなたのことを思っています！\n
言いつけは絶対です！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（……やっぱり、何かがずれている感じがする）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会話が成立するかどうか。\n
それ以前の問題だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（…………。\n
……どうしてこんなに歪んでいるのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "普通の幼馴染というのは、こういった関係ではないような気がする。\n
もっと健全で、まっとうであるべきだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（いつからこうなんだっけ……？\n
最初から……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もうちょっと、最初の頃はまともだったような気がする。\n
でも、気のせいかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "まともなペーター＝ホワイトといわれても、思い出すどころか想像することすら出来ないからだ。"

hide per_m_02_5
show per_m_02_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0031
Peter "「[firstname]？\n
どうかしましたか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「いえ、なんでもないわ。\n
……ねえ、ペーターはどこに行くところだったの？」"

hide per_m_02_9
show per_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0032
Peter "「僕は会長に頼まれた仕事で、塔まで書類を届けに行くところです。\n
ああ、ですがあなたのためならこんな書類！！」"

hide per_m_03_9
show per_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0033
Peter "「ここで燃やして、なかったことにしちゃいましょう！\n
そうしたら一緒に遊べますよ！！！」"

play sound se_0468
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱちん、とペーターが指を鳴らす。"

play sound se_0375
$ flash_color("orange_3", .1)
$ flash_color("dark_orange", .1)

play music gag4_a_ali
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "{size=+20}「！？」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_8")
T "「や、{size=+20}やめなさいっ！{/size}」"

play sound se_0313
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターが手にしていた茶色い書類袋。\n
指を鳴らす音と同時に、めらりと炎に包まれた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "媒体なしに燃やすとは見事だが、魔法に感心している場合ではない。\n
私は慌てて止める。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やめろという私の声に反応して、書類を焼こうとしていた炎はすでに消失していた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "茶封筒の端が焼け焦げて黒くなってはいるものの、ぎりぎり中身は無事のようだ。"

hide per_m_02_1
show per_m_01_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0034
Peter "「危ないですよ、[firstname]！\n
燃えているものに手を出そうとするなんて、不用意すぎます！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_13")
T "（……どっちが！！）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_14")
T "「不用意なのはあんたでしょう！？\n
考えなし！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「……あんた、何考えているのよ。\n
塔に届けないといけない書類なんでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "いや、もう。「考えなし」といった通り、何も考えていないのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「しかも、あんたが直接届けるということは、他の生徒には任せられないような大事なものなんじゃないの？」"

hide per_m_01_5
show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_15")
voice pet_g0035
Peter "「はあ。まあ、普通よりは重要性の高いものなのでしょうね……。\n
……ですが、あなたより大事なものなんてこの世には存在しません！」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぴん、とペーターのウサギ耳が立っている。\n
そんなことを堂々と宣言されても……。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「……塔に行かなきゃいけないのね？」"

hide per_m_02_8
show per_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice pet_g0036
Peter "「いえ、行かなければならないというわけでは……。\n
あなた以上に優先されるものはないのですから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……ペーター。\n
私、やるべきことをやらない人って嫌いなの」"

hide per_m_03_9
show per_m_02_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice pet_g0037
Peter "「ああ、それなら、{size=+20}僕は人でなくてウサギですからなんの問題もありませんよ！{/size}」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「……{size=+20}ウサギでも、嫌いなの{/size}」"

hide per_m_02_13
show per_m_01_13 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_g0038
Peter "「……え～？\n
ウサギ、嫌いなんですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_10")
T "「……え～、じゃないわよ。\n
行ってきなさい」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "寄ってはみたものの、仕事の邪魔になるようなことをするつもりはない。"

hide per_m_01_13
show per_m_01_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0039
Peter "「ええ、分かりました！\n
では僕、速攻で行ってきますから！ 」"

hide per_m_01_3
show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0040
Peter "「待っていてくれます！？\n
すぐです、本当にすぐですから！！！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_1")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "身長は、ペーターのほうがもちろん私よりも大きい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "だというのに、こうしておねだりするペーターは、潤んだ赤い双眸で上目遣いに見える。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……昔からこうだった気がする）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昔から、こうなると弱い。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「……ちゃんと仕事しなさいよ」"

hide per_m_02_3
show per_m_01_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice pet_g0041
Peter "「ええ、ですから……っ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「私も、一緒に塔に行ってあげるわ。\n
特にやることもなくて暇だったの」"

hide per_m_01_10
show per_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
Peter "{size=+20}「！！！！！！」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ぱあっとペーターの顔が輝く。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ストーカーだの何だの言いつつも、こんなにも喜ばれてしまうと悪い気はしない。\n
私も、現金なものだ。"

hide per_m_01_2
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

$ time_effect()##PLEASE MANUALLY ADJUST ME
play music corridor_day_p_wam
pause .501
play sound se_0158
play sound se_0774
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今にもスキップをしそうなペーターと一緒に、来た道を戻るようにして廊下を歩く。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「そういえば……。\n
先刻あちこち見て回っているときに、鍵のかかっている部屋があったんだけれど、そこは何なの？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「ほら、シンフォニアの秘宝がある小部屋云々……、なんて噂もあるじゃない？\n
それで気になったんだけど、ペーターは知っている？」"

##[rchara1 PAY ATTENTION="false"]
show per_m_02_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0042
Peter "「ああ、それは物置ですよ。\n
自治会の備品などを管理している部屋なので、鍵がかけてあるんです」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_3")
T "「物置……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一気に夢の覚める、現実だ。"

hide per_m_02_8
show per_m_02_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0043
Peter "「あなたが中を見たいというんでしたら、いつでも開けて差し上げますよ？\n
遠慮なく言ってください」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_11")
T "「いえ……、いいわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "物置なんて、開けてもらっても仕方ない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そこが秘密の部屋だなんて思っていなかったはずなのに、残念だと思う。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "簡単に見つかってしまってはシンフォニアの秘宝、なんて呼ばれたりはしないと分かっているのだが……。"

hide per_m_02_1
show per_m_03_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0044
Peter "「ふふ、可愛らしいですね。\n
シンフォニアの秘宝を期待していたんですか？」"

hide per_m_03_6
show per_m_03_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0045
Peter "「では、今度、美術館でもご一緒しませんか？」"

hide per_m_03_4
show per_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0045_5
Peter "「秘宝ではありませんが、シンフォニアにしかない、珍しいマジックアイテムや美術品がたくさん陳列されていますよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「美術館……？\n
ああ、そういえばそういう施設もあるって聞いていたわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「まだ行ったことがなかったの。\n
ペーター、案内してくれる？」"

hide per_m_03_11
show per_m_02_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0046
Peter "「喜んで！！！\n
あなたと二人で美術館……！！」"

hide per_m_02_5
show per_m_01_2 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice pet_g0047
Peter "「なんて素敵なんでしょうね！\n
いつ行きます？今すぐですか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_14")
T "「……塔に書類を届けないといけないんじゃなかったの？」"

hide per_m_01_2
show per_m_02_7 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice pet_g0048
Peter "「……そう、ですけど。\n
ですから……、こんな書類その辺で焼いてしまいましょうよ、[firstname]」"

hide per_m_02_7
show per_m_03_9 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice pet_g0049
Peter "「どうせ困るのは風紀委員長のユリウス＝モンレーです。\n
ああ、ついでに会長も困りますか」"

hide per_m_03_9
show per_m_02_4 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_14")
voice pet_g0050
Peter "「……ふむ。\n
いいこと尽くめじゃありませんか」"

play sound se_0551
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "すっと再び、白い手袋に包まれたペーターの手が持ち上がる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_10")
T "「困らせないで、仕事しなさいよ。\n
……ヤギじゃないんだから」"

hide per_m_02_4
show per_m_02_10 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_10")
voice pet_g0051
Peter "「ヤギ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_15")
T "「あら？\n
知らない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_03_4")
T "「白ヤギさんと黒ヤギさんは、お手紙のやりとりをしているけれど、二人とも読まずに食べちゃうのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_5")
T "「ウサギなら、途中で書類の抹消なんてしちゃいけないわ」"

hide per_m_02_10
show per_m_01_8 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_5")
voice pet_g0052
Peter "「まあ、僕は食欲に負けて仕事を放り出すほど、愚かな動物ではありませんけど……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_1")
T "「なら、賢く振る舞って」"

hide per_m_01_8


scene bg20_gd_day with stripe_l_medlong

play music garden_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな他愛のない会話をしながら、二人で塔を目指す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "思えば、ペーターが先にシンフォニアへ入学してしまって以来、こんなふうに二人で歩くことはなかったような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "会えばペーターは過剰なまでに私に構いたがり、私はそれが鬱陶しく、殴り倒したり逃げたりしていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_2")
T "（……普通にしていれば、普通以上なのに）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "見目がいい分、非常にもったいない。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（いつも、こうなのよね……。\n
……はあ）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（…………）"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_5")
T "（……？）"

play sound se_0158
play sound se_0774

scene bg_par15_rg_tow_day with stripe_l_medlong
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "塔へと続く道を歩きながら、すれ違う生徒達がやたらとこちらに視線をやってくるのに気付いた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "新入生である私が注目されるはずがない。\n
となると、ペーターだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "やはり自治会書記なんて役職についていると、名も売れているのだろうか。"


show per_m_02_3 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice pet_g0053
Peter "「……？\n
どうかしましたか？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ペーターはそんな周囲の視線には気付いていないのか、気にした様子はない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "もしかしたら、自治会の役員として注目を浴びることに、すでに慣れているのかもしれない。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「いえ、なんでもないわ。\n
さ、急ぎましょうか」"

hide per_m_02_3
show per_m_03_5 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice pet_g0054
Peter "「ええええっっ！？そんな！\n
急がなくたっていいですよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「先刻は、すぐすますって言ったじゃない」"

hide per_m_03_5
show per_m_02_6 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice pet_g0055
Peter "「それは、あなたを待たせている場合の話です！\n
せっかくのあなたとのデートなんですから、もっとゆっくり歩きましょうよ！」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "{size=+20}「デートじゃないわよ」{/size} "

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "のろのろと分かりやすく歩調を落とすペーターをせきたて、塔へと向かう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "この場に長く留まりたくない。\n
私にとっては慣れない注目で、居心地悪い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "視線を浴びながら、逃げ出すように早足になる。"

hide per_m_02_6
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par15_rg_tow_day with Dissolve(.5)

scene bg25_rr_day
with stripe_l_medium

scene bg_par19_fi
with stripe_l_long

play music laboratory_day_p_wam
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その後も案の定、ペーターが騒ぎ立て、ユリウスに迷惑をかけた。"


show yuri_m_03_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0000
Julius "「……職務に忠実でない、いつものおまえでいい。\n
今に比べれば、まだマシだ……」"

hide yuri_m_03_11
show yuri_m_02_11 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice jul_g0001
Julius "「……人格崩壊を起こすな」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_11")
T "（ペーターは、元からこうじゃない）"

hide yuri_m_02_11
show yuri_m_02_11 at left
with dis
##[rchara1 PAY ATTENTION="false"]
show per_m_03_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice pet_g0056
Peter "「失礼な男ですね。\n
ねえ、[firstname]、こんなの放っておいて、行きましょう」"

hide per_m_03_9
show per_m_02_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_11")
voice pet_g0057
Peter "「役目を終えれば長居は無用です、こんな陰気な場所。\n
ああ、[firstname]、あなたにこの辛気臭さが移りでもしたら……！」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（いつも、こう）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ユリウスは、まるで未知のものを見るかのような目で見ている。\n
居心地の悪い、先刻までの視線と同じように。"

hide yuri_m_02_11

hide per_m_02_7
##[chara1 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par19_fi with Dissolve(.8)

scene bg_par15_rg_tow_day
with stripe_l_medium

scene bg06_sk_h_day with stripe_l_medlong

scene bg06_sk_h_eve with Dissolve(1.2)
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "と、ここまでが、この前までの話。"

with dis
$ hi_mes()

scene bg06_sk_h_eve with Dissolve(.8)

scene bg06_sk_h_nig with Dissolve(1)

scene bg06_sk_h_day with Dissolve(1)

scene bg_par15_rg_ros_day with stripe_l_medlong

scene bg_par02_ct_ros_day
with stripe_l_long

play music dining_nig_p_wam
play sound se_0229
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "各寮には、食堂とは別にカフェテリアと呼ばれる空間がある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "基本的に設備としては食堂とよく似ており、生徒が頭でイメージした食べ物により近いものを提供するという魔法が備わっている……。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "……のだが、そのメニューには違いがある。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "食堂のメニューがボリュームのあるしっかりしたものが多いのに対し、カフェテリアのメニューは飲み物や軽食を中心とした、あっさりとしたものが多い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "放課後の雑談や、朝食時などには、食堂よりもこちらを使う生徒のほうが多かったりする。\n
私もそんな生徒の一人。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "図書館にて興味をひく本を見繕い、それを携えカフェテリアに赴くというのが、部活動や委員会に参加していない私の放課後の過ごし方だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "今日もそうやって過ごすつもりで、本を片手にカフェテリアへと赴く。\n
お気に入りの席にすわり、用意するのは紅茶だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "こういうところにも寮長の影響があるのか、噂によると赤薔薇寮と帽子屋寮のカフェテリアは紅茶が美味しいらしい。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私はまだ他の寮と飲み比べたりしたことがないので分からないが、赤薔薇寮のカフェテリアで供される紅茶は確かに美味だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_17")
T "（さて……、と）"

play sound se_0718
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "さっそく、図書館から借りてきた本のページをめくる。"

play sound se_0718
pause .6
play sound se_0718
pause .4
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どれくらいそうして読書を楽しんでいたのか。\n
ふと、目の前に影がさしたのに気付いて、顔を上げた。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "目の前には、顔見知りの女子生徒が二人。\n
並んで立っていた。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人とも同じ赤薔薇寮の生徒で、朝食時などには席が近ければ普通に言葉を交わす仲だ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "その二人が、何やらもじもじとした様子で私の目の前にいる。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_06_13")
T "（？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「あなた達、どうしたのよ？\n
座らないの？？？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "わざわざこうして顔を出すということは、何か私に用事があるのだろう。\n
そう思って水を向けてみたところ、二人は安心したように息を吐いた。"

##[rchara1 PAY ATTENTION="false"]
show rose_a2_1 at center
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0045
Seito "「あ……」"

hide rose_a2_1
show rose_a2_1 at left
with dis

show rose_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0036
Seito "「なんだ、いつも通り……」"

hide rose_a2_1
show rose_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0046
Seito "「座っていいの……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_6")
T "（……？？？）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_11")
T "「当たり前じゃない。\n
何よ、脅えるみたいに……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達の反応。\n
それは、まるで何かを恐れているかのようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "読んでいた本は、そんな難解な内容の本ではなかったはず。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "しかし、声をかけるだけで身構えなければいけないほどの顰め面でもしていただろうか。"

hide rose_a2_5
show rose_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0047
Seito "「……じゃ、私達もいつも通りに」"

hide rose_b1_3
show rose_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0037
Seito "「座るわね……」"

play sound se_0161
pause .5
play sound se_0161
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人はそれぞれ椅子を引くと、私の向かいへと並んで座った。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「？\n
なんで、わざわざ断ったりするの……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "どこに座ろうと、私が咎めるはずがない。"

hide rose_a2_3
show rose_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0048
Seito "「……よかったわ。\n
変わらないのね」"

hide rose_b1_2
show rose_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0038
Seito "「……ああ、緊張した」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_7")
T "「……一体、どうしたの？\n
私、何かした？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女達の口ぶりでは、私がまるでとんでもなく怖い人物のようだ。\n
話しかけるだけで緊張するだとか、どうなっているのだか……。"

hide rose_a1_2
show rose_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0049
Seito "「いや、昨日見ちゃったのよ。\n
あなた、副寮長と一緒だったでしょう？」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_1")
T "（副寮長……？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "一瞬それが誰を指しているのかが分からない。\n
が、昨日一緒だったと言われて思い出す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "おそらくはペーターのことだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "昨日会った役職持ちといえばユリウスも該当するが、彼とは風紀委員の会議室で話しただけだ。\n
一緒にいたというニュアンスではない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そういえば、ペーターは副寮長でもあったような気がする。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_14")
T "「ああ、ペーターのこと？」"

hide rose_b1_1
show rose_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tak_g0039
Seito "「そうそう、ペーター……、ホワイト副寮長のことよ。\n
……私、あんな副寮長初めて見たわ」"

hide rose_a1_5
show rose_a1_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice man_g0050
Seito "「副寮長があんなにはしゃいでいるのなんて、ねえ。\n
天変地異の前触れかと思ったわ」"

hide rose_b1_9
show rose_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_14")
voice tak_g0040
Seito "「それに、あなたったら、副寮長に対して、その……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_13")
T "「何？」"

hide rose_b1_1
show rose_b2_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice tak_g0041
Seito "「恐れ多いことを……」"

hide rose_a1_4
show rose_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_13")
voice man_g0051
Seito "「恐れ多いっていうか、怖いもの知らずよ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_12")
T "「？？？」"

hide rose_b2_5
show rose_b1_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_12")
voice tak_g0042
Seito "「ずばずば物を言うし、叩いたりもしていたらしいじゃない……？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「あ……、あ～……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_15")
T "（もしかして、暴力的な女だと思われちゃったのかしら）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "脅えられるほどのことはしていないと思うが、名門校だとおおごとなのかもしれない。"

hide rose_a1_1
show rose_a1_9 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0052
Seito "「実はすごい人なのかしら、なんて思っちゃったのよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_6")
T "「そ、そんな……。\n
たいしたことじゃ……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（ああ、でも、たいしたことじゃないなんて言ったら、また怖がられる？）"

hide rose_b1_7
show rose_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice tak_g0043
Seito "「ホワイト副寮長に、あんなふうに出来るなんて信じられない」"

hide rose_a1_9
show rose_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice man_g0053
Seito "「絶対、何かある、怖い人だって話題になっているわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_11")
T "（ペーター？）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "彼女らが恐れているのは、私ではない。\n
ペーターに対しての振る舞い。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "つまり、恐れているのは、ペーター＝ホワイト。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「…………。\n
……ペーターって、いつもあんな感じよ？」"

hide rose_b1_4
show rose_b2_7 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice tak_g0044
Seito "「まさか！」"

hide rose_a1_1
show rose_a1_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice man_g0054
Seito "「何を言っているの！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_7")
T "「……そんなに意外？」"

hide rose_b2_7
show rose_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_7")
voice tak_g0045
Seito "「あなたの言うことがね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「でも、いつも私には……」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_3")
T "（そう、よね。\n
常にあんな……、残念な感じ）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "顔だけはいいのに……、と。\n
天は二物を与えずという言葉の意味を実感させられる。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それが私にとってのペーター＝ホワイトという人物。\n
どうやら、彼女達にとってはそれは違うらしい。"

hide rose_a1_4
show rose_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0055
Seito "「ねえねえ。\n
あなた、副寮長とはどういう関係なの？」"

menu:
    "ただの幼馴染。":
        jump gakuen_peter1_4a
    "ペーターは、私のことが好きみたい。":
        jump gakuen_peter1_4b
label gakuen_peter1_4a:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「別に……。\n
ただの幼馴染よ？」"

hide rose_b1_5
show rose_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice tak_g0046
Seito "「幼馴染……！？」"

hide rose_a2_3
show rose_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice man_g0056
Seito "「そ、そうなんだ……」"

hide rose_b1_4
show rose_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice tak_g0047
Seito "「副寮長の……」"

jump gakuen_peter1_5
label gakuen_peter1_4b:
$ lovechara_peter_points =+ 1
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_5")
T "「そうね……。\n
私はなんとも思っていないけれど、ペーターは私のことを好きみたいね」"

hide rose_b1_5
show rose_b1_5 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice tak_g0048
Seito "「……す、好き？\n
副寮長が、あなたを……」"

hide rose_a2_4
show rose_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_5")
voice man_g0057
Seito "「あなたってやっぱりただものじゃないわね。\n
そんなことさらっと言えちゃうなんて……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_2")
T "「まあ、幼馴染だし……」"

hide rose_b1_5
show rose_b1_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_02_2")
voice tak_g0049
Seito "「幼馴染！？」"

jump gakuen_peter1_5
label gakuen_peter1_5:
with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_15")
T "「え、いや……」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "なんだか、また怖がられ始めてしまったようだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人は私を、何か恐ろしいものを見るような目で見ている。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "付き合いがあるだけでこんな扱いを受けるとは、一体ペーターはシンフォニアで何をしてきたというのか。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_7")
T "「そりゃあね？\n
ペーターは変質者でストーカーもどきだけど……、幼馴染ぐらいいるわよ」"

hide rose_a1_2
show rose_a1_7 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_7")
voice man_g0058
Seito "「そこよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_12")
T "「どこよ」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "びしっと指でさされての指摘に、私も即答で返す。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そんな私達のどこかずれた会話に、隣で聞いていたもう一人の女子生徒がくすくすと笑いながら補足説明をいれてくれた。"

hide rose_b1_4
show rose_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0050
Seito "「あなたといる副寮長と、私達の知っている副寮長とのギャップが激しすぎるの。\n
……私達が、目を疑ったぐらいに」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_12")
T "「まあ、ずっとあのテンションでいたら過労死しそうよね。\n
普段は、もうちょっとまともなの？」"

hide rose_a1_7
show rose_a1_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice man_g0059
Seito "「まともっていうか……。\n
普段の副寮長って、超クールよ？」"

hide rose_b1_9
show rose_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice tak_g0051
Seito "「すっごく冷たくて、孤高の人っていう感じで……」"

hide rose_a1_5
show rose_a1_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_12")
voice man_g0060
Seito "「……いわゆる、クールビューティーみたいな？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_14")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_04_17")
T "{size=+20}（誰それ？？？）{/size} "

hide rose_b2_3
show rose_b2_4 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice tak_g0052
Seito "「や、本当なのよ？\n
そんな不審そうな顔しないでよ、嘘じゃないから……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

hide rose_a1_1
show rose_a1_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice man_g0061
Seito "「本当なんだってば！\n
普段の副寮長は、愚かな人間とは関わりたくないって感じの、冷血っぽい人なんだから！」"

hide rose_b2_4
show rose_b2_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice tak_g0053
Seito "「うんうん。\n
自分以外の人間は皆愚かで、汚らわしくて、近寄りたくもないし理解もしたくないし……、って感じの人よね」"

hide rose_a1_4
show rose_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_6")
voice man_g0062
Seito "「自ら滅ぼすほど積極的に関わりたくもないけれど、何か外的要因で人類が滅ぶのならばありがたい……、って感じの人よね」"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_5")
T "（えらく、具体的な……）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「……とっても嫌な人間ね。\n
それが、あなた達から見たペーター＝ホワイトなの？」"

hide rose_a2_1
show rose_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_13")
voice man_g0063
Seito "「嫌な人間だとか思えるほど、近くに寄せてもらえないわ。\n
私達なんて、認識されていないんじゃないかしら」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_11")
T "「大袈裟な……」"

hide rose_a2_5
show rose_a1_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice man_g0064
Seito "「真実よ。\n
嘘じゃなくて、本当のこと」"

hide rose_b2_3
show rose_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_05_11")
voice tak_g0054
Seito "「そんな副寮長が、あなたにだけは態度が全然違うから、びっくりしたのよ。\n
もしかしたら、あなたも本当は怖い人なんじゃないかと……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_18")
T "「ええ？\n
ないない、そんなことないわ」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_15")
T "「誰と知り合いで、誰と親しくしていようが、私は私よ」"

hide rose_a1_8
show rose_a1_2 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice man_g0065
Seito "「みたいね。\n
……よかったわ」"

hide rose_b1_2
show rose_b1_3 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_15")
voice tak_g0055
Seito "「本当にね。\n
これからも、仲良く話しましょうね」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_2")
T "「ええ、もちろんよ。\n
変な誤解で、遠慮なんかしないで」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そう答えると、二人は、ようやく安心したようだ。\n
手元にそっと紅茶のカップを呼び寄せた。"

play sound se_0174
with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "そうしてから二人顔を見合わせると、そこからが本題というように、ずいっと身を乗り出してくる。"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_02_15")
T "「な、なによ？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "用件を聞くより先に、嫌な予感と共に身構えてしまった。"

hide rose_a1_2
show rose_a2_3 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0066
Seito "「友人として遠慮が要らないみたいだから、聞かせてもらうわね……。\n
ずばり！副寮長との関係は！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_5")
T "「え、だから、幼馴染……」"

hide rose_b1_3
show rose_b1_2 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_5")
voice tak_g0056
Seito "「ただの幼馴染じゃないんでしょう！？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_6")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "二人とも、目が好奇心にきらきらしている。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_01_12")
T "（……警戒されたままにしておいたほうが、よかったかも）"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_04_17")
T "「幼馴染は幼馴染よ。\n
腐れ縁なの」"

hide rose_a2_3
show rose_a2_5 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_04_17")
voice man_g0067
Seito "「そうなの。\n
……で、本当のところは？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_01_2")
T "{size=+20}「幼馴染よ」{/size} "

hide rose_b1_2
show rose_b1_1 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_01_2")
voice tak_g0057
Seito "「えー。\n
本当にそれだけ～？」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_05_4")
T "「{size=+20}本当に本当に本当よ{/size}。\n
……私の言葉が、そんなに信じられない？」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "ここはわざとらしいぐらいに被害者っぽく、友人に信じてもらえない悲劇をアピールしてみせる。"

hide rose_a2_5
show rose_a2_4 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0068
Seito "「えっ！？\n
違うの、あなたが信じられないわけじゃなくて……っ」"

hide rose_a2_4
show rose_a2_1 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0069
Seito "「副寮長がああなっちゃうことが信じられないというか……」"

hide rose_b1_1
show rose_b1_9 at right
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice tak_g0058
Seito "「そうなの。\n
副寮長があんな顔で笑ったり、萎れたりするなんて、今まで誰も見たことがなかったから……」"

hide rose_a2_1
show rose_a2_8 at left
with dis
with dis
$ hi_mes()
$ show_mes("frame_par_chara")
$ face("ali_m_06_16")
voice man_g0070
Seito "「……というか、感情をあんなに表に出すことなんて、ねえ？\n
別人みたい……」"

with dis
$ hi_mes()
$ show_mes("frame_par_heroine")
$ face("ali_m_06_13")
T "「…………」"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私にとっては日常でも、彼女達にとっては「らしくない」、ペーター。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_02_16")
T "（私は、私の知らないペーターを知らないのよね）"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "当たり前といえば当たり前すぎ。\n
言語としても成立しない感想が脳裏に浮かんだ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "私が知っているのは、私と一緒にいるときのペーターだけ。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "他の人に対してどう接しているのかだとか、私が見ていないところでのペーターのことを、私はほとんど知らない。"

with dis
$ hi_mes()
$ show_mes("frame_par_togaki")
$ face("ali_m_06_16")
T "それでも、私の前にいるときのペーターが異常であることぐらいは分かる。\n
誰に対しても、ああいうふうになるわけではないだろう。"

with dis
$ hi_mes()
$ show_mes("frame_par_monologue")
$ face("ali_m_05_5")
T "（彼女達のよく知る……、ペーター＝ホワイトってどんな人なのかしら）"

hide rose_a2_8

hide rose_b1_9
##[chara2 PAY ATTENTION="false"]
with dis
$ hi_mes()

scene bg_par02_ct_ros_day with Dissolve(.8)

scene bg_par15_rg_ros_day
with stripe_l_medium

scene bg_map_eve
with stripe_l_medium

scene bg_map_nig with Dissolve(1.2)
##endmemory
$ routechara = "Peter"
jump gakuen_friend_check_castle
