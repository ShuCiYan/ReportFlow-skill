# Model Recommender

先识别 Decision Goal、对象、证据类型和不确定性，再从 `models/library.yaml` 选择 1–3 个互补方法。推荐输出必须包括 `Model | Why fit | Required evidence | Limitation | Do not use when`。

禁止因为模型存在于库中就自动使用。若模型会制造未经证据支持的评分、排名或因果关系，拒绝推荐并说明原因。跨类别组合必须解释每个模型承担的不同工作。

## Routing examples

- 行业结构/竞争：Value Chain + Porter；不自动加 SWOT。
- 用户任务/产品：JTBD；需要优先级时再加 RICE；有可检验实验时再加 A/B Test。
- 留存下降：Cohort + Interview；只有存在随机分流条件才推荐 A/B Test。
- 工业设备经济性：Unit Economics + Scenario/Sensitivity；不得用 PMF 或 Hook 替代项目成本数据。
