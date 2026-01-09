# APatch-PC - Android Boot IMG 修补工具

一个用于修补Android设备boot.img文件的Windows工具

## 功能特性

- 🔧 **一键修补** - 简单拖拽即可完成boot.img修补
- 🔒 **自定义密码** - 支持自定义AP密码保护
- 🖥️ **跨环境兼容** - 还有Python脚本源文件来尝试自己diy
- 📦 **完整打包** - 包含所有必要的工具和资源文件

## 快速开始

### 方法一：使用拖拽的方法修补（推荐）

1. 下载 `APatch_EXE.zip` 文件[win平台]
2. 将 `boot.img` 文件拖拽到 `APatch-PC` 上
3. 等待自动修补
4. 修补完成,当前目录多出APatch_boot.img
### 方法二：使用脚本加指令

1. 确保已安装Python 3.6+
2. 运行以下命令：
```bash
APatch-PC boot.img [密码]
```
3. 等待修补完毕生成APatch_boot.img

**参数说明：**
- `boot.img`：需要修补的boot镜像文件路径
- `[密码]`：可选参数，自定义AP密码（默认：root1234）


### 修补流程

1. **解包boot镜像** - 使用magiskboot工具解包原始boot.img
2. **内核重命名** - 将kernel重命名为APatch-kernel
3. **内核修补** - 使用kptools工具对内核进行APatch修补
4. **重新打包** - 将修补后的内核重新打包为boot镜像
5. **清理临时文件** - 删除过程中生成的临时文件


## 注意事项

⚠️ **重要提醒**：

- 请确保备份原始boot.img文件
- 修补后的镜像仅适用于支持APatch的设备
- 使用前请确认设备兼容性
- 错误的修补可能导致设备无法启动

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

本项目未使用任何开源许可，其全部著作权归原作者所有。

未经作者书面许可，不得复制、修改、分发或用于商业用途。

## 相关链接

- [APatch官方文档](https://apatch.dev)
- [Apatch官方GitHub](https://github.com/bmax121/APatch)
- [KernelPatch官方GitHub](https://github.com/bmax121/KernelPatch)

---

**免责声明**：使用本工具修补boot.img存在一定风险，作者不对因使用本工具导致的任何设备损坏或数据丢失负责。请在充分了解风险后谨慎使用。
