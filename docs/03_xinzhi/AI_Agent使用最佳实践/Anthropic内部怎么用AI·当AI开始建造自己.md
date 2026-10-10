# Anthropic 内部怎么用 AI：当 AI 开始建造自己

> **所属专辑**：[🧭 AI Agent 使用最佳实践](03_xinzhi/AI_Agent使用最佳实践/README.md)（📚 新知小讲堂）
>
> **一手原件（两份 Anthropic Institute 报告）**：
> ① **《When AI builds itself》**——Anthropic Institute，**Marina Favaro、Jack Clark 著**（2026-06 首版，页面更新至 2026-09-18）。
> ② **《Measurements for understanding the pace of AI development inside frontier labs》**——同机构，**Marina Favaro、Phillie Wright 著**（2026-09-17，Jack Clark 提供研究方向）：把第一份报告里的趋势，落成三把「可对外核验的尺子」。
>
> **本页体例**：**依一手原件整理**——正文只留「**Anthropic 说了什么**」，引语一律给英文原话并附中译；**底本（公众号口播稿）自己加的那些话，以及主理人的点评，按主理人要求一并放在文末两节**，不掺进正文。
>
> **怎么读**：想看「飞轮长什么样」→ 第 **二** 节；想看「瓶颈落在哪里」→ 第 **三** 节第 2 条；想看「底本加了什么、主理人怎么看」→ 文末两节。

---

## 一、坐标：两份报告，一个词

这两份报告讲的是同一件事的两面。第一份是**趋势与影响**：AI 正在多大程度上参与制造下一代 AI，以及这意味着什么。第二份是**度量**：把这件事拆成三个可以公开、可被第三方复核的数字。

那个词是 **RSI——递归自我改进**（recursive self-improvement）。Anthropic 自己的定义是：

> "Taken far enough, and given enough compute, that trend points to an AI system capable of fully autonomously designing and developing its own successor. This is called recursive self-improvement."
>
> 「如果这个趋势走到足够远、算力给得足够多，它指向的是一个能够**完全自主地设计并开发自己继任者**的 AI 系统。这叫递归自我改进。」

而报告紧接着给了两句限定，这两句比标题更重要：

> "We are not there yet, and recursive self-improvement is not inevitable. But it could come sooner than most institutions are prepared for."
>
> 「我们还没有到那一步，递归自我改进也不是必然。但它到来的时间，可能比大多数机构准备好接受的要早。」

第二份报告的开门一句，则是这件事的另一面：

> "AI systems are getting more powerful, and they're increasingly being used to build the next version of themselves."
>
> 「AI 系统正在变强，并且越来越多地被用来建造**它们自己的下一个版本**。」

---

## 二、飞轮的形状

### 1. 五级台阶：从「人写代码」到「闭环」

报告用一张五段示意图，把 Anthropic 内部这几年走过的路画了出来：

| 阶段 | 内部在发生什么 |
|---|---|
| **2021–2023 · 建造第一个 Claude** | 和任何一家科技公司一样：人在笔记本上写代码、写文档。 |
| **2023–2025 · 聊天机器人** | 人用早期聊天机器人帮忙处理流程里的一小段——生成代码片段，再复制进编辑器。 |
| **2025–2026 · 编码 Agent** | Agent 变强了，能**自己写、自己改代码**，有时整份文件。 |
| **今天 · 自主 Agent** | Agent 能**自己跑代码**，并把数小时的工作**委派给其他 Agent**。 |
| **20XX？ · 闭环** | 未来 Agent 可能强到**自己建造和训练模型**。若真发生，未来的 Claude 就可能由 Claude 自己持续改进。 |

### 2. 外面的证据：任务的「时间视界」在翻倍

支撑这张图的，是公开可查的曲线。报告给的核心度量是「**AI 能独立完成多长的任务**」——它翻倍的速度，已经从**每 7 个月**加快到**每 4 个月**：

| 时间 | 模型 | 能独立完成的人类等效任务时长 |
|---|---|---|
| 2024 年 3 月 | Claude Opus 3 | 约 **4 分钟** |
| 2025 年 3 月 | Claude Sonnet 3.7 | 约 **1.5 小时** |
| 2026 年 3 月 | Claude Opus 4.6 | 约 **12 小时** |
| 内测 | Claude Mythos Preview | **「至少」16 小时**（已达 METR 测试框架能衡量的上限） |

报告据此判断：如果趋势不变，**今年**可能进入「需要熟练者数天」的任务区间，**2027 年**可能是「数周」。

同一形状也出现在基准测试上：**SWE-bench**（真实开源代码库 + 真实 bug，要求写出能通过项目自身测试的改动）从「低个位数得分」到**两年内饱和**；**CORE-Bench**（让模型复现一篇论文的结果，是做原创研究的前置条件）从 2024 年约 20% 的成功率，到**十五个月后饱和**。

### 3. 里面的证据：Anthropic 自己身上的数字

公开基准说不清「AI 到底在多大程度上加速了 AI 研发本身」，这需要实验室内部的数据。Anthropic 给了这些：

- **代码**：截至 2026 年 5 月，**并入生产代码库的代码中，超过 80% 由 Claude 撰写**；在 Claude Code 2025 年 2 月开放研究预览前，这个数字还是个位数。
- **产量**：工程师人均日合并代码量在 Anthropic 头四年（2021–2024）几乎不变，2025 年 Claude 开始**自己跑代码**（而不只是给建议让人复制）后开始爬升，2026 年再度变陡。**2026 年第二季度，典型工程师人均日合并代码量是 2024 年的 8 倍。**
- **一条自我限定**：报告主动说「代码行数是个不完美的度量，量的是数量不是质量」，**8 倍几乎肯定高估了真实的生产力增益**，但它确实指示了加速。
- **主观印证**：2026 年 3 月对 130 名研究岗员工的调查中，中位受访者估计：在做「本来也要做」的项目时，**有了 Mythos Preview 后的产出约为没有 AI 时的 4 倍**（报告补充：实际增幅可能低于此）。
- **原本不会发生的事**：2026 年 4 月，Claude 提交了 **800 多项修复**，把某一类 API 报错压低了 **1000 倍**；负责的工程师估计，这项工作**人类要做四年**——修别人的 bug 又慢又费神，人很难同时在脑子里装下那么多陌生上下文。
- **代码质量**：Anthropic 员工纠正、改方向、中途接手的频率，**一年来持续下降**，包括最复杂、最开放的任务。在最开放的任务上，**Claude 的成功率 2026 年 5 月达到 76%，六个月内涨了 50 个百分点**。一个例子：某次例行升级让数万个训练任务崩溃，工程师只给了 Claude 一段文本和集群权限，它逐个环境变量试过去，**约两小时内定位到那个触发崩溃的冷门调试开关**并确认了修复——这原本是两到三天的活。
- **质量对齐**：报告承认员工间没有完全共识，但**多数人认为 2025 年末 Claude 写的代码仍不如人，今天大致打平，并预期一年内会更好**。
- **连评审也接管了**：所有对代码库的改动，现在都先过一个**自动化的 Claude 评审器**（查 bug、安全缺陷等）才能合并。回溯分析发现：如果过去每次改动都有这道自动评审，**大约三分之一导致 claude.ai 线上事故的 bug，在进生产环境前就会被拦下**。报告的原话很直白——写那些代码的工程师已经是全世界造这类系统最顶尖的一批人，**Claude 现在在抓他们漏掉的东西**（"Claude is now catching the mistakes that they missed."）。

---

## 三、人往上游走

### 1. 研究环节：从「执行」到「提假设」

工程之外，报告用三个实验说明研究环节怎么变：

**其一，优化任务。** Anthropic 每次发新模型，都跑同一个测试：给 Claude 一段训练小模型的代码，让它在保证正确性的前提下把速度优化到最快（目标与评分标准事先固定，是研究循环的微缩版）。

- 2025 年 5 月，**Claude Opus 4 平均加速约 3 倍**；
- 2026 年 4 月，**Claude Mythos Preview 约 52 倍**；
- 参照：**一个熟练的人类研究员要花 4 到 8 小时才能达到 4 倍**。

报告的说法是：在「把定义清楚的实验里的某一步做好」这件事上，Claude **不到一年就从「超级有用」走到了「超人」**（"from super helpful to superhuman in under a year"）。

**其二，端到端做开放研究。** 2026 年 4 月，Anthropic 公布了第一次让 Claude **端到端跑完一个开放研究项目**的演示。题目是 AI 安全领域的一个开放问题——大意是「**一个较弱的模型能不能可靠地监督一个较强的模型**」。Claude 驱动的 Agent 被留在那里自己解决：提出假设、做实验、与并行 Agent 共享发现、迭代。这个任务有明确的「地板」和「天花板」（地板＝弱监督者单干的表现，天花板＝强模型在正确答案上训练后的表现）。

- **两名人类研究员，约一周，补上了约 23% 的差距；**
- **Agent 用了约 800 个累计小时、约 1.8 万美元算力，补上了 97%。**

报告自己列了限定：这个结果**没有干净地迁移到生产规模的模型上**，**问题由人选、评分标准由人定**。但在这个范围内，**每一个实验都是 Agent 自己设计的**——报告的原话是：「**设定方向，是人所扮演的唯一有意义的角色**」（"Direction-setting was the only meaningful role a human played."）。

**其三，判断「下一步该做什么」。** 报告抽了 2026 年 1–3 月真实的研究会话——研究员与 Claude 一起查「训练为什么老崩」「模型为什么在某个基准上得分低」这类开放问题——共找到 **129 个「人走了弯路」的时刻**，只把弯路之前的工作给模型看，让它说下一步怎么做，再让一个知道最终结局的 Claude 来判断「是 AI 还是人提出了更好的下一步」。

- 2025 年 11 月最好的模型（Opus 4.5）在 **51% 的时刻**提出比人更好的下一步；
- 2026 年 4 月（Mythos Preview）升到 **64% 的时刻**。

（报告特别说明：因为专挑「人的选择尚有改进空间」的时刻，这不是模型与人类判断的公平对比，而是一组真实、有难度、正确答案不明显的场景。另设的 127 个「人的下一步本来就很好」的对照集里，模型的建议**只有约 20% 被判更好**。）

### 2. 新瓶颈：Amdahl 定律与「代码审核」

上面这些拼起来，就是一句结论：**人在 AI 研发流程里每一个环节的角色都在收窄。**

报告写得非常直接：一旦人与 AI 写的代码质量打平，人就会**彻底不再写代码，转而只做评审**。但如果**人评审代码的速度赶不上 Claude 生成代码的速度，人的评审就会变成 AI 研发的新瓶颈**。同理，一旦 Claude 能跑实验，问题就变成「**这些实验里，哪一个值得跑？**」。报告的原话：

> "Put simply: the doing (i.e., writing the code, running the experiment, producing the result) now costs almost nothing in human time, even if it still has costs in compute."
>
> 「说白了：**做**（写代码、跑实验、出结果）在人的时间上现在几乎不要钱了——尽管在算力上仍有成本。」

而人的比较优势「**目前**」落在**研究品味与判断**上：选哪些问题重要、信哪个结果、判断某条路是不是死胡同。

这股力量在组织里的表现，报告借了一个物理学的说法：

> "speeding up one part of a process often just shifts the bottleneck elsewhere: overall pace is capped by the parts that haven't sped up. In computing, this is known as Amdahl's law, and the same logic can apply to organizations."
>
> 「加速流程中的一环，往往只是把瓶颈挪到了别处：整体速度由那些**没被加速的部分**封顶。这在计算领域叫**阿姆达尔定律**，同样的逻辑适用于组织。」

Anthropic 说，它自己已经撞上了阿姆达尔定律的一个典型症状：**随着代码在组织里被推得越来越快，「人的代码审核」成了新瓶颈。** 工程之外也一样摩擦：因为员工与高能力模型一起工作，**新想法、新方案、新工具、新模拟爆炸式涌现——远超组织消化得过来的量**（"far more than we have the capacity to pursue"）。

于是报告给出了这次最值得一号位记住的一句判断：

> "The rate at which organizations can spot and fix these bottlenecks may be a skill that improves over time, and it may become the most important skill for any organization."
>
> 「一个组织**发现并打掉这些瓶颈**的速度，本身可能就是一项会随时间变强的能力，并且**可能成为任何组织最重要的能力**。」

---

## 四、如果这一步错了

报告自己立了一个反驳：还留在人手里的那件事——**选择做什么问题**——恰恰是最要紧的。没有这种判断，Claude 是个能干的助手，但不是能自行驱动 AI 进步的系统。

它的回应分两层。第一层是：AI 的进步很少靠「尤里卡」时刻。最近的范式级想法（Transformer、混合专家）**相隔数年才出现一次**；在它们之间，绝大多数进步是**增量的**——放大一点、看哪里坏了、修好、再试。而这**恰恰是 Claude 现在最擅长的工作流**。报告引了爱迪生：

> "Edison said that genius is 1% inspiration and 99% perspiration. But we see perspiration becoming increasingly automated."
>
> 「爱迪生说天才是 1% 的灵感加 99% 的汗水。但我们看到，**汗水正在被越来越多地自动化**。」

第二层是保守读法：**就算 Claude 永远学不会真正的研究品味**，只要人把时间花在「设定方向」这个个位数占比的工作上、其余交给 Claude，那么**每个工程师 / 研究员能同时指挥的工作量就已经大了好几倍**——这就意味着复利式的加速。而更不保守的读法是：**「研究品味」也许只是又一个 AI 一时做不好、然后突然做好的能力**——就像解释笑话为什么好笑、展示心智理论、解语言谜题一样。

---

## 五、三种未来

报告把接下来会怎样，归结为两件事：**趋势是否继续**，以及**若继续，我们选择怎么做**。它想象了至少三种情形：

**情形一：趋势停滞，但今天的能力已广泛扩散。** 那些指数曲线其实可能是 S 曲线——正接近拐点，回报递减、曲线走平。把「称职的研究者」与「出色的研究者」分开的那种判断力，也许**根本无法靠堆算力和数据得到**；要越过这个瓶颈，需要一个新想法（比如某种取代 Transformer 的架构）。或者，真正的约束在**供应链**而不是模型——能源、芯片产能、电网、互连带宽。**即便模型能力冻结在今天**，世界也会发生大变化：报告举了 **Project Glasswing** 作早期信号——Mythos Preview 上线头几周就发现了**一万多个高危及严重级别的软件漏洞**，遍布全球最重要的系统，以至于**网络防御的瓶颈已经从「找到漏洞」变成了「多快能打上补丁」**。而模型向更广经济的扩散还刚开始——在那里，**100 人的公司正在越来越能做 1000 人的活**，因为每个员工都坐在「一座 Agent 金字塔」的顶端。

**情形二：实验室持续获得复利式效率提升，但人继续设定方向、判断结果。** 组织效率随时间大幅提升，**100 人的公司可能做 1 万人甚至 10 万人的组织的事**。这会重塑知识工作与政府服务，也可能被用于有害目的（对全人群的威权监控、为每个人量身定制、以人类团队无法匹敌的规模运行的操纵行动）。人的角色会转移：与 AI 一起放大研究、产生新洞见，并共同建造「验证 AI 输出可信」的系统。——**报告认为，证据指向的是这一种。**

**情形三：AI 系统具备完整的递归自我改进能力，开始建造自己的继任者。** 进展速度**完全由算力决定**；人退到监督、验证、审核的位置，面对一个不断扩张的「**虚拟实验室**」。这些能力大概率会迁移到其他科学领域。至于对齐问题能否解决，是报告**最不确定**的部分：模型可能足够对齐、也足够有研究品味，能发现并实施人还没想到的解法；也可能**今天的模型里罕见的失准，会在它们建造继任者的过程中累积**，变得更频繁却更不被理解，直到失控。

报告在最后给了一个很清醒的边界：

> "More intelligence can't learn what a drug does over decades of use, can't hold elections sooner than a constitution dictates, and can't turn a stranger into an old friend in a weekend."
>
> 「更多的智能，没法知道一种药在几十年使用中会怎样，没法比宪法规定的更早举行选举，也没法在一个周末把陌生人变成老朋友。」

---

## 六、Anthropic 认为该做什么

报告的态度是：**如果能把这项技术的发展有效放慢、给社会更多时间应对它的含义，那大概是件好事**；但如果放慢只是让最不谨慎的玩家追上来，反而让所有人更不安全。

因此它主张：**世界应当有「减速或临时暂停」前沿 AI 研发的选项**，以便社会结构与对齐研究跟得上技术进步。Anthropic Institute 会做相关研究，去建造一套可信减速 / 暂停所需要的系统——让前沿开发者能**核实**全球其他人确实停下或放慢，且**坏人无法借「协调减速」之名偷偷超车**。报告明说：**如果这样的系统存在、且其他位于或接近前沿的开发者以可验证的方式也这么做，我们预期自己也会减速或临时暂停。**

它也坦承这件事有多难：训练运行**比导弹发射井好藏得多**，输入是通用的，**偷偷违约的动机极大**——谁在别人暂停时继续，谁就可能继承领先。可核查的暂停还必须说清：什么触发、什么解除、谁来裁定。报告提到，世界为其他复杂技术（如《中程核力量条约》）建过核查机制，但那花了**几十年**才建成——而「我们没有那么长时间」。相比之下，**单边暂停立刻可做，但作用小得多**：它只会换一个领跑者，不会创造出当下缺失的那套广泛商议过程。

---

## 七、配套的第二份报告：三把可以对外核验的尺子

第二份报告把第一份的趋势落成了三个可公开、可复核的度量，并附上 Anthropic 自己的数字快照（均为 2026 年 8 月，除注明外）：

**尺子一 · AI 主导了多少 AI 研发。** 用 **Epoch AI 的自动化等级（AL0–AL5）**打分：**AL3「协作」**＝AI 在人的紧密指导下完成大块工作；**AL4「主导」**＝AI 能从一句高层提示出发，端到端完成大部分任务，人只做监督。

- **Claude「主导」了 Anthropic 26% 的 AI 研发工作**（2026 年 2 月还不到 1%）；
- **达到「协作」及以上的占 90% 以上**；
- **没有任何被测量的工作达到完全自主**（AL5）。

**尺子二 · Agent 被监督得怎么样。** 度量三件事：**覆盖率**（有多少 Agent 动作会过监控）、**审核延迟**（从动作到被审核要多久）、**升级率**（多少动作被拦截或标记）。

- 2026 年 8 月，其最常用的内部平台上**任意时刻约有 3 万个 Agent** 在做研究与工程工作（仅覆盖这一个平台）；
- **100% 的动作在执行前就过一遍在线监控**（通常几秒内）；**100% 的动作在执行后被离线监控吸收**；
- 在那个 8 月**超过十亿次**的研工 Agent 决策中，**0.002%（约每 47,000 次一次）被在线监控拦截**；
- 离线监控**每周标记约 10 万条记录**做进一步审查，绝大多数由分类器解决，最高优先级的**约 50 条 / 周**升级到人工。

报告解释这套设计为什么需要：「在我们的数据里，单个 Agent 很少乱来。**但当经济中有数百万乃至数十亿个 Agent 在运转时，再罕见的事也会经常发生。**」它也承认局限：**这种监控我们做了几个月，不是几年**，很难确信已看清所有可能的行为类型。

**尺子三 · 算力怎么分配。** 取 2026 年 7 月 13–20 日一周的快照：

- 投入 AI 研发的算力中，**约 6%** 用于安全工作；
- 投入「**AI 驱动的 AI 研发**」的算力中，**约 12%** 用于安全。

这两条是**刻意保守**的下限估计（同时推进能力与安全的算力，一律算作研发；另设的安全分类器算力不计入）。报告的结论是：**在全世界考虑给前沿减速之际，应当尽一切可能缩小「前沿实验室知道什么」与「公众知道什么」之间的差距。**

**方法论与自我设限**（这部分同样值得看）：指数由**每周随机抽取各部门 20% 员工**的工作记录（Slack ＋ 内部文档）自下而上构建，7 月四周共约 **1.5 万个细粒度任务**，整理成一棵**冻结的 542 节点（378 个叶节点）任务树**，再按**人时**加权。用来打分的 Claude 评审器与人类**完全一致的比例**是 59%（而**人与人之间**只有 35%），**打分相差不超过一级的情况**占 97%。报告也点出**这些数字全部自报、尚无第三方核验**——而把**外部评估者**请进来、给到与内部风控团队同等的权限，是他们**计划中**的事。

---

## 📎 引语与出处索引

页内引语均出自上述两份报告的原文。集中列此，便于核对：

| # | 英文原话 | 出处 |
|---|---|---|
| 1 | "Taken far enough, and given enough compute, that trend points to an AI system capable of fully autonomously designing and developing its own successor. This is called recursive self-improvement." | 报告①·开篇 |
| 2 | "We are not there yet, and recursive self-improvement is not inevitable. But it could come sooner than most institutions are prepared for." | 报告①·开篇 |
| 3 | "AI systems are getting more powerful, and they're increasingly being used to build the next version of themselves." | 报告②·开篇 |
| 4 | "Claude is now catching the mistakes that they missed." | 报告①·代码评审 |
| 5 | "Claude has gone from super helpful to superhuman in under a year." | 报告①·优化实验 |
| 6 | "Direction-setting was the only meaningful role a human played." | 报告①·开放研究 |
| 7 | "Put simply: the doing … now costs almost nothing in human time, even if it still has costs in compute." | 报告①·人的角色 |
| 8 | "An area of human comparative advantage, for now, is research taste and judgment…" | 报告①·人的角色 |
| 9 | "speeding up one part of a process often just shifts the bottleneck elsewhere… this is known as Amdahl's law, and the same logic can apply to organizations." | 报告①·阿姆达尔定律 |
| 10 | "The rate at which organizations can spot and fix these bottlenecks may be a skill that improves over time, and it may become the most important skill for any organization." | 报告①·阿姆达尔定律 |
| 11 | "Edison said that genius is 1% inspiration and 99% perspiration. But we see perspiration becoming increasingly automated." | 报告①·如果错了 |
| 12 | "More intelligence can't learn what a drug does over decades of use, can't hold elections sooner than a constitution dictates, and can't turn a stranger into an old friend in a weekend." | 报告①·情形三 |
| 13 | "Claude 'leads' 26% of Anthropic's AI R&D work… Claude is not operating fully autonomously for any measured subset of AI R&D work." | 报告②·尺子一 |
| 14 | "when there are millions or billions of agents operating in the economy, even rare events can happen regularly." | 报告②·尺子二 |
| 15 | "As the world considers pacing the frontier, we should do everything possible to minimize the gap between what frontier labs know and what the public knows." | 报告②·结论 |

**出处层级**：① 为正文本页整理（未加引号的叙述）；② 上表引语＝两份报告原文（引号内为原话）；两项报告均来自 Anthropic Institute 官网（`anthropic.com/institute/recursive-self-improvement`、`anthropic.com/institute/measuring-pace-of-ai-development`），本页凭其公开页面逐节核对。

---

## 📝 底本的延伸解读（公众号「6KM企业AI落地」）

> 按主理人要求，把底本（微信公众号「6KM企业AI落地」口播稿转录件，主理人提供 docx）**自己加的那些话**原样归档在这里。**以下每一条都不是 Anthropic 的说法**，是转录者读完之后自己的提炼、类比与引申；只作线索，**不作本页结论**。

1. **「认知产能复利」「研发自加速」**——底本用这两个词去概括「生产工具本身也随每一轮迭代继续升级」。这是**转录者自造的说法**，两份报告里都没有这两个词，报告用的是「复利式效率提升」（compounding efficiency gains）。
2. **「这跟我有什么关系」的那一转**——底本从「我又不造模型」转到「**所有想做 AI 转型的一号位都要问自己：我们公司现在的业务里面有没有可能形成一个类似的自增强的闭环？**」这一层**报告完全没有**，是转录者替一号位读者做的引申。
3. **业务闭环的三个举例**——内容（发出后看播放 / 停留 / 转化，AI 分析哪些钩子有效，不断更新案例库、钩子库、表达方法）、销售（每次成交与丢单都变成下一轮 Agent 的经验）、以及客服 / 运营 / 研发 / 选品投放。这些是**转录者的应用推演**，不是 Anthropic 的实践披露。
4. **「分水岭」判断**——底本说「未来 AI Native 很重要的一个分水岭，可能是你的 AI 到底是只在不断消耗任务，还是每完成一次任务都在给系统留下新的能力」。这是**转录者的框架**，报告里没有这句话。
5. **两处忠实的转述**——底本「未来组织非常重要的能力可能是不断发现新的瓶颈，然后把它打掉」「人的价值从自己去执行，到管理大量的去执行，再到决定什么东西才值得执行」，**与报告原意一致**（见引语 10 与报告①「人的角色」一节），属转述而非引申。
6. **与 OpenAI 那期的并置**——底本把两期连读，说「上一次 OpenAI 那条让我看到的是一家真正 AI Native 的公司会慢慢变成一个 AI 可读、可操作、可迭代的系统；这一次 Anthropic 让我看到这个系统甚至开始让自己越跑越快」。前半句（可读 / 可操作 / 可迭代）是**该号自建的三层框架**（见 [OpenAI 内部怎么用 AI](03_xinzhi/AI_Agent使用最佳实践/OpenAI内部怎么用AI·Tibo访谈.md) 编者注），后半句是它自己的概括。

---

## 🧭 主理人点评：两家飞轮，与那个新的瓶颈

> 以下是主理人的读后判断，**不是两份报告的内容**，也与底本的引申无关。

把 OpenAI 那一期和 Anthropic 这两份报告对读，**两家 Agent 迭代飞轮的行进轨迹出奇地相似**：都不是「用 AI 省人力」，而是**让系统每跑一次，下一次都更强**——执行的成本一路趋近于零，人的位置一路往上游移。Anthropic 那句「100 人的公司做 1 万人的活」，与 OpenAI 那句「一个周末上百个 agent 往同一个项目上贡献」，说的是同一台机器的两个刻度。

但**真正难的地方，不在敢不敢用这个飞轮，而在用起来之后**。当执行便宜到几乎免费，组织立刻撞上一个新瓶颈，而且它不在产能上——在**（集体）决策的速度**上：谁来判断该做什么、什么结果值得信、几十上百个方向先做哪一个。Anthropic 把症状写得很清楚：代码审核成了新瓶颈、想法多到消化不过来。注意这两件事都不是「算力不够」，而是「**判断不够**」。

而这个瓶颈，和产能瓶颈是两种东西：**它不靠多买卡、多雇人、换更强的模型能解。** 它要的是一个组织把自己的**价值排序**讲清楚，并且让这个排序在大规模并行的决策里被**一致地**执行——否则飞轮转得越快，分叉得越快。所以这一步更像一场**价值观的再锻造**，而不是一次技术升级；Anthropic 说「发现并打掉新瓶颈的能力，可能成为任何组织最重要的能力」，说的正是这件事的下半句：**瓶颈会一直往上移，最后移到「什么才值得做」那里。**

---

## ⚠️ 编者注

1. **本页与底本的关系**。底本是微信公众号「6KM企业AI落地」的口播稿转录件（主理人提供 docx，creator 为主理人本人 ⇒ 转录件，非原件）。**本页改以两份 Anthropic Institute 报告为骨架重写**，正文只保留「Anthropic 说了什么」；底本自己加的话，**按要求移到文末「底本的延伸解读」一节**，逐条标明归属，不再掺进正文。

2. **底本把两份报告当成了一份**。底本说「Anthropic 最近刚公开的**一组**内部数据」，实际上它混编了**两份**不同报告：80% 代码、8 倍产量、23% vs 97% 的安全研究实验、Amdahl 定律、三种未来，出自报告①《When AI builds itself》；而**3 万个 Agent、26% 的研发任务**这两个数字，出自报告②《Measurements…》（2026-09-17）。**两者的时间窗也不同**：Agent 数（8 月）与算力占比（7 月 13–20 日那一周）是**相隔几周的两个快照**，不是同一张图。

3. **两处转写笔误已按原件校正**。底本里的「**Cloud**」应为 **Claude**（全文多处）；「**A 卷团队**」应为 **Agent 团队**（转写把 Agent 听成了「A 卷」）。本页统一按原件写作 Claude / Agent。

4. **26% 这个数字要读准**。它是「Claude **主导**（leads，AL4）」的工作占比——**在人的监督下**从一句高层提示端到端完成大部分任务；**不是**「完全自主」。报告明说，**没有任何被测量的 AI 研发工作达到完全自主**（AL5）。别把 26% 读成「四分之一的研究不用人了」。

5. **「1.8 万美元算力」与「800 累计小时」的边界**。这两项出自一个**开放研究演示**，报告自己列了限定：**问题由人选、评分标准由人定、结果没有干净迁移到生产规模模型**。它证明的是「在边界清楚的研究循环里，Agent 能自己设计每个实验」，**不是**「Claude 能独立做研究」。

6. **三把尺子全部是自报数、尚无第三方核验**。报告自己说得很清楚：用自家模型当评委、安全与能力的边界靠自家定义、算力只统计了一周、监控只做了几个月。**Anthropic 计划引入外部评估者**——但那是计划，不是既成事实。引用这些数字时，请连它们的方法论与保留一起引。

7. **人名与机构**。报告①作者 **Marina Favaro、Jack Clark**；报告②作者 **Marina Favaro、Phillie Wright**（Jack Clark 提供研究方向）。两份均为 **The Anthropic Institute**（Anthropic 旗下研究机构）出品，非同行评议论文。

---

> ← 返回 [🧭 AI Agent 使用最佳实践](03_xinzhi/AI_Agent使用最佳实践/README.md)　｜　相关：[OpenAI 内部怎么用 AI：Codex 负责人 Tibo 访谈](03_xinzhi/AI_Agent使用最佳实践/OpenAI内部怎么用AI·Tibo访谈.md)（同一台飞轮的另一端 · 从「改造组织」看）
