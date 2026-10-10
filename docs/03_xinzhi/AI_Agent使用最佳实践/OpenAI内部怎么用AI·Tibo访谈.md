# OpenAI 内部怎么用 AI：Codex 负责人 Tibo 访谈

> **所属专辑**：[🧭 AI Agent 使用最佳实践](03_xinzhi/AI_Agent使用最佳实践/README.md)（📚 新知小讲堂）
>
> **一手原件**：The Pragmatic Engineer 播客《Building Codex with Tibo Sottiaux》—— 主持 Gergely Orosz，2026-09-09 发布，约 1 小时 13 分。嘉宾 Thibault「Tibo」Sottiaux 是 **Codex 的创建工程师之一**，现任 OpenAI **核心产品与平台负责人**（Head of Core Products & Platform）—— ChatGPT 与 Codex 都在这个组织之下。
>
> **本页体例**：**依一手原件整理**——节目官方页的 12 条要点与 15 段章节时间轴，配合可查证的逐字稿引语。凡引语，一律给英文原话并附中译；正文只做「**他说了什么**」的整理，**不掺入第三方转录稿的框架与评论**（相关处理见文末编者注）。
>
> **怎么读**：只关心「OpenAI 内部怎么用」，直接跳到**第四节**；想看逐句依据，见文末「引语与出处索引」。

---

## 一、这场访谈的坐标

| 项 | 内容 |
|---|---|
| **节目** | The Pragmatic Engineer Podcast（主持 Gergely Orosz） |
| **嘉宾** | Thibault「Tibo」Sottiaux —— 应用数学出身 → 比利时创业 → Google 伦敦 → DeepMind → OpenAI |
| **嘉宾职务** | Codex 创建工程师之一；现任 OpenAI **核心产品与平台负责人**（Core Products & Platform，含 Codex 与 ChatGPT） |
| **发布** | 2026-09-09　｜　**时长** 约 1 小时 13 分 |
| **本页所据** | 节目官方页的 12 条要点、15 段章节时间轴、以及若干可核对的逐字稿引语 |

**章节时间轴**（回看原件用）

| 时间 | 章节 | 时间 | 章节 |
|---|---|---|---|
| 00:00 | 开场 | 41:19 | Codex 背后的研发流程 |
| 07:21 | 在 Google 的日子 | 46:39 | 代码评审在 Codex 团队 |
| 12:41 | 什么把他带到 OpenAI | 52:09 | 维护与架构 |
| 15:19 | Codex 的早期 | 56:43 | AI 工具如何拓宽工程师的能力边界 |
| 18:20 | 为什么用 Rust 写 | 1:02:30 | 合并：ChatGPT ＋ Codex |
| 21:15 | 为什么开源 | 1:07:16 | Tibo 自己怎么用 Codex 与 ChatGPT |
| 25:50 | 为什么 Codex 兼容别家模型 | 1:10:44 | 给想做 AI 的工程师的建议 |
| 32:09 | Harness 是怎么工作的 | 36:44 | Harness 与模型的相互追赶 |

---

## 二、Codex 的来路，与三个工程决定

### 1. 它一开始不是产品，是给自家用的工具

Codex 起初是**为了让 OpenAI 自己的研究与工程跑得更快**而做的内部尝试：团队拿 OpenAI 的 Python 代码库训练模型，再围绕它搭起早期的 agent，要改的是四件事——写代码的速度、代码风格、**架构品味**、基础设施的效率。这个内部项目后来与公司更大范围的「AI 软件工程」计划合流，才有了早期的 Codex 云产品与 CLI。

Tibo 的来路解释了这套偏好。他学的是应用数学，早年做的都是「用数学把系统变高效」的问题——临床试验的药品供应链、钢铁行业的物流、欧洲的电网优化；先在比利时创业，再去 Google 伦敦、DeepMind，最后到 OpenAI。他在 Google 吃过一个教训：一个自己做得很快乐、有几百个用户的广告项目，被副总裁从加州飞来一刀砍掉——回头看才明白，那件事**没有产品市场匹配，用户反馈回路也很差**。他由此养成一个习惯：**持续追问自己手上的工作到底有没有用**。

> 他加入 OpenAI 的触发点很具体：2023 年他听说，如此规模的 ChatGPT 其实只由**大约 20 名工程师**建造和维护。他既惊讶于这个数字，也被「研究与产品贴得这么近」这件事吸引。

### 2. 核心为什么用 Rust —— 即使当时模型更会写 Python

Codex 的核心 agent 用 **Rust** 写，而不是当时模型更擅长的 Python 或 TypeScript——这在 AI 工具链里并不常见。理由是先定下的一批设计原则：核心要**健壮、安全、高效、可扩展**，因为他们设想的是「Codex 实例跑在数百万台云端机器上」。Rust 的编译期检查与正确性保证正好对上这件事。

用不同语言把**产品界面**与**agent 核心**隔开，本身就是一条架构原则：

> "If you write everything in the same code base, in the same language, it's like, inevitably, you're going to be a little bit sloppy. And you're going to intertwine things more than you should."
>
> 「如果你把所有东西写在同一个代码库、用同一种语言，那你不可避免地会松一些，会把本来不该缠在一起的东西缠在一起。」

### 3. 为什么开源，以及为什么兼容别家模型

Codex 选择了**开源**。Tibo 讲的好处是**信任**与**贡献者社区**——公开地做，本身就有推动力；新人甚至可以先看仓库和 PR 再决定加入。他也坦承代价：有时团队做出来的东西，会先被别人抄进别的工具里发布，这件事**扎人**，但在开放里做事就是这个价钱。

开源也解释了另一件事：**Codex 能配别家的模型用**。他最直接的竞争对手（Claude Code）只能配 Anthropic 自家的模型；而即便 Codex 哪天被锁死到某个模型上，任何人仍可 fork 出这个 harness、改几行代码去支持别的模型。他的判断是：**靠「让用户用上最好的模型」取胜，而不是靠锁定**。

### 4. 本地跑，还是云上跑

Codex 默认**在你的机器上沙箱运行**，需要额外权限的动作会先问你——这是已经持续一年多的默认形态。也可以放到云上的托管 VM 里跑，那条路更接近 ChatGPT Work 的环境，更可扩展、也更不依赖你手上那台笔记本。长期方向是两者混用、再逐步把编排做得更顺。

---

## 三、Harness 与模型：谁领先谁

这是这期访谈里工程含量最高的一段。**harness** 是模型外面那一层脚手架——它给模型工具，也给它护栏、权限、指令、可操控性与可靠性上的种种弥补。

Tibo 的描述是：**harness 通常比最新模型「领先一步」**——先把缺的能力用脚手架补上，等模型自己学会了，再把这些「拐杖」一根根拆掉。每轮新模型出来，注入上下文的开发者消息会变短，harness 会变小。

团队内部因此反复问同一个问题——**这件事该改 harness，还是该等模型？**

> "It's always a question of like okay we see today that you know we are very good at this but we're not very good at this … this should be like a harness change or should this be a model change."
>
> 「总归是那个问题：今天我们这件事做得很好、那件事做得不好——这该是一次 harness 的改动，还是一次模型的改动？」

判断的依据是：模型大概多久能自己学到（一个月？三个月？半年？）。如果答案是「很快」，他们可能干脆不做 harness 的工作，等下一代模型。

一个具体例子：为了把 agent 摁在单一目标上跑上几天甚至几周，团队几个月前加了一个 `/goal` 命令；而按他的说法，**最新的模型已经不需要它了**——你直接让模型干一周就行。自己造的拐杖，自己拆掉。

---

## 四、OpenAI 内部怎么用 Codex

这是本页的正题。

### 1. 新人上手的第一句话是「你问过 Codex 了吗？」

主持人问 Tibo：给新加入 Codex 团队的人什么提示？他的回答是一句反问——

> "Have you asked Codex?"

因为**在 OpenAI，Codex 默认接进了 Slack、每一份文档、以及全部代码**。新人常常惊讶于「什么都能问」：这个项目谁在做、某个决定当初为什么这么定，都能直接问它。

这件事成立，靠的不是模型，而是**组织习惯**：团队**有意把工作放在公开频道里**，**有意把文档开成更宽的权限**。信息是敞开的，agent 才够得着。

### 2. 代码评审：模型已经「超人」，流程被强制接管

Codex 团队很早就训练了专门的代码评审模型，能追踪多层依赖、找出人类评审者要花几小时才能定位的逻辑错误。

> "These models have reached superhuman levels in code review—not just in correctness, but also in security."
>
> 「这些模型在代码评审上已经到了超人水平——不只是正确性，安全上也是。」

在 OpenAI，**所有 Pull Request 都要过强制的 AI 安全扫描**；一旦被标出安全问题，PR 会被**自动拦下、不予合并**。

但他给了一个更值得琢磨的判断：代码评审的价值**从来就不只是抓 bug**。

> "It has always been a ritual of information exchange to align teams and spark discussion—ideally occurring before code is written."
>
> 「它一直是一种信息交换的仪式——让团队对齐、激发讨论，最好发生在代码被写出来之前。」

所以他的结论是：**正确性与安全的检查会被自动化**；真正该由人花心思的是关于**意图**的讨论——

> "What exactly are you trying to do? Is this worth doing?"

这些讨论不必发生在 PR 里，但必须发生。

### 3. 维护与重构的成本正在塌缩

他把维护称为一笔**为了系统能继续跑而交的税**：升级第三方依赖、打补丁、把系统养在健康状态——过去又贵又烦，团队总往后拖，而它对安全偏偏很要紧。现在这类活大可以交给 agent：**模型能在几小时内扫完整个代码库并直接处理掉**。

更大的位移在重构：

> "In the past, a full architectural refactor might take years. Now, that cost is compressed drastically."
>
> 「过去一次完整的架构重构可能要几年；现在这个成本被大幅压缩。」

而成本下降，**不是让架构判断变得不要紧，而是更值钱**：

> "Good abstractions, clear boundaries, and explicit invariants—if you draw the shape correctly, you can change anything inside the 'box' quickly without affecting other services. Design for rapid iteration."
>
> 「好的抽象、清晰的边界、明确的不变量——只要『盒子』的形状画对了，你就能快速改它里面的任何东西，而不影响别的服务。**为快速迭代而设计。**」

### 4. 一个周末，100 个 agent 往同一个项目上贡献

> "Collaboration of this scale previously took years to expand; now it happens over a weekend."
>
> 「这种规模的协作，过去要花几年才扩张得起来；现在一个周末就发生了。」

（他描述的是 OpenAI 内部有时会出现的情形：**同一个周末里，上百个 agent 往同一个项目上贡献代码**。这句话的两半都是他说的——但请注意它说的是**协作规模**，不是「团队编制」，别读成「一个团队从几十人涨到上百人」。）

### 5. 人往上游走：意图、品味、系统掌控

把上面几节拼起来，他在团队里反复强调的三条原则是：**清晰地表达意图**、**架构品味**、**系统掌控**。他认为 AI 时代最稀缺的是两种能力：

**一是好奇心，和快速读懂系统的能力。**

> "The people who succeed at OpenAI are those who can quickly read a system, dive into a new codebase, and immediately understand its purpose."
>
> 「在 OpenAI 做得好的人，是那种能快速读懂一个系统、扎进一个新代码库、立刻明白它是干嘛的人。」

**二是把意图讲清楚，以及架构上的品味。** 当 AI 接手越来越多的执行，工程师更该做的是**把「盒子」的边界划清楚**——它该做什么、必须满足哪些不变量——而不是纠结盒子里面怎么实现：

> "Once you agree on the function and constraints of a box, what happens inside matters less."
>
> 「一旦你们对盒子的功能和约束达成一致，里面怎么实现就没那么重要了。」

以及一句近乎提纲的话：

> "If you cannot explain what you are trying to achieve, if you cannot articulate your intent, if you lack connection with the community you serve, or if you lack taste—producing good work becomes significantly harder."
>
> 「如果你讲不清自己想达成什么、说不明白自己的意图、跟你所服务的这群人没有连接、或者没有品味——想做出好作品，会难得多。」

---

## 五、合并：ChatGPT ＋ Codex

Codex 起于**本地**的编码 agent，ChatGPT 是**完全托管在云上**的产品——两套技术栈与运营方式都不一样，合并的难处在这里。合并的核心，是**把本地编码 agent 的能力高效地搬到云上**，让它进到每月 20 美元的 Plus 套餐里、服务数以亿计的用户；目前 **ChatGPT Work 里跑的就是 Codex 的 harness**，目标是把两者彻底统一成一个产品——用户在哪种形态里，都能拿到同一份智能。

一个有意思的细节：合并这件事本身，**Codex 也参与了**——干基础设施的活、补文档、跟踪争论与决定、找出两套系统之间的差异。Tibo 形容它**几乎像这个项目的记者**。

---

## 六、他自己怎么用

Tibo 把 Codex 与 ChatGPT Work 当**个人 agent** 用：记笔记、问问题、出报告、做幻灯片、探代码。他重度依赖**口述**、**手机**，以及 **Slack、Notion、Google Docs 的上下文**。

落到具体动作上，他常干这几件事：看某个功能的**用户口碑**、看**生产用量**、找**该废弃的东西**、搞清**别的团队在忙什么**，以及**隔夜把探索性的任务丢给 agent 跑**——早上起来看结果。

他对「待机状态」的看法也变了：早年为难题熬到深夜、进入心流是常态；现在他仍会打开编辑器写一点代码（因为手感舒服），但 AI 带来的好处是**更快拿到更多数据**——与其凭直觉拍板，不如先派个 agent，一分钟内拿数据回来再决定。

---

## 七、他给工程师的建议

- **好奇心**：真的想知道系统是怎么运转的；
- **快**：能迅速读懂一个新代码库、一个新系统；
- **持续问「为什么」**：一遍又一遍地问下去；
- **贴着用户**：清楚自己是在为谁做、用户要什么、产品到底该完成什么；
- **基本功还在**：系统设计、抽象、清晰、对用户的同理心、学习速度——这些并没有因为 AI 变快而过时。

关于「想做 AI 方向」的工程师，他的落点也很朴素：**品味与意图，和纯技术能力一样重要**。

---

## 📎 引语与出处索引

页内引语均出自该集逐字稿（经公开报道转引）。集中列此，便于核对：

| # | 英文原话 | 位置 |
|---|---|---|
| 1 | "If you write everything in the same code base, in the same language, it's like, inevitably, you're going to be a little bit sloppy. And you're going to intertwine things more than you should." | 为什么用 Rust |
| 2 | "It's always a question of like okay we see today that you know we are very good at this but we're not very good at this … this should be like a harness change or should this be a model change." | Harness 与模型 |
| 3 | "Have you asked Codex?" | 新人上手 |
| 4 | "These models have reached superhuman levels in code review—not just in correctness, but also in security." | 代码评审 |
| 5 | "It has always been a ritual of information exchange to align teams and spark discussion—ideally occurring before code is written." | 代码评审 |
| 6 | "What exactly are you trying to do? Is this worth doing?" | 代码评审 · 意图 |
| 7 | "In the past, a full architectural refactor might take years. Now, that cost is compressed drastically." | 维护与架构 |
| 8 | "Good abstractions, clear boundaries, and explicit invariants—if you draw the shape correctly, you can change anything inside the 'box' quickly without affecting other services. Design for rapid iteration." | 维护与架构 |
| 9 | "Collaboration of this scale previously took years to expand; now it happens over a weekend." | 协作规模 |
| 10 | "The people who succeed at OpenAI are those who can quickly read a system, dive into a new codebase, and immediately understand its purpose." | 稀缺能力 |
| 11 | "Once you agree on the function and constraints of a box, what happens inside matters less." | 稀缺能力 |
| 12 | "If you cannot explain what you are trying to achieve, if you cannot articulate your intent, if you lack connection with the community you serve, or if you lack taste—producing good work becomes significantly harder." | 三条原则 |

**出处层级**：① 节目官方页（12 条要点、15 段章节时间轴、节目说明）＝ 节目方一手；② 上表引语＝该集逐字稿原话，经公开报道转引（引号内为原话，转引渠道见下）；③ 正文中未加引号的叙述＝对该集内容的整理。转引渠道：macrostream.ai（2026-09-10）、BigGo Finance、Podscripts 逐字稿页、becurious.to 摘要、bestblogs.dev 逐字稿节选。

---

## ⚠️ 编者注

1. **本页与旧底本的关系**。此前本站曾据一份**二手口播稿转录件**（微信公众号「6KM企业AI落地」，主理人提供 docx，无署名、无日期）落过一版页面。那一版按「照录原文、只分段」处理，**忠实地照录了那份转录稿**——其中也包含**转录者自己的评论与自建框架**。**本页改以一手原件为骨架重写**，正文只保留「Tibo 说了什么」，转录稿的话术与解读**一律不收**。

2. **旧底本中最需要剔除的一件，是「可读／可操作／可迭代」这套三层框架**。它并非 Tibo 的命名或结构——那份底本自己也说得诚实：「你把这一个多小时的访谈从头看到尾，都不一定能得出接下来我要说的这一些结论。」本页因此不再采用这套框架。**若你要引用这三点，请归给这套框架的作者（该公众号），不要归给 Tibo 或 OpenAI。**

3. **「一个周末上百个 Agent」这句，两半都是 Tibo 说的**（见引语 9），指的是**协作规模**——同一周末有上百个 agent 往同一个项目上贡献。旧底本把它写成「以前一个团队一个项目要花一年才能慢慢扩张到几十上百个工程师」，那是转录者的改写，**本页已按原话校正**。

4. **必须分清「OpenAI 内部版的 Codex」与「对外卖的 Codex」**。第四节讲的「默认接入 Slack／文档／代码」「公开频道、宽文档权限」，都是 **OpenAI 内部**的用法——**对外部用户出售的 Codex 并没有这层上下文**。把内部流水线当成产品能力来预期，是读这类材料最容易踩的坑。

5. **「30 分钟拿到第一版报告」这条本页未采纳**。旧底本有此说法，但本次在一手材料里**未能核实到**；可核实的是他**用手机口述任务、把探索性任务留在隔夜跑**（见第六节）。存疑的数字宁可不写。

6. **人名与职务**：他的通行名是 **Tibo**（Thibault Sottiaux），底本里出现过「Tebow」「Table」等转写误写，本页统一为 Tibo。底本称他「Codex 负责人」——按原件，他现在的职务是 OpenAI **核心产品与平台负责人**（Head of Core Products & Platform），Codex 与 ChatGPT 都在其下。

---

> ← 返回 [🧭 AI Agent 使用最佳实践](03_xinzhi/AI_Agent使用最佳实践/README.md)　｜　相关：[Tibo：交互的变革](03_xinzhi/AI前沿认知和方法论/Tibo·交互的变革.md)（同一人的另一场访谈 · 讲产品与分发）
