"""
.. _ref_export_data_example:

Export data contained in a DataFrame to a new format
====================================================
**将 DataFrame 中包含的数据导出为新格式**

本脚本以静态模拟为例，说明如何将数据从 DataFrame 导出到另一种格式。
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

example_path = examples.download_crankshaft()
# 自动检测模拟类型，请使用
simulation = post.load_simulation(example_path)

# 要启用 auto-completion 功能，请使用等效的命令：
simulation = post.StaticMechanicalSimulation(example_path)

# 打印 simulation ，了解可用内容的概况
print(simulation)

###############################################################################
# Extract elemental nodal stress
# ------------------------------
# **提取单元节点应力**

stress = simulation.stress_nodal(all_sets=True)
print(stress)

###############################################################################
# Export to a numpy.ndarray
# -------------------------
# **导出为 numpy.ndarray**

# 要导出为 numpy.ndarray，DataFrame 必须只包含列标签值单一组合的数据。

# 选择一个荷载步，因为 dataframe 包含多个荷载步的数据
stress_1 = stress.select(set_ids=1)
print(stress_1)

# 将其导出为 numpy.ndarray
stress_1_array = stress_1.array
print(stress_1_array)
