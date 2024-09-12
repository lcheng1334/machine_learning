""""""
import os
"""
def test_os():
    print(os.listdir("test")) # 列出路径下内容
    print(os.path.isdir("test/a")) # 判断指定路径是不是文件夹
    print(os.path.exists("test")) # 判断指定路径是否存在
"""

def get_files(path):
    """
    使用递归方式返回此文件夹中所有的文件列表
    :param path: 被指定文件夹
    :return: List列表包含全部文件
    """
    if os.path.isdir(path):
        print(f"当前判断的文件夹是{path}")
        file_list = []
        for file in os.listdir(path):
            # print(file)
            new_path = path + "/" + file
            if os.path.isdir(new_path):
                file_list = file_list + get_files(new_path)
            else:
                file_list.append(new_path)

    else:
        print(f"指定的目录{path}不存在")
        return []

    return file_list

if __name__ == '__main__':
    # test_os()
    print(get_files("D:/code/skill/test"))