import os
import requests
from git.repo import Repo

Token = 'PLEASE_INPUT_YOUR_OWN_ACCESS_TOKEN'

def main():
    have_data = True
    pages = 1
    repo=[]
    headers = {
        'Authorization':'token '+ Token,
        'Accept': 'application/vnd.github.v3+json'
    }
    while have_data:
        url = "https://api.github.com/user/repos?page={}".format(pages)
        r = requests.get(url, headers=headers)
        repo_data = r.json()
        if len(repo_data) == 0:
            have_data = False
        # print(repo_data)
        for i in repo_data:   # 添加所需要的字段
            repo.append([i['name'],i['language'],i['stargazers_count'],i['forks_count'],i['ssh_url'],'fetch'])
        pages += 1

    # 查看获取到的所有仓库数据
    total_num = 0
    for i in repo:
        print(str(total_num+1) + ": " + str(i))
        total_num += 1

    # 将所有仓库下载到本地文件夹
    count = 1
    total_download = 0
    print("########################################")
    print("准备下载所有仓库至当前文件夹...")
    for i in repo:
        print("-------------------------------------------")
        print("【开始下载】-> %s/%s. %s 仓库..." % (count, total_num, i[0]))
        print("\b\b下载链接：%s" % (i[4]))
        try:
            Repo.clone_from(i[4], os.path.join(os.path.dirname(os.path.abspath(__file__)), "Repos/"+i[0]))
        except Exception as e:
            print("%s 仓库下载出错" % i[0])
            print(e)
            i[5]='Download_Error'
            continue
        i[5]='Download_OK'
        total_download += 1
        print("【下载完毕】-> %s. %s 仓库..." % (count, i[0]))
        count += 1
    print("-------------------------------------------")
    print("所有仓库处理完成")
    print("########################################")

    # 检测是否全部下载完成
    print("正在检测下载完成情况...")
    test_count = 0   # 统计正常下载的仓库数量
    for i in repo:
        if(i[5] == 'Download_Error'):
            print("下载出错: " + i[0])
        elif (i[5] == 'Download_OK'):
            test_count += 1
    if test_count == total_download:
        print("下载检测完成")
        print("您的GitHub总仓库数为：%s" % total_num)
        print("本项目下载的仓库数为：%s" % total_download)
        print("Bye^_^")

if __name__ == "__main__":
    main()