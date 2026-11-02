# CAD Homework Agent

用 Codex 在云端通过 Python 自动完成机械制图作业：二维草图（DXF/PNG）与三维零件（STEP/STL）。本仓库提供可运行的**示例与自动化基础环境**；尚未收到两份具体作业文件，因此**不代表已完成实际作业**。

## 1. 在 Codex 云端使用

1. 在 Codex 的“创建云端环境”界面选择 GitHub 仓库 `Cyz666jason/cad-homework-agent` 和默认分支 `main`。
2. 设置环境初始化命令：`bash scripts/setup.sh`。
3. 环境创建后，在 Codex 任务中执行 `bash scripts/smoke_test.sh`，检验工具链。
4. 把两份题目资料（草图和三维零件图）加入 `inputs/`，再让 Codex 根据题目原始尺寸生成新的建模脚本及产物。

> **重要**：目前 GitHub 上此仓库是 **Public**。如果作业资料含个人信息、教师未公开的内容或需要保密，请先在 GitHub 的 Settings → General → Danger Zone → Change repository visibility 改为 **Private** 再上传文件。

## 2. 本地/云服务器安装

建议 Linux x86_64 + Python 3.11 / 3.12，内存 8 GB 起（建议 16 GB），不必配 GPU。

```bash
bash scripts/setup.sh
bash scripts/smoke_test.sh
```

单独生成演示文件：

```bash
.venv/bin/python scripts/build_example.py --out exports/demo
```

预期生成：

| 文件 | 说明 |
| --- | --- |
| `exports/demo/plate_sketch.dxf` | 二维轮廓与孔位（单位 mm） |
| `exports/demo/plate_sketch.png` | 二维预览 |
| `exports/demo/plate.step` | 可编辑/互操作的三维实体交换格式 |
| `exports/demo/plate.stl` | 三维打印/几何预览网格 |
| `exports/demo/manifest.json` | 建模参数、尺寸、体积与文件清单 |

这套演示采用一个 80×50×8 mm 的四孔安装板，仅用于**测试环境是否能正确建模**，不是你的实际作业答案。

## 3. 自动化实现方式

- **CadQuery**：Python 参数化三维实体建模和 STEP/STL 导出。
- **ezdxf**：二维 DXF 几何绘制。
- **matplotlib**：无 GUI 的草图预览图。
- **pytest**：检查生成文件、孔数、边界尺寸和几何导入。

此基础环境不强制安装 FreeCAD 或 SolidWorks。DXF 不等价于含完整约束历史的原生 CAD 草图，STEP 也不等价于 SolidWorks 的原生 `.SLDPRT`。如果老师指定 `.FCStd`、`.SLDPRT` 或 `.SLDDRW` 等格式，先确认软件与交付标准后再扩展环境。

## 4. 把实际作业交给 Codex

上传题目后，可以发送：

> 阅读 `inputs/` 下的两份作业，分别完成二维草图和三维零件。先提取题图上所有可靠的尺寸、单位、几何约束和指定的交付格式；不得自行编造缺失尺寸。生成参数化脚本和对应 DXF/STEP/STL/PNG（以题目要求为准），保存到 `exports/assignment-sketch/` 和 `exports/assignment-part/`，运行几何验证与测试，并用中文列出已完成内容、尺寸核验结果以及需要确认的问题。若题图不清晰，标出无法确定的尺寸，不得声称全部完成。

更多规则见 `AGENTS.md`。

## 5. 文件组织

```text
cad-homework-agent/
├── AGENTS.md                    # Codex 的建模与验收要求
├── .devcontainer/               # 可选的容器开发环境
├── inputs/                      # 题目文件（上传前确认隐私）
├── scripts/
│   ├── setup.sh                 # 一键装依赖
│   ├── smoke_test.sh            # 环境与示例验收
│   └── build_example.py         # 双文件示例：草图 + 三维零件
├── tests/                       # 自动核验
├── requirements.txt
└── exports/                     # 所有生成结果（默认不提交到 Git）
```

## 6. 使用边界

- 尚未提供题目文件，项目暂时只生成**测试样例**。
- 缺失的尺寸、视图或公差必须明确标记、等待补充，不能按想象完成作业。
- 机械建模无需 GPU；对 GUI 桌面交互、SolidWorks 专用格式则需要其他软件环境。
