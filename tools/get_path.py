import os

def get_path(path):
    file_list = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            # 文件名列表，包含完整路径
            # print(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            file_list.append(os.path.join(home, filename))
    return file_list


if __name__ == '__main__':
    file_list = get_path("./source/assets/images")

    for file in file_list:
        file = file.replace("./source", "")
        file = file.replace("\\", "/")
        print("- " + file)