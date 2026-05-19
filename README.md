# 🎸 BandoriPet — 把バンドリ角色养在桌面上！

<p align="center">
  <a href="https://github.com/HELPMEEADICE/BANDORI-PET-REV"><img alt="GitHub Repo" src="https://img.shields.io/badge/GitHub-BANDORI--PET--REV-ff69b4?logo=github"></a>
  <a href="https://github.com/HELPMEEADICE/BANDORI-PET-REV/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/HELPMEEADICE/BANDORI-PET-REV?color=blue"></a>
  <a href="https://github.com/HELPMEEADICE/BANDORI-PET-REV/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/HELPMEEADICE/BANDORI-PET-REV?color=yellow"></a>
  <a href="https://github.com/HELPMEEADICE/BANDORI-PET-REV/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/HELPMEEADICE/BANDORI-PET-REV?color=orange"></a>
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white"></a>
  <a href="https://luajit.org/"><img alt="LuaJIT" src="https://img.shields.io/badge/LuaJIT-2.1+-000080?logo=lua&logoColor=white"></a>
  <a href="https://www.live2d.com/"><img alt="Live2D" src="https://img.shields.io/badge/Live2D-Cubism%20v2-EE82EE?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNy45M2MtMy45NS0uNDktNy0zLjg1LTctNy45M3MzLjA1LTcuNDQgNy03LjkzdjE1Ljg2em0yLTE1Ljg2YzMuOTUuNDkgNyAzLjg1IDcgNy45M3MtMy4wNSA3LjQ0LTcgNy45M1Y0LjA3eiIvPjwvc3ZnPg=="></a>
  <a href="https://github.com/HELPMEEADICE/BANDORI-PET-REV"><img alt="Last Commit" src="https://img.shields.io/github/last-commit/HELPMEEADICE/BANDORI-PET-REV?color=green"></a>
</p>

> **⚠️ 免责声明：本项目仅供学习交流使用。角色模型版权归原作者及版权方所有，请勿用于商业用途。**

你是否曾幻想过香澄每天早上对你喊「キラキラドキドキ！」？你是否想在工作摸鱼的时候让友希那在一旁冷冷地盯着你（然后偷偷露出猫耳）？你是否想让爱音在你桌面上炫耀她刚学会的吉他 riff？你是否想把祥子和灯放在同一张桌面上上演属于你的 MyGO×AveMujica 小剧场……

**现在，你的梦想实现了！！！**

BandoriPet 是一个基于 Live2D Cubism SDK 和 PySide6 的开源桌面宠物项目，支持 **51+ 位** BanG Dream! 角色、**305+ 套**服装，让你的桌面一秒变成 CiRCLE 排练室！

![Example](example.png)

---

## ✨ 特性

- ⚡ **自研 LuaJIT 渲染核心** — 基于 [Live2D-v2-Lua](https://github.com/EasyLive2D/Live2D-v2-Lua)（作者 [@HELPMEEADICE](https://github.com/HELPMEEADICE)），纯 LuaJIT 实现，性能相较原 live2d-py 提升 **6 倍+**（30fps → 180fps+），支持头部追踪、拖拽移动、点击互动，老婆会跟着你的鼠标转头！
- 💬 **LLM 角色扮演聊天** — 接入大语言模型，每个角色都有专属 System Prompt，支持中日英多语言 + 动作标签。
- 🎨 **像素风桌面宠物** — 也可以切成像素小人的形态，CPU 友好，可爱不减！
- 🌓 **Fluent Design 设置面板** — 暗色/亮色主题切换，图形化选角选装界面。
- 📌 **始终置顶 + 无边框** — 趴在你的窗口上方，赶都赶不走（误）。
- 🔔 **系统托盘** — 右键一键切角色 / 开设置 / 优雅退场。
- 👥 **多角色同时显示** — 不止一个！你想放几个就放几个（只要你 GPU 撑得住）。

---

## 📦 快速开始

### 1. 环境要求

- **Python 3.10+** & **LuaJIT 2.1+**
- Windows / macOS（Apple Silicon & Intel）
- 支持 OpenGL 3.3+ 的显卡（核显也能跑）

### 2. 克隆仓库

```bash
git clone https://github.com/HELPMEEADICE/BANDORI-PET-REV.git
cd BANDORI-PET-REV
```

### 3. 下载模型文件（必需！）

> 💡 **推荐：zstd 压缩流格式模型包**（~900MB，流式加载无需解压到磁盘，性能损失极低）
>
> | 下载渠道 | 链接 |
> |----------|------|
> | 🚀 **ModelScope** | [models.zip](https://modelscope.cn/datasets/HELPMEEADICE/BanG-Dream-Live2D/resolve/master/models.zip) |
> | ☁️ **Google Drive** | [下载](https://drive.google.com/file/d/1t0TNRSV5gv2fTnFh-oWi70XNU1Xvfpub) |
> | 🐌 **百度网盘** | [下载](https://pan.baidu.com/s/1fn7DfgFQLbM6ScS-qCJLYQ?pwd=3724) 提取码：`3724` |

> 🚨 **传统 7z 模型包**（~4GB，需解压到磁盘）
>
> | 下载渠道 | 链接 |
> |----------|------|
> | 🚀 **ModelScope** | [models.7z](https://modelscope.cn/datasets/HELPMEEADICE/BanG-Dream-Live2D/resolve/master/models.7z) |
> | ☁️ **Google Drive** | [下载](https://drive.google.com/file/d/1qX9rEhBviT5auwCLg7g3klBbT5wAbjnL) |
> | 🐌 **百度网盘** | [下载](https://pan.baidu.com/s/17GAJy2_WEZZbdVdZAMfXHQ?pwd=3724) 提取码：`3724` |

下载后将 `models/` 放入项目根目录。若使用 7z 包，解压后的目录结构应为：

```
BandoriPet/
├── models/
│   ├── kasumi/
│   ├── yukina/
│   ├── anon/
│   ├── tomorin/
│   └── ...
```

### 4. 安装依赖

**创建并激活虚拟环境（macOS 必须，Windows 推荐）：**

```bash
# 创建虚拟环境（只需执行一次）
python3 -m venv venv

# 激活（macOS / Linux）
source venv/bin/activate

# 激活（Windows）
venv\Scripts\activate
```

**Python 包：**

```bash
pip install -r requirements.txt
```

**第三方依赖（从源码编译时需要）：**

```bash
mkdir third_party

# PyQt-Fluent-Widgets（必须用 PySide6 分支！）
git clone -b PySide6 --single-branch https://github.com/zhiyiYo/PyQt-Fluent-Widgets.git third_party/PyQt-Fluent-Widgets
pip install -e third_party/PyQt-Fluent-Widgets

# Live2D-v2-Lua（自研 LuaJIT Live2D 渲染核心，无需 pip install）
git clone https://github.com/EasyLive2D/Live2D-v2-Lua.git third_party/Live2D-v2-Lua
```

**macOS 额外步骤：**

macOS 需要安装 LuaJIT 并编译支持 LuaJIT 的 lupa：

```bash
brew install luajit

pip install lupa --no-binary lupa \
  --config-setting="--build-option=--with-lua-lib=$(brew --prefix luajit)/lib" \
  --config-setting="--build-option=--with-lua-include=$(brew --prefix luajit)/include/luajit-2.1"
```

### 5. 启动！

**Windows：**

```bash
python main.py
```

**macOS：**

```bash
python3 main.py
```

---

## 🧸 支持的乐队 & 角色

全部 **51 位**角色均支持 Live2D 模型显示与 **300+ 套**服装。已配置 LLM 角色扮演 Prompt 的角色可开启 AI 对话。

| 乐队 | 角色 | 服装 | LLM |
|------|------|:---:|:---:|
| **Poppin'Party** | 户山香澄 · 花园多惠 · 牛込里美 · 山吹沙绫 · 市谷有咲 | ✅ | ✅ |
| **Afterglow** | 美竹兰 · 青叶摩卡 · 上原绯玛丽 · 宇田川巴 · 羽泽鸫 | ✅ | ✅ |
| **Pastel\*Palettes** | 丸山彩 · 冰川日菜 · 白鹭千圣 · 大和麻弥 · 若宫伊芙 | ✅ | ✅ |
| **Hello, Happy World!** | 弦卷心 · 濑田薰 · 北泽育美 · 松原花音 · 奥泽美咲 | ✅ | ✅ |
| **Roselia** | 凑友希那 · 冰川纱夜 · 今井莉莎 · 宇田川亚子 · 白金燐子 | ✅ | ✅ |
| **RAISE A SUILEN** | LAYER · MASKING · LOCK · PAREO · CHU² | ✅ | ✅ |
| **Morfonica** | 仓田真白 · 桐谷透子 · 广町七深 · 二叶筑紫 · 八潮瑠唯 | ✅ | ✅ |
| **MyGO!!!!!** | 千早爱音 · 高松灯 · 要乐奈 · 椎名立希 · 长崎素世 | ✅ | ✅ |
| **Ave Mujica** | 丰川祥子 · 若叶睦 · 三角初华 · 八幡海玲 · 祐天寺若麦 | ✅ | 🚧 |
| **其他角色** | 纯田真奈 · 户山明日香 等 | ✅ | 🚧 |

> Poppin'Party 全员 + 美竹兰 + 凑友希那共 **7 位**角色已配置本地角色扮演 Prompt（`characters/` 目录）。更多角色的 Prompt 模板见 `PROMPT.md`，欢迎提交 PR 补全！

---

## 🎨 像素宠物 & 角色扮演扩展

`pixels/` 目录下目前有有咲和乐奈的像素小人（`.webp` + 动作帧配置）。

`characters/` 目录下有 40+ 位角色的高级 LLM 角色扮演 Prompt（含动作标签和表情系统）。

**想要更多像素角色？想要给未配置的角色注入灵魂？**

👉 **热烈欢迎 PR！** 只要你推的角色还没上，这就是你的回合！🎉

- 像素风格宠物：参考 `pixels/` 下的格式添加新角色动作帧即可。
- 高级角色扮演 Prompt：参考 `PROMPT.md` 和 `characters/` 下的现有 Prompt 格式。

只要你也推 XX，我们就是异父异母的亲兄弟姐妹！🥹

---

## 🏗️ 从源码打包

本项目使用 `cx_Freeze` 打包为独立可执行文件。注意打包时模型文件不会被打包进去，用户需自行下载放入 `models/`。

### Windows

```bash
python setup.py build
```

构建产物在 `BUILD/BANDORI-PET-REV-RELEASE-WIN-AMD64/` 下。

### macOS

确保已按「快速开始」章节完成 LuaJIT 和 lupa 的安装，然后执行：

```bash
python3 setup.py bdist_mac
```

构建产物为 `build/BandoriPet.app`。构建完成后将 `models/` 放入 `build/BandoriPet.app/Contents/Resources/models/`，然后双击或执行以下命令启动：

```bash
open build/BandoriPet.app
```

---

## 🤖 与 Claude Code 集成

BandoriPet 支持通过 Claude Code 的 Hooks 机制，将 Claude 的工具执行状态实时推送到悬浮窗，让角色实时展示 Claude 正在做什么。

### 前置条件

1. 在设置面板中启用 **AI 状态端口**（默认 `38472`），可选设置访问 Token。
2. 确保 `curl` 和 `jq` 已安装（macOS 自带 curl，`brew install jq` 安装 jq）。

### 配置步骤

**1. 创建 hook 脚本**

将项目根目录下的 `bandori-ai-overlay.sh` 复制到 `~/.claude/` 并赋予执行权限：

```bash
cp bandori-ai-overlay.sh ~/.claude/bandori-ai-overlay.sh
chmod +x ~/.claude/bandori-ai-overlay.sh
```

脚本通过环境变量控制行为：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `BANDORI_AI_ENDPOINT` | `http://127.0.0.1:38472/ai-events` | 事件接收地址 |
| `BANDORI_AI_TOKEN` | 空 | Bearer Token（设置面板中配置） |
| `BANDORI_AI_SOURCE` | `claude` | 悬浮窗显示的来源标签 |
| `BANDORI_AI_CHARACTER` | 空 | 指定推送给哪个角色（空则广播） |
| `BANDORI_AI_TTL_MS` | `4500` | 完成/错误状态的显示时长（毫秒） |
| `BANDORI_AI_DISABLED` | 空 | 设为 `1` 临时禁用推送 |

**2. 在 Claude Code 全局设置中注册 Hooks**

编辑 `~/.claude/settings.json`，添加以下配置：

```json
{
  "hooks": {
    "PreToolUse": [
      { "hooks": [{ "type": "command", "command": "~/.claude/bandori-ai-overlay.sh", "timeout": 3 }] }
    ],
    "PostToolUse": [
      { "hooks": [{ "type": "command", "command": "~/.claude/bandori-ai-overlay.sh", "timeout": 3 }] }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "~/.claude/bandori-ai-overlay.sh", "timeout": 3 }] }
    ],
    "UserPromptSubmit": [
      { "hooks": [{ "type": "command", "command": "~/.claude/bandori-ai-overlay.sh", "timeout": 3 }] }
    ]
  }
}
```

### 效果

配置完成后，Claude Code 执行任务时，悬浮窗会实时显示：

- 📝 **收到指令** — 用户发送 prompt 时
- 🔧 **执行命令 / 读写文件 / 搜索网页** — 工具调用时
- ✅ **完成** — Claude 回复结束时
- ❌ **出错** — 工具失败或响应中断时

### 手动推送事件

也可以直接调用命令行工具手动推送事件（适合在自己的脚本或 CI 中使用）：

```bash
# 源码目录
python bandori_ai_event.py --state stream --text "正在处理..." --source "my-script"

# 构建后的 app（macOS）
./BandoriPet.app/Contents/MacOS/bandori-ai-event --state done --text "部署完成！" --ttl-ms 5000
```

支持的 `--state` 值：`thinking` / `tool` / `stream` / `done` / `error` / `idle` / `clear`

---

## 🛠️ 技术栈

| 技术 | 用途 |
|------|------|
| **PySide6** | Qt for Python 主框架 |
| **Live2D-v2-Lua** | 自研 LuaJIT Live2D v2 渲染核心（替代 live2d-py，性能提升 6x+） |
| **lupa** | Python ↔ LuaJIT FFI 桥接 |
| **PyQt-Fluent-Widgets** | Win11 风格 Fluent Design 组件库 |
| **PyOpenGL** | OpenGL 渲染后端 |
| **cx_Freeze** | 打包为独立 exe |

---

## 📄 许可

本项目代码基于 [GPLv3](LICENSE) 开源。

角色模型、贴图、动作等资源文件版权归原版权方所有，请勿用于商业用途。

---

## 🙏 致谢

- [Live2D Cubism SDK](https://www.live2d.com/)
- [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)
- [Live2D-v2-Lua](https://github.com/EasyLive2D/Live2D-v2-Lua) — 自研 LuaJIT 渲染核心
- 所有为 BanG Dream! 角色模型做出贡献的同人作者们 💙

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=HELPMEEADICE/BANDORI-PET-REV&type=Date)](https://star-history.com/#HELPMEEADICE/BANDORI-PET-REV&Date)

---

## 🍎 本 Fork 的改动（macOS 适配）

本 Fork 基于原仓库，主要针对 macOS 进行了以下改动：

### Bug 修复

- **修复 macOS app bundle 内资源路径问题**：`lua_hit_area_projection.py` 和 `model_manager.py` 在 frozen 模式下同时查找 `MacOS/` 和 `Contents/Resources/`，解决 `band.json`、Lua 字节码等文件找不到的问题。

### macOS 构建支持

- **`setup.py`**：新增 `bdist_mac` 命令支持，可直接构建 `.app` bundle，配置了 `Info.plist`（含 `LSUIElement`）、bundle ID、图标等。
- **`macos_patch.py`**：新增原生 `NSStatusItem` 状态栏图标支持（`install_ns_status_item`），替代在 macOS 上不稳定的 `QSystemTrayIcon`。
- **`main.py`**：macOS 上使用原生状态栏图标；图标路径查找兼容 bundle 内 `Resources/` 目录；`init_tray` 延迟到事件循环启动后执行。

### 新功能

- **AI 状态悬浮窗改版**：隐藏输入框和发送按钮，悬浮窗仅作为状态展示；内容超时后自动隐藏窗口（`content_cleared` 信号）。
- **双击角色打开聊天窗口**：Live2D 和像素模式均支持双击角色直接打开聊天界面。
- **悬浮窗不抢焦点**：显示和更新时不打断其他窗口（如终端）的键盘焦点。

---

<p align="center"><strong>キラキラドキドキ！～ ✨</strong></p>
