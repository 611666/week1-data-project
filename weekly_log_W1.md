# 第一周日志

## 一、环境搭建与工具配置

### 1.1 Python 环境
- 安装 Anaconda（D盘路径），配置环境变量
- 创建 `pytorch_env` 虚拟环境，Python 3.10
- 安装 PyTorch CPU 版本，验证 `import torch` 成功
- 安装 pandas 等数据处理库

### 1.2 版本控制工具
- 注册 GitHub 账号（用户名：611666）
- 安装 Git 命令行工具
- 安装 GitHub Desktop 图形客户端
- 配置 Git 用户名和邮箱
- 遇到 GitHub Desktop 首次登录授权失败，通过重新登录解决

### 1.3 云平台账号
- 注册 Google Colab，测试 T4 GPU 环境
- 注册 Kaggle 账号

### 1.4 API 服务
- 注册通义千问/智谱清言等 LLM API 服务
- 获取 API Key 并本地保存

---

## 二、综合小任务完成过程

### 2.1 项目结构设计
### 2.2 数据读取与处理（src/main.py）
- 使用 pandas 读取 `data.csv` 成绩数据
- 计算平均分、最高分、最低分
- 统计及格人数（score >= 60）
- 使用 `value_counts(bins=5)` 分析成绩分布

### 2.3 遇到的问题与解决
- **问题1**：`ModuleNotFoundError: No module named 'pandas'`
  - 解决：`pip install pandas` 安装依赖
  
- **问题2**：`TypeError: keys must be str, not Interval`
  - 原因：`value_counts(bins=5)` 生成的区间对象无法直接 JSON 序列化
  - 解决：遍历字典，将 Interval 键转换为字符串

### 2.4 输出结果
- 成功生成 `result.json`，包含完整统计数据

---

## 三、Git 版本控制实践

- 初始化本地仓库
- 第一次 commit：`初始化项目结构`（包含所有基础文件）
- 第二次 commit：`完成数据读取和统计功能`（main.py 添加注释）
- 第三次 commit：`完善文档和代码整理`（README 补充测试状态）
- 推送到 GitHub 远程仓库：https://github.com/611666/week1-data-project

---

## 四、本周收获

1. 掌握了 Anaconda 虚拟环境的管理
2. 熟悉了 pandas 数据处理和 JSON 输出
3. 学会了 Git 基本操作和 GitHub 协作流程
4. 理解了数据类型转换在 JSON 序列化中的重要性

---

## 五、下周计划

- 继续学习 Python 数据处理进阶技巧
- 尝试使用 LLM API 完成自动化任务
- 探索 Colab 云端运行环境