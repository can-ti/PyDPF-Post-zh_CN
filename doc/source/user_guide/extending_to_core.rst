.. _user_guide_extending_to_core:

************************
Use PyDPF-Core operators
************************

PyDPF-Post 基于 PyDPF-Core，但针对后处理进行了精简。由于 PyDPF-Post 可与 PyDPF-Core 协同工作，
因此您可以使用 PyDPF-Core 强大的、可扩展的 `operators <https://dpfdocs.pyansys.com/operator_reference.html>`_ 来促进数据操作和更通用的数据转换。

PyDPF-Core 可以访问来自 Ansys 求解器结果文件以及第三方文件格式的数据。使用 PyDPF-Core，您可以通过使用操作符将简单的构建块链接在一起，从而从中组装复杂的工作流。
DPF 中的数据由与物理无关的数学量表示，这些数学量被描述在一个自给自足的实体中，该实体被称为 :class:`Field <ansys.dpf.core.field.Field>` 。

To show the range of PyDPF-Core and PyDPF-Post capabilities, the following
examples show how they work together.


Export to VTK file
------------------

这段代码展示了如何使用传统 PyDPF-Post API 将字段容器（fields_container）导出为 VTK 文件：

.. code:: python

    # 实例化 solution 对象。

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # 实例化一个 result 对象。这是一个位移结果。

    >>> displacement = solution.displacement()

    # 这是结果数据（数据容器）。

    >>> norm = displacement.norm

    # 从结果数据中提取 fields_container 结果。

    >>> fields_container = norm.result_fields_container
    
    # 导入 DFP-Core API。

    >>> from ansys.dpf import core

    # 实例化专用运算符

    >>> vtk_operator = core.Operator("vtk_export")

    # 设置连接。

    >>> vtk_operator.inputs.mesh.connect(solution.mesh)
    >>> vtk_operator.inputs.file_path.connect("vtk_example.vtk")
    >>> vtk_operator.inputs.fields1.connect(fields_container)

    # Run the operator.

    >>> vtk_operator.run()


Export to HDF5 file
-------------------

这段代码展示了如何使用传统的 PyDPF-Post API 将相同的字段容器导出到 HDF5 文件：（Hierarchical Data Format 是一种常见的跨平台数据储存文件）

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate a result object. This is a displacement result.

    >>> displacement = solution.displacement()

    # This is the result data (data container).

    >>> norm = displacement.norm

    # Extract the fields_container result from the result data.

    >>> fields_container = norm.result_fields_container
    
    # Import the DPF-Core API.

    >>> from ansys.dpf import core

    # Initialize a dedicated operator.

    >>> h5_operator = core.Operator("serialize_to_hdf5")

    # Set the connection.

    >>> h5_operator.inputs.mesh.connect(solution.mesh)
    >>> h5_operator.inputs.file_path.connect("hdf5_example.h5")
    >>> h5_operator.inputs.data.connect(fields_container)

    # Evaluate the operator.

    >>> h5_operator.eval()

