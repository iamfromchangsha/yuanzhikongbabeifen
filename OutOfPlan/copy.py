import shutil
import os

def copy_folder_to_multiple_destinations(src, destinations):
    """
    将源文件夹复制到多个目标位置。

    :param src: 源文件夹路径（字符串）
    :param destinations: 目标文件夹路径列表（列表）
    """
    for dest in destinations:
        try:
            # 确保目标路径存在，如果不存在则创建它
            os.makedirs(dest, exist_ok=True)
            
            # 构建完整的目标路径，包含源文件夹名称
            dest_full_path = os.path.join(dest, os.path.basename(os.path.normpath(src)))
            
            # 复制文件夹及其中的所有内容
            shutil.copytree(src, dest_full_path)
            print(f"成功复制到 {dest_full_path}")
        except FileExistsError:
            print(f"跳过 {dest_full_path}，因为该文件夹已经存在")
        except Exception as e:
            print(f"复制到 {dest} 时出错: {e}")

# 示例使用
source_folder = 'images'  # 源文件夹路径
target_folders = [
    '3258002142',
'3374646309',
'3771559496',
'3913172125',
'4155148647',
'4177005826',
'4368180889',
'4439638385',
'4614250133',
'4695379693',
'4708499698',
'4982493094',
'5281993344',
'5356326142',
'5562942226',
'5568121591',
'5851299305',
'5866978584',
'5872001700',
'5889692007',
'5936021703',
'6004314276',
'6004986047',
'6008600754',
'6030109463',
'6063623782',
'6063969841',
'6096569242',
'6106125852',
'6138765177',
'6158733858',
'6181972990',
'6203424385',
'6222109362',
'6235349098',
'6235811813',
'6440383436',
'6470654773',
'6477171863',
'6486873926',
'6508222706',
'6509368661',
'6521363329',
'6543073883',
'6546496899',
]  # 目标文件夹路径列表

copy_folder_to_multiple_destinations(source_folder, target_folders)