"""
.. _ref_modal_sub_results_example:

Extract components of results - Modal Simulation
================================================
**提取部分结果 - 模态分析**

在该脚本中，将对模态模拟进行处理，以提取弹性应变和位移等结果的子组件。
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

example_path = examples.download_all_kinds_of_complexity_modal()

# 自动检测模拟类型，请使用
simulation = post.load_simulation(example_path)

# 要启用 auto-completion 功能，请使用等效的命令：
simulation = post.ModalMechanicalSimulation(example_path)

# 打印 simulation ，了解可用内容的概况
print(simulation)


###############################################################################
# Extract X displacement over a list modes
# ----------------------------------------
# 提取列表模态的 X 位移

###############################################################################
# 打印time-freq支持有助于选择正确的模态

print(simulation.time_freq_support)

# 获取前 2 阶模态的 X 位移
x_displacement = simulation.displacement(modes=[1, 2], components=["X"])
# equivalent to
# x_displacement = simulation.displacement(set_ids=[1, 2], components=["X"])
print(x_displacement)

x_displacement.plot(set_id=1)

###############################################################################
# Extract XX and XY elastic strain over a list modes
# --------------------------------------------------
# 提取模态列表中的 XX 和 XY 弹性应变

# 获取第 3 阶模态的 XX 和 XY 弹性应变
XX_XY_elastic_strain = simulation.elastic_strain_nodal(
    modes=[3], components=["XX", "XY"]
)
print(XX_XY_elastic_strain)
