import streamlit as st
import os
import json
import random
import time

# 设置页面标题和布局
st.set_page_config(page_title="B站创作者申诉智能管理后台", layout="wide")

st.title("B站创作者申诉智能管理后台")

# --- 指标计算 --- 
st.subheader("核心效率指标")
col1_metric, col2_metric = st.columns(2)
with col1_metric:
    st.metric(label="AHT 降低率", value=f"{random.randint(70, 85)}%")
with col2_metric:
    st.metric(label="机审覆盖率", value=f"{random.randint(60, 75)}%")

st.markdown("---")

# 创建左右两栏
col1, col2 = st.columns(2)

with col1:
    st.header("申诉内容与规则库")

    # 申诉文本输入框
    appeal_text = st.text_area("请输入创作者申诉文本:", height=300)

    # 读取并展示规则库
    try:
        # 注意：这里保留你之前的路径
        with open("bilibili_rules.txt", "r", encoding="utf-8") as f:
            rules_text = f.read()
        st.expander("B站社区规则库").text_area("规则详情", rules_text, height=400, disabled=True)
    except FileNotFoundError:
        st.error("错误：未找到 `creator_appeal_analyzer/bilibili_rules.txt` 文件。请确保文件路径正确。")


with col2:
    st.header("智能分析与处理建议")

    if st.button("开始分析", disabled=not appeal_text):
        with st.spinner("正在进行 Mock 分析..."):
            time.sleep(1) # 模拟分析耗时
            
            # Mock 逻辑
            # 逻辑A：红色告警
            if any(keyword in appeal_text for keyword in ["注销", "曝光", "垃圾"]):
                analysis_result = {
                    "emotion_polarity": "极度负面",
                    "matching_rules": ["可能涉及账号安全或严重社区冲突"],
                    "confidence_score": 0.4
                }
            # 逻辑B：绿色分流
            elif any(keyword in appeal_text for keyword in ["授权", "原创", "误伤"]):
                analysis_result = {
                    "emotion_polarity": "正面",
                    "matching_rules": ["内容原创性申诉，可能为误判"],
                    "confidence_score": 0.9
                }
            # 逻辑C：黄色复核
            else:
                analysis_result = {
                    "emotion_polarity": "中性",
                    "matching_rules": ["常规申诉，规则匹配模糊"],
                    "confidence_score": 0.7
                }

           # --- 智能分析结果展示 ---
            st.subheader("AI 分析结果")
            st.json(analysis_result)

            st.subheader("风险等级评估")
            confidence = analysis_result.get("confidence_score", 0)
            emotion = analysis_result.get("emotion_polarity", "")
            
            action_suggestion = ""
            if confidence < 0.6 and emotion == "极度负面":
                st.error("🔴 红色（加急）：检测到高危词汇，情绪极度负面，建议人工优先处理。")
                action_suggestion = "manual_review"
            elif confidence == 0.9:
                st.success("🟢 绿色（自动）：高置信度原创申诉，建议自动处理。")
                action_suggestion = "overturn"
            else:
                st.warning("🟡 黄色（复核）：规则匹配存在模糊地带，建议人工复核。")
                action_suggestion = "manual_review"

            st.subheader("后续处理建议")
            if action_suggestion == "manual_review":
                st.info("建议：转交人工审核。")
                if emotion == "极度负面":
                    st.text_area("建议安抚回复文案", "您好，非常理解您的心情。系统已识别高优先级并转交人工复核，我们将全力保障您的合法权益，请耐心等待。", height=100)
            elif action_suggestion == "overturn":
                st.success("建议：申诉通过，执行‘释放流量’指令。")


# --- 终极对齐：全场景一致的策略分析看板 ---
            st.markdown("---")
            st.subheader("📊 策略深度分析 (Strategy Insights)")
            
            # 1. 准备统一的柱状图数据和 Altair 图表对象
            import pandas as pd
            import altair as alt

            conflict_data = pd.DataFrame({
                "类型": ["搬运/二创", "引流营销", "软色情", "不实信息"],
                "浓度": [42, 28, 15, 12]
            })

            # 强制横向坐标轴的关键：axis=alt.Axis(labelAngle=0)
            bar_chart = alt.Chart(conflict_data).mark_bar(color="#00AEEC").encode(
                x=alt.X("类型", sort=None, axis=alt.Axis(labelAngle=0, labelFontSize=12)), 
                y=alt.Y("浓度", title="冲突浓度 (%)"),
            ).properties(height=300)

            # 2. 分场景布局逻辑
            if action_suggestion == "overturn":
                # 绿色场景：仅显示提示和图表，上下排列
                st.success("✅ 申诉已通过")
                st.info("创作者诉求已满足，满意度预期回升，无需额外情绪转正处理。")
                
                st.write("**规则冲突浓度 (Conflict Density)**")
                st.altair_chart(bar_chart, use_container_width=True)
                st.caption("💡 解释：误伤点集中在‘二创’规则，建议优化该类目机审阈值。")

            else:
               # 红/黄色场景：情绪指标与图表上下对齐排列
                # 模块一：情绪分析
                with st.container():
                    st.write("**预期情绪转正率 (Sentiment Recovery)**")
                    st.progress(0.72)
                    st.info("💡 针对负面件，通过同理心文案预估可抑制 72% 的二次投诉。")
                
                st.write("") # 增加间距
                
                # 模块二：冲突分析
                with st.container():
                    st.write("**规则冲突浓度 (Conflict Density)**")
                    st.altair_chart(bar_chart, use_container_width=True)
                    st.caption("💡 解释：误伤点集中在‘搬运/二创’规则，建议优化该类目机审阈值。")
