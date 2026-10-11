# Kavak 内部怎么用 AI：一家由 Agent 运营的公司

> **所属专辑**：[🧭 AI Agent 使用最佳实践](03_xinzhi/AI_Agent使用最佳实践/README.md)（📚 新知小讲堂）
>
> **一手原件**：**a16z Podcast**《The Self-Improving Company ｜ Kavak's AI Playbook》（**2026-08-10** 发布 · 约 **37 分钟**），主持人 **Angela Strange** 与 **Gabriel Vasquez**（a16z 合伙人），嘉宾 **Alejandro Maza Ayala**（Kavak **首席产品与 AI 官**，节目里称 Ale Maza）。本页**依官方节目页要点 ＋ 14 段章节时间轴 ＋ 可核对逐字稿引语**整理；引语一律给英文原话并附中译。
>
> **本页体例**：依一手原件整理——正文只留「**Kavak 说了什么、做了什么**」。底本（微信公众号「猫不白」的一篇转述稿）的框架、人名转写与评议**不收录**，相关对勘见文末编者注。
>
> **怎么读**：想知道「他们到底改了什么」，看第二节；想知道「一个客户一个 Agent」长什么样，看第三节；想知道「评估为什么被当成刹车」，看第五节；想知道「他们为什么把两年的系统推倒」，看第七节。

---

## 一、这场访谈的坐标

| 项 | 内容 |
|---|---|
| **节目** | a16z Podcast《The Self-Improving Company ｜ Kavak's AI Playbook》（主持 **Angela Strange**、**Gabriel Vasquez**，均为 a16z 合伙人） |
| **嘉宾** | **Alejandro Maza Ayala**（节目里称 Ale Maza）——Kavak **首席产品与 AI 官**（Chief Product & AI Officer） |
| **发布** | 2026-08-10　｜　**时长** 约 37 分钟 |
| **本页所据** | 节目官方页要点、14 段章节时间轴、若干可核对的逐字稿引语 |

**Kavak** 是拉美最大的二手车交易平台，墨西哥起家，做的是**买车、翻新、卖车、做车贷**。

它有一个别家没有的条件：**拉美没有现成的基础设施**。用 Alejandro 的话说——

> "We also had to build a fintech and a logistics company and the Carfax… basically all the infrastructure for this to work didn't exist in LatAm. So we had to build everything vertically."
>
> 「我们还得自己造一家金融科技公司、一家物流公司，还有自己的 Carfax 式检测体系……因为让这件事成立的全部基础设施，在拉美根本不存在。所以我们只能把一切都垂直自建。」

因为这些能力都得自己造，**没有一个环节外包**。这一集访谈讲的，就是这家公司怎么把自己的组织结构围绕 Agent 重做了一遍。

---

## 二、三个决定：围绕 Agent 重建公司

在这一段里，Kavak 的立场是「**仅仅给员工发 AI 工具是不够的**」，于是**把公司的系统、团队与客户体验围绕 Agent 重新设计了一遍**。

Alejandro 用的词是「赌」：

> "So we bet the company in transforming to a company run by agents."
>
> 「我们把整家公司押了上去，就为了转成一家**由 Agent 运营的公司**。」

他拿来问自己的，不是「我们哪里能加 AI」，而是一个反向问题：

> "The question we ask ourselves is: how would we build Kavak in 2035, with Fable 10 or GPT 10 level intelligence?"
>
> 「我们问自己的是：**假如手上有 2035 年那种智力水平的模型，我们会怎么重新造一遍 Kavak？**」

**第一个决定：围绕 Agent 重建公司。** 他点名批评了最常见的那条路：

> "The first instinct is, okay, let's adopt AI. And you basically leave your structure as it is and just give ChatGPT or Claude to your team. And then there's no efficiencies. Your customers have the same problems and nothing happens."
>
> 「第一反应往往是：好，我们上 AI 吧——然后组织结构原封不动，只是给团队发 ChatGPT 或者 Claude。结果**没有效率提升，客户的问题还是那些问题，什么都没发生**。」

具体动作是：**把大部分 API 与系统重写一遍**，让 Agent 能真的动手干活。

**第二个决定：把 Agent 放到真实客户面前去教。**

> "The only way to really make them work is if you teach them. How do you teach them? You put them out in the open, you put them in front of customers, you get that data, you get those evals. And then you train your agents."
>
> 「要把它们真正跑起来，唯一的办法是**教它们**。怎么教？把它们放到开放环境里、放到客户面前，拿到数据、拿到评测，然后训练你的 Agent。」

**第三个决定：换一套衡量体系。** Kavak 原本是一家**交易型**公司——盯的是买了几辆车、卖了几辆车、要买多少刹车片。转型后它成了**关系型**公司：数据库里有一千万客户，每人配一个 Agent，**唯一的考核目标是这个客户的终身价值**。

| 三个决定 | 他原话里的说法 |
|---|---|
| 重建公司，而非加装工具 | 不改结构只发 ChatGPT／Claude ＝ 什么都不会发生 |
| 造出「超过最好员工」的 Agent | 把 Agent 放到客户面前、拿评测、再训练 |
| 从交易型指标换成关系型指标 | 从「卖了几辆车」换到「这个客户的终身价值」 |

**这条路不是一次做成的**：主持人在节目里直接说，Kavak 在转型中「**不得不大幅收缩**」，而且「**第一年根本没跑通**」。Alejandro 没有否认，也没有给数字——他只是说，黑客松、赞助用例、自下而上的采纳，这些替代方案「**都行不通**」。

---

## 三、一个客户一个 Agent：每天 10 万到 20 万个

大多数公司做 Agent 是**一个任务一个 Agent**——一个客服 Agent、一个销售 Agent、一个财务 Agent。Kavak 把这个关系倒过来了：**一个客户一个 Agent**。

> "When a customer comes in right now, an agent will get spawned specifically for this customer, with its own virtual machine."
>
> 「现在一个客户进来，就会**为他单独生成一个 Agent，配一台自己的虚拟机**。」

> "It will remember years of interaction of these customers with Kavak… Come up with a strategy and set a long-term goal to maximize the lifetime value of this customer, and do whatever it takes to make the customer happy and convert them into all our different products across time."
>
> 「它会记得这些客户与 Kavak **几年间的全部互动**……然后自己拟一套策略、设一个长期目标：**最大化这个客户的终身价值**，并且不择手段地让客户满意、把他带进我们的各种产品线。」

它甚至不是一次任务做完就结束。这些 Agent 有自己的作息——**睡下、设个闹钟，等下一次行动**；有的只跑三分钟，有的跑几个小时，有的能跑上三天。每天这样被实例化的 Agent，**在十万到二十万个之间**。

> "We realized we could bet that long-running agents with hard goals, not just workflows, could maximize our customers' satisfaction — and obviously their lifetime value."
>
> 「我们认定了一件事：**跑得久、带硬目标的 Agent——而不只是工作流——才能最大化客户满意度与终身价值。**」

| | 一个任务一个 Agent（常见做法） | 一个客户一个 Agent（Kavak 的做法） |
|---|---|---|
| 生命周期 | 任务结束即结束 | 长期存活，睡下再醒，跨年 |
| 记忆 | 单次会话 | 客户的全部历史 |
| 目标 | 完成这一步 | 最大化这个客户的终身价值 |
| 规模 | 按任务数 | 每天 10 万–20 万个 |

---

## 四、超人类的 Agent

Kavak 一开始就没打算做一个「够用」的 Agent：

> "We could build superhuman agents. This means that by every dimension that matters, our agents would outperform the best human we had ever hired."
>
> 「我们可以造出**超人类的 Agent**——意思是，在**每一个我们在意的维度上，Agent 的表现都超过我们雇过的最好的那个人**。」

他给的对照是：再好的销售也会累、会忘、会情绪不好，也记不住几百万个客户，更不可能同时是汽车专家、贷款专家、保险专家、金融专家；而 Agent 可以同时装着这些知识，并且不疲惫。

Kavak 公开的几组数字（均为自述，见编者注）：

| 指标 | 数字 |
|---|---|
| 由 Agent 完成的客户互动 | **96％** |
| 由 Agent 完成的交易 | **95％** |
| 每天被实例化的 Agent | **10 万–20 万个**（每个自带虚拟机） |
| 销售 Agent 对最好人工团队的转化优势 | 上线时高约 **50％**，录制时约 **2.1 倍** |
| NPS 与客户满意度 | **变为原来的三倍** |
| 墨西哥的汽车贷款审批 | 过去两个多月 → **不到 3 分钟** |
| 数据库里的客户 | **约 1000 万**（每人一个 Agent） |

而他们做的不是客服，是**销售**——而且是**把 15 个专家团队装进一个 Agent**：

> "We never built customer support or customer service agents. We built sales agents… the way Kavak did it back in 2020, 2021, you needed to be extremely good at 15 different things and have 15 different experts in 15 different teams… The first thing we did was, can we get an agent to be better than the expert in each of these things? And then put it together — a mega expert."

他说，在拉美卖一辆车极难：客户要在两万个 SKU 里挑，还要选融资、走完贷款流程、配保险，多半还要把旧车折价卖回给公司。所以他们的第一步是——**先让 Agent 在每一件事上都超过那个领域的专家，再把它们合成一个「超级专家」，然后把它放到客户面前**。

---

## 五、Evals：和造 Agent 花一样多的投入

Kavak 在评测上的投入，几乎和做 Agent 本身一样多：

> "We spend about the same amount of engineering time, tokens, and money on building evals as on building agents. We measure business results first — like whether the customer converted — not superficial KPIs like call minutes. This approach lets us move fast because we have the right brakes."
>
> 「我们在**评测上投入的工程时间、Token 与钱，和造 Agent 差不多**。我们先量业务结果——比如客户到底转化了没有——而不是像通话时长那种漂亮的表面指标。这套做法让我们能跑得快，**因为我们有对的刹车**。」

他说的「业务结果」，指的是**车卖出去没有、贷款批下来没有、客户回来没有、利润提高没有**——而不是通话时长那类表面指标。

---

## 六、Agent 撞墙时，调用一个 API

常见的人在环（human in the loop）设计是「**AI 不行了就转人工**」；Kavak 的说法是，Agent 一旦把问题扔给人，它就丢掉了这个任务，学习闭环也断了。所以他们的做法相反——**Agent 遇到解决不了的问题不退出，而是调一个 API 求助，而 API 另一头接的，可能是一个人**。

> "If an agent hits a wall, it calls an API for help, and a human assists. This closes the loop and generates data to train the agent."
>
> 「如果 Agent 撞了墙，它会调用一个 API 求助，然后由人来协助。**这样闭环才闭合，也才产生出可以训练 Agent 的数据。**」

在这套设计里，Agent 仍然握着这个任务，人只是它调用的一种能力。而把这套关系画成组织图，得到的说法正好相反：

> "If you map this out in an org chart, it's really human teams that have an agent."
>
> 「如果你把它画成组织图，其实是**人类团队配了一个 Agent**。」

在物理世界里，人暂时还不可替代——墨西哥约有 **800 名技师**，他们身边配了一个**副手 Agent**（语音转写作 El Mic／El Mike，见编者注），负责指导与校核，**保修索赔因此下降了约 26％**（有 20–26％ 一说）。

于是团队里的工作，基本就三类：

> "If you look at a team, you'll have engineering, AI, operations, like everything — and they're either **building the agents**, **working for the agents**, or **being in the physical world in front of the customer**."
>
> 「看一个团队，里面会有工程、AI、运营……他们要么**在造 Agent**，要么**在为 Agent 工作**，要么**在物理世界里面对客户**。」

| | 过去的说法 | Kavak 节目里的说法 |
|---|---|---|
| 谁调用谁 | 人调用 AI（人对 AI 下指令） | **有时 AI 是人的工具，有时人是 AI 的工具** |
| 谁拥有任务 | 人拥有，AI 辅助 | **Agent 拥有任务，人是它调用的能力** |
| 谁向谁汇报 | 明确定义 | 有团队负责人**同时向 Agent 汇报**，团队结构很平、很资深 |

---

## 七、推倒重来：把两年的系统删掉

Kavak 还做了一件事：**把自己已经跑通的系统删掉重来**。

> "We initially built multi-agent systems that could perform whole functions… We had **tens of thousands** of these agents running the business by December. But when **Opus 4.5** came out, I realized **the graph and multi-agent lattice work would constrain the new level of intelligence**. So we **destroyed everything we had built for two years** and started over with a virtual machine harness, where each agent has access to memory, evals, and a CLI to access every tool and API in the company."
>
> 「我们最初造的是多 Agent 系统……到 12 月已经**有几万个**这样的 Agent 在跑业务。但 **Opus 4.5** 出来之后，我意识到**那套图结构与多 Agent 网格，反而会限制新的智力水平**。所以我们**把两年里造的东西全推倒了**，改用一台虚拟机作为骨架——每个 Agent 都能访问记忆、评测，以及一个能调起全公司工具与 API 的命令行。」

他自己的说法是：

> "We decided to **destroy everything we had been building for two years** that was working — that brought us to profitability, that brought us amazing growth — and start over with a harness we thought would be robust and scalable."
>
> 「我们决定**推倒两年里建起来的一切**——它是有效的，它把我们带到了盈利，带来了惊人的增长——然后用一个我们认为更稳、更能扩展的骨架从头再来。」

这套新骨架是：**给 Agent 一台虚拟机，连同记忆、评测与全公司的工具、API，再给它一个长期目标，让它自己想办法。**

---

## 八、从一支 Agent 的 CEO，到一所 Jedi Academy

节目里谈到「AI 能不能干领导层的活」，Kavak 的做法是：**把一个城市交给一个 Agent 当 CEO。**

> "We carved out a city in Mexico — Cuernavaca — and we put an agent in one of our harnesses as a CEO… It's only been running for six weeks now. The goal of the first month was to **double the profits**. It didn't reach it, but it was **1.5x — like 50％ more profits** — just by managing the city… People were like, that was the last job AI was supposed to take. And no, it isn't really."
>
> 「我们划出墨西哥的一座城市——库埃纳瓦卡——把我们的一个 Agent 放进骨架里当 CEO……到现在只跑了六周。**首月的目标是把利润翻倍，它没做到，但做到了 1.5 倍，也就是多出 50％ 的利润**——而且还只是在管这一座城市……大家原以为**CEO 是 AI 最后才会接的活**，结果并不是。」

它是怎么管的？**盯每一个数字、每一个客户，做出最准的预测，然后每天把一线的执行计划逐条压下去**——给库埃纳瓦卡的所有现场员工发当天的工作安排，晚上再让他们用语音汇报进度。结果是：客户满意度上去了，库存周转变好了，融资渗透率也变好了。

人这一侧，Kavak 开了一所自己的学校：

> "We launched a program inside Kavak that's called the **Jedi Academy**. From the CEO to AI engineers to mechanics, we train everyone. And after six weeks, they launch state-of-the-art agents to production."
>
> 「我们在 Kavak 内部开了一个项目，叫 **Jedi Academy**。从 CEO 到 AI 工程师再到技师，**所有人都要训**。六周之后，他们能把最先进的 Agent 发到生产环境。」

代价是：要么学会，要么离开。

> "You have the choice to train and get the skills to perform in this new reality… Or maybe leave Kavak if this is not for you. But this is the way we're going."
>
> 「你有两个选择：学会它，在新现实里干活；或者，如果这不适合你，离开 Kavak。**但这就是我们要走的路。**」

训练后的组织形态也变了样——**团队很平、成员很资深、授权极大**；而在 2020 或 2022 年，没有人会造 Agent，更没有人会听 Agent 的指挥。

---

## 九、Token 分三档

给大机构领导者的建议，他给了两条：一条管方向，一条管钱。

> "Two things. First, it has to be **top-down**… Leaders have to have a very clear plan on what to build… I've seen so many companies that's just like, we're doing a **hackathon**, people are coming up with use cases, we're sponsoring some of these use cases — **that doesn't work**."
>
> 「两件事。第一，**必须自上而下**……领导者要对『建什么』有非常清楚的计划……我见过太多公司就是：**搞个黑客松**，大家提用例，我们赞助几个——**这没用**。」

> "An army doesn't really work if everyone comes up with ideas on the strategy and tactics and goes to the battlefield and does whatever they want."
>
> 「军队是不能这样打的：每个人都在自己发明战略战术，上了战场各打各的。」

第二条是 **把 Token 当成一笔要算 ROI 的钱**——他把它分成三档：

| 档位 | 是什么 | 能不能算价值 |
|---|---|---|
| **Tier 3（最值钱）** | 跑组织真实工作的 Agent | 每一枚 Token 的 ROI **可以直接算出来** |
| **Tier 2** | 价值可以间接衡量的用途（例如进到代码库里的产出） | **间接可衡量**，可以据此推到生产 |
| **Tier 1** | 大多数公司停在这一档：员工各自用 ChatGPT、Claude Code 之类 | **不知道价值** |

> "It's not just about adoption — it's really about having a very clear vision, and then **measuring that each token you spend is bringing you those benefits**, and just iterate, iterate, iterate."
>
> 「重点不只是采纳率，而是要有非常清楚的愿景，然后**去量你花的每一枚 Token 到底带回来什么**，接着就是不停迭代、迭代、迭代。」

---

## 十、创造性破坏：那台发电机与福特那座工厂

访谈最后谈的是经济学——他提到 **熊彼特（Joseph Schumpeter）的创造性破坏**：

> "There's this concept in economics about **creative destruction** from Joseph Schumpeter… It's hard to adopt AI deeply. It's really hard for a CEO today — especially of a large company or public company — to go and say: Hey, I'm betting everything on AI. The company has to look this way. I'll destroy and rebuild everything I've been building for the past 40 years to become an AI-native company."
>
> 「经济学里有个概念叫**创造性破坏**……**深度采纳 AI 是极难的**。今天一个 CEO——尤其是大公司或上市公司的 CEO——很难站出来说：『我把一切都押在 AI 上。公司必须变成这个样子。**我要推倒我过去 40 年建起来的一切，重新变成一家 AI 原生公司。』**所以就在他们在位子上慢慢采纳的时候，**围绕 AI 优势新建的公司可以长起来，然后接管市场。**」

他用来打比方的是电力——**技术早就准备好了，改变发生得很晚**：

> "What needed to be done was to **destroy that factory**, build it on a flat surface — not in the center of New York, but in Connecticut or New Jersey — and **redesign your whole factory around small dynamos and electricity**. And then you get like the **three-X improvement in productivity** that powered the US during the 20th century."
>
> 「当时该做的是：**把那座工厂拆掉**，在一块平地上重建——不是建在纽约市中心，而是建到康涅狄格或者新泽西去——然后**围绕小型发电机和电力，把整座工厂重新设计一遍**。这样你才能拿到那个**把 20 世纪美国托起来的三倍生产力提升**。」

爱迪生那台高效发电机在 1880 年代就已经在纽约和伦敦商用了，**技术等了几十年**；而多数工厂主做的事，只是**把烧煤的引擎换成电动机，厂房还是那座厂房**——于是只拿到大约 **6％** 的效率。他补了一句：「你本来可以比福特早四十年建出福特那座工厂。」

> "Companies are swapping the coal engine for the electric engine."
>
> 「今天的公司，正在**把烧煤的引擎换成电动机**。」

访谈收在这里：

> "Economic value in humanity for the past 4,000 years **has been delivered by organizations, not by individuals**. So what you want to self-improve **is the organization**."
>
> 「过去四千年里，人类的经济价值**是由组织、而不是由个人交付的**。所以你要让它自我改进的东西——**是组织本身。**」

节目的名字就叫《The Self-Improving Company》（自我改进的公司）。

---

## 🧭 章节时间轴（依节目章节）

| 起点 | 章节 | 本页对应 |
|---|---|---|
| 00:00–01:53 | 开场：一家由 Agent 运营的组织 | 一、四 |
| 02:06–03:22 | Alejandro 的来路与 Kavak 之前 | 一 |
| 03:59–05:15 | Agent 怎么与客户互动 · 系统设计 | 三 |
| 05:42–07:50 | 转型背后的三个决定 | 二 |
| 08:15–10:37 | Evals：Agent 规模化与安全的底座 | 五 |
| 10:59–13:11 | 销售 Agent 超过人类团队 | 四 |
| 13:29–15:43 | 由 Agent 端到端跑完的金融服务 | 四 |
| 16:01–19:31 | 库埃纳瓦卡的 AI CEO 实验 | 八 |
| 19:55–22:41 | Jedi Academy：全员再训练 | 八 |
| 22:41–24:08 | 转型后的组织形态 | 六 |
| 25:13–28:03 | 给公司与领导者的实操建议 | 九 |
| 28:03–31:12 | 为「客户导向的 Agent」重做架构 | 七 |
| 31:25–34:39 | 创造性破坏 · 新创始人的机会 | 十 |
| 34:47–36:08 | 给创始人的收尾建议 | 十 |

---

## 📎 引语与出处索引

页内英文引语集中列此，便于核对：

| # | 英文原话 | 出处 |
|---|---|---|
| 1 | "We bet the company in transforming to a company run by agents." | Alejandro Maza Ayala · 04:00 |
| 2 | "How would we build Kavak in 2035, with Fable 10 or GPT 10 level intelligence?" | 同上 · 04:00 |
| 3 | "The first instinct is, okay, let's adopt AI. And you basically leave your structure as it is and just give ChatGPT or Claude to your team. And then there's no efficiencies… nothing happens." | 同上 · 05:41 |
| 4 | "The only way to really make them work is if you teach them… You put them out in the open, you put them in front of customers, you get that data, you get those evals." | 同上 · 06:11 |
| 5 | "An agent will get spawned specifically for this customer, with its own virtual machine." | 同上 · 04:00 |
| 6 | "Set a long-term goal to maximize the lifetime value of this customer, and do whatever it takes to make the customer happy." | 同上 · 04:27 |
| 7 | "Long-running agents with hard goals, not just workflows." | 同上 · 04:54 |
| 8 | "We could build superhuman agents… by every dimension that matters, our agents would outperform the best human we had ever hired." | 同上 · 00:00（节目开场） |
| 9 | "Every day, between 100 and 200,000 agents get instantiated… with its own virtual machine." | 同上 · 00:22 |
| 10 | "We spend about the same amount of engineering time, tokens, and money on building evals as on building agents… This lets us move fast because we have the right brakes." | 同上 · 07:52 |
| 11 | "We never built customer support agents. We built sales agents." | 同上 · 10:56 |
| 12 | "If an agent hits a wall, it calls an API for help, and a human assists. This closes the loop." | 同上 · 24:08 |
| 13 | "They're either building the agents, working for the agents, or being in the physical world in front of the customer." | 同上 · 22:56 |
| 14 | "We had tens of thousands of these agents running the business by December. But when Opus 4.5 came out… we destroyed everything we had built for two years." | 同上 · 28:03 |
| 15 | "The goal of the first month was to double the profits. It didn't reach it, but it was 1.5x — like 50％ more profits." | 同上 · 15:50（库埃纳瓦卡） |
| 16 | "We launched a program inside Kavak that's called the Jedi Academy. From the CEO to AI engineers to mechanics, we train everyone." | 同上 · 00:39 |
| 17 | "The transformation has to be top-down… That doesn't work."（黑客松与自下而上） | 同上 · 25:38 |
| 18 | "Economic value for the past 4,000 years has been delivered by organizations, not by individuals." | 同上 · 30:26 |
| 19 | "I'll destroy and rebuild everything I've been building for the past 40 years to become an AI-native company." | 同上 · 32:18（谈在位者） |
| 20 | "Redesign your whole factory around small dynamos and electricity. And then you get the three-X improvement in productivity." | 同上 · 33:48（爱迪生与福特） |

**出处层级**：① a16z 官方节目页（描述与嘉宾头衔）＝ **节目方一手**；② 00:00–06:11 段落为节目方放出的开场逐字稿，逐字可靠；③ 06:11 之后各条为**播客逐字稿转引**（转录站与播客笔记站整理，含语音转写噪声，本页已按上下文校正，见编者注）；④ 正文中未加引号的叙述 ＝ 对上述内容的整理。**引语第 10 条的措辞以播客笔记站转引为准，非逐字稿原文。**

---

## ⚠️ 编者注

1. **与底本的关系。** 本页原有一版底本：微信公众号「**猫不白**」的转述稿《AI 真正淘汰的不是员工而是公司》（无日期，主理人提供 docx；元信息显示为转录件）。底本本身是**一位号主对这场访谈的转述加评议**——「我觉得」「我特别认同」「我判断」这类句子贯穿全篇。**本页改以一手原件（a16z 播客本集）重写**，正文只保留「Kavak 说了什么、做了什么」，底本的框架与评议**一律不收**。

2. **人名与头衔要更正。** 底本把嘉宾写成「**Ali Masa**」，同一篇里又写作「**Eddie Masa**」——**是同一个人的两种转写**。官方写作 **Alejandro Maza Ayala**，节目里昵称 **Ale Maza**，头衔是 Kavak 的 **Chief Product & AI Officer（首席产品与 AI 官）**，不是底本所称的「AI 负责人」。

3. **底本的几处笔误（均已在本页改正，留痕存档）**：①「**Ava** 捕捉问题」——同段前文写的是 **Eval**，此处应为 Eval 的转写错误；②「Kavak **比原来**其实也做了大量 multi agent workflow graph」——「比原来」应为「**本来**」；③「**开发**现在很多团队基本就三类工作」——「开发」为衍字；④ 底本说工厂当年是「把**蒸汽机**换成电动机」——原件说的是**把烧煤的引擎换成电动机**。

4. **数字口径。** ① 本集全部经营数字（96％／95％／10–20 万／2.1 倍／三倍 NPS／3 分钟／1000 万客户）**均为高管在风投播客上的自述，未经审计、未给定义与基线**；② **2.1 倍没有基线**——是对哪一批人工、在多长时间窗、线索如何分配，都未说明，且漏斗由公司自己掌握；③ **「利润 50％」要写准**——是**首月做到 1.5 倍（＋50％），对 2 倍的目标**，且**只有一座城市、六周、没有对照组**；④ 底本说「96％ 的客户互动」「95％ 的交易流程」，与原件一致，可放心用。

5. **底本漏收、但本集分量很重的几件事**：**库埃纳瓦卡的 AI CEO 实验**、**技师副手 Agent 与保修索赔下降**、**Jedi Academy 全员再训练**、**Token 分三档算 ROI**、**「6％ 效率」这个说法**、**熊彼特与爱迪生／福特那套类比**，以及**「必须自上而下、黑客松没用」这条判断**。以上均已补入正文。

6. **语音转写噪声（已按上下文校正）。** 本集逐字稿为语音转写件，人名机构名多有错：Kavak 被转成 Kabag／Kabak／Kovac／Quebec，Oppy Analytics 转成 **Opi Analytics**，ChatGPT 转成 **Chad GPT**，库埃纳瓦卡 **Cuernavaca** 转成 Cuba，技师副手 Agent 的名字在 **El Mic ／ El Mike** 之间摆动（本页保留两写）。凡此类，本页按公开报道校正，不臆补。

7. **两处容易读错的归属。** ①「**想踩油门你得先有刹车**」是底本对 he said「we have the right brakes」的**意译**，不是原话；②「**模型越聪明，workflow 可能越薄**」是**底本作者自己的判断**——他的原话指向的是「harness 更薄、约束更少」（见第七节），方向一致但不是他的词。③ 同理，「**AI 真正淘汰的不是员工而是公司**」是底本的标题式概括；他本人的说法是**创造性破坏与「AI 原生新公司接管市场」**。

8. **一处需要点明的事实**：Kavak 的**当前经营状况并未披露**。「带我们到盈利」那句话说的是**他们后来推倒的那套旧系统**；节目里还明确提到转型期**「不得不大幅收缩」且「第一年没跑通」**。这条与「转型顺利」的印象相反，读上面的数字时请一并记住。

9. **与隔壁三页对照着读**：[OpenAI 内部怎么用 AI](03_xinzhi/AI_Agent使用最佳实践/OpenAI内部怎么用AI·Tibo访谈.md) 是一家**工具公司**怎么用 Agent 造工具；[Anthropic 内部怎么用 AI](03_xinzhi/AI_Agent使用最佳实践/Anthropic内部怎么用AI·当AI开始建造自己.md) 是一家**模型公司**怎么用 Agent 造下一代模型；[麦肯锡内部怎么用 AI](03_xinzhi/AI_Agent使用最佳实践/麦肯锡内部怎么用AI·4万人与2.5万个Agent.md) 是一家**靠人赚钱的服务企业**怎么把 Agent 接进运转。Kavak 是第四种：一家**普通交易型公司**，把整家公司的组织结构围绕 Agent 重做了一遍。

---

> ← 返回 [🧭 AI Agent 使用最佳实践](03_xinzhi/AI_Agent使用最佳实践/README.md)　｜　相关：[OpenAI 内部怎么用 AI](03_xinzhi/AI_Agent使用最佳实践/OpenAI内部怎么用AI·Tibo访谈.md)（工具公司怎么用 Agent）　[Anthropic 内部怎么用 AI](03_xinzhi/AI_Agent使用最佳实践/Anthropic内部怎么用AI·当AI开始建造自己.md)（模型公司怎么用 Agent）　[麦肯锡内部怎么用 AI](03_xinzhi/AI_Agent使用最佳实践/麦肯锡内部怎么用AI·4万人与2.5万个Agent.md)（服务企业怎么用 Agent）
