.. _installation:

************
Installation
************

Install using ``pip``
---------------------

Python 的标准软件包安装程序是 `pip <https://pypi.org/project/pip/>`_ 。

要在 Ansys 2021 R1 或更高版本中使用 PyDPF-Post，请使用此命令安装最新版本：

.. code:: bash

   pip install ansys-dpf-post

PyDPF-Post 的绘图功能需要安装 `PyVista <https://pyvista.org/>`_ 。要安装 PyDPF-Post 及其可选的绘图功能，请使用此命令：

.. code:: bash

   pip install ansys-dpf-post[plotting]

关于 PyDPF-Post 绘图功能的更多信息，请参见 :ref:`user_guide_plotting` 。


Install without internet
------------------------

如果由于网络隔离而无法使用 ``pip`` 在主机上安装 PyDPF-Post，可以下载与你的平台和 Python 解释器版本相对应的 wheelhouse。
要获取最新版本，请到 **Assets** 部分查看 GitHub 上的 `最新 PyDPF-Post 版本 <https://github.com/ansys/pydpf-post/releases/latest>`_ 。

wheelhouse 是一个 ZIP 文件，包含 PyDPF-Post 运行所需的所有包的 Python wheels 。
要使用下载的 wheelhouse 安装 PyDPF-Post，请将 wheelhouse 解压缩到本地目录，然后在本地目录中运行以下命令：

.. code:: bash

   pip install --no-index --find-links=. ansys-dpf-post

请注意，PyDPF-Post wheelhouses 不包括可选的绘图依赖项。为了实现绘图功能，还需要下载 `PyVista wheel <https://pypi.org/project/pyvista/#files>`_，并解压到同一本地目录，然后再运行前面的命令。


Install in development mode
---------------------------

如果你想编辑 PyDPF-Post 并为其做出贡献，请克隆该版本库，并使用 ``pip`` 和 ``-e`` 开发标志安装它：

.. include:: ../pydpf-post_clone_install.rst


Check the installation
----------------------

运行以下 Python 代码来验证 PyDPF-Post 的安装：

.. code:: bash

   from ansys.dpf import post
   from ansys.dpf.post import examples
   simulation = post.load_simulation(examples.simple_bar)
   print(simulation)
