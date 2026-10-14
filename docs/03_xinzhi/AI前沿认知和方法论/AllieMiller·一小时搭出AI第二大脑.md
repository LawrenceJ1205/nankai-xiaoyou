# Allie Miller：一小时搭出 AI「第二大脑」

> **所属专辑**：[🤖 AI 前沿认知和方法论](03_xinzhi/AI前沿认知和方法论/README.md)（📚 新知小讲堂）
>
> **一手原件**：**Silicon Valley Girl 播客**《How to Build an AI Brain in 1 Hour: 3 Documents, Zero Coding》（主持 **Marina Mogilko**，**2026-04-07** 发布 · 约 **59 分钟**；视频版标题为《Ex-Amazon AI Chief: 59-minute step-by-step tutorial on how to build your second brain with AI》）。嘉宾 **Allie K. Miller**——LinkedIn 上关注度最高的 AI 商业声音（**200 万+ 关注**）、**2025 年 TIME100 AI**；曾组建 IBM 首个多模态 AI 团队，后任 **AWS 初创企业机器学习全球负责人**，现创办顾问公司 **Open Machine**（客户含诺华、ServiceNow、华纳兄弟探索等）。本页**依节目官方页要点 ＋ 全 17 段章节时间轴 ＋ 可核对逐字稿引语**整理。
>
> **本页体例**：依一手原件整理——正文只留「**她说了什么、演示了什么**」。节目中间插入的**赞助商段落不收录**；引语一律给英文原话并附中译。
>
> **怎么读**：想照做，直接看**第五、七节**（现场演示 ＋ 三份文档）；想知道「她的系统长什么样」，看第三节；想知道「AI 到底算不算同事」，看第八节。

---

## 一、这场访谈的坐标

| 项 | 内容 |
|---|---|
| **节目** | Silicon Valley Girl Podcast（主持 **Marina Mogilko**） |
| **嘉宾** | **Allie K. Miller** |
| **嘉宾身份** | LinkedIn 关注度最高的 AI 商业声音（200 万+）；**2025 年 TIME100 AI**；前 IBM 首个多模态 AI 团队负责人；前 **AWS 初创企业机器学习全球负责人**；顾问公司 **Open Machine** 创始人兼 CEO |
| **发布** | **2026-04-07**　｜　**时长** 约 59 分钟 |
| **本页所据** | 节目官方页要点、全 17 段章节时间轴、可核对的逐字稿引语 |

主持人给这一集的定义是：「**这是我能录到的最实用的一期 AI 节目。**」一整集她都在**当场演示**——不写一行代码。

---

## 二、从「问答助手」到「替我干活的系统」

她先把过去两年分成两段。

> "Two years ago you could kind of ask AI to do research for you. You'd get back a sort of synthesis and you would have to take that knowledge and then do something with it. But now the AI system that you're using, or multiple agents, can take action on your behalf."
>
> 「两年前，你让 AI 做调研，它给你一份综述，但**接下来做什么还得你自己来**。现在不一样了——你用的 AI 系统、或者多个 Agent，**能替你采取行动。**」

她给了两档体感的差别：

> "When I look at an AI assistant that I just ask questions to and get an answer back, versus a thing that is meaningfully taking delegated work from me and managing multiple hours worth of work and workflows — this felt like 20 to 30% productive. This, depending on the task, is anywhere between like 2x and 10x."
>
> 「只用来『提问—拿答案』的 AI 助手，大概让我多了 **20% 到 30% 的产出**；而那种**真正从我手里接过活、能管好几个小时工作量与流程**的东西，看任务不同，是 **2 倍到 10 倍。**」

她说这一集想给的不只是效率，而是**一次心态切换**——「哪怕我没讲到你的具体用例，你也能把这套学法搬到你自己身上」——以及一张让她「不那么害怕」的地图。

---

## 三、她的系统：36 个工作流、约 100 个 Agent

主持人问她自己的系统到底长什么样，她报了一串数：

> "I have 36 proactive workflows with 28 master agents, and each of them spin up probably two on average. So call it 50-ish sub-agents… somewhere around like a hundred total agents."
>
> 「我有 **36 个主动式工作流**、**28 个主 Agent**，每个平均再展开大约两个子 Agent，也就是 50 来个子 Agent……**加起来大约 100 个 Agent。**」

她把重点放在「**主动**」两个字上——这是她认为最大的变化：

> "What can AI do that I don't have to kick off? …If you know that you're going to go to it every single morning and ask that question, that process of asking — not just the task itself and the prompt itself, but the task — should be automated."
>
> 「**有什么是 AI 能做、而我不必去手动发起的？**……如果你知道自己每天早上都会去问同一个问题，那**『去问』这个动作本身就该被自动化**——不只是任务和提示词，是那件事本身。」

她举了两个具体的工作流：

- **每周五的收尾**：一份「**本周尚未回复的紧急邮件**」汇总，**按紧急度排序**、附上**已经拟好的部分回复**，还带**转派给同事**的能力，以及**没回就提醒**的机制；
- **每天早上 6 点的晨报**：起床时它已经跑了好几个小时——行业新闻、当天旧金山／纽约的活动（「好让我好歹有个社交生活」）、当日着装与天气，以及**会议入场简报**：如果当天要见某位财富 500 强 CEO 或 CFO，她只要**回一个关键词**，就能**当场调起一个 Agent 为这场会议做材料**。

承接方式她说得很随意：**大多数是邮件**，按类分进不同文件夹。

---

## 四、四个 Claude，先分清用哪个

主持人请她讲清楚工具的层级，她把 Claude 拆成四层（并说明**别的厂商也在做类似的多个版本**）：

| 形态 | 它是什么 | 能不能「替你做」 |
|---|---|---|
| **Claude 网页版** | 单线程对话；能联网查；能很方便地建项目、连 Notion／Gmail 等预置连接器 | **不太行**——擅长「取回答案」，不擅长动手 |
| **Claude Cowork** | 面向职场人的 Agent 平台：**能指向你桌面上的本地文件、能直接动手**（「给我做一份 Google 文档」之类） | 能 |
| **Claude Code** | 控制力更强、能力更多、可定制更多，**也能拿来造软件** | 能，且更深 |
| **Claude 浏览器扩展** | 「有点像旁边那个随机的小表亲」：可以直接**接管你的鼠标与 Chrome 窗口**，在某个具体网站（比如做海报的页面）上替你操作 | 能，但只在一个点上 |

她的结论是：**四层里，前三层可以通用同一套 skill（技能）。**

---

## 五、现场演示：把一份「晨报」搭出来

这是整集的核心。她用**语音**对着 Claude 说了一段——**故意的口语、故意的不规整**：

> 「我每天早上都觉得压力很大，我想让你给我做一份晨报。我还不想给你我的日历和邮箱，因为我还不信任你。所以至少，我要你抓和我行业相关的资讯——我是 Apple TV 的高管，把最近的新闻和新闻稿捞出来，**至少总结三条**。这三条要按**『哪个最能让我第二天走进会议室时有面子』**、或者**『哪个被讨论得最多』**来排。第二件事，把和我行业相关的**最离谱的 AI 故事**抓出来——写的时候**每两个词就给我用一次『game changer』和『wild』**。还要给我天气，告诉我今天穿什么，我在旧金山。还有，我最近想多social一点，在结尾加上**未来四天旧金山值得去的三个活动**。」

她的点评是这集最实用的一句：

> "I just don't think about prompt engineering anymore. The rambling for 1 minute, 10 minutes is going to be more valuable. Not because it's longer, although that is helpful sometimes. It is because I have been able to communicate all that weird nuance."
>
> 「我已经**不再去想『提示词工程』了**。你**絮絮叨叨地说上一分钟、十分钟，反而更有价值**——不是因为它长（长有时确实有用），而是因为**我把那些奇怪的细节都讲出去了**。」

接着是自动化那一步：Claude 反问**两个问题**——「每天几点送？」「用什么格式送？」——她答「**6 点**」「**Word 文档**」。**就这两句，系统就开建了。** 它在右上角给出**六步进度**，第一步是「读取 skill creator 的说明」。

她还补了一个「反着用」的技巧——**让 Claude 来问你**：

> 「你可以直接说：**问我问题，帮我弄清楚一份晨报该怎么做**。」Claude 内置了一个叫 **ask user questions** 的技能，可以像面试一样逐题问下去，问到一个够用的理解度，再进入规划。

---

## 六、skill 是什么：一个工具箱

她用机械师的比喻解释 skill：

> "Imagine you're a mechanic and you have a toolbox. Let's say inside the toolbox you got a hammer, a screwdriver, a wrench… Claude has the ability to look inside of its toolbox and go, 'She's asking for this bolt — I have a wrench, this is perfect,' and start using the wrench, i.e. that skill."
>
> 「想象你是个机械师，有一个工具箱，里面有锤子、螺丝刀、扳手……Claude 能**在自己的工具箱里翻**：『她要拧这颗螺栓——我有扳手』，然后就用那个扳手，也就是那个 skill。」

但它不止会用现成的，**还能造新的**：

> "It can also build brand new tool-skill things for you. So it can add new things to your toolbox."
>
> 「它**也能替你造新的工具**——给你的工具箱里加新东西。」

她给了几个该做成 skill 的例子：**你写 LinkedIn 帖子的方式、写短视频脚本的方式、挑播客嘉宾的方式、品牌规范**，以及一个很有意思的——**「去掉 AI 腔」的 skill**（把任何产出里的 AI 味词句清掉）。

> "Basically, it is a folder. And anyone can make a folder."
>
> 「说白了，skill 就是**一个文件夹**。**谁都建得了文件夹。**」

文件夹里通常三样东西：**一份文件说明你要它做什么**（里面可以写「去访问 Gmail／Google 日历」）、**一些示例**、**一些资源**（比如你过去一年的社媒数据 CSV）。而且**它可迁移**——明天改用别的工具，把 skill 上传过去就能用。

---

## 七、先建三份文档

主持人问「一开始该建哪些文件」，她给了三份：

| # | 文档 | 内容 |
|---|---|---|
| 1 | **个人宪法（personal constitution）** | 「跟你今年是哪年、上周干了什么无关」——**你是谁、你在核心处信奉什么**。她自己的核心价值是「创业精神」「高能动性（agency）」。她说这在硅谷已流行一阵：**有些人入职时就直接把一份「个人宪法」递给你，说「了解我、研究我」。** |
| 2 | **当年的目标文档** | 可以是年度、季度、月度、周度——想养成的新习惯、想戒掉的习惯、想管理的具体输入输出（「一周跑两次」「一周至少一次家庭晚餐」「少出 30% 的差」）。 |
| 3 | **核心业务战略文档** | 不写细到「六月找了哪家供应商」，而是**做什么、服务谁、不服务谁、价值主张是什么**——加上那些**不在官网上的东西**：「我们过去三年试着做播客、没做成，原因是……」 |

她给了这个投资的最小做法：

> "You literally take this section of the podcast, take the transcript… feed it into Claude and say: 'Allie said three documents that I had to make. Ask me questions for the next hour and you are going to make these three documents for me.' And you get to go on a walk and just answer those questions."
>
> 「你就把这段播客的转录稿喂进去，跟它说：**『Allie 说了三份我该建的文档。接下来一小时你问我问题，然后帮我把这三份做出来。』**然后你就可以**去散个步，边走边答**。」

她团队的做法是**集体花一小时**：全员上 Zoom、静音但开画面，**这一小时什么都不干，只建上下文文档**——她们管它叫「**context hack**」。她的判断是：**这 20 分钟，会在你第一周省下 3 小时。**

---

## 八、为什么「AI 是实习生」这句话不对

她在这段有一个明确的态度表达：

> "I actually get pretty annoyed when I hear people say, 'Oh, AI is an intern.' I'm like, 'What intern has PhD-level intelligence, the ability to read the entire internet?'"
>
> 「听到有人说『AI 就是个实习生』，我其实挺恼火的——**哪个实习生有博士级的智能、还能读遍整个互联网？**」

她给的框架是**四层递进**：**微任务执行者（microtasker）→ 伴侣（companion）→ 委托对象（delegate）→ 队友（teammate）**。她的晨报系统属于**委托**：「我交给它活，它替我做，做完还给我」。而**队友**是「托起一整个系统，不只托起一个人」。

> "I think the people who are using AI the best… they are looking at AI as a teammate, as a first-class teammate."
>
> 「我认为**把 AI 用得最好的人，是把它当成一个队友——一个一等公民那样的队友。**」

她也点出一个组织里正在发生的问题——知识囤积：

> "I'll get success stories — amazing tales of some individuals who are AI super users getting that 3x gain, 5x gain — they are probably not sharing that insight with their teammates because they are hoarding it."
>
> 「我会听到一些成功案例——某些**AI 超级用户**拿到 3 倍、5 倍增长——但他们**大概率没把这个心得分享给同事**，因为**他们把它囤起来了。**」

所以她的建议是：**把 AI 当共享队友**，正是为了**降低那种还没跟上的人的摩擦**，让整支队伍转换得更顺。

---

## 九、怎么从一套系统搬到另一套

被问到工具选择，她说两年前她 99% 的时间用 ChatGPT，**现在 99% 的时间用 Claude Code**——但她强调自己会**刻意保持可迁移**，因为「我在教几百万人用这些东西，我得知道外面在发生什么」。她建议：

> "Pick one core AI tool — for now my main recommendations are going to be Claude, ChatGPT and Gemini — pick one of those, and you have to find time to test out their agentic versions."
>
> 「**先挑一个主力工具**（现在我主要推荐 Claude、ChatGPT、Gemini 三个里选一个），然后**一定得抽时间试它们各自的 Agent 版本。**」

而迁移之所以容易，靠的**不是平台功能，是文件组织**：

> "A lot of the agent AI systems are more simple than really technical leaders are trying to make it out to be. You can just create a very nicely organized file system and be in a really good position."
>
> 「很多 Agent 类 AI 系统，**比技术负责人试图让你以为的要简单**。你只要**建一个整整齐齐的文件系统**，位置就很好。」

---

## 十、她怎么看接下来 12 个月

节目后段她做了一个预测，重点不是「更强的 Agent」，而是一个更底层的词——**自学习**。她先拆了一个常见误解：现在你以为「它在聊天中学到了我」，其实**没有**——那只是**你的对话进了它的上下文**；它给你写的「记忆文件」，也只是加进 RAG 或即时上下文而已。

> "The actual self-learning that we might see is that the model itself might update and improve and literally learn. And like the model weights would change."
>
> 「真正可能出现的那种自学习是：**模型自己在更新、在变好、在真正地学——模型的权重会变。**」

而且触发它的**不会是人喊一句「你现在可以自学习了」**，而是某种**环境信号**：

> "It's going to be looking at some sort of environmental trigger or context… 'I've been listening to Marina's calls for the last five months… she just hired Jeff Smith, and Jeff Smith lives in New York. Therefore I just got feedback that I can update in my own brain that she picked the New York one.'"
>
> 「它会是靠某种**环境触发或上下文**……『我听 Marina 的会已经五个月了……她刚招了 Jeff Smith，而 Jeff Smith 住在纽约——**于是我自己更新了一条：她选了那个在纽约的。』**」

她把这个趋势落到一个判断上：**一年后 AI 给的建议，会和一位优秀的战略顾问相当。**

---

## 🧭 章节时间轴（依节目官方章节）

| 起点 | 章节 | 本页对应 |
|---|---|---|
| 00:00 | 开场预告 | 二 |
| 01:06 | 10 倍产出：36 个工作流、100 个 Agent，这套系统怎么运转 | 三 |
| 05:57 | 给非技术的人设置 Claude | 四 |
| 07:14 | 写提示词最好的办法：直接向 Claude 抱怨 | 二、五 |
| 09:30 | Claude Chat / Cowork / Code 有什么区别 | 四 |
| 13:24 | 现场演示：从零搭一份晨报 | 五 |
| 15:53 | Claude 里的「skill」是什么：工具箱 | 六 |
| 19:01 | 几分钟内在一套 AI 系统间迁移 | 九 |
| 20:27 | AI 是实习生还是队友——为什么这件事要紧 | 八 |
| 23:04 | 每个人都该先建的三份上下文文档 | 七 |
| 33:46 | Allie 怎么用 AI 经营她的咨询业务 | 二、三 |
| 35:40 | Allie 现场点评 Marina 的 Claude 配置 | 九 |
| 40:10 | 什么时候该信 AI，什么时候不该 | 八 |
| 46:05 | 未来 12 个月 AI 会怎样 | 十 |
| 49:45 | 你的 AI 会比你的战略顾问更懂你 | 十 |
| 52:11 | 当每个人都 10 倍产出时，团队会怎样 | 八 |
| 54:25 | 一年后的差距：用 Claude 的人与不用的人 | 九、十 |

---

## 📎 引语与出处索引

页内英文引语集中列此，便于核对：

| # | 英文原话 | 位置 |
|---|---|---|
| 1 | "Two years ago you could kind of ask AI to do research for you… But now the AI system that you're using, or multiple agents, can take action on your behalf." | 约 01:30 |
| 2 | "This felt like 20 to 30% productive. This, depending on the task, is anywhere between like 2x and 10x." | 约 01:45 |
| 3 | "I have 36 proactive workflows with 28 master agents… somewhere around like a hundred total agents." | 01:06 |
| 4 | "What can AI do that I don't have to kick off?" | 约 02:10 |
| 5 | "I just don't think about prompt engineering anymore. The rambling for 1 minute, 10 minutes is going to be more valuable." | 约 14:30 |
| 6 | "Imagine you're a mechanic and you have a toolbox… Claude has the ability to look inside of its toolbox." | 15:53 |
| 7 | "Basically, it is a folder. And anyone can make a folder." | 约 17:30 |
| 8 | "I actually get pretty annoyed when I hear people say, 'Oh, AI is an intern.'" | 约 21:00 |
| 9 | "I think the people who are using AI the best… they are looking at AI as a teammate, as a first-class teammate." | 约 21:30 |
| 10 | "They are probably not sharing that insight with their teammates because they are hoarding it." | 约 22:20 |
| 11 | "You can just create a very nicely organized file system and be in a really good position." | 约 20:00 |
| 12 | "Pick one core AI tool… and you have to find time to test out their agentic versions." | 约 19:30 |
| 13 | "The actual self-learning that we might see is that the model itself might update and improve and literally learn. And like the model weights would change." | 47:47 |
| 14 | "The advice we're going to be getting from AI in a year, they're going to be comparable to a great strategist." | 50:15 |

**出处层级**：① 节目官方页（本集要点、嘉宾身份、全 17 段章节时间轴）＝ **节目方一手**；② 上表引语＝该集逐字稿原话（官方视频与节目页所附转录；本页已按上下文校正语音转写噪声）；③ 正文中未加引号的叙述 ＝ 对上述内容的整理。

---

## ⚠️ 编者注

1. **出处与日期**：一手原件为 **Silicon Valley Girl 播客，2026-04-07 发布**（官方节目源日期；YouTube 视频版标题为《Ex-Amazon AI Chief: 59-minute step-by-step tutorial on how to build your second brain with AI》，该页标注为 2026-04-03——**两个日期差 4 天，本页取官方源日期**）。

2. **页面中段的赞助商内容不收录**。本集在「搭晨报」演示前后插了一整段 Miro 的推广（主持人自述用 Miro 做嘉宾调研的实验），该段**不是访谈内容**，本页已整段剔除。凡底本或转录页把这段并入访谈正文的，属混淆。

3. **她演示用的具体产品是 Claude（Anthropic）**，包括 Claude 网页版／Cowork／Code 与浏览器扩展。**这是「她选的工具」，不是「唯一正确的做法」**——引用时请带上「她以 Claude 为例」这层限定；她本人也明确说「先选一个主力工具，三家里哪个都行」。

4. **数字全为自述、未经审计**：36 个工作流／28 个主 Agent／约 100 个 Agent／2x–10x／20–30%，均出自她本人在节目里的说法，**没有定义、没有基线、没有第三方核验**。其中「100 个 Agent」是 36 × 每主 Agent 约 2 个子 Agent 的口头折算，她自己也在同一段里反复修正措辞（先说「几乎上千个」，随即改为「大约一百个」）——**请按「约 100 个」引**。

5. **语音转写噪声（已校正）**：底稿为自动转录，厂商与产品名多有错——`Chadgebati`＝ChatGPT、`Code-ex`＝Codex、`Co-work`＝Cowork、`cloud`／`cloud code`＝Claude／Claude Code、`jeies`＝「小玩意儿」之意、`Perplexity or Computer`＝Perplexity 的 Computer 功能。凡此类，本页按公开名称校正，不臆补。

6. **「AI 是实习生」这句话是她明确反对的说法**，属**立场句**，不是行业定论——本页照录她的原话，供读者自己判断；引用时请归给 Allie Miller，不要当成普遍共识。

7. **与第 2 篇、第 12 篇接起来读**：第 2 篇《[MIT NotebookLM 学习法](03_xinzhi/AI前沿认知和方法论/MIT_NotebookLM.md)》讲的是**怎么用 AI 学一门课**，本页讲的是**怎么用 AI 搭一套替你干活的系统**；第 12 篇吴恩达讲的「认知卸载」是**风险面**（把思考外包出去），本页讲的是**操作面**——两者并不矛盾，但读的时候请把「**让 AI 替我干活**」与「**让 AI 替我判断**」分开。

---

> ← 返回 [🤖 AI 前沿认知和方法论](03_xinzhi/AI前沿认知和方法论/README.md)　｜　相关：[MIT NotebookLM 学习法](03_xinzhi/AI前沿认知和方法论/MIT_NotebookLM.md)（怎么用 AI 学一门课）　[吴恩达：AI 正在重新给人的能力定价](03_xinzhi/AI前沿认知和方法论/吴恩达·AI重新给人定价.md)（认知卸载：外包思考的风险）　[🛠️ AI Skill 工具箱](03_xinzhi/AI_Skill工具箱/Cloud_Code.md)（动手部分）
