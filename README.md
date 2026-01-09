# APatch-PC - Android Boot Image 修补工具

一个用于修补Android设备boot.img文件的Windows工具，支持APatch内核修补功能。

## 功能特性

- 🔧 **一键修补** - 简单拖拽即可完成boot.img修补
- 🔒 **安全可靠** - 支持自定义AP密码保护
- 🖥️ **跨环境兼容** - 支持Python脚本和编译后的可执行文件
- 📦 **完整打包** - 包含所有必要的工具和资源文件

## 快速开始

### 方法一：使用可执行文件（推荐）

1. 下载 `APatch-PC.exe` 文件
2. 将 `boot.img` 文件拖拽到 `APatch-PC.exe` 上
3. 按照提示完成修补过程

### 方法二：使用Python脚本

1. 确保已安装Python 3.6+
2. 运行以下命令：
```bash
python APatch-PC.py boot.img [密码]
```

**参数说明：**
- `boot.img`：需要修补的boot镜像文件路径
- `[密码]`：可选参数，自定义AP密码（默认：root1234）

## 项目结构

```
APatch-PC/
├── APatch-PC.py          # 主程序脚本
├── APatch-PC.exe         # 编译后的可执行文件
├── magiskboot.exe        # boot镜像解包/打包工具
├── kptools-x86_64-win.exe # 内核修补工具
├── APatch.kpimg-android  # APatch内核镜像
├── boot.img              # 示例boot镜像文件
└── README.md             # 项目说明文档
```

## 技术实现

### 修补流程

1. **解包boot镜像** - 使用magiskboot工具解包原始boot.img
2. **内核重命名** - 将kernel重命名为APatch-kernel
3. **内核修补** - 使用kptools工具对内核进行APatch修补
4. **重新打包** - 将修补后的内核重新打包为boot镜像
5. **清理临时文件** - 删除过程中生成的临时文件

### 兼容性设计

项目采用PyInstaller兼容设计，支持两种运行模式：

- **开发模式**：直接运行Python脚本，使用当前目录资源
- **打包模式**：运行编译后的exe，自动从临时目录加载资源

```python
def resource_path(relative_path):
    """获取资源的绝对路径，兼容开发和打包环境"""
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
```

## 编译说明

如需自行编译，请使用以下命令：

```bash
pyinstaller --add-data "magiskboot.exe;." --add-data "kptools-x86_64-win.exe;." --add-data "APatch.kpimg-android;." --onefile APatch-PC.py
```

## 注意事项

⚠️ **重要提醒**：

- 请确保备份原始boot.img文件
- 修补后的镜像仅适用于支持APatch的设备
- 使用前请确认设备兼容性
- 错误的修补可能导致设备无法启动

## 故障排除

### 常见问题

1. **文件不存在错误**
   - 检查boot.img文件路径是否正确
   - 确保文件扩展名为.img

2. **权限不足**
   - 以管理员身份运行程序
   - 检查文件读写权限

3. **修补失败**
   - 确认boot.img文件完整性
   - 检查设备兼容性
   - 尝试使用默认密码

## 许可证

本项目基于开源许可证发布，具体许可证信息请查看LICENSE文件。

## 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 更新日志

### v1.0.0 (2024-01-09)
- 初始版本发布
- 支持基本的boot.img修补功能
- 实现跨环境兼容性
- 提供可执行文件和Python脚本两种使用方式

## 相关链接

- [APatch官方文档](https://apatch.dev)
- [Magisk项目](https://github.com/topjohnwu/Magisk)
- [Android Boot Image格式说明](https://source.android.com/docs/core/architecture/bootloader/boot-image-header)

---

**免责声明**：使用本工具修补boot.img存在一定风险，作者不对因使用本工具导致的任何设备损坏或数据丢失负责。请在充分了解风险后谨慎使用。