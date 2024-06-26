==========
PyDPF-Post
==========

Ansys 数据处理框架（DPF）为数值仿真用户和工程师提供了访问和转换仿真数据的工具箱。利用 DPF，您可以在仿真工作流中对大量仿真数据进行复杂的前处理或后处理。

Python ``ansys-dpf-post`` 软件包为后处理提供了一个面向物理的高级应用程序接口。通过加载仿真（由其结果文件定义），可以提取仿真元数据和结果，然后对其进行后处理操作。

最新版本的 DPF 支持以下的 Ansys 求解器结果文件：

- Mechanical APDL (`.rst`, `.mode`, `.rfrq`, `.rdsp`)
- LS-DYNA (`.d3plot`, `.binout`)
- Fluent (`.cas/dat.h5`, `.flprj`)
- CFX (`.cad/dat.cff`, `.flprj`)

有关文件支持的更多信息，请参阅 PDF-Core 文档中的 `主页 <https://dpf.docs.pyansys.com/version/stable/index.html>`_ 。

PyDPF-Post 利用 PyDPF-Core 项目的 ``ansys-dpf-core`` 包，该包可在 `PyDPF-Core GitHub <https://github.com/ansys/pydpf-core>`_ 获取。
使用 ``ansys-dpf-core`` 软件包可以使用 DPF 构建更高级和定制化的工作流。

Brief demo
~~~~~~~~~~

只要安装了 Ansys 2023 R1 或更高版本，一旦开始使用 PyDPF-Post，DPF 服务器就会自动启动。

要为 MAPDL 结果文件加载模拟以提取和后处理结果，请使用此代码：

.. code:: python

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> simulation = post.load_simulation(examples.download_crankshaft())
    >>> displacement = simulation.displacement()
    >>> print(displacement)


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

             results         U
              set_id         3
      node      comp
      4872         X -3.41e-05
                   Y  1.54e-03
                   Z -2.64e-06
      9005         X -5.56e-05
                   Y  1.44e-03
                   Z  5.31e-06
       ...

.. code:: python

    >>> displacement.plot()


.. figure:: ./images/crankshaft_disp.png
    :width: 300pt

.. code:: python

    >>> stress_eqv = simulation.stress_eqv_von_mises_nodal()
    >>> stress_eqv.plot()

.. figure:: ./images/crankshaft_stress.png
    :width: 300pt

要使用 Ansys 2021 R1 至 2022 R2 运行 PyDPF-Post，请使用此代码启动传统 PyDPF-Post 工具：

.. code:: python

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.download_crankshaft())
    >>> stress = solution.stress()
    >>> stress.eqv.plot_contour(show_edges=False)

.. figure:: ./images/crankshaft_stress.png
    :width: 300pt


有关如何使用 PyDPF-Post 的综合示例，请参见 :ref:`gallery` 。


Key features
~~~~~~~~~~~~

**计算效率**

PyDPF-Post 以 DPF 为基础，其 dataframe 工作在 DPF 服务器上进行本地加载和后处理，由于是用 C 和 FORTRAN 编写的，
因此可以实现快速的后处理工作流。由于 PyDPF-Post 以 Pythonic 方式呈现结果，因此您可以快速开发简单或复杂的后处理脚本。

**Easy to use**

PyDPF-Post API 自动使用链式 DPF 运算符，使后处理更容易。PyDPF-Post 文档描述了如何使用运算符来计算结果。
这允许您构建自己的自定义低级脚本，以使用 `PyDPF-Core <https://github.com/ansys/pydpf-core>`_ 对潜在的数千兆字节模型进行快速后处理。

Documentation and issues
------------------------
PyDPF-Post 最新稳定版的文档托管在 `PyDPF-Post documentation <https://post.docs.pyansys.com/version/stable/>`_ 。

在文档标题栏的右上角有一个选项，可以从查看最新稳定版本的文档切换到查看开发版本或以前发布版本的文档。

你也可以 `查看 <https://cheatsheets.docs.pyansys.com/pydpf-post_cheat_sheet.png>`_ 或 `下载 <https://cheatsheets.docs.pyansys.com/pydpf-post_cheat_sheet.pdf>`_ PyDPF-Post cheatsheets。这一页参考资料提供了使用 PyDPF-Post 的语法规则和命令。

在 `PyDPF-Post Issues <https://github.com/ansys/pydpf-post/issues>`_ 页面，您可以创建问题来报告错误和申请新功能。
在 `PyDPF-Post Discussions <https://github.com/ansys/pydpf-post/discussions>`_ 页面或 Ansys Developer 门户网站上的 `Discussions <https://discuss.ansys.com/>`_ 页面，
您可以发布问题、分享想法并获得社区反馈。

如需联系项目支持团队，请发送电子邮件至 `pyansys.core@ansys.com <pyansys.core@ansys.com>`_ 。


.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :hidden:

   getting_started/index
   user_guide/index
   api/index
   examples/index
   contributing
