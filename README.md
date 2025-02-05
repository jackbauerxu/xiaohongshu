# 小红书工具包

## 功能特性
- 内容批量分析
- 任务队列管理
- 数据热重载机制

## 快速开始
```bash
pip install -r requirements.txt
python -m xiaohongshu_tool.core.task_manager
```xiaohongshu_tool/core/task_manager.py

## 依赖要求
- Python 3.8+
- 核心依赖：
  - requests >= 2.26.0
  - pandas >= 1.3.0
  - python-dotenv >= 0.19.0
```

## 配置示例（.env）
```ini
API_KEY=your_xhs_api_key
TIMEOUT=30
```
xiaohongshu-tool/
├── xiaohongshu_tool/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── analyzer.py      # 分析模块
│   │   ├── task_manager.py  # 任务管理
│   │   └── models.py        # 数据模型
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py        # 日志工具
│   └── __init__.py
├── tests/                   # 单元测试
│   ├── __init__.py
│   └── test_core.py
├── requirements.txt         # 依赖清单
├── setup.py                 # 打包配置
├── .gitignore
└── README.md                # 项目说明
