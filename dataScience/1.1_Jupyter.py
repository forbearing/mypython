1:主题
    pip install jupyterthemes
        # https://github.com/dunovank/jupyter-themes
    jt -l               # 查看有哪些主题
    jt -t oceans16      # 设置主题
    jt -r               # 恢复默认主题
    jt -t monokai -f roboto -nf robotosans -tf robotosans -N -T -cellw 70% -dfs 10 -ofs 10
        -t      设置主题
        -f      设置代码字体
        -nf     设置 notebook 的字体

2:自动代码补全
    python -m pip install jupyter_contrib_nbextensions
        # 由 jupyter 的扩展插件 Nbextensions 库来实现
    jupyter contrib nbextension install --user --skip-running-check
        # 安装完成后，勾选 Table of Contents 以及 Hinterland。
        # 其中 Hinterland 是用来自动补全代码的

3:Jupyter Notebook 输出 pdf 并支持中文显示
