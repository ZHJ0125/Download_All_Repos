# Download All Your Repos From Github

> 下载您托管在 GitHub 的所有仓库，包括私有仓库

## 如何使用

### 0. 克隆本项目

```powershell
# 克隆本项目
X:\>git clone https://github.com/ZHJ0125/Download_All_Repos.git
# 进入项目文件夹
X:\>cd Download_All_Repos
```

### 1. 开发环境搭建 (Windows10 + Python3.x + Venv)

```powershell
# 检查 Python 版本，需要是 Python3
X:\Download_All_Repos>python -V
Python 3.7.2
# 检查 pip 是否安装
X:\Download_All_Repos>pip -V
pip 22.0.4 from D:\python\python3\install\lib\site-packages\pip (python 3.7)
# 创建并激活虚拟环境（以 Windows CMD 为例）
X:\Download_All_Repos>python -m venv env
X:\Download_All_Repos>env\Scripts\activate
# 安装依赖项
(env) X:\Download_All_Repos>pip install -r requirements.txt
```

### 2. 获取 `Personal access tokens`

由于私有仓库的访问限制，所以需要先申请 Token 才能使用本项目下载私有仓库的内容。

点击此链接 [https://github.com/settings/tokens](https://github.com/settings/tokens) 进入 Token 申请界面，点击 `Generate new token` 生成一个新 token

* `Note` 选项为 token 起一个名字
* `Expiration` 设置密钥的过期时间，我选择7天
* `Select scopes` 需要勾选 `repo`，其他选项不用勾选

最后点击 `Generate token` 生成即可

此时会跳转到 `Personal access tokens` 页面，在此页面复制您的 `Token`

***注意：确保立即复制您的个人访问令牌。你将无法再次看到它！另外，不要泄露您的 Token。***

得到 Token 之后，将其复制到 [main.py](main.py) 里的 `Token` 随对应的字符串。

### 3. 运行主程序

```powershell
# 在 Windows CMD \ venv 虚拟环境中运行
(env) X:\Download_All_Repos>python main.py
```

程序运行完成后，会在当前目录下创建 `Reops` 文件夹，并将您的所有仓库下载到此文件夹中
