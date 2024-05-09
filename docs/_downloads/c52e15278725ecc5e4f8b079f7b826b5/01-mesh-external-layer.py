"""
.. _ref_mesh_external_layer_example:

Reduce Model Size by using Mesh External Layer for Result and Mesh extraction
=============================================================================
**通过使用网格外层进行结果和网格提取来减少模型大小**

本例显示了静态分析中网格外层的后处理。外层是实体单元，其中至少有一个面朝向几何体外部。

该功能适用于所有类型的 Mechanical simulation，允许您缩小网格和提取数据的大小，以提高处理性能。
由于较大的应力和应变通常位于模型的表层，因此在大多数情况下，计算外层的结果可获得等效的最大值。
"""

###############################################################################
# Perform required imports
# ------------------------
# **执行所需的导入**

###############################################################################
# 本示例使用了一个提供的文件，您可以通过导入 DPF ``examples`` 包获得该文件。

from ansys.dpf import post
from ansys.dpf.post import examples

###############################################################################
# Get ``Simulation`` object
# ----------------------------
# **将结果文件加载到允许访问结果的 ``Simulation`` 对象中。**

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
# **提取位移数据**

###############################################################################
# 提取外部图层的位移数据。

displacement_ext = simulation.displacement(
    external_layer=True
)  # 默认该参数 `external_layer=False`
displacement_ext.plot()

print(
    f"`external_layer=True` 的节点数： {len(displacement_ext.index.mesh_index)}"
)
print(f"`external_layer=False` 的节点数： {len(simulation.mesh.node_ids)}")

###############################################################################
# Extract stress/strain data
# --------------------------
# **提取应力/应变数据**

###############################################################################
# 提取外层的应力或弹性应变数据。由于外层单元的连续性保持不变，因此可以在外层轻松完成平均值和不变量的计算。

elemental_stress_ext = simulation.stress_principal_elemental(
    components=[1], external_layer=True
)
elemental_stress_ext.plot()

print(
    f"`external_layer=True` 的节点数： {len(elemental_stress_ext.index.mesh_index)}"
)
print(
    f"`external_layer=False` 的节点数： {len(simulation.mesh.element_ids)}"
)

elastic_strain_eqv_ext = simulation.elastic_strain_eqv_von_mises_nodal(
    external_layer=True
)
elastic_strain_eqv_ext.plot()

###############################################################################
# Extract the external layer on a selection of elements
# -----------------------------------------------------
# **提取选定单元上的外部图层**

all_elements = simulation.mesh.element_ids
elements = []
for i in range(0, int(all_elements.size / 2)):
    elements.append(all_elements[i])
elemental_stress_ext = simulation.stress_principal_elemental(external_layer=elements)
elemental_stress_ext.plot()

###############################################################################
# Extract the external layer on a selection of elements for nodal results
# -----------------------------------------------------------------------
# **在所选单元上提取外部图层以获得节点结果**

elastic_strain_eqv_ext = simulation.elastic_strain_eqv_von_mises_nodal(
    external_layer=elements
)
elastic_strain_eqv_ext.plot()

###############################################################################
# Extract the external layer on a selection of elements and scope results
# -----------------------------------------------------------------------
# **提取选定单元上的外部图层并确定结果范围**

sub_elements = []
for i in range(0, int(len(elements) / 2)):
    sub_elements.append(elements[i])
elemental_stress_ext = simulation.stress_principal_elemental(
    external_layer=elements, element_ids=sub_elements
)
elemental_stress_ext.plot()
