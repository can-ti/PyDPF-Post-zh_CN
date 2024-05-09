"""
.. _ref_data_data_frame_example:

Explore the data of a result with the DataFrame - Harmonic Simulation
=====================================================================
**使用 DataFrame 查看结果数据 - 谐波分析**

本脚本以谐波模拟为例，说明如何与每个结果返回的 post DataFrame 对象交互。
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

example_path = examples.download_harmonic_clamped_pipe()
# 自动检测模拟类型，请使用
simulation = post.load_simulation(example_path)

# 要启用 auto-completion 功能，请使用等效的命令：
simulation = post.HarmonicMechanicalSimulation(example_path)

# 打印 simulation ，了解可用内容的概况
print(simulation)

###############################################################################
# Extract displacement over all sets as an example
# ------------------------------------------------
# **以提取所有 sets 的位移结果为例**

displacement = simulation.displacement(all_sets=True)
print(displacement)
print(type(displacement)) # <class 'ansys.dpf.post.dataframe.DataFrame'>

###############################################################################
# 循环遍历所有列和行，了解 DataFrame 并获取每个索引的值。

# columns
for column in displacement.columns:
    print(f'Column with label "{column.name}" and available values {column.values}.')

# rows
for row in displacement.index:
    print(f'Row with label "{row.name}" and available values {row.values}.')

###############################################################################
# 这里的 “complex” 列标签代表复数，0 表示实数部分，1 表示虚数部分。 --ff


###############################################################################
# Make selections in this DataFrame
# ---------------------------------
# **在此 DataFrame 中进行选择**

###############################################################################
# 上面显示的所有标签和数值都可用于选择 DataFrame 的子部分。

all_real_values = displacement.select(complex=0)
print(all_real_values) # 这段代码首先调用 displacement 对象的 select 方法，选择复数部分为 0（即实数部分）的位移信息。然后，代码打印了选择的位移信息。

all_imaginary_values = displacement.select(complex=1)
print(all_imaginary_values) # 这段代码首先调用 displacement 对象的 select 方法，选择复数部分为 1（即虚数部分）的位移信息。然后，代码打印了选择的位移信息。

sets_values = displacement.select(set_ids=[1, 2])
print(sets_values)

node_values = displacement.select(node_ids=[3548])
print(node_values)

###############################################################################
# Make selections by index in this DataFrame
# ------------------------------------------
# **在此 DataFrame 中按索引进行选择**

###############################################################################
# 要按索引选择每个标签的值，可以使用 iselect 方法。（注意这个方法索引值是从 0 开始的。 --ff）
# 从索引到 ID 的顺序与上述索引值方法返回的顺序一致。

sets_values = displacement.iselect(set_ids=0)
print(sets_values)

node_values = displacement.iselect(node_ids=[0])
print(node_values)

###############################################################################
# Make multi selections in this DataFrame
# ---------------------------------------
# 在此 DataFrame 中进行多重选择



real_values_for_one_set_onde_node = displacement.select(
    node_ids=[3548], set_ids=1, complex=0
)
print(real_values_for_one_set_onde_node)

###############################################################################
# Make selections to plot the DataFrame
# -------------------------------------
# 选择并绘制 DataFrame


displacement.plot(set_ids=1, complex=0)
