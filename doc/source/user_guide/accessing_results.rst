.. _user_guide_accessing_results:

**************
Access results
**************

除了作为浏览结果文件内容的入口外， :class:`Simulation <ansys.dpf.post.simulation.Simulation>` 对象还提供对结果本身的访问。
您可以使用专用方法查询结果。

下面是获得 ``displacement`` 结果的方法：

.. code:: python

	# 实例化仿真对象

	>>> from ansys.dpf import post
	>>> from ansys.dpf.post import examples
	>>> simulation = post.load_simulation(examples.multishells_rst)

	# 将位移数据提取为 DataFrame 对象

	>>> displacement = simulation.displacement()
	>>> # 也可以调用 `stress` 、 `elastic_strain` (...)

	# 有关可提取的结果，请参阅以下列表。

您可以使用 *keyword arguments* 进一步指定其他选项，包括组件、范围和时间。详细示例请参见 :ref:`ref_result_keywords` 。

PyDPF-Post 支持两种类型的结果文件：

* Structural (RST)
* Thermal/electric (RTH) (with the legacy *load_solution()* method only)

您只能请求结果文件中可用的结果。要确定哪些结果可用，请参阅 :ref:`user_guide_accessing_file_metadata` 。


Structural result files
=======================

本节将详细介绍如何使用传统的 ``Solution`` 对象访问结构结果。

从结构分析结果 (RST) 文件加载 ``Solution`` 对象后，可以查询以下这些 ``Result`` 对象：

* ``displacement``
* ``stress``
* ``elastic_strain``
* ``plastic_strain``
* ``structural_temperature``

Displacement
------------
位移是结构分析的 DOF 解。DOF 解的位置参数必须是模态参数。

您可以使用 :class:`Displacement <ansys.dpf.post.displacement.Displacement>` 访问结果对象：

.. code:: python

    # 实例化 solution 对象

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # 实例化位移结果对象

    >>> displacement = solution.displacement()

位移 ``Result`` 对象对应一个矢量场。要获取该场的标量分量（Y 分量），请使用以下命令访问子结果：

.. code:: python

    # 实例化 solution 对象

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # 实例化位移结果对象

    >>> displacement = solution.displacement()

    # 获取 Y 位移结果数据

    >>> u_y = displacement.y
    >>> u_y.get_data_at_field()

更多信息，请参阅 :ref:`ref_api_result_data` 。


Stress
------

您可以通过以下方式访问 :class:`Stress <ansys.dpf.post.stress.Stress>` 结果对象：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate the stress result object

    >>> stress = solution.stress()

``Stress`` 结果对象对应于一个张量场。要获得该场的标量分量，例如法向应力_yy，请访问子结果：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate the stress result object

    >>> stress = solution.stress()

    # Get the yy stress result data

    >>> s_yy = stress.yy
    >>> s_yy.get_data_at_field()

您可以据此查询其他组件以及整个张量数据。更多信息，请参阅 :ref:`ref_api_result_data` 。


Elastic and plastic strain
--------------------------
您可以使用 :class:`ElasticStrain <ansys.dpf.post.strain.ElasticStrain>` 和 :class:`PlasticStrain <ansys.dpf.post.strain.PlasticStrain>` 访问结果对象：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate the strain result objects

    >>> elastic_strain = solution.elastic_strain()
    >>> plastic_strain = solution.plastic_strain()

``Strain`` 结果对象对应于一个张量场。要获取该场的标量分量（如剪切应变_xy），请访问子结果：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate the elastic strain result object

    >>> elastic_strain = solution.elastic_strain()

    # 获取 xy 弹性应变结果数据

    >>> e_xy = elastic_strain.xy
    >>> e_xy.get_data_at_field()

您可以据此查询其他组件以及整个张量数据。更多信息，请参阅 :ref:`ref_api_result_data` 。


Structural temperature
----------------------
您可以通过以下方式访问 :class:`StructuralTemperature <ansys.dpf.post.temperature.StructuralTemperature>` 结果对象：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # 实例化结构温度结果对象

    >>> structural_temperature = solution.structural_temperature()

访问"温度标量"字段的方法如下：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate the structural temperature result object

    >>> structural_temperature = solution.structural_temperature()

    # Get the structural temperature result data

    >>> temperature = structural_temperature.scalar
    >>> temperature.get_data_at_field()


Miscellaneous results
---------------------

``Solution`` 对象可能包含其他杂项 :class:`ansys.dpf.post.misc_results.MecanicMisc` 结果对象，
您可以访问这些对象。例如，您可以访问 ``nodal_acceleration`` 结果对象：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # 获取节点加速度结果数据

    >>> acceleration = solution.misc.nodal_acceleration()

除位置外，所有关键字参数都适用于其他结果。更多信息，请参阅 :ref:`ref_result_keywords` 。

某些子结果可以作为关键字参数提供，例如节点加速度的标量分量：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Get the result data

    >>> acceleration = solution.misc.nodal_acceleration(subresult="Y")

要确定可用的查询，可以浏览结果文件中的元数据。更多信息，请参阅 :ref:`user_guide_accessing_file_metadata` 。


Thermal/electric result files
=============================

本节将详细介绍如何使用传统的 ``Solution`` 对象访问热/电结果。

从热/电分析结果文件 (RTH) 中加载 ``Solution`` 对象后，就可以查询这些 ``Solution`` 对象：

* ``temperature``
* ``heat_flux``
* ``electric_field``
* ``electric_potential``

Temperature
-----------
温度是热力学分析的 DOF 解。

您可以通过以下方式访问 :class:`Temperature <ansys.dpf.post.temperature.Temperature>` 结果对象：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.steady_therm)

    # Instantiate the temperature result object

    >>> temperature = solution.temperature()

如上所述， DOF 解的位置参数必须是节点参数。您可以直接访问标量场：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate the temperature result object

    >>> temperature = solution.temperature()

    # Get the y temperature result data

    >>> temp = temperature.scalar
    >>> temp.get_data_at_field()


Heat flux
---------
您可以通过以下方式访问 :class:`HeatFlux <ansys.dpf.post.temperature.HeatFlux>` 结果对象：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.steady_therm)

    # Instantiate the heat_flux result object

    >>> heat_flux = solution.heat_flux()


``HeatFlux`` 结果对象对应一个矢量场。要获取该场的标量分量（x 分量），请访问子结果：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate the temperature result object

    >>> heat_flux = solution.heat_flux()

    # Get the y heat_flux result data

    >>> heat_flux_x = heat_flux.x
    >>> heat_flux_x.get_data_at_field()

您可以据此查询其他组件。更多信息，请参阅 :ref:`ref_api_result_data` 。


Electric field
--------------
您可以使用 :class:`ElectricField <ansys.dpf.post.electric_results.ElectricField>` 访问结果对象：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.electric_therm)

    # Instantiate the electric field result object

    >>> electric_field = solution.electric_field()

``electric_field`` 结果对象对应一个矢量场。要获取该场的标量分量（如 x 分量），请访问子结果：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate the electric field result object

    >>> electric_field = solution.electric_field()

    # Get the y electricfield result data

    >>> electric_field_x = electric_field.x
    >>> electric_field_x.get_data_at_field()

更多信息，请参阅 :ref:`ref_api_result_data` 。


Electric potential
------------------
您可以使用 :class:`ElectricPotential <ansys.dpf.post.electric_results.ElectricPotential>` 访问结果对象：

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.steady_therm)

    # Instantiate the electric potential result object

    >>> electric_potential = solution.electric_potential()

``electric_potential`` 结果对象对应于一个标量场。您可以使用

.. code:: python

    # Instantiate the solution object

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)

    # Instantiate the electric potential result object

    >>> electric_potential = solution.electric_potential()

    # Get the y electric potential result data

    >>> ep = electric_potential.scalar
    >>> ep.get_data_at_field()
