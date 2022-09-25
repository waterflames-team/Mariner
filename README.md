# mariner_rrx 一个RingRobotX的技能包管理器
[gitee](https://gitee.com/waterflames-team/mariner)

安装：
```shell
pip3 install mariner-rrx
```

# 使用
### 安装技能包
```shell
marx install 技能名
```

### 安装RingRobotX
```shell
marx get-rrx
```

### 安装本地的mar文件技能包
```shell
marx install-local 技能文件路径
```

### 卸载技能包
```shell
marx uninstall 技能包名
```

### 更新技能包
```shell
marx upgrade 技能包名 #更新一个
marx upgrade-all #全部更新
```

### 打包mar技能文件
```shell
marx build #在需要打包的技能目录下运行
marx build [--skill_name=技能名] #在rrx根目录或者func_packages里运行需要指定技能名
```