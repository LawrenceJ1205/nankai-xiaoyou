# Paul Graham × Amjad Masad（Replit）：vibe coding 之后，是「自驾驶公司」

> **所属专辑**：[🤖 AI 前沿认知和方法论](03_xinzhi/AI前沿认知和方法论/README.md)（本辑第 34 篇）
>
> **出处**：YC 官方节目 **How to Build the Future**，主持人 **Paul Graham**（YC 联合创始人），嘉宾 **Amjad Masad**（Replit 联合创始人兼 CEO），2026-11-07 发布，44 分 14 秒，YouTube 编号 `Q78dJ0vkWe8`。本页依据 **YC Library 官方英文转录**（A 级一手），不是任何一份中文转述稿。
>
> **整理方式**：本篇为**资料型**——按对谈顺序重新组织，关键判断保留英文原话；中文小标题为本页所加。凡转述与原文不符处，一律以原文为准。
>
> **标注**：🔵 ＝ 英文原话（与 YC 官方转录逐条核过）　｜　🟡 ＝ 待核口径　｜　⚪ ＝ 本页归纳
>
> **提醒**：YC 官方转录自带标点，但仍是口语逐字稿，含重复、改口与转写噪声（人名、公司名错拼见编者注第 2 条）。引语按转录原样收录，本站只修正明显转写错拼并留痕，不增删词。

---

## 一句话

**「AI 越强，执行越便宜，判断越昂贵」的又一实证**：PG 亲手投出的这家「让人人写软件」的公司，正把 1000 万美元的企业软件项目换成 25 万美元的 Replit 用量——而 PG 本人在这场对谈里完成了对手艺时代的哀悼。

---

## 一、手艺人的哀悼：从 object code 到「2025 年底大家都信了」

开场第一句就是 Amjad 的判断：

> 🔵 “I think with AI, everyone will have to go through this period of denial and then depression and then eventually acceptance.”

PG 自陈他就是「否认」的那位。2024 年夏 Amjad 给他演示 agent 写码时，他的第一反应是：

> 🔵 “Don't look at the code. That's object code… The stuff I've spent decades making is just object code.”

他形容当时的 Amjad 像邦德反派（bond villain），并复述了自己的手艺人式编程观：

> 🔵 “I spend three years writing a thousand lines of code, and if I can get it down to nine hundred and eighty in the next month, so much the better.”

⚪ 注意这场哀悼的终点是共识而非分歧：PG 说**到 2025 年底，所有人都意识到 AI 会写全部代码**；Amjad 则说自己的哀悼期 2020 年就走完了——“I had the grief of the craft that I love is gone.”

---

## 二、为什么是 Replit 先做出来：看见用户在做「人肉 agent」

Vibe coding 不是天降灵感，是把用户已经 manual 做的事自动化。Amjad 讲了两层观察：

第一层，agent 出现前，Replit 的自动补全已经写了多少代码：

> 🔵 “I mean you you could probably say like fifty-sixty percent.”

第二层，他把用户请进办公室，亲眼看见「从没写过代码的人」怎么用 AI：

> 🔵 “So they would open ChatGPT in one window. They would open Replit in another window… they would like copy the code, put it into Replit. Replit would like produce some error. They would like copy the error, put it into ChatGPT… All we have to do is make an API… we have to automate the entire process.”

⚪ 这段是全篇最可抄的方法：**新产品的原型常常已经在用户手里以「人肉拼装」的形态跑着**，创业者要做的是把那条循环焊死。技术上真正新的是两件事——**跑到完成（run to completion）**而不是一轮对话，以及 **agent 自己开通数据库、Redis 等基础设施**。Amjad 还透露：模型公司当时主动来问「你们怎么让 Replit Agent 跑起来的」；且 **2024 年的 harness 比 today 复杂十倍**——模型越强，工程越薄，护城河越要往前挪。

还有一条组织层的巧合：早期为「多人协作」造的全套原语，让 agent 进来就像「另一个用户」：

> 🔵 “The agent is just another user on the same system… even you and the agents could work on the same project and it will just work.”

产品上线时约三成时间跑不通，但用户照样付钱，因为替代项是外包：

> 🔵 “Thirty percent of the time it would not work… you either like pay like a hundred thousand dollars to get an app done for an engineer somewhere, or you pay Replit like a thousand dollars.”

PG 在这里补了一句值得所有创业者抄的反转——外包公司存在的本身就是需求信号：“Arguably the whole existence of the outsourcing shops was evidence of a market there.”

---

## 三、1000 万的项目变成 25 万：从公司里的「野草」长进企业

企业采用不是自上而下的采购，而是从内部工具开始、由「公司里的 scrappy 人」带进去：

> 🔵 “It starts with internal stuff… we've actually scoped this project out and it would have been ten million dollars, we spent two hundred fifty thousand thousand dollars on Replit.”

> 🔵 “A lot of people who bring Replit into their organization will get promoted… because they'll are having great impact.”

PG 把企业焦虑接了过来：每家公司都在问「我们得用 AI，可谁真的在用？」——答案就是那个在用 Replit 做东西的人。Amjad 说，科技公司的冲击反而小（“they can fish for their own”），**真正会「搬起石头砸自己的脚」的是银行与制造业**。

---

## 四、token 配给 vs ROI：把「谁在产出价值」做成产品

对谈里最锋利的一段交锋，起于 PG 的一个两难：企业 IT 要管控，野心用户要绕开官僚——你替谁？Amjad 先给了一个具体反对对象：

> 🔵 “I disagree with like rationing tokens. So the way companies are approaching this as saying everyone gets $100 of tokens a month.”

> 🔵 Paul Graham：“What they should care about is ROI.”

> 🔵 “What we see from our customers is there's a power law of ROI inside companies. So one person could drive 100X… it used to be 10x, now it's 100x, it's a thousand X.”

⚪ 策略是先服从再发明：短期「给管理员要的管控」进门（PG 注解为 “That's how you get in”），长期把「哪里在发生好东西」做成可见的仪表，再带客户往前走。PG 随即把这桩生意拔高到最大公司们的根本病：**大公司之所以是大公司，就是因为算不清个人产出的价值**——谁把这个能力哪怕提升 10%，就是在修大公司的根本问题。

---

## 五、自驾驶公司：比 vibe coding 大一号的说法

Amjad 明确宣布退役旧词：

> 🔵 “I don't think we describe ourselves as vibe coding now… We wrote this blog post called the self-driving company… We think Replit is the platform for the transformation for self-driving companies.”

PG 立刻施压：这种大话谁都能说，IBM 的人听了也会点头——“You just have to make that be not vague.” Amjad 的回应是承认一切都会被抄，但要一直跑在前面：

> 🔵 “Everything we've kind of popularized ended up being copied… they're copying the old version of you… You're a movie and they're copying this frame from like six months ago.”

⚪ 加上他在本篇开头的判断——**「重造自己」过去是可选项，现在是必修课**（“It used to be optional… it's now mandatory almost”）——这一节的分量在于：AI 是商品化之力，所有能力都会贬值，唯一的问题是下一站在哪。

---

## 六、一万个 agent 上不了你的 MacBook

往后看的具体预言：企业从用一个 agent 到一万个，本地机器扛不住，工作必然搬云：

> 🔵 “You go from everyone using one agent to 10 agents to 100 agents to 10,000 agents at some point. You can't run 10,000 agents on your MacBook.”

> 🔵 Paul Graham：“It stuff has to live in the cloud.”

---

## 七、两个世界差两年：一小时翻转 80% 的焦虑

Amjad 讲了一个电信公司黑客松的实测：

> 🔵 “Pre using Replit, just for like an hour, like 80% were anxious and were worried about their jobs… And after they used Replit, it flipped. Like 80% were optimistic.”

PG 的收束很冷：硅谷之外的世界落后两年，而在这个行当里**落后两年等于永远落后**——两年前 vibe coding 还不存在。Amjad 补了企业侧的现状：多数银行还在用 2023 年水平的 ChatGPT，"barely connected to anything"。PG 则看到了一笔大账：**COBOL 终于要被重写了**。

面对这场变化的个人姿势，PG 给的是那句比喻：

> 🔵 “If you have this tidal wave approaching the beach, the safest place to be is surfing on it… Not standing on the beach holding onto a palm tree.”

---

## 八、怎么「活在未来」：默认世界是指数的

收尾问答是全篇的心法。PG 总结 Amjad 的过人之处只有一条：**默认假设是「指数世界」而不是静止世界**。Amjad 的自证：

> 🔵 “Once you truly understand the exponential… I can look at GPT 2 and extrapolate… I imagine chats, I imagine agents, I imagine personal assistant, all of that back in 2019 when I first saw GPT 2.”

> 🔵 “I do think I have an ability to kill the sacred cow… I'm fine with like throwing away things and starting over… They should read keep your identity small, one of your essays.”

被问到怎么教孩子面对 AI，他的答案只有一个词组：**flexibility、adaptability、终身学习**。PG 最后的注脚把人钉在时代上：为「一切每六个月变一次」的世界量身定做的人，就是那个默认剧变的人——“That's why Replit's doing so well.”

---

## 📡 编者注

1. **材料层级** ⚪：本页依 **YC Library 官方英文转录**整理（A 级），对应视频 2026-11-07 发布、44:14；YC 库页 `video_duration` 当时未回填，时长取自播客聚合源并与其官方章节表（末章 43:46 起）互证。中文侧暂未见授权中文全文，各转述稿未采作底本。
2. **转录噪声与更正** 📜：官方转录存在多处错拼，本页引用时按上下文更正并在此留痕：Raplet／Replo／Raptor 均指 **Replit**；“Mark Andreessen”＝Marc Andreessen；“Larry Allison”＝Larry Ellison；Amjad 口误自纠处（如 “Raplet”）不再逐条标。另转录在一段对答中错插说话人标签 “Aaron Ross Powell”（现场并无此人，该句实为 PG 所说）；PG 一句 “Robert proved that back in the 1980s” 指代不明，未采。
3. **数字口径** 🟡：50–60%（agent 前的代码占比）与三成失败为 Amjad 口头自述；1000 万→25 万美元为客户口径的转述（未经审计的原话引用）；10x／100x／1000x 为趋势性说法非测量值；80% 焦虑→80% 乐观为该公司自述的黑客松前后调查样本。引用时请带口径。
4. **「自驾驶公司」出处** ⚪：该词出自 Replit 官方博客文章名，Amjad 原话提到 “We wrote this blog post called the self-driving company”；本页标题取意于此，不是引语。
5. **PG 的投资原则原话** 🔵：“If you make it ten percent easier, you don't just get ten percent more people, you get twice as many.”——这是他早年投 Replit 的论据（对谈中提及 super linear relationship），属 PG 一贯论断。
6. **与前几篇的关系** ⚪：与第 29 篇 [Anton Osika](03_xinzhi/AI前沿认知和方法论/AntonOsika·别做软件做生意.md)（同为「人人可写软件」线，Lovable 侧）、第 16 篇 [Aaron Levie](03_xinzhi/AI前沿认知和方法论/AaronLevie·AI的价值在应用层.md)（token 补贴与应用层）、第 13 篇 [吴恩达](03_xinzhi/AI前沿认知和方法论/吴恩达·瓶颈转移到哪里.md)（每个环节都成瓶颈）、第 35 篇 [Chaubard](03_xinzhi/AI前沿认知和方法论/Chaubard·博士创业十个习惯.md)（同期 YC 新集）对读；创业一侧可接 [🚀 南开人创业](04_chuangye/README.md) 的「创业 ABC」。

> ← 返回 [🤖 AI 前沿认知和方法论 · 专辑首页](03_xinzhi/AI前沿认知和方法论/README.md)
