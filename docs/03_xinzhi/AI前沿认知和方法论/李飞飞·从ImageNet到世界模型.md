# 李飞飞：从 ImageNet 到世界模型

> **所属专辑**：[🤖 AI 前沿认知和方法论](03_xinzhi/AI前沿认知和方法论/README.md)（📚 新知小讲堂）
>
> **一手原件**：**Lenny's Podcast**《The Godmother of AI on jobs, robots & why world models are next》（主持 **Lenny Rachitsky**，**2025-11-16** 发布 · 约 **79 分钟**；官方视频 YouTube `Ctjiatnd6Xk`）。嘉宾 **李飞飞（Dr. Fei-Fei Li）**——斯坦福大学教授、**ImageNet** 发起人、前 Google Cloud 首席 AI 科学家、斯坦福**以人为本 AI 研究院（HAI）**联合创始人、**World Labs** 创始人。本页**依节目官方页要点 ＋ 官方章节时间轴 ＋ 可核对逐字稿引语**整理；引语一律给英文原话并附中译。
>
> **本页体例**：依一手原件整理——正文只留「**她说了什么**」。中文网络上流传的同题转述稿（新浪财经、网易等多个转载）的标题式概括与评议**不收录**，相关说明见文末编者注。
>
> **怎么读**：想知道「世界模型是什么」，看第六节；想知道「AI 从哪来」，看第二至第四节；想知道「她怎么看 AGI」，看第五节；想知道「Marble 能干什么」，看第八节。

---

## 一、这场访谈的坐标

| 项 | 内容 |
|---|---|
| **节目** | Lenny's Podcast（主持 **Lenny Rachitsky**） |
| **嘉宾** | **李飞飞（Dr. Fei-Fei Li）** |
| **嘉宾身份** | 斯坦福大学教授；ImageNet 发起人；前 Google Cloud 首席 AI 科学家；斯坦福人工智能实验室（SAIL）前主任；斯坦福**以人为本 AI 研究院（HAI）**联合创始人；**World Labs** 创始人（2024 年创立） |
| **发布** | **2025-11-16**　｜　**时长** 约 79 分钟 |
| **发布时点** | 恰在 **World Labs 发布其首个世界模型产品 Marble** 的同一时间 |
| **本页所据** | 节目官方页要点、官方章节时间轴、可核对的逐字稿引语（含时间码） |

这一集她讲了两件事：**AI 是怎么一路走到今天的**（她自己就在其中），以及**她认为下一步在哪里**——不是语言模型，而是世界模型与空间智能。

---

## 二、AI 的来路：从图灵之问到 AI 寒冬

她先给了自己的立场：她不是技术乌托邦主义者。

> "I'm not a utopian. So it's not like I think AI will have no impact on jobs or people. In fact, I'm a humanist. I believe that whatever AI does currently or in the future is up to us. It's up to the people."
>
> 「我不是乌托邦主义者，并不是说我认为 AI 不会影响就业和人。我是一个**人本主义者**：**AI 现在和将来做什么，取决于我们，取决于人。**」

她对技术的总体判断是「净正向、但双刃」：

> "I do believe technology is a net positive for humanity. If you look at the long course of civilization… humans just kept innovating ourselves and innovating our tools, and with that, we make lives better, we make work better, we build civilization, and I do believe AI is part of that. …I think every technology is a double-edged sword. And if we're not doing the right thing as a species, as a society, as communities, as individuals, we can screw this up as well."
>
> 「我相信技术对人类是净正向的……人类一直在创新自己、创新工具，于是一点点把生活变好、把工作变好、把文明建起来——我认为 AI 是其中的一部分。……但**每一项技术都是一把双刃剑**。如果我们作为物种、社会、社区、个人没有做对的事，我们**同样可以把这件事搞砸。**」

她引了一句自己在国会作证时被广泛引用的话：

> "There's nothing artificial about AI. It's inspired by people. It's created by people. And most importantly, it impacts people."
>
> 「**AI 里没有任何『人工』的东西**。它由人启发、由人创造，而最重要的是——它影响着人。」

然后是那段少被完整讲过的历史。她说第一代 AI 研究者不是她：第一代人上溯到 20 世纪 50、60 年代，而**图灵在 40 年代就提出了那个大胆的问题——「有没有会思考的机器」**；真正作为一门领域开始，是 1956 年的**达特茅斯会议**，会上 **John McCarthy** 造出了「人工智能」这个词。此后 50 至 80 年代是早期探索（逻辑系统、专家系统，也有神经网络的早期尝试）；到 80 年代末、90 年代、21 世纪初的约二十年，是**机器学习的开端**——计算机编程与统计学习的联姻，其核心认识是：**纯粹基于规则的程序，撑不起我们想象的那么多认知能力，必须让机器自己去学模式。**

她自己是在 **2000 年**进入这个领域的（在 Caltech 读博），正好赶在所谓「AI 寒冬」的中段：公众不太关注、经费也不多。

她还补了一个常被忽略的时间感：**不到十年前，「AI」还是个不敢碰的词。**

> "I was in a conversation in one of the early days… in the middle of 2015, middle of 2016, some tech companies avoid using the word AI because they were not sure if AI was a dirty word. And I remember… we're encouraging everybody to use the word AI because to me, that is one of the most audacious questions humanity has ever asked."
>
> 「2015 年中、2016 年中那阵，**有些科技公司刻意不用『AI』这个词**，因为他们不确定 AI 是不是一个『脏词』。而我记得……我们在鼓励所有人用这个词，因为在我看来，那是人类在科学与技术之路上**问过的最大胆的问题之一**。」

> "I think 2017-ish was the beginning of companies calling themselves AI companies."
>
> 「大概**2017 年前后**，才开始有公司管自己叫 AI 公司。」

---

## 三、ImageNet：从一个被忽视的原料开始

她选择从**视觉智能**切入 AI，理由很直接：人是深度视觉动物，而智能的很大一部分建立在视觉—知觉—空间理解之上，与语言是互补关系。

她与学生在早期锁定了一个**「北极星问题」：物体识别**。她给的理由是尺度——我们在世界上是**在「物体」这个层级**与世界打交道、推理和互动的，不是分子层级：你要端起一只茶壶，不会去想「这是一百片瓷」，而是把它当成一个物体。

但她撞上了一个绕不开的痛点：**这些模型没有数据可训练。**

> "There was one singular pain point: these models don't have data to be trained on. And as a field, we were so focusing on these models, but it dawned on me that human learning, as well as evolution, is actually a big data learning process."
>
> 「有一个单一的痛点：**这些模型没有数据可训练。**整个领域都在盯模型，但我意识到——**人类的学习、乃至进化，本身就是一个大数据的学习过程。**」

于是有了 ImageNet：从 2006、2007 年开始，她与学生去抓整个互联网上的物体图像，**精心整理了约 1500 万张图像，建了 22,000 个概念的分类体系**（借用了语言学家在 WordNet 上的工作），**开源给研究社区**，并办起一年一度的 ImageNet 挑战赛。她自己也说，今天回头看，「几个研究生加一个教授就能干成这件事」这个假设，**在当时就不算太疯，现在则完全算妄想。**

---

## 四、2012 与「三件套」

她圈出了那个转折点：**2012 年**。

> "2012 was the moment that many people think was the beginning of the deep learning or birth of modern AI, because a group of Toronto researchers led by Professor Geoffrey Hinton participated in ImageNet Challenge, used the ImageNet big data and two GPUs from NVIDIA, and created successfully the first neural network algorithm that can… make a huge progress towards solving the problem of object recognition."
>
> 「**2012 年**是很多人认为的深度学习开端、现代 AI 的诞生时刻：Hinton 教授带队的一组多伦多研究者参加 ImageNet 挑战赛，用了 ImageNet 的大数据，加上**两块 NVIDIA 的 GPU**，做出了第一个能大幅推进物体识别的神经网络算法。」

她把这件事抽象成一个可复用的配方：

> "The combination of the trio — big data, neural network, and GPU — was kind of the golden recipe for modern AI."
>
> 「**大数据、神经网络、GPU——这三者的组合，就是现代 AI 的黄金配方。**」

她强调，从 2012 到今天（包括 ChatGPT），**这个配方没变**：数据变成了互联网规模（主要是文本）、网络结构比 2012 复杂得多、GPU 从两块变成几十万块——但**三件套仍然是三件套**。

---

## 五、AGI 与还需要哪些突破

她对这个词的态度很直白。

> "I don't know if anyone has ever defined AGI. …For me, that's always the North Star of AI. And from that point of view, I don't know what's the difference between AI and AGI."
>
> 「我不知道有谁真正定义过 AGI。……对我来说，AI 一直就是那个北极星。从这个角度讲，**我不知道 AI 和 AGI 有什么区别。**」

> "I wonder if Alan Turing is around today and you ask him to contrast AI versus AGI, he might just shrug and say, 'Well, I asked the same question back in the 1940s.' …I feel AGI is more a marketing term than a scientific term."
>
> 「我想，如果图灵今天还在，你让他区分 AI 和 AGI，他大概会耸耸肩说：『我在 1940 年代问的就是同一个问题。』……**我觉得 AGI 更像一个营销术语，而不是科学术语。**」

她并不认为现有路线已经够用，给了两个具体的「做不到」：

- 拿一段办公室视频让模型**数椅子**——「一个幼儿或小学生能做的事」，今天的 AI 做不到；
- 给 AI 现代的天体观测数据，让它**推出 17 世纪那套运动方程**——做不到。她把这条与 Demis Hassabis 那个「让最前沿模型回到 20 世纪末、看它能不能重做爱因斯坦的突破」的提法并列，结论是：**还很远。**

她特别提醒：**AI 是最年轻的学科之一**，没有任何一门成熟的科学会说自己「创新完了」。

---

## 六、世界模型与空间智能

她解释了「世界模型」是什么——用的是「从提示到一个可探索的世界」这个说法：

> "A simple way to understand a world model is that this model can allow anyone to create any words in their mind's eye by prompting, whether it's an image or a sentence, and also be able to interact in this world, whether you're browsing and walking or picking objects up or changing things, as well as to reason within this world."
>
> 「理解世界模型的一个简单方式是：它让**任何人都能用提示词，把心里的那个世界造出来**——图也好、句子也好——并且能**在这个世界里互动**：走动、浏览、拿起物体、改变东西，还能**在这个世界里推理**。」

> "World model is a foundation that you can use to reason, to interact, and to create worlds."
>
> 「世界模型是一个底座，你可以用它来**推理、互动、创造世界**。」

她给「空间智能」下了自己的定义：

> "Spatial intelligence to me is the ability to create, reason, interact, make sense of deeply spatial world, whether it's 2D or 3D or 4D, including dynamics and all that."
>
> 「对我来说，**空间智能**是创造、推理、互动、并**理解一个深度空间化的世界**的能力——不管是 2D、3D 还是 4D，包括动态。」

她为何认为这是语言之外的另一半：她举了**混乱的应急救援现场**——火灾、车祸、自然灾害里，人怎么组织起来救人、控火、防止次生灾难，很大一部分是**移动、对物体与情境的即时理解**；语言是其中一部分，但语言本身灭不了火。

她还给了科学史上的一例：**DNA 双螺旋**的发现里，关键一步是 Rosalind Franklin 拍的那张 X 光衍射照片——一张平面的 2D 图像；而 Watson 和 Crick 靠的是**在三维空间里的推理**，才从中推出了那个不可能是二维的双螺旋结构。**「你不可能靠二维思考推出那个结构。」**

她区分了世界模型与「视频生成」：世界模型要的不是一段看过就走的视频，而是**有 3D 结构的、可导航、可互动、可推理的世界**。（她也提到 World Labs 在几周前放出过单张 H100 上的实时视频生成演示，但强调那是技术的一部分，不是 Marble 的产品形态。）

---

## 七、苦涩的教训：为什么它在机器人上不够用

主持人转述 Ben Horowitz 的提问：**为什么「苦涩的教训」单靠它自己，在机器人上大概行不通？**

她先讲了苦涩的教训是什么——Richard Sutton 那篇论文的核心是：从算法发展史看，**简单的模型配上海量数据，最终总会赢过复杂但数据少的模型。**

> "This paper came years after ImageNet. That to me was not bitter. It was a sweet lesson. That's why I built ImageNet."
>
> 「那篇论文是 ImageNet 之后好几年才出的。**对我来说它不苦，是甜的**——我造 ImageNet，就是因为我相信大数据会起这个作用。」

那为什么它在机器人上不够？她给了三层理由：

**一是数据更难拿。**语言模型的设置是「完美的」——训练数据是词、输出也是词，目标函数和数据结构完全对齐；而机器人要的是**三维世界里的动作**，可它的训练数据里恰恰**缺动作**。所以得靠遥操作数据、合成数据来补。她说自己「非常羡慕搞语言的同事」。

**二是机器人是物理系统。**

> "Robots are closer to self-driving cars than a large language model."
>
> 「**机器人更接近自动驾驶汽车，而不是大语言模型。**」

不光要有「脑子」，还要有身体、要落地场景。她以自动驾驶为参照：从 2005、2006 年 Sebastian Thrun 带队赢下 DARPA 挑战赛，到今天街上跑的 Waymo，**这条路走了二十年，而且还没走完**——况且自动驾驶还是「简单版机器人」：只是在二维路面上跑的金属盒子，目标是**不碰任何东西**；而机器人是**三维世界里要碰东西**的。

**三是这门学问还很年轻**，苦涩的教训在机器人上「**还有待检验**」。

访谈里她自己插了一段感慨——她说人脑大约只耗 **20 瓦**：

> "We operate on about 20 watts. That's dimmer than any light bulb in the room I'm in right now. And yet we can do so much. …The more I work in AI, the more I respect humans."
>
> 「我们只靠大约 **20 瓦**运行——比我现在这屋里任何一盏灯泡都暗。可我们能做到这么多。……**我在 AI 里做得越多，就越尊敬人。**」

---

## 八、Marble：从提示到可探索的世界

**Marble** 是 World Labs 推出的第一批产品之一，就在这期播客上线的同时发布。

> "We've spent a year and plus building the world's first generative model that can output genuinely 3D worlds. That's a very, very hard problem."
>
> 「我们花了一年多，做出了**世界上第一个能输出真正 3D 世界的生成模型**——这是个非常非常难的问题。」

> "We call it prompt to worlds."
>
> 「我们管它叫**『从提示到世界』**。」

用户就那一处她觉得最有趣的反馈：进入世界前会先看到**一个个点的骨架**，再渲染出纹理——那是工程师们试了很多版本后特意保留的**可视化引导**，不是模型的一部分，却成了用户最喜欢的地方之一。

它已经在用的场景（均为节目里的说法）：

| 场景 | 说法 |
|---|---|
| **虚拟制片（电影）** | 与索尼合作、由一家虚拟制作公司用 Marble 的场景拍摄了发布视频；对方说这**把制作时间缩短了约 40 倍** |
| **机器人合成数据** | 已有研究者找上门，想用 Marble 造多样化的训练环境 |
| **心理研究** | 一个心理学家团队来联系，想用它做研究——研究病人对不同沉浸式场景（杂乱／整洁等）的脑反应 |
| **游戏 / 设计 / 创意** | 从提示词直接生成可探索的世界；也支持把镜头轨迹**导出成视频** |

---

## 九、创办 World Labs 的十八个月

World Labs 的四位联合创始人（她自己、Justin Johnson、Christoph Lassner、Ben Mildenhall）都出自 AI、图形学、计算机视觉的研究一线。团队**约 30 人，以研究者和研究工程师为主**，另配设计与产品——她的说法是**要做一家扎在空间智能深科技里、但认真做产品的公司。**

公司刚成立约 18 个月。问她「有什么想对 18 个月前的自己说」，她的回答不是技术判断，而是**竞争强度**：

> "I'm surprised and it puts me into paranoia sometimes that how intensely competitive AI landscape is — from the model, the technology itself, as well as talents."
>
> 「我偶尔会因此陷入警觉：**这个 AI 竞争的激烈程度**——从模型、技术本身，到人才——都超出我的预期。」

她被问到一个更个人化的问题：为什么她总能待在「未来发生的地方」（Princeton → Stanford → SAIL 首位女性主任 → Google Cloud → World Labs）。她的答案是**「智力上不害怕」**：

> "I'm an intellectually very fearless person. …When I hire young people, I look for that."
>
> 「我是一个**在智力上非常不害怕的人**。……我招年轻人时，也在找这个特质。」

> "I don't overthink of all possible things that can go wrong, because that's too many."
>
> 「我不会去把所有可能出错的环节都想一遍——**那种东西太多了。**」

---

## 十、以人为本的 AI：每个人在 AI 里的位置

**HAI（斯坦福以人为本 AI 研究院）**是她 2018 年联合创办的。她那年刚从 Google 的休假回来，本可以留在工业界，但她判断「AI 会是一项文明级技术」，于是在《纽约时报》撰文，主张给 AI 的开发与应用立一个**以人为中心**的框架，并在斯坦福把它落成研究、教育、政策与生态四块工作。六七年后，它已是全球最大的以人为本 AI 研究机构，横跨斯坦福八大学院。

节目最后，她回答了那个「她在世界各地都被问」的问题——**如果我是一个音乐家、一个中学老师、一个护士、一个会计、一个农民，我在 AI 里还有位置吗？**

> "AI is about people. And when people ask me that question, it's a resounding yes. Everybody has a role in AI."
>
> 「**AI 是关于人的。**当人们问我这个问题，答案是**一个响亮的『有』**——**每个人在 AI 里都有位置。**」

> "No technology should take away human dignity. And the human dignity and agency should be at the heart of the development, the deployment, as well as the governance of every technology."
>
> 「**任何技术都不应剥夺人的尊严。**人的尊严与能动性，应当放在每一项技术的**开发、部署与治理**的核心位置。」

她给不同人的答案具体而不同：**如果你是年轻艺术家、你的热情是讲故事，就让 AI 当工具**——「你怎么讲故事」才是独一无二的；**如果你是快退休的农民，AI 依然与你有关，因为你是一个公民**，你有权对 AI 怎么用发出声音；**如果你是护士，AI 最该帮的就是你们**——智能摄像头带来更多信息、机器人来搭手，因为这个行业**过劳、缺人**，而社会在变老。

---

## 🧭 章节时间轴（依节目官方章节）

| 起点 | 章节 | 本页对应 |
|---|---|---|
| 00:00 | 开场：AI 与它对人的影响 | 二 |
| 05:31 | AI 的演进 | 二 |
| 09:37 | ImageNet 的诞生 | 三 |
| 17:25 | 深度学习的崛起 | 四 |
| 23:53 | AI 的未来与 AGI | 五 |
| 29:51 | 世界模型导论 | 六 |
| 40:45 | AI 与机器人中的「苦涩的教训」 | 七 |
| 48:02 | 发布 Marble：一个生成式世界模型 | 八 |
| 51:00 | Marble 的应用与用例 | 八 |
| 01:01:01 | 创始人的历程与心得 | 九 |
| 01:10:05 | 斯坦福的以人为本 AI | 十 |
| 01:14:24 | AI 在各行各业里的角色 | 十 |
| 01:18:16 | 收尾 |

---

## 📎 引语与出处索引

页内英文引语集中列此，便于核对（时间码取自该集逐字稿）：

| # | 英文原话 | 位置 |
|---|---|---|
| 1 | "I'm not a utopian… I'm a humanist. I believe that whatever AI does currently or in the future is up to us. It's up to the people." | 06:43 |
| 2 | "I do believe technology is a net positive for humanity… I think every technology is a double-edged sword." | 06:43 |
| 3 | "There's nothing artificial about AI. It's inspired by people. It's created by people. And most importantly, it impacts people." | 07:44 |
| 4 | "In the middle of 2015, middle of 2016, some tech companies avoid using the word AI because they were not sure if AI was a dirty word." | 21:56 |
| 5 | "2017-ish was the beginning of companies calling themselves AI companies." | 22:03 |
| 6 | "There was one singular pain point: these models don't have data to be trained on… human learning, as well as evolution, is actually a big data learning process." | 16:30 |
| 7 | "The combination of the trio — big data, neural network, and GPU — was kind of the golden recipe for modern AI." | 19:16 |
| 8 | "I don't know if anyone has ever defined AGI… I feel AGI is more a marketing term than a scientific term." | 25:13 |
| 9 | "A simple way to understand a world model is that this model can allow anyone to create any words in their mind's eye by prompting… as well as to reason within this world." | 35:07 |
| 10 | "Spatial intelligence to me is the ability to create, reason, interact, make sense of deeply spatial world, whether it's 2D or 3D or 4D, including dynamics and all that." | 59:11 |
| 11 | "This paper came years after ImageNet. That to me was not bitter. It was a sweet lesson. That's why I built ImageNet." | 41:54 |
| 12 | "Robots are closer to self-driving cars than a large language model." | 45:28 |
| 13 | "We operate on about 20 watts… The more I work in AI, the more I respect humans." | 47:49 |
| 14 | "We've spent a year and plus building the world's first generative model that can output genuinely 3D worlds." | 49:08 |
| 15 | "We call it prompt to worlds." | 50:54 |
| 16 | "It has cut our production time by 40x."（转述虚拟制作合作方之语） | 53:28 |
| 17 | "We have a team of 30-ish people now, and we are predominantly researchers and research engineers." | 01:01:12 |
| 18 | "I'm an intellectually very fearless person… I don't overthink of all possible things that can go wrong, because that's too many." | 01:05:31 |
| 19 | "AI is about people… Everybody has a role in AI." | 01:15:28 |
| 20 | "No technology should take away human dignity. And the human dignity and agency should be at the heart of the development, the deployment, as well as the governance of every technology." | 01:16:07 |

**出处层级**：① 节目官方页（本集要点、官方章节时间轴、嘉宾与出处信息）＝ **节目方一手**；② 上表引语＝该集逐字稿原话（YouTube 官方视频 `Ctjiatnd6Xk`；逐字经公开转录页转引，本页已按上下文校正语音转写噪声）；③ 正文中未加引号的叙述 ＝ 对上述内容的整理。

---

## ⚠️ 编者注

1. **本页的出处与日期，请照本文写。** 一手原件是 **Lenny's Podcast，2025-11-16 发布**。中文互联网上（新浪财经 2026-05-22、网易等同题转载，来源标注「图灵人工智能」）把它当作「最新访谈」流传，实为 **2025 年 11 月**的一集——**引用请带日期，别写成 2026 年。**

2. **本页与第 1 篇的关系。** 第 1 篇《[AI 时代生存指南](03_xinzhi/AI前沿认知和方法论/AI_shidai_shengcun.md)》里，李飞飞只是一段短评（「AI 是创造力的放大镜」「招聘时更看重候选人多快用 AI 强化自我」）。本页是**同一人的完整深度访谈**；那两句短评在**本集原件里找不到逐字对应**，属那份汇编稿的概括，引用时请勿归到本集。

3. **标题里的「语言模型只是开始，世界模型才是下一个前沿」是中文转述稿的概括**，不是她的原话。她在本集里的说法是「**beyond language**」（语言之外还有一大块可推进）与「world models and spatial intelligence is a key missing piece of embodied AI」，方向一致，但请按原话引。

4. **语音转写噪声（已按公开名称校正）**：本集逐字稿为自动转录，人名机构名多有错——`JAT-GPT`＝ChatGPT、`WordLab`＝World Labs、`stever`＝Stanford、`Marvel`＝Marble、`Alan Turi`＝Alan Turing、`Jeff Hinton`＝Geoffrey Hinton、`Percy Leung`＝Percy Liang、`Chris Batting`＝Christopher Manning、`John H. Mendy`＝John Etchemendy、`Professor James Landy`＝James Landay、`Cinch`＝Sinch（赞助商）。凡此类，本页按公开名称校正，不臆补。

5. **数字口径**：① ImageNet「约 1500 万张图像、22,000 个概念、2006–2007 年启动、2012 年 AlexNet 用两块 GPU 夺冠」为**可核对的公开史实**；② 「制作时间缩短 40 倍」出自**虚拟制作合作方的转述**（她与索尼合作拍了 Marble 发布视频），**不是可审计指标**；③ 「20 瓦」「半亿年的进化」是修辞，不是测量值；④ World Labs「约 30 人」「成立约 18 个月」为节目当时（2025-11）口径。

6. **两处容易读错的归属**：① 「AGI 是营销术语」是她的**原话**（`more a marketing term than a scientific term`），可直接引；② 关于「ImageNet 启发了 Scale AI」——她说的是 Alexandr Wang 早年给她发信讲过这件事，本页只在正文一笔带过，未展开。

7. **与隔壁几页对照着读**：[Dario](03_xinzhi/AI前沿认知和方法论/Dario·AI重写工作的三层价值迁移.md) 讲的是**价值层**（AI 怎么重写工作）、[Linda Hill](03_xinzhi/AI前沿认知和方法论/LindaHill·权力的迁移与AI时代的领导力.md) 讲**组织层**、本页讲的是**技术路线层**——三者合起来是「AI 往哪走」的三种问法。

---

> ← 返回 [🤖 AI 前沿认知和方法论](03_xinzhi/AI前沿认知和方法论/README.md)　｜　相关：[AI 时代生存指南](03_xinzhi/AI前沿认知和方法论/AI_shidai_shengcun.md)（第 1 篇 · 五位领袖的短评合集）　[Dario：AI 重写工作的三层价值迁移](03_xinzhi/AI前沿认知和方法论/Dario·AI重写工作的三层价值迁移.md)（价值层）　[Linda Hill：权力的迁移](03_xinzhi/AI前沿认知和方法论/LindaHill·权力的迁移与AI时代的领导力.md)（组织层）
