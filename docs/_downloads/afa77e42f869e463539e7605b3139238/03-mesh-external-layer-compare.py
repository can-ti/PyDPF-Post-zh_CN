"""
.. _ref_mesh_external_layer_compare_example:

Validate External Layer results with full Mesh
==============================================
**使用完整网格验证外层结果**

此示例显示以下各项之间的后处理比较：
 - 仅在外层提取结果和网格。
 - 在整个网格上提取结果和网格。

外层是 solid 单元层，其中至少有一个面朝向几何体的外部。

该功能适用于所有类型的力学仿真，允许您缩小网格和提取数据的大小，以提高处理性能。由于较大的应力和应变通常位于模型的外层，因此在大多数情况下，在外层计算结果可提供等效的最大值。
"""

###############################################################################
# Perform required imports
# -------------------------
# **执行所需的导入**

###############################################################################
# 本示例使用了一个提供的文件，您可以通过导入 DPF ``examples`` 包获得该文件。


from ansys.dpf import post
from ansys.dpf.post import examples

###############################################################################
# Get ``Simulation`` object
# ----------------------------
# **将结果文件加载到允许访问结果的 ``Simulation`` 对象中**

###############################################################################
# 必须使用结果文件的路径实例化 ``Simulation`` 对象。例如，Windows 下为 ``"C:/Users/user/my_result.rst"`` 或 Linux 下为 ``"/home/user/my_result.rst"`` 。

example_path = examples.download_crankshaft()
# 自动检测模拟类型，请使用
simulation = post.load_simulation(example_path)

# 要启用自动完成功能，请使用等效的命令：
simulation = post.StaticMechanicalSimulation(example_path)

# 打印 simulation，了解可用内容的概况
print(simulation)

###############################################################################
# Extract displacement data
# -------------------------
# **提取整个网格和外层的位移数据**

displacement_ext = simulation.displacement(external_layer=True)
displacement = simulation.displacement()  # default is `external_layer=False`
displacement_ext.plot()
displacement.plot()

print(
    f"number of nodes with `external_layer=True`: {len(displacement_ext.index.mesh_index)}"
)
print(
    f"number of nodes with `external_layer=False`: {len(displacement.index.mesh_index)}"
)

###############################################################################
# Extract stress/strain data
# --------------------------
# **提取应力/应变数据**

###############################################################################
# 提取整个网格和外层的应力或弹性应变数据。
# 由于保持单元的连通性不变，因此可以很容易地在外部层上进行平均和不变量计算。

elemental_stress_ext = simulation.stress_principal_elemental(
    components=[1], external_layer=True
)
elemental_stress = simulation.stress_principal_elemental()
elemental_stress_ext.plot()
elemental_stress.plot()

print(
    f"number of elements with `external_layer=True`: {len(elemental_stress_ext.index.mesh_index)}"
)
print(
    f"number of elements with `external_layer=False`: {len(elemental_stress.index.mesh_index)}"
)

elastic_strain_eqv_ext = simulation.elastic_strain_eqv_von_mises_nodal(
    external_layer=True
)
elastic_strain_eqv = simulation.elastic_strain_eqv_von_mises_nodal()
elastic_strain_eqv_ext.plot()
elastic_strain_eqv.plot()
