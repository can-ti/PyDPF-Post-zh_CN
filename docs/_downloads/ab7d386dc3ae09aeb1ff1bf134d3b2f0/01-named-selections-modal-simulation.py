"""
.. _ref_ns_modal_example:

Extract results on named selections - Modal Simulation
=======================================================
**提取指定选项的结果 —— 模态分析**

该脚本对静态模拟进行处理，以提取应力、位移等结果。此外，还可通过对特定节点、单元进行扫描来选择结果的子部分。
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
# Get the ``Simulation`` object
# -----------------------------
# **获取允许访问结果的 ``Simulation`` 对象**

###############################################################################
# 必须使用结果文件的路径实例化 ``Simulation`` 对象。例如，Windows 下为 ``"C:/Users/user/my_result.rst"`` 或 Linux 下为 ``"/home/user/my_result.rst"`` 。

example_path = examples.download_modal_frame()
# 自动检测模拟类型，请使用
simulation = post.load_simulation(example_path)

# 要启用 auto-completion 功能，请使用等效的命令：
simulation = post.ModalMechanicalSimulation(example_path)

# 打印 simulation ，了解可用内容的概况
print(simulation)

###############################################################################
# Get the available named selections
# ----------------------------------
# **获取可用的已命名选区（组件）**

print(simulation.named_selections)

###############################################################################
# Extract displacements on named selections
# -----------------------------------------
# **提取指定选区的位移**

bar1_tot_displacement = simulation.displacement(named_selections=["BAR_1"], norm=True)
print(bar1_tot_displacement)
bar1_tot_displacement.plot()

bar2_tot_displacement = simulation.displacement(named_selections=["BAR_2"], norm=True)
print(bar2_tot_displacement)
bar2_tot_displacement.plot()

# both
tot_displacement = simulation.displacement(
    named_selections=["BAR_1", "BAR_2"], norm=True
)
print(tot_displacement)
tot_displacement.plot()

###############################################################################
# Extract stress and averaged stress on named selections
# ------------------------------------------------------
# **提取已命名选区上的应力和平均应力**

eqv_stress = simulation.stress_eqv_von_mises_nodal(named_selections=["_FIXEDSU"])
print(eqv_stress)
eqv_stress.plot()

# without selection
elemental_stress = simulation.stress_elemental(named_selections=["BAR_1"])
print(elemental_stress)
elemental_stress.plot()
