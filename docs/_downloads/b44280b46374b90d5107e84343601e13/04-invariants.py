"""
.. _ref_invariants_example:

Extract stress/strain invariants - Static Simulation
=====================================================================
**提取应力/应变不变量 - 静态模拟**

本脚本以静态模拟为例，说明如何提取张量不变量。
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
# Extract elemental nodal stress and strain
# -----------------------------------------
# **提取单元节点应力应变**

stress = simulation.stress(all_sets=True)
print(stress)

strain = simulation.elastic_strain(all_sets=True)
print(strain)

###############################################################################
# Compute principal invariant averaged and unaveraged on stress and strain
# ------------------------------------------------------------------------
# **计算应力和应变的平均和非平均主不变量**

# `stress_principal` 方法通常用于计算单元的主应力。这意味着它在每个单元上都计算一个主应力值，这个值是在单元的整个体积上平均的。
princ_stress_1 = simulation.stress_principal(components=[1]) 
print(princ_stress_1)

# `stress_principal_nodal` 方法通常用于计算节点的主应力。这意味着它在每个节点上都计算一个主应力值，这个值是由连接到该节点的所有单元的应力值平均得到的。
nodal_princ_stress_2 = simulation.stress_principal_nodal(components=[2]) 
print(nodal_princ_stress_2)
nodal_princ_stress_2.plot()

# 因此，stress_principal 方法得到的主应力更适合于评估整体的应力分布，而 stress_principal_nodal 方法得到的主应力更适合于评估局部的应力集中。

nodal_princ_strain_2 = simulation.elastic_strain_principal_nodal(components=[2])
print(nodal_princ_strain_2)
nodal_princ_strain_2.plot()


###############################################################################
# Compute von Mises eqv averaged and unaveraged on stress and strain
# ------------------------------------------------------------------------
# **计算应力和应变的平均和非平均 von Mises eqv**

stress_eqv = simulation.stress_eqv_von_mises(set_ids=[1])
print(stress_eqv)

nodal_stress_eqv = simulation.stress_eqv_von_mises_nodal(set_ids=[1])
nodal_stress_eqv.plot()

nodal_strain_eqv = simulation.elastic_strain_eqv_von_mises_nodal(set_ids=[1])
nodal_strain_eqv.plot()
