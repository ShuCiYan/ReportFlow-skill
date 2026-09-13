# 章节问题与证据路由

这是主技能的按章参考。每章先选最相关的问题，再按统一 Master Fact Base 和 Claim–Evidence 规则执行。

## Chapter 3｜技术体系、任务能力与技术成熟度

核心问题按六组组织：任务所需能力；模型和数据改变了什么；真实环境中能完成哪些任务；指标及测试条件如何解释；Benchmark与客户任务之间差距多大；关键瓶颈及未来12–24个月观察指标。证据分层为 `Research → Supplier Test → Independent/Relevant-condition Test → Customer-site → Normal Operation`。完整技术栈、VLM/VLA/World Model、移动/抓取/双臂/灵巧操作和长序列任务均须回到具体任务与测试条件。

优先证据：原始论文、Benchmark/Dataset项目页、企业技术白皮书、客户任务数据、NIST、NASA TRL、DOE ARL。必须区分研究基准、评测框架、训练基础设施、供应商测试和客户现场证据；不同机器人、任务、环境、指标和测试条件不得直接排名。

## Chapter 4｜产业链、供应链、制造体系与价值捕获

新增核心问题 Q0｜Current Supply Chain Reality：当前具身智能机器人的上游核心供给、中游产品化与下游客户/应用分别由哪些环节构成？各环节提供什么，采用自研、外采、定制采购、联合开发还是系统集成？哪些可依托汽车、工业机器人、消费电子和精密制造等邻近产业，哪些仍处于人形专门适配、验证和量产爬坡？哪些环节供应选择较丰富，哪些仍高度定制？必须同时记录批量良率、寿命、一致性、单位成本、MTBF、实际产量、产能利用率、替换周期和售后能力的Unknown，不得把缺失数据自动判断为瓶颈。

核心问题：BOM和高价值部件是什么？关节、执行器、减速器、丝杠、电机、灵巧手、触觉、计算和电池分别如何验证？规模生产卡在哪里？每个环节还要回答当前瓶颈、供应商/设计切换代价和价值捕获位置。总成与零件不得重复计算；企业自制、外购、联合开发、系统集成分别标注。

优先证据：供应商规格、上市公司年报/招股书、采购价格、产能公告、成本披露和制造资料。不得把售价写成BOM，不得把BOM下降写成TCO下降。核心问题是“放量时谁真正赚钱”。

Supply Chain Fact Base字段：`Supply Chain Position → Module/Component → Function → Representative Suppliers/OEM Participation → Self-developed/Procured/Customized/Co-developed/Integrated → Adjacent-industry Base → Humanoid-specific Adaptation → Current Evidence → Evidence Confidence → Key Unknown → Commercial Meaning`。必须先完成上游—中游—下游结构，再进入Delivery/Value Chain分析。

视觉优先问题：客户任务如何经过部件、模组、整机、测试、客户现场集成和售后形成价值捕获？哪些环节已有直接证据，哪些仍为部分证据或 Unknown？优先考虑机制/价值链图、切换成本×差异化/稀缺性矩阵、规模化链条阶段图和中国制造基础与人形量产能力的左右对照；不得将政策目标、产线规划或融资画成实际放量。

## Chapter 5｜市场规模、市场结构与竞争格局

建立 Market Size Definition Table，记录机构、机器人定义、是否包含非人形、时间、出货/安装/收入口径和预测假设。市场边界不可拼接；预测上下限不是统计置信区间；科研、教育和展演采购也可构成真实付费市场，但必须与工业生产市场分开。无必要时不自建宏大 TAM。

竞争研究从 Customer → Task → Budget → Existing Alternative 开始；只有 Same-market Check 通过才做直接比较。视觉优先使用竞争边界图、替代方案矩阵或同口径比较表，不从公司名单或未经定义的排名开始。

## Chapter 6｜应用场景、客户任务与真实需求

研究单位：`Customer × Task × Existing Alternative × Robot Advantage × Required KPI`。不问“为什么需要人形”，而问相较替代方案是否创造增量价值。记录 Buying Center：使用部门、运营负责人、采购、信息化/安全、财务和最终批准者；按行业、任务、客户类型、部署阶段和证据侧别采样。客户个体反馈不等于总体结论。

## Chapter 7｜部署成熟度与商业采用证据

严格沿用第一章冻结的部署/使用证据轨、商业/交易/财务证据轨、Evidence Confidence 和 Scale Gate。不得恢复 T/C 评分，也不使用 `D×C+E` 等综合公式。逐案区分 Demo、PoC/Pilot、Paid Pilot、Binding Order、Delivery、Acceptance、Normal Operation、Payment/Revenue、Renewal/Repurchase、Multi-site 和 Independent Customer Replication。

## Chapter 8｜代表企业深度研究

四家公司使用双页式组织：第一页回答公司、产品、技术、客户与任务；第二页回答商业证据、交付、收入/订单/融资、客户/供应商经济性、风险、替代解释和未来验证指标。未披露不等于零；非目标业务收入不得替代人形机器人业务收入；既有业务能力能否迁移到人形机器人属于 Analysis。

## Chapter 9｜四家公司横向竞争与商业化路径比较

比较产品路径、技术路径、客户路径、场景、标准化程度、交付方式、商业证据、收入质量、复购、生态、成本、服务、资本结构和 Scale Gate；每个结论同时回答是否属于同一市场、机制、替代解释、边界和反证。不做脱离口径的总分排名。

必须执行 `Observed Difference → Mechanism → Alternative Explanation → Boundary → Disconfirming Evidence`；竞争对象区分 Direct Competitor、Adjacent Competitor、Alternative Solution 和 Future Competitor。机器人企业之间的比较不能替代客户现实替代方案比较。

## Chapter 10｜客户、开发者与公开用户反馈

来源包括客户公告、开发者社区、GitHub、论坛、公开访谈和 Reddit 等。记录平台、时间窗、版本、真实使用者判定、纳入/排除、去重、利益关联、编码字典、AI聚类和人工复核；AI聚类不提升样本代表性。个体反馈必须标注为个案。

## Chapter 11｜商业模式、交付体系与客户/供应商经济性

分三层记录：客户经济性、供应商经济性、交付系统。客户侧记录 TCO、ROI、Payback、利用率、部署周期、工程天数、定制、维护和人工替代；供应商侧记录 BOM、毛利、良率、保修、现场服务、回款、现金流、SLA 和服务网络；交付系统记录安装、验收、培训、复位和持续服务。毛利不等于现金流，RaaS不自动意味着高利润，收益不得重复计算。

## Chapter 12｜风险、规模化条件与行业 SWOT

SWOT必须来自前11章证据，不得在本章首次提出重大结论。每项风险记录 Risk、Mechanism、Evidence、Thesis Affected、Trigger、Impact、Mitigation/What to Watch，至少覆盖技术、硬件、供应链、客户经济性、交付、资本、监管、安全、竞争、替代技术和宏观需求。

## Chapter 13｜核心结论与未来12–24个月观察指标

输出 Investment Thesis、Supporting Evidence、Key Uncertainties、Disconfirming Evidence、12–24 Month Signals。无统一队列、分母和观察窗口时，不计算 Pilot 转化率。Repurchase、Multi-site、Independent Customer 分别记录；Leading/Lagging 指标说明相对目标或结果。指标优先使用常态运行小时、人工介入率、故障率、验收、TCO、Payback、毛利、服务成本、交付周期和回款。

## Chapter 14｜AI辅助产业研究方法与可复用SOP

记录 AI 的 Query Design、Source Discovery、Fact Extraction、Conflict Detection、Evidence Grading、Claim Mapping、反例发现和结构化作用；Evidence Ledger记录版本/访问时间，另建 Metric Dictionary、纳入/排除规则、Conflict Log、AI模型/日期、Human Correction Log、Stop Rule、AI Error Log和AI/人工耗时。人工负责边界、原始来源核验、事实认定、权重和最终判断。AI不是证据来源。SOP：Define Question → Source List → Search → Extract → Verify → Unknown/Disputed → Compare → Counterargument → Judgment → Audit。

## Chapter 15｜主要参考资料

只从全局 Canonical Source Registry 生成。不得手工重新编号，不得遗漏正文使用来源，也不得加入正文没有使用的无关条目。
