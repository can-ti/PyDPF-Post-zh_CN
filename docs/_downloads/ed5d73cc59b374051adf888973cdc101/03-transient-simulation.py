"""
.. _ref_transient_example:

Transient Simulation with Animation
===================================
**带动画的瞬态模拟**

该脚本对瞬态模拟进行处理，以提取应力、应变和位移等结果。
此外，还可提取所选时间步长的数据并显示动画。
"""

###############################################################################
# Perform required imports
# ------------------------
# **执行所需的导入**
# 本示例使用了一个提供的文件，您可以通过导入 DPF ``examples`` 包获得该文件。

from ansys.dpf import post
from ansys.dpf.post import examples

###############################################################################
# Get ``Simulation`` object
# -------------------------
# **获取 ``Simulation`` 对象**

# 获取允许访问结果的 ``Simulation`` 对象。必须使用结果文件的路径实例化 ``Simulation`` 对象。
# 例如，Windows 下为 ``"C:/Users/user/my_result.rst"`` 或 Linux 下为 ``"/home/user/my_result.rst"`` 。

example_path = examples.find_msup_transient()

# 自动检测模拟类型，请使用：
simulation = post.load_simulation(example_path)

# 要启用自动完成功能，请使用等效的命令：
simulation = post.TransientMechanicalSimulation(example_path)

# 打印 simulation ，了解可用内容的概况
print(simulation)


###############################################################################
# Extract displacement at all times or on a selection
# ---------------------------------------------------
# **全部或选择性提取位移量**

# 查询所有 times 的位移矢量场
displacement = simulation.displacement(all_sets=True)
print(displacement)
# 动画显示具有多个分量的向量场的范数
displacement.animate(deform=True, title="U")

# 这段代码首先调用 simulation 对象的 displacement 方法，获取模拟中所有集合（由 all_sets=True 指定）的位移信息。
# 然后，代码打印了获取到的位移信息。
# 最后，代码调用 displacement 对象的 animate 方法，生成了一个动画来展示位移信息。参数 deform=True 表示在动画中展示形变，参数 title="U" 设置了动画的标题为 "U"。


# 使用 `components` 参数获取特定组件
x_displacement = simulation.displacement(all_sets=True, components=["X"])
print(x_displacement)
x_displacement.animate(deform=True, title="UX")


# 使用 “norm=True” 获取向量结果的范数
displacement_norm = simulation.displacement(all_sets=True, norm=True)
print(displacement_norm)
displacement_norm.animate(deform=True, title="U norm")

# 获取模拟中可用的 time set ID
print(simulation.set_ids)

# 提取给定时间步长上的位移，或从已计算的位移 Dataframe 中选择时间步长
displacement = simulation.displacement(set_ids=simulation.set_ids[5:])
displacement = displacement.select(set_ids=simulation.set_ids[5:])
print(displacement)

###############################################################################
# Extract strain at all times or on a selection
# ---------------------------------------------------
# **全部或根据选择提取应变**

strain = simulation.elastic_strain_nodal(all_sets=True)
print(strain)

strain = simulation.elastic_strain_nodal(set_ids=simulation.set_ids[10:])
print(strain)


###############################################################################
# Animate strain eqv over all times
# ---------------------------------
# **全部 times 的应变方程动画**

strain_eqv = simulation.elastic_strain_eqv_von_mises_nodal(all_sets=True)
strain_eqv.animate(deform=True, title="E_eqv")


