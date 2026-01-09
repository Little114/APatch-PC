import os
import sys
#这是Little的代码,如果看到了这个注释请多多支持
def patch_boot_img(boot_img_path, password="root1234"):
    if not os.path.exists(boot_img_path):
        print(f"错误: 文件不存在 - {boot_img_path}")
        return False
    
    if not boot_img_path.lower().endswith('.img'):
        print(f"错误: 请尝试将boot.img文件拖拽到此文件上运行,或者输入指令")
        return False
    
    print(f"开始修补: {boot_img_path}")
    print(f"使用AP密码: {password}")
    
    try:
        if os.path.exists('APatch_boot.img'):
            os.system('del APatch_boot.img')
        os.system(f'magiskboot.exe unpack "{boot_img_path}"')
        
        if os.path.exists('ramdisk.cpio'):
            os.system('del ramdisk.cpio')
        
        if os.path.exists('kernel'):
            os.system('rename kernel APatch-kernel')
        
        os.system(f'kptools-x86_64-win.exe -p --image APatch-kernel --skey "{password}" --kpimg APatch.kpimg-android --out kernel')
        os.system(f'magiskboot.exe repack "{boot_img_path}"')
        
        if os.path.exists('APatch-kernel'):
            os.system('del APatch-kernel')
        if os.path.exists('kernel'):
            os.system('del kernel')
        os.system('rename new-boot.img APatch_boot.img')
        print("修补完成!\n\n你可以安全关闭此窗口\n")
        input("boot密码是: " + password)
        
    except Exception as e:
        print(f"修补过程中出现错误: {e}")
        return False

def show_usage():
    print("使用方法:")
    print("1. 拖拽方式: 直接将boot.img文件拖拽到此文件上")
    print("2. 命令行方式: 1.py boot.img [密码]")
    print("   默认密码: root1234")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        dragged_file = sys.argv[1]
        
        if len(sys.argv) > 2:
            custom_password = sys.argv[2]
            patch_boot_img(dragged_file, custom_password)
        else:
            patch_boot_img(dragged_file)
    else:
        show_usage()

        input()
