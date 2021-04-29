https://zhuanlan.zhihu.com/p/144499776
1:环境
    1:创建环境
        conda create -n env_name python=3.7 --clone another_env
            -n          新环境名字
            python=3.7  使用 python 版本
            --clone     从其他环境复制
        conda create -n hybfkuf --clone base            # 不指定 python 版本
    2:删除环境
        conda remove -n env_name --all
    3:查看环境
        conda env list
        conda info -e
    4:激活环境
        conda activate env_name
        source activate env_name
    5:退出环境
        conda deactive
        source deactive
    6:not activated on startup
        conda config --set auto_activate_base false
    7:conda for shell
        conda init bash
        conda init zsh
        conda init fish

2:包相关
    1:查看当前环境包列表
        conda list
        conda list -n env_name
    2:安装包
        conda install package_name
        conda install package_name_1 package_name_2
        conda install package_name=1.1.0
        conda install scipy=0.15.0 curl=7.26.0 -n py34_env
            # 向当前环境安装多个包,并指定包版本与python版本,一般情况下不用指定python版
        conda install --name myenv scipy
            # 向指定虚拟环境中安装指定包
        conda install pip           # 安装 pip 到当前虚拟环境
        pip install numpy
    3:更新包
        conda update unmpy          # 更新指定包
        conda update                # 更新所有包
        conda update python         # 更新 python
        conda update conda          # 更新 conda 本身/库
        conda update anaconda
        conda upgrade --all
    4:卸载包
        conda remove scipy
        conda remove scipy curl
        conda remove -n myenv scipy     # 删除指定环境下的包
    5:搜索包
        conda search search_item

3:重现环境
    # 1:使用conda管理python一个重要的考量就是可迁移性
    # 2:spec list 文件和 environment.yml 文件之间的区别在于： 
    #   1:environment.yml 文件不针对特定操作系统，并且使用YAML格式。
    #     environment.yml 仅列出了软件包名称，由 conda 基于软件包的名称构建环境。 
    #   2:另一个区别是 -export 还包括使用pip安装的软件包，而 spec list 则没有
    1:clone
        conda create --name new_env --clone old_env
    2:Spec List
        # 相同操作系统的计算机之间复制环境，可以生成 spec list
        conda list --explicit > spec-list.txt                   # 生成 spec list 文件
        conda create --name python-course --file spec-list.txt  # 重现环境
    3:Environment.yml
        conda env export > environment.yml      # 导出 environment.yml 文件
        conda env create -f environment.yml     # 重现环境

4:Conda Pack 重现环境
    # 1:spec list 和 environment.yml 文件都基于记录当前环境包信息，到新机器重建的思路。
    #   而Conda Pack用的是将当前环境的文件直接打包，带到新机器拆包使用的思路
    # 2:conda-pack 指定平台和操作系统，目标计算机必须具有与源计算机相同的平台和操作系统
    1:安装 conda pack
        conda install -c conda-forge conda-pack     # 从 conda 安装
        pip install conda-pack                      # cong pip 安装
    2:打包环境
        conda pack -n my_env
        conda pack -n my_env -o out_name.tar.gz
    3:重现环境
        mkdir -p path_to_my_new_env # 建议放在anaconda的envs文件夹中
        tar -xzf my_env.tar.gz -C path_to_my_new_env # 解压包中文件
        source path_to_my_new_env/bin/activate # 激活该环境
        (my_env) $ python # 进入一下该环境下的 python 随后退出
        (my_env) $ conda-unpack # 十分重要，请不要忽略


其他命令
    conda update -n base -c defaults conda          # 更新 conda
