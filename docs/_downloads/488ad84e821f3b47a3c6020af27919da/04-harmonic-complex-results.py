"""
.. _ref_harmonic_example:

Harmonic Simulation
===================

本脚本对谐波模拟进行了处理，并使用了更复杂的结果。
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
# -------------------------
# 获取允许访问结果的 ``Simulation`` 对象。必须使用结果文件的路径实例化 ``Simulation`` 对象。例如，Windows 下为 ``"C:/Users/user/my_result.rst"`` 或 Linux 下为 ``"/home/user/my_result.rst"`` 。

example_path = examples.download_harmonic_clamped_pipe()
# 要自动检测模拟类型，请使用：
simulation = post.load_simulation(example_path)

# 要启用自动完成功能，请使用等效的命令：
simulation = post.HarmonicMechanicalSimulation(example_path)

# 打印 simulation，了解可用内容的概况

print(simulation)


###############################################################################
# Extract displacement over a list of frequencies sets
# ----------------------------------------------------
# **提取 frequencies sets 列表上的位移** 

###############################################################################
# 打印 `time_freq_support` 有助于选择正确的频率

print(simulation.time_freq_support)

displacement = simulation.displacement(set_ids=[1, 2])
print(displacement)

subdisp = displacement.select(complex=0, set_ids=1)
print(subdisp)
subdisp.plot(title="U tot real")

subdisp = displacement.select(complex=1, set_ids=1)
print(subdisp)
subdisp.plot(title="U tot imaginary")

subdisp = displacement.select(complex=0, set_ids=2)
print(subdisp)
subdisp.plot(title="U tot real")

###############################################################################
# Extract stress eqv over a list of frequencies sets
# --------------------------------------------------
# **在 frequencies sets 列表中提取应力方程**

stress_eqv = simulation.stress_eqv_von_mises_nodal(set_ids=[1, 2])
print(stress_eqv)

sub_eqv = stress_eqv.select(complex=0, set_ids=1)
print(sub_eqv)
sub_eqv.plot(title="S_eqv real")

sub_eqv = stress_eqv.select(complex=1, set_ids=1)
print(sub_eqv)
sub_eqv.plot(title="S_eqv imaginary")

sub_eqv = stress_eqv.select(complex=0, set_ids=2)
print(sub_eqv)
sub_eqv.plot(title="S_eqv real")
