B站创作者申诉智能管理后台(Bilibili Creator Appeal AI Manager)

项目背景：针对B站内容安全业务中“创作者申诉情绪对抗”与“判罚规则理解门槛高”的痛点，打造的一套基于AI策略的申诉分流与反馈闭环原型。

🔗在线演示
点击访问实时[Demo](https://bilibili-appeal-analyzer.streamlit.app/)(注：若显示Sleeping，请点击页面按钮唤醒，约需30秒)

🎯核心业务逻辑
本项目推翻了传统的“匀速审核”思维，通过AI实现场景化分流治理：
智能分流（Routing）：利用LLM语义识别，自动区分“高危投诉（红色）”、“争议复核（黄色）”与“误伤自动释放（绿色）”。
情绪转正（Sentiment Recovery）：针对负面件自动生成同理心安抚文案，预估可降低20%的二次客诉率。
策略反哺（Insights）：实时监测规则冲突浓度，通过数据发现高误伤规则（如“二创”类），驱动底层审核策略迭代。

✨核心功能亮点
多维度看板：集成AHT（平均处理时长）预估、机审覆盖率等核心效率指标。
动态可视化：基于Altair实现的规则冲突浓度柱状图，直观展现业务瓶颈。
场景化UI：根据申诉风险等级动态调整界面元素，过滤冗余信息。

🛠️技术实现
框架：Streamlit(Python-based)
AI逻辑：基于Gemini1.5模型的Prompt Engineering及场景Mock逻辑。
可视化：Altair/Pandas数据处理。
部署：Streamlit Cloud(VibeCoding敏捷开发模式)。

📂文件结构说明
app.py:主程序逻辑，包含UI布局与AI分流引擎。
bilibili_rules.txt:模拟B站社区规则知识库，供AI检索与展示。
requirements.txt:项目依赖清单。

📝项目复盘
在本项目中，我深入权衡了AI置信度与人工干预的边界。对于低置信度的争议件（黄色场景），系统不执行自动决策，而是挂载历史判例辅助人工复核，确保了审核的严肃性与人性化的平衡。
