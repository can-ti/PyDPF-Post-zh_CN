"""
.. _ref_static_example:

Static Simulation
=================

在该脚本中，将对静态模拟进行处理，以提取应力、位移等结果。此外，还可通过对特定节点或单元进行扫描来选择结果的子部分。
"""

###############################################################################
# Perform required imports
# ------------------------
# 执行所需的导入.

# 本示例使用了一个提供的文件，您可以通过导入 DPF ``examples`` 包获得该文件。

from ansys.dpf import post
from ansys.dpf.post import examples

###############################################################################
# Get ``Simulation`` object
# -------------------------
# 获取允许访问结果的 ``Simulation`` 对象。必须使用结果文件的路径实例化 ``Simulation`` 对象。
# 例如，Windows 下为 ``"C:/Users/user/my_result.rst"`` 或 Linux 下为 ``"/home/user/my_result.rst"`` 。

example_path = examples.find_static_rst()
example_path

# 若要自动检测模拟类型，请使用：
simulation = post.load_simulation(example_path)

# 要启用 auto-completion 功能，请使用等效的命令：
simulation = post.StaticMechanicalSimulation(example_path)

# 打印 simulation ，了解可用内容的概况
print(simulation)

# 获取模拟结果中的位移数据
displacement = simulation.displacement()
print(displacement)


###############################################################################
# Select sub parts of displacement
# ---------------------------------

# 获取 X 位移
x_displacement = displacement.select(components="X")
print(x_displacement)
print(type(x_displacement)) # <class 'ansys.dpf.post.dataframe.DataFrame'>

# 等同于：
x_displacement = simulation.displacement(components=["X"])
print(x_displacement)

# 绘制 X 位移图
x_displacement.plot()

# 提取特定节点上的位移
nodes_displacement = displacement.select(node_ids=[1, 10, 100])
nodes_displacement.plot()

# 等同于：
nodes_displacement = simulation.displacement(node_ids=[1, 10, 100])
print(nodes_displacement)

###############################################################################
# Compute total displacement (norm)
# ---------------------------------
# 计算选定节点上的位移范数

nodes_displacement = simulation.displacement(
    node_ids=simulation.mesh.node_ids[10:], norm=True
)
print(nodes_displacement)
nodes_displacement.plot()

# 这段代码首先调用 simulation 对象的 displacement 方法，获取模拟中特定节点的位移信息。这些节点的 ID 是从 simulation.mesh.node_ids[10:] 获取的，这意味着它获取的是除了前10个节点之外的所有节点的 ID。
# 参数 norm=True 表示获取的是位移的范数（即位移的大小）。然后，代码打印了获取到的位移信息。
# 最后，使用 plot 方法绘制了位移信息的图形。具体的绘图结果取决于 nodes_displacement 对象的类型和 plot 方法的实现。
# 如果你需要更具体的信息，如 nodes_displacement 的具体类型或 plot 方法的具体行为，你可能需要查阅相关的文档或源代码。

###############################################################################
# Extract tensor stress, apply averaging, compute equivalent
# ----------------------------------------------------------
# 从 rst 文件中提取原始单元节点应力：

elem_nodal_stress = simulation.stress()
print(elem_nodal_stress)

# 从结果文件中计算节点应力
nodal_stress = simulation.stress_nodal()
print(nodal_stress)

# 从结果文件计算单元应力
elemental_stress = simulation.stress_elemental()
print(elemental_stress)

# 提取特定单元的单元应力
elemental_stress = elemental_stress.select(element_ids=[5, 6, 7])
elemental_stress.plot()

# 从结果文件中计算节点等效应力
eqv_stress = simulation.stress_eqv_von_mises_nodal()
print(eqv_stress)
eqv_stress.plot()
