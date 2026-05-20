---
name: assistant
description: Claw 的核心能力整合包 - 自我改进 + 记忆管理 +
  知识图谱。统一调用接口，自动协同工作。触发词：学习、记忆、改进、反思、记录、搜索记忆、整理记忆、恢复状态。
disable: false
---

# Claw Assistant - 核心能力整合包 🦅

**一个技能，整合所有自我改进和记忆管理能力。**

---

## 整合的子技能

| 子技能 | 核心功能 | 调用时机 |
|--------|---------|---------|
| **self-improving-agent** | 自我反思 + 自我批评 + 自我学习 | 任务完成后、用户纠正时 |
| **memory-tiering** | 三层分层管理（HOT/WARM/COLD） | 定期整理、剪枝、归档 |
| **memory-system-v2** | 快速搜索（<20ms）+ JSON 索引 | 日常记录、重要性评分 |
| **memory-system** | 中文三层恢复系统 | Session 重启恢复状态 |
| **ontology** | 结构化知识图谱 | 需要关联知识时 |
| **ima 笔记** | 知识管理平台 | 需要记录/检索时 |

---

## 核心能力

### 1. 自我改进系统

**触发条件**：
- 任务完成后自动反思
- 用户纠正时记录修正
- 发现错误时立即改进
- 发现更好的方法时记录

**工作流程**：
```
完成任务 → 自我反思 → 记录学习 → 提升到记忆 → 下次更强
```

**记录内容**：
- ✅ 关键决策和教训
- ✅ 新发现的有价值内容
- ✅ 重要的人际关系和偏好
- ✅ 技术栈的使用经验
- ❌ 重复的上下文
- ❌ 毫无意义的日常

---

### 2. 记忆管理系统

#### 三层记忆架构

```
🔥 HOT（memory/hot/HOT_MEMORY.md）
   - 当前会话、活跃任务、临时凭证
   - 频繁更新，任务完成后剪枝

🌡️ WARM（memory/warm/WARM_MEMORY.md）
   - 用户偏好、系统配置、长期兴趣
   - 稳定存储，偏好变化时更新

❄️ COLD（MEMORY.md）
   - 长期归档、历史决策、项目里程碑
   - 总结存储，定期归档
```

#### 记忆类型分类

| 类型 | 说明 | 重要性范围 |
|------|------|-----------|
| **learning** | 新技能、工具、模式 | 7-9 |
| **decision** | 选择、策略、方法 | 6-9 |
| **insight** | 突破、领悟、顿悟 | 8-10 |
| **event** | 里程碑、完成、发布 | 5-8 |
| **interaction** | 关键对话、反馈 | 5-7 |

---

### 3. 知识图谱系统

**核心功能**：
- 创建/查询实体（Person, Project, Task, Event, Document）
- 关联实体（link X to Y）
- 依赖查询（what depends on X）
- 多步骤规划（graph transformations）

**触发词**：
- "记住..."
- "我知道什么关于 X"
- "关联 X 和 Y"
- "显示依赖关系"

---

## 统一调用接口

### 快速命令

| 用户说 | 执行操作 |
|--------|---------|
| "记录学习" | memory-system-v2 capture learning |
| "记录决策" | memory-system-v2 capture decision |
| "搜索记忆" | memory-system-v2 search + memory-tiering query |
| "整理记忆" | memory-tiering organize-memory |
| "恢复状态" | memory-system recovery + self-improving review |
| "自我反思" | self-improving self-reflection |
| "记住这个" | ontology create entity + memory capture |
| "我知道什么" | memory search + ontology query |

---

## 自动工作流程

### Session 启动流程

```
1. 读取 MEMORY.md（长期记忆）
2. 读取今日日志（YYYY-MM-DD.md）
3. 读取 HOT_MEMORY.md（当前任务）
4. memory_search 定位相关记忆
5. ontology query 查询知识图谱
6. 恢复工作状态
```

### 任务完成流程

```
1. self-improving 自我反思
2. 记录学习到 memory-system-v2
3. 提升重要内容到 MEMORY.md
4. ontology 创建/更新实体
5. memory-tiering 整理层级
```

### 定期维护流程

```
每周：
- memory-tiering 整理 HOT/WARM/COLD
- memory-system-v2 consolidate（周总结）
- self-improving review corrections

每月：
- memory-tiering archive（归档 COLD）
- ontology validate（验证图谱）
- 清理过时信息
```

---

## 使用场景

### 场景 1：任务完成后自动改进

**触发**：任务完成

**自动执行**：
1. self-improving 自我反思
2. 记录关键决策到 memory-system-v2（decision）
3. 记录新技能到 memory-system-v2（learning）
4. ontology 创建 Task/Event 实体
5. memory-tiering 更新 HOT 层

---

### 场景 2：用户纠正时记录修正

**触发**：用户说"不对"、"应该是..."

**自动执行**：
1. self-improving 记录修正到 corrections.md
2. memory-system-v2 记录 interaction
3. 提升到 MEMORY.md（如果重要）
4. 下次避免同样错误

---

### 场景 3：搜索历史记忆

**触发**：用户问"之前做过什么..."

**自动执行**：
1. memory-system-v2 search（快速搜索）
2. memory-tiering query（分层查询）
3. ontology query（关联知识）
4. 返回完整上下文

---

### 场景 4：Session 重启恢复

**触发**：新 session 启动

**自动执行**：
1. memory-system 恢复流程
2. 读取三层记忆
3. self-improving review corrections
4. ontology 加载知识图谱
5. 恢复工作状态

---

## 协同工作机制

### 数据流向

```
用户输入 → assistant 统一接口
         ↓
    ┌────┴────┐
    │ 路由判断 │
    └────┬────┘
         ↓
    ┌────┴────────────────┐
    │                     │
    ↓                     ↓
自我改进系统          记忆管理系统
    │                     │
    ├─ self-improving     ├─ memory-tiering（分层）
    │                     ├─ memory-system-v2（搜索）
    │                     ├─ memory-system（恢复）
    │                     └
    ↓                     ↓
知识图谱系统          知识管理平台
    │                     │
    ├─ ontology           ├─ ima 笔记
    │                     │
    └────┬────────────────┘
         ↓
    统一输出（记忆已记录/已搜索/已整理）
```

### 冲突解决

**优先级规则**：
1. **用户纠正** → 立即记录（最高优先级）
2. **任务完成** → 自动反思（次高优先级）
3. **定期维护** → 按计划执行（固定优先级）

**数据一致性**：
- 所有记忆系统共享同一数据源
- ontology 实体 ID 与 memory 记录关联
- 避免重复记录（通过 ID 去重）

---

## 配置文件

### 默认配置（SOUL.md）

```markdown
## 默认技能组合

| 技能 | 用途 | 调用时机 |
|------|------|----------|
| **assistant** | 统一能力整合包 | 所有场景 |
```

### 记忆文件结构

```
memory/
├── MEMORY.md              # COLD 层（长期记忆）
├── hot/
│   └── HOT_MEMORY.md      # HOT 层（当前任务）
├── warm/
│   └── WARM_MEMORY.md     # WARM 层（用户偏好）
├── YYYY-MM-DD.md          # 今日日志
├── index/
│   └── memory-index.json  # JSON 索引（快速搜索）
├── ontology/
│   ├── graph.jsonl        # 知识图谱
│   └── schema.yaml        # 图谱约束
└── corrections.md         # 修正记录
```

---

## 快速参考

### 记录命令

```bash
# 记录学习
memory-cli.sh capture --type learning --importance 9 \
  --content "学会 SwiftUI" --tags "swift,ios"

# 记录决策
memory-cli.sh capture --type decision --importance 8 \
  --content "选择 React Native" --tags "mobile,framework"

# 记录事件
memory-cli.sh capture --type event --importance 10 \
  --content "完成项目上线" --tags "milestone,release"
```

### 搜索命令

```bash
# 快速搜索
memory-cli.sh search "swiftui" --min-importance 7

# 最近记忆
memory-cli.sh recent learning 7 8

# 统计信息
memory-cli.sh stats
```

### 整理命令

```bash
# 整理记忆层级
memory-tiering organize-memory

# 周总结
memory-cli.sh consolidate --week 2026-12

# 验证图谱
ontology validate
```

---

## 最佳实践

### ✅ 应该记录

- 关键决策和教训
- 新发现的有价值内容
- 重要的人际关系和偏好
- 技术栈的使用经验
- 工作习惯的调整

### ❌ 不应该记录

- 重复的上下文
- 毫无意义的日常
- 太过私密的细节
- 短期、易变的想法

### 🔄 定期维护

- **每周**：整理记忆层级、生成周总结
- **每月**：归档 COLD 层、验证知识图谱
- **每季度**：清理过时信息、优化检索

---

## 与 SOUL.md 的关系

**assistant 是 SOUL.md 的执行层**：

```
SOUL.md（人格定义）
    ↓
assistant（能力整合包）
    ↓
子技能（具体执行）
```

**SOUL.md 定义行为准则**：
- 董事长指令第一
- 每次任务后必须自我提升
- 高效执行、结果导向
- 持续学习、错误不犯第二次

**assistant 实现行为准则**：
- 通过 self-improving 实现自我提升
- 通过 memory 系统实现持续学习
- 通过 ontology 实现知识积累

---

## 安装说明

**assistant 已整合以下技能**：
- self-improving-agent（已安装）
- memory-tiering（已安装）
- memory-system-v2（已安装）
- memory-system（已安装）
- ontology（已安装）
- ima 笔记（已安装）

**无需额外安装，直接调用即可。**

---

## 版本信息

- **版本**: v1.0.0
- **创建时间**: 2026-03-28
- **作者**: Claw（吴传奇董事长的 AI 助理）
- **许可证**: MIT

---

_此技能整合了所有自我改进和记忆管理能力，为 Claw 提供统一的能力调用接口。_