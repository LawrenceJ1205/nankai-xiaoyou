# Aaron Levie：AI 的价值在应用层

> **所属专辑**：[🤖 AI 前沿认知和方法论](03_xinzhi/AI前沿认知和方法论/README.md)（📚 新知小讲堂）
>
> **一手原件**：**红杉资本《Training Data》播客**《Box's Aaron Levie: On Reinventing Yourself in the AI Age and Enterprise Diffusion》（主持 **Sonya Huang**，红杉合伙人；**2026-09-15** 发布 · 约 **65 分钟**）。嘉宾 **Aaron Levie**——**Box** 联合创始人兼 CEO。本页**依节目官方页要点 ＋ 官方章节时间轴 ＋ 可核对逐字稿引语**整理；引语一律给英文原话并附中译。
>
> **本页体例**：依一手原件整理——正文只留「**他说了什么**」；引语一律给英文原话并附中译，未加引号的叙述为整理。
>
> **怎么读**：想看「价值在哪一层」，看第二节；想看「一家上市 20 年的公司怎么把公司押上去」，看第四节；想看「为什么编程扩散得快、别的知识工作慢」，看第十节。

---

## 一、这场访谈的坐标

| 项 | 内容 |
|---|---|
| **节目** | 红杉资本《Training Data》播客（主持 **Sonya Huang**，红杉合伙人） |
| **嘉宾** | **Aaron Levie**，**Box** 联合创始人兼 CEO |
| **公司** | Box：企业内容管理与协作平台；他在节目里自述「只有 **13 亿美元**营收（revenue run rate）」；坐在**数千亿份文件**之上 |
| **发布** | **2026-09-15**　｜　**时长** 约 65 分钟 |
| **本页所据** | 节目官方页要点、官方章节时间轴、可核对的逐字稿引语（含时间码） |

这一集的主线是：**一家上市 20 年的公司怎么把自己重做成 AI 公司**；顺带回答了当下最热的那个问题——**模型和能力那么强，价值到底落在哪一层？**

---

## 二、价值在哪一层：应用层 vs 模型层

主持人开场问的是「**应用公司是不是最热的新实验室（neolab）**」。他的回答从「桥」开始：

> "In the real world, in the enterprise, what you need is some bridge from the model's capability to the actual workflow that the enterprise has."
>
> 「在真实世界里、在企业里，你需要的是一座**从『模型的能力』到『企业真实工作流』之间的桥**。」

> "Probably $1 trillion has been bet on basically one of two outcomes: either that bridge is very limited, or that bridge is actually very vast and needs to be able to take on a lot of depth within organizations."
>
> 「大概**一万亿美元**押在了这两种结果之一上：这座桥**要么非常有限、要么非常庞大**，庞大到要在组织内部承担很深的厚度。」

他判断**桥是很宽的**，并给了理由——模型之外还有五到十件「**更运营、更苦更累的活**」：

> "The model could be the most intelligent superintelligence in the world, but that workflow still requires you to connect up to other data systems. It still requires these moments where there's a human-in-the-loop interaction. There are delays in the workflow, so the agent has to sit idle. There's change management of the actual business process. There are legacy systems that haven't been modernized."
>
> 「模型可以是世界上最聪明的超级智能，但那条工作流**仍然要接上别的数据系统**、**仍然要有人在环环节**、**仍然会有等待**（Agent 只能干等）、**仍然要做业务流程的变革管理**、**仍然有没现代化过的遗留系统**。」

> "The models will be insanely valuable, but the application of bringing those models into real workflows — in banking and life sciences and healthcare and government — that's just going to be a lot of software."
>
> 「模型会极有价值，但**把模型带进真实工作流**——在银行、生命科学、医疗、政府里——**那就是一大堆软件。**」

他用云的类比说明这不是新故事：AWS／GCP／Azure 造出了万亿市值的基础设施，而**在此之上又长出了万亿市值的软件公司**（Snowflake、Databricks），当年没人预见到。**智能这一层也是同理。**

他也点出模型公司自己的两难：**要离客户近，就要往上走；要让生态信任你，就得留出空间。** 这个张力会持续好几年。

---

## 三、Token 补贴为什么是暂时的

被问到「模型公司可以补贴、给出更低的价格」，他给了这一集最锋利的一段：

> "When these companies become public, I think they will be held to basically the same laws of capitalism as everybody else. …the subsidization of tokens, I think, just has to be a temporary phenomenon."
>
> 「等这些公司上市，**它们会被同样的资本主义规律约束**。……**Token 的补贴，我认为只能是一个暂时现象。**」

他还指出一个更微妙的结构问题——**如果高毛利的 API 在补贴应用端，而客户都搬去了应用产品、API 收入没了，这个平衡就撑不住。**

然后是他对竞争格局的判断：有几类玩家**不靠推理赚钱**——「Meta 算一个、马斯克的公司可能算一个、中国肯定算一个，英伟达也算一个」——它们可以把推理毛利压到 10%，只为了摊平巨额算力。

> "As long as there aren't insane, closely held proprietary secrets, then no matter what, you're going to have cost per token go down on a like-for-like basis. All of which means more value accrues to the application layer."
>
> 「只要没有那种疯狂的、秘而不宣的独门秘方，那么**单位 Token 成本一定会往下走**。而这**意味着更多价值流向应用层。**」

他甚至认为**大实验室自己也愿意看到这个结果**：

> "If I were one of the two or three biggest labs, I think I'd prefer this outcome too… at some point you'll just be nationalized if you're the only thing that exists as intelligence."
>
> 「如果我是那两三家最大的实验室之一，**我大概也宁可要这个结果**……**因为如果你成了世界上唯一的『智能』，早晚会被国有化。**」

他的落点：**这不该被押成「一两家拿走 95% 的价值」**，应当是一个**更有活力的环境**。

---

## 四、Box 把公司押在 AI 上

他把公司史讲成三段：**云 → AI 早试 → ChatGPT 时刻**。

- 起点是「**在云上安全地存储、分享数据**」：企业从本地系统迁往云，需要更好地存储、分享、协作、管理那些**非结构化数据**。
- **2015 年起**就在碰 AI：图像分类、OCR 之类「看起来很有用」，但「**贵得离谱，而且每个用例都得训一个模型**」——于是**搁置**。
- **ChatGPT 那一刻**：它找到了一个形态，「打开所有人的脑子」——原来可以做成交互式系统，问一句、拿回一段越来越复杂的答案。

> "We jumped all in. We sort of did the whole company pivot. Everything was exactly like, academically, what you should do. We had a team carved out. We put the best people on the team. We met every day."
>
> 「我们**全押了进去，做了整家公司的转型**。**学术上讲，该做的每一步我们都做了**：抽出一个专门的团队、把最好的人放进去、每天碰头。」

为什么值得押？因为他手上有一个别家没有的底座：

> "We sit on hundreds of billions of files. Every single one of those files contains critical information for an enterprise. …So now agents can go and basically be farmed out to go and answer questions about that data."
>
> 「我们坐在**数千亿份文件**上。每一份都装着企业的关键信息。……于是现在可以**把 Agent 撒出去，去回答关于这些数据的问题**。」

两个「本垒打」用例：一是最简单的——**你有 100 万份合同，去看里面写了什么**（把关键结构化数据抽出来、进库、再查询、分析、自动化）；二是**长时程 Agent**——比如银行开户，「把每一步能自动化的都自动化，只在需要复核／验证的环节转给人」，于是**过去要一两周的来回，现在一小时**。

---

## 五、workslop：AI 写的代码被接受，AI 写的内容不被接受

主持人抛出一个反差：编程领域用 AI「不仅被接受、而且被欢迎」，内容领域却是**过敏式抵触**——「workslop」（工作糊料）。他先把两件事分开：

> "For most of the world, code is a utility. It's just trying to accomplish something."
>
> 「对绝大多数人来说，**代码是工具**，它只是要办成一件事。」

所以——

> "If you can tell an agent, 'Please go generate my entire backend system or my front-end system,' it's not only acceptable, it's preferable. That was the thing that was blocking us from moving forward."
>
> 「如果你能让 Agent『**去把我的整个后端／前端生成出来**』，那**不仅可接受，而且更好**——因为那正是挡着我们往前走的东西。」

但内容不一样，因为它承载的是**对你这个人的判断**：

> "When you get a presentation from somebody, there's still this association which is: I'm trying to decide if I can trust that person to go and execute on that thing."
>
> 「你收到某个人的一份汇报，里面还有一种关联：**我在判断我能不能信任这个人去把这件事做出来。**」

他也承认自己身上有这个矛盾：

> "I'm doing workslop for some of my brainstorms and decisions, but when I get it from somebody else, I'm like, 'Hmm, should I trust you?'"
>
> 「我自己的一些头脑风暴和决策也在用 AI 糊——**可当它来自别人时，我又会想：我该信你吗？**」

他甚至说了一句半开玩笑的话：

> "I would hate to be a college professor. I would totally quit, because… I don't know anymore what you did."
>
> 「我**绝对不想当大学老师**，我会直接辞职——因为**我已经不知道那是不是你做的了。**」

他的结论是：这是**一个社会要花三到五年才能熬过去的过程**——就像你看到一个财务模型，知道那是宏跑的，也不影响你用它。

---

## 六、harness 与 evals

他讲了 Box 的**agentic harness**（脚手架）：它**吃透了自家系统的领域理解**——文件系统、权限结构、搜索排序的取舍规则（「用户翻十个文件时，凭什么挑那一个」）。它能拉全文、切片、临时做向量化，**一轮里做多次检索、重排、再挑最相关的信息，必要时读完整篇**。

> "Then we compare that against, well, what if we just gave Claude our API, or gave OpenAI our API? And we see meaningfully better results on accuracy and latency, because we know exactly how to tune it for our workflows."
>
> 「然后我们拿它跟『**直接把我们的 API 交给 Claude 或 OpenAI**』比——**在准确率和时延上明显更好**，因为我们**确切知道该怎么为我们的工作流调优。**」

评测方面，他说每个模型都要跑**上百个测试**，其中两个正式的：

| 评测 | 是什么 |
|---|---|
| **Complex Work Eval** | 面向生命科学、金融服务、公共部门、科技等**领域专有的文档型评测**：「给你这五份文档和这组问题，你的答案是什么？」 |
| **Box 内部 holdout** | 用 Box 自己员工与数据的真实使用来跑，同样对每个模型评一遍 |

他能据此**跟踪模型的每一点进步**（「半个点的提升我们都看得到」），并按**成本／准确率**给出默认模型，同时允许客户从「模型花园」里任选。

他还讲了 Box Labs 在做的事：**在 Agent 层、harness 层做某种『自动研究』，去爬山式地提升准确率**——「一家银行的百页贷款文档，用现成模型是 70% 还是 97%，**决定你到底能不能自动化这条流程**。你得从基座模型**一路爬到 97%。**」

---

## 七、模型竞赛、开放权重与记忆

**模型竞赛**：他说各家在自家用例上的表现**大体跟编程能力正相关**，**例外是 Gemini 在一些用例上明显更好**（他猜是工具调用更强）。当时的状态是「**Fable 5.1 明显是 SOTA**」，而整体是「**Grok、Muse、Fable 这一档、还有 GPT-5.6 那一代，咬得很紧——现在是彻底的赛跑。**」

**开放权重**：他的回答是个三段式——

> "Probably higher than people think, lower than what enterprises actually want, and much, much, much, much lower than what it will be in five years."
>
> 「**比人们以为的高，比企业真正想要的低，比五年后的样子低得多得多。**」

他坦承有「**30% 以上是图个新鲜**」（「我想试试 GLM」），也说眼下还有工程摩擦（「有时随机地**在链条中间突然说起中文**——这对银行来说就有点怪」）。但他认同一种「两开」格局：**用旗舰模型做编排，把长尾任务外包给便宜模型**——于是可能出现「**两边各花一半的钱，但开放权重那边跑了十倍多的 Token**，**大家都赢，但赢法不同。**」

**记忆与持续学习**：他很感兴趣，但指出**企业最大的摩擦是权限与访问控制**：

> "Let me introduce you to a lawyer. The lawyer has this tiny little access point of just the five projects they're working on, because somebody one door over is working on the competitive project for another company… They have to be hard barriers."
>
> 「让我给你介绍一位律师：**他只有五个项目的极小访问口径**——因为**隔壁那扇门里的人，正在为另一家公司做竞品项目**……这些**必须是硬墙。**」

他给了一个他觉得最实用的框架：**「什么该进上下文，什么该进权重」需要一张 T 形表**——「**当数据的变化率不高、而放进权重能大幅提升准确率**时，才值得固化进权重」。

---

## 八、记录系统在 Agent 世界里要做的两件事

主持人提到网上的争论：「每家软件公司都想卖我它自己的 Agent，我不要——我要**它的记录系统（system of record）好好配合我的 Agent**。」他的回答是「#Claudeforce」（调侃 Salesforce 的一次发布会），然后给出两条**必须同时做**的事：

**第一，做一个极其出色的、专门针对自己产品的 Agent。**

> "That agent has to be provably 10 or 20 points better than an off-the-shelf agent at using your system — not because you've hobbled the other side."
>
> 「那个 Agent 必须**可证明地比通用 Agent 用你的系统强 10 到 20 个点**——**不是因为你把对方的手脚绑住了。**」

**第二，必须「无头化」（go headless）**——把 API 暴露给 Claude、ChatGPT 等平台，让外部 Agent 能通过 MCP 之类的方式调用你。

他也给了自己的体感证据：

> "I use Salesforce more today, probably by an order of magnitude, than I ever have, because I MCP into it via Claude or ChatGPT."
>
> 「我今天用 Salesforce 的频率，**大概是过去的十倍**——因为**我通过 Claude 或 ChatGPT 用 MCP 接了进去。**」

他不喜欢「收费站」这个比喻（「没人有过在收费站的好体验」），但承认**这类公司需要有某种按量计费的商业模式**——「**只要你真在替客户解决问题，它就能赚到钱。**」

他还举了一个他认为被低估的方向：**一个常驻后台的合规 Agent**——「想象企业的合规负责人和治理负责人**从没可能同时出现在所有地方**；现在他们可以**坐在每个员工旁边**，在你要做违反治理政策的事时说一句。」

---

## 九、聊天框会一直在，但企业的主体在后台

关于「聊天框会不会是主导界面」，他给的是**双轨**答案：

> "The universal chat system that you ask a question to and get an answer back — that's going to be a mainstay. That UI will always exist. …It's just like your product has a search box."
>
> 「那种普适的聊天系统会**一直存在、一直强**——就像你的产品一定有搜索框一样。」

但**企业的主体是后台流程**：

> "Most of the enterprise is made up of processes and workflows that are happening behind the scenes. Sometimes they should be happening with people, but you could never afford to have them happen with people, so they just didn't happen."
>
> 「企业的大多数，是**在后台发生的流程**。有些事**本该由人来做，但成本高到根本做不起，于是它干脆就没发生过。**」

所以他要的不是聊天，而是**仪表盘、工作流、队列、任务列表**——「我聊天只是为了『补课』」。

由此他推出一个对**垂直软件**有利的判断：**通吃的水平产品会越来越重**，而**懂那个流程的垂直玩家**才摆得出「对的按钮、对的标签、对的名字」；后台异步 Agent 干得越多，越偏向**懂流程的应用公司**。（他说法律领域已经有 Harvey、Legora 这类，安全与长时程编码 Agent 也在长出来。）

> "In five years from now, I would bet like 90% of all tokens in the enterprise are things a user never kicked off and they just see a result."
>
> 「**五年后，我打赌企业里 90% 的 Token 是用户从没发起过的事**——他们只是看到一个结果。」

---

## 十、为什么编程扩散得快，别的知识工作没有

这是整集最实用的分析。他把编程的「有利属性」列成五到六条，再拿别的知识工作逐条对照：

> "The utility of code is almost 100% represented by the amount of text that you can generate. …If you could have the world's greatest programmer who never had to sleep, never had to eat, could intuit what to build, and could just sit at a computer all day long, your value creation would be 100% correlated with how many hours they could sit at that computer and type lines of code."
>
> 「**代码的效用，几乎 100% 就体现在你能生成多少文本。**……你只要有一个不用睡、不用吃、天生就知道该造什么、能整天坐在电脑前的绝世程序员，**你的价值创造就跟『他在那台电脑前敲了多少小时代码』100% 正相关。**」

其余几条：**模型被疯狂训练在这上面**；**每家实验室都把编程当作要不断超越的竞争基准**（而且他们自己每天就在给自己出题）；**用户是史上最技术的一群人**——「跑出 bug 或者 MCP 服务器报『连接无效』，他们自己会修，**他们不会去找 IT**」；以及**这是个薪酬极高的行业**，哪怕 10%–20% 的提效也自动值钱。

然后对照**销售**：

> "The sales rep's value creation is basically convincing an external customer to buy software or technology or a Caterpillar truck from them. …They're still rate-limited and constrained by: Did the customer respond to them? Do they want to meet? Can they meet next Tuesday? Does the customer have budget?"
>
> 「销售的价值创造，基本是**说服一个外部客户从他们那里买东西**。……他们**始终被这些外部因素限速**：客户回不回你？想不想见？下周二能不能见？客户有没有预算？」

他还点了一个最容易被忽略的差别：

> "Most engineers in 2026… the code's in GitHub. You just connect it to GitHub. …There's no 'give us your GitHub' for knowledge work."
>
> 「2026 年的大多数工程师……**代码就在 GitHub 上，你连上去就行**。……**但知识工作里没有『把你的 GitHub 给我』。**」

再加上**权限口径完全不同**（「嗨 Sally，能不能帮我开一下那个文件共享？」）——他的结论是两句话：

> "One, Silicon Valley has to prepare for diffusion taking a lot longer than they think. And the second thing — the good news — is this is all correlated to applied-layer value creation."
>
> 「**一，硅谷得准备好：扩散会比他们以为的慢很多。二（好消息是），这全都跟应用层的价值创造正相关。**」

落点是一句他反复说的判断：

> "In a world where AI builds things so much faster, the shift probably moves to whoever can actually get it to the customer being in the best position."
>
> 「在一个 AI 造东西快得多的世界里，**优势会移向『谁真能把东西送到客户手里』那一方。**」

---

## 十一、给创始人的建议

**关于自己**：他说自己「**什么都玩**」；信息来源「很遗憾，大概是 95% 靠 Twitter」——每天晚上翻一遍信息流去拼图。他因此给在校生一条很直接的建议：

> "I want to send an emergency alert to everybody who's a sophomore or junior in college and just be like, follow these 20 accounts on Twitter… You're either a year ahead or a year behind simply based on your feed."
>
> 「我想给**所有大二大三的学生发一条紧急警报**：去关注这 20 个账号……**你到底是领先一年还是落后一年，可能就取决于你的信息流。**」

**关于年轻创始人**：他既羡慕又不羡慕——

> "I saw a product a week and a half ago… I was like, this would have been a 40-person project five years ago. And it was two people."
>
> 「一个半星期前我看到一个产品……**这在五年前是 40 人的项目。而它是两个人做的。**」

**关于自己的限制**：他承认 Box 有一件**不会做**的事——

> "We're very uncomfortable with the idea of removing the code review… because our customers can't possibly entrust us with their data security and compliance if we don't take that seriously. So we're always going to have a little bit of a discount on the productivity."
>
> 「我们对『**取消代码评审**』这件事非常不安……因为**不认真对待的话，客户不可能把数据安全与合规托付给我们**。所以我们**在生产力上永远会打一点折扣。**」

**关于公司内部怎么推**：Box 的 CIO「非常 AI 上头」，有一个 AI 卓越中心，还招了内部 AI 博士；**但他们不「刷 Token」**——确实有一张按 Token 用量排的名单，用途是**检查**：「前三名 AI 用户里，**大概有一个有一半 Token 是浪费的，另两个做的事我们必须办一场内部培训教给大家**。」他说他们真的会把人叫进一间屋子，让那个用得好的人**当场演示**。

最后是他的总结判断：

> "The thing is going to be an enterprise diffusion play, so you have to get it to the enterprise. Anybody who mistakes the mandate right now, you're just going to lose. It's game over."
>
> 「这件事**注定是一场企业扩散战**，所以你必须**把它送到企业手里**。**任何现在搞错了任务的人，都会输——直接出局。**」

---

## 🧭 章节时间轴（依节目官方章节）

| 起点 | 章节 | 本页对应 |
|---|---|---|
| 00:00 | 开场：Aaron Levie 与一点闲话 | 一、十一 |
| 01:55 | 应用公司是不是最热的新实验室？ | 二 |
| 06:56 | 实验室会往上走到应用层吗？ | 二、三 |
| 12:34 | Box 与「把公司押在 AI 上」 | 四 |
| 16:50 | 本垒打用例：读 100 万份合同、长时程 Agent | 四 |
| 18:42 | workslop：为什么 AI 代码被接受、AI 内容不被接受 | 五 |
| 24:08 | 造 Box 的 agentic harness，以及真正要紧的 evals | 六 |
| 27:23 | 模型竞赛的现状 | 七 |
| 29:25 | 开放权重在企业里的采用 | 七 |
| 32:34 | 记忆、持续学习，以及什么该进权重 | 七 |
| 37:29 | Box Labs 与 Agent 世界里的记录系统 | 六、八 |
| 44:55 | 聊天会不会是企业 AI 的主导界面？ | 九 |
| 48:00 | 为什么编程扩散得快、其余知识工作没有 | 十 |
| 54:31 | 保持「接在线上」、把公司做成 AI 原生，以及取胜要靠什么 | 十一 |

---

## 📎 引语与出处索引

页内英文引语集中列此，便于核对（时间码取自该集逐字稿）：

| # | 英文原话 | 位置 |
|---|---|---|
| 1 | "In the real world, in the enterprise, what you need is some bridge from the model's capability to the actual workflow that the enterprise has." | 01:45 |
| 2 | "Probably $1 trillion has been bet on basically one of two outcomes: either that bridge is very limited, or that bridge is actually very vast." | 01:45 |
| 3 | "The model could be the most intelligent superintelligence in the world, but that workflow still requires you to connect up to other data systems… legacy systems that haven't been modernized." | 04:29 |
| 4 | "The models will be insanely valuable, but the application of bringing those models into real workflows… is just going to be a lot of software." | 04:29 |
| 5 | "It's the company that doesn't care among ten different models which model is performing that task." | 09:09 |
| 6 | "The subsidization of tokens, I think, just has to be a temporary phenomenon." | 09:58 |
| 7 | "At some point you'll just be nationalized if you're the only thing that exists as intelligence." | 11:11 |
| 8 | "We sit on hundreds of billions of files. Every single one of those files contains critical information for an enterprise." | 15:08 |
| 9 | "If you can tell an agent, 'Please go generate my entire backend system or my front-end system,' it's not only acceptable, it's preferable." | 19:26 |
| 10 | "I'm reading it, one, for the substance, and I'm also reading it, two, for the calculation of: did the person write it?" | 22:18 |
| 11 | "I would hate to be a college professor. I would totally quit, because… I don't know anymore what you did." | 22:40 |
| 12 | "We see meaningfully better results on accuracy and latency, because we know exactly how to tune it for our workflows." | 24:12 |
| 13 | "Whether you're getting 70% accuracy with an off-the-shelf model or 97% is a world of difference in whether you can actually automate that process." | 37:45 |
| 14 | "We're just neck and neck on Grok, Muse, the Fable class, and GPT-5.6… It's a total race right now." | 27:55 |
| 15 | "Probably higher than people think, lower than what enterprises actually want, and much, much, much, much lower than what it will be in five years."（开放权重） | 29:25 |
| 16 | "Let me introduce you to a lawyer. The lawyer has this tiny little access point of just the five projects they're working on… They have to be hard barriers." | 33:18 |
| 17 | "You have to build an agent that is insanely great at your product. That agent has to be provably 10 or 20 points better than an off-the-shelf agent at using your system." | 39:47 |
| 18 | "You have to go headless. You literally have to make sure that your APIs are exposed to Claude and ChatGPT." | 42:34 |
| 19 | "I use Salesforce more today, probably by an order of magnitude, than I ever have, because I MCP into it via Claude or ChatGPT." | 42:34 |
| 20 | "In five years from now, I would bet like 90% of all tokens in the enterprise are things a user never kicked off and they just see a result." | 46:06 |
| 21 | "The utility of code is almost 100% represented by the amount of text that you can generate." | 48:26 |
| 22 | "There's no 'give us your GitHub' for knowledge work." | 50:51 |
| 23 | "Silicon Valley has to prepare for diffusion taking a lot longer than they think." | 52:52 |
| 24 | "You're either a year ahead or a year behind simply based on your feed." | 56:07 |
| 25 | "In a world where AI builds things so much faster, the shift probably moves to whoever can actually get it to the customer being in the best position." | 63:58 |
| 26 | "Anybody who mistakes the mandate right now, you're just going to lose. It's game over." | 63:58 |

**出处层级**：① 节目官方页（本集要点、官方章节时间轴、嘉宾信息）＝ **节目方一手**；② 上表引语＝该集逐字稿原话（官方视频与节目页文字稿；本页已按上下文校正语音转写噪声）；③ 正文中未加引号的叙述 ＝ 对上述内容的整理。

---

## ⚠️ 编者注

1. **出处与日期**：一手原件为**红杉资本《Training Data》播客，2026-09-15 发布**，主持 **Sonya Huang**（红杉合伙人），时长约 65 分钟。同一位嘉宾在 2026 年还上过 Silicon Valley Girl 播客（《Box CEO on the Next 3 Years That Will Make 100 New Founders Rich》）——**两场内容有重叠也有出入，本页只据红杉这一场**，若日后引用别处，请分场标注。

2. **语音转写噪声（已按公开名称校正）**：底稿为自动转录，人名机构名多有错——`Aaron Levy`＝Aaron Levie、`Enthropic`／`entropic`＝Anthropic、`Merkore`＝Mercor、`cloud`／`chatbt`＝Claude／ChatGPT、`Stan Ducken Miller`／`Duckenmiller`＝Stan Druckenmiller、`Pangram`＝AI 文本检测工具 Pangram、`Claudeforce`＝他为调侃 Salesforce 发布会起的谐趣说法、`Caterpillar truck`＝卡特彼勒卡车、`Trajectory / Applied Computer / Prime Intellect`＝三家做定制模型的公司（`Applied Compute`）。凡此类，本页按公开名称校正，不臆补。

3. **模型名字面照录，不作推测**：他提到的 **Fable 5.1**、**Grok**、**Muse**、**GPT-5.6**、**GLM** 等均为**节目当时的说法**；「Fable」在这一时间线上被用作前沿模型的代号（同站 Kavak 篇也出现过「Fable 10」）。本页**照录不解释**，请勿把某个名字当成唯一的事实认定。

4. **数字口径**：① **Box 的营收规模**——他在节目里说「**we're only 1.3 billion in revenue run rate**」，即约 **13 亿美元 ARR**（页首「约 1.3 亿」为笔误口径，**以 13 亿为准**）；② 「$1 万亿押在这座桥上」「五年后 90% 的 Token」「10 到 20 个点」均为**他的口头估计与预测，不是现状、也未经审计**；③ 「数千亿份文件」是自述的规模量级。

5. **两处需要点明的性质**：① 「**10 到 20 个点更好**」是**他对记录系统厂商的要求**（必须做到的及格线），**不是 Box 已公开验证的成绩**——他说得很清楚：「必须**可证明地**比通用 Agent 强」；② 「**90% 的 Token 用户从没发起过**」是**预测句**（「五年后我打赌」），**不是今天的比例**，引用时请保留时间前缀。

6. **他对本文所涉竞争格局的判断带立场**：Box 是应用层公司，他自己也承认「**I'm also equally very biased — I have a very concentrated bet with very limited diversification**」（我为应用层说话，因为我的赌注高度集中）。读第二节与第三节时请带这层自觉。

7. **与第 5、6 篇的关系**：第 5 篇《[红杉 · 结果即服务](03_xinzhi/AI前沿认知和方法论/Hongshan_jieguo.md)》与第 6 篇《[红杉 · MAD 框架](03_xinzhi/AI前沿认知和方法论/Hongshan_MAD.md)》同出红杉视角，讲的是**投资判断**；本页是同一家机构对一位**上市公司 CEO** 的访谈，讲的是**落地现场**——三篇连读，正好是「投资视角 → 企业现场」。与第 13 篇吴恩达也有一处呼应：**「瓶颈一步步外移」**（编程解决后轮到代码评审、再轮到「决定造什么」）在本页以「编程为何扩散快」的形式再度出现。

---

> ← 返回 [🤖 AI 前沿认知和方法论](03_xinzhi/AI前沿认知和方法论/README.md)　｜　相关：[红杉资本 · 结果即服务](03_xinzhi/AI前沿认知和方法论/Hongshan_jieguo.md)（投资视角一）　[红杉资本 · MAD 框架](03_xinzhi/AI前沿认知和方法论/Hongshan_MAD.md)（投资视角二）　[吴恩达：当写代码快 100 倍，瓶颈会转移到哪里](03_xinzhi/AI前沿认知和方法论/吴恩达·瓶颈转移到哪里.md)（瓶颈外移）
