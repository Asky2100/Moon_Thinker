---
# Moon Thinker - AI 驱动的思维训练平台
domain:
  - multi-modal
tags:
  - AI
  - React
  - TypeScript
  - 观点讨论
  - 辩证思维
license: Apache License 2.0
---

# 🌙 Moon Thinker

**一个面向热点公共议题的 AI 驱动观点表达与讨论平台**

Moon Thinker 通过"问题驱动 + 立场分流 + 结构化评论 + AI 分析"的创新模式，重构传统社交平台的讨论流程。用户通过直观的左右滑动操作快速表达立场，系统自动将不同观点分区展示，并借助 AI 技术对讨论内容进行深度分析，帮助用户高效获取信息、理性参与讨论。

[![ModelScope](https://img.shields.io/badge/魔搭创空间-在线体验-blue)](https://www.modelscope.cn/studios/Taunomodel/Moon_Talk)
[![GitHub](https://img.shields.io/badge/GitHub-开源代码-black)](https://github.com/Asky2100/Moon_Thinker)

## 🎬 演示视频

<https://github.com/Asky2100/Moon_Thinker/releases/download/v1.0.0/Moon_Talk.mp4>

*完整的产品演示，展示了核心功能和交互流程*

## 📖 项目简介

### 核心问题
当前社交平台存在的痛点：
- ❌ 观点表达低效，讨论结构混乱
- ❌ 信息噪声过高，难以快速筛选有价值内容
- ❌ 不同立场混杂，容易引发情绪化对立
- ❌ 缺乏结构化的观点汇总与分析

### 解决方案
Moon Thinker 创新性地采用：
- ✅ **左右滑动表态** - 降低参与门槛，快速表达观点
- ✅ **立场分流展示** - 支持/反对/中立评论自动分区
- ✅ **AI 智能分析** - 自动生成观点摘要、论证质量评估
- ✅ **结构化讨论** - 清晰的信息层级，理性讨论环境

## 🎯 核心功能

### 1. 话题浏览与表态
- 📱 卡片式话题展示，移动端优先设计
- 👈👉 左右滑动快速选择立场（支持/反对）
- ⏭️ 可选择跳过，进入下一话题
- 🏷️ 话题分类标签（社会、科技、情感、哲学等）

### 2. 立场分流评论系统
- 💬 按立场自动分区的评论展示
- 📊 实时统计各立场的投票比例
- 🔄 支持评论回复与多层级讨论
- 👍👎 评论点赞/反对功能

### 3. AI 智能分析（核心创新）
- 🤖 **话题整体分析**：双方核心观点概览、分歧点提炼
- 🔍 **评论质量评估**：论证方式、证据强度、逻辑分析
- 📈 **观点聚类**：自动归纳相似观点，标签化展示
- 💡 **AI 辩证视角**：提供中立、多角度的思考维度

### 4. 用户系统
- 👤 基于 Supabase 的用户认证系统
- 📝 个人观点历史记录
- 🎨 个性化头像与资料
- 📊 参与讨论的统计数据

## 🛠️ 技术架构

### 前端技术栈
- **框架**：React 18.3.1 + TypeScript 5.8.3
- **构建工具**：Vite 7.0.0
- **UI 框架**：Tailwind CSS 3.4.17
- **路由管理**：React Router DOM 6.30.1
- **状态管理**：Zustand 4.4.7
- **动画效果**：Framer Motion 11.0.8
- **组件库**：Headless UI 1.7.18
- **图标库**：Lucide React

### 后端技术栈
- **数据库**：Supabase (PostgreSQL)
- **认证系统**：Supabase Auth
- **实时数据**：Supabase Realtime
- **AI 模型**：支持 DeepSeek、OpenAI 等兼容 OpenAI API 的大模型

### 架构设计
```
┌─────────────────────────────────────────────┐
│            前端 (React + TypeScript)         │
├─────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ 话题浏览 │  │ 评论系统 │  │ AI 分析  │  │
│  └──────────┘  └──────────┘  └──────────┘  │
├─────────────────────────────────────────────┤
│          状态管理 (Zustand)                  │
├─────────────────────────────────────────────┤
│  ┌──────────────┐      ┌─────────────────┐ │
│  │ Supabase SDK │      │ AI API (LLM)    │ │
│  └──────────────┘      └─────────────────┘ │
└─────────────────────────────────────────────┘
          │                      │
          ▼                      ▼
┌──────────────────┐    ┌─────────────────┐
│ Supabase 数据库  │    │ DeepSeek/OpenAI │
│ - 话题表         │    │ - 观点分析      │
│ - 评论表         │    │ - 摘要生成      │
│ - 用户表         │    │ - 质量评估      │
└──────────────────┘    └─────────────────┘
```

## 🚀 快速开始

### 环境要求
- Node.js 16.x 或更高版本
- npm 或 yarn 包管理器

### 本地开发

1. **克隆项目**
   ```bash
   git clone https://github.com/Asky2100/Moon_Thinker.git
   cd Moon_Thinker
   ```

2. **安装依赖**
   ```bash
   npm install
   ```

3. **配置环境变量**

   复制 `.env` 文件并填写以下配置：
   ```env
   # AI 配置
   VITE_AI_PROVIDER=deepseek              # AI 提供商: deepseek/openai
   VITE_AI_API_KEY=your_api_key_here     # AI API 密钥
   VITE_AI_BASE_URL=https://api.deepseek.com/v1
   VITE_AI_MODEL=deepseek-chat           # 模型名称

   # Supabase 数据库配置
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
   ```

4. **启动开发服务器**
   ```bash
   npm run dev
   ```
   访问 http://localhost:5173 查看应用

5. **构建生产版本**
   ```bash
   npm run build
   ```

### ModelScope 创空间部署

项目已在 ModelScope 创空间部署，支持在线体验：

1. **访问创空间**：https://www.modelscope.cn/studios/Taunomodel/Moon_Talk

2. **环境变量配置**（在创空间设置中添加）：
   ```
   AI_PROVIDER=deepseek
   AI_API_KEY=<你的 API 密钥>
   AI_BASE_URL=https://api.deepseek.com/v1
   AI_MODEL=deepseek-chat
   SUPABASE_URL=<你的 Supabase URL>
   SUPABASE_ANON_KEY=<你的 Supabase 密钥>
   ```

## 📁 项目结构

```
Moon_Thinker/
├── src/
│   ├── components/          # React 组件
│   │   ├── Header.tsx       # 头部导航
│   │   ├── SwipeCard.tsx    # 话题滑动卡片
│   │   ├── CreateTopicModal.tsx  # 创建话题弹窗
│   │   └── LoginModal.tsx   # 登录弹窗
│   ├── pages/               # 页面组件
│   │   ├── Home.tsx         # 首页（话题浏览）
│   │   ├── TopicDetail.tsx  # 话题详情页
│   │   ├── Profile.tsx      # 个人中心
│   │   └── UserProfile.tsx  # 用户资料
│   ├── store/               # 状态管理
│   │   └── useAppStore.ts   # Zustand 全局状态
│   ├── lib/                 # 工具库
│   │   └── supabase.ts      # Supabase 客户端
│   ├── types/               # TypeScript 类型定义
│   │   └── index.ts
│   ├── App.tsx              # 主应用组件
│   └── main.tsx             # 应用入口
├── dist/                    # 构建输出目录
├── public/                  # 静态资源
├── app.py                   # Python 服务器（部署用）
├── Dockerfile               # Docker 配置
└── package.json             # 项目依赖
```

## 💡 AI 创新点

Moon Thinker 的核心创新在于将 AI 技术深度融入讨论流程：

### 1. 观点提炼与摘要
- 自动分析支持方与反对方的核心论点
- 生成双方观点概览，快速把握争议焦点
- 提取关键词与高频论据

### 2. 论证质量评估
- 分析评论的论证方式（事实论证、逻辑论证、情感论证）
- 评估证据强度（高/中/低）
- 识别逻辑谬误与论证缺陷

### 3. 观点聚类与结构化
- 对相似观点进行自动聚类
- 标签化展示不同论证角度
- 构建结构化的观点知识图谱

### 4. 辩证思维引导
- AI 提供中立、多角度的分析视角
- 生成引导性问题，推动深度讨论
- 识别讨论盲点，提示补充论据

## 🎨 交互设计

### 移动端优先
- 📱 参考抖音、小红书的交互模式
- 👆 手势操作流畅自然
- ⚡ 即时反馈，强交互感

### 信息层级
```
首页 (话题卡片流)
  ↓ 左右滑动表态
话题详情页
  ├── 立场统计 (可视化图表)
  ├── AI 话题分析
  │   ├── 双方核心观点
  │   ├── 主要分歧点
  │   └── AI 辩证视角
  ├── 评论列表 (按立场分区)
  │   ├── 支持方评论
  │   ├── 反对方评论
  │   └── 中立评论
  └── 发表评论区
```

## 🌟 业务价值

### 对用户
- ⚡ **高效表达**：滑动即可表态，降低参与门槛
- 🎯 **精准筛选**：立场分区，快速定位相关观点
- 🧠 **理性思考**：AI 分析辅助，提升讨论质量
- 📊 **清晰对比**：结构化展示，理解争议焦点

### 对平台
- 📈 **提升活跃度**：清晰交互路径，增强用户粘性
- 💎 **沉淀数据**：结构化观点数据，支持深度分析
- 🔍 **应用扩展**：可扩展至舆情分析、趋势监测
- 🎓 **研究价值**：公共议题研究的数据基础

## 🔮 未来展望

### 内容生产升级
- 🤖 AI 驱动的热点话题自动获取与生成
- 📰 接入新闻平台与社交媒体热榜
- 🔄 基于时效性与热度的动态更新机制

### 功能扩展
- 🔗 多层级回复与引用功能
- 🔀 跨立场互动与观点对比视图
- 📈 观点变化趋势跟踪与分析
- 🏆 用户贡献度与影响力系统

### 应用场景拓展
- 🎓 **教育领域**：课堂辩论辅助工具
- 💼 **企业场景**：方案评审与意见收集
- 🏛️ **公共决策**：舆情分析与观点汇总
- 🔬 **学术研究**：社会议题研究平台

## 📄 开源协议

本项目基于 Apache License 2.0 开源协议。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 📧 联系方式

- GitHub: https://github.com/Asky2100/Moon_Thinker
- ModelScope: https://www.modelscope.cn/studios/Taunomodel/Moon_Talk

---

**用理性思辨，看多元世界 🌙**
