"""
.. _ref_result_on_path:

Request result on a specific path
=================================
**请求特定路径上的结果**

本例展示了如何请求特定坐标路径的结果。
"""

###############################################################################
# Perform required imports
# ------------------------
# **执行所需的导入**

from ansys.dpf import post
from ansys.dpf.post import examples

###############################################################################
# Get ``Solution`` object
# -----------------------
# **获取 ``Solution`` 对象**

solution = post.load_solution(examples.static_rst)

###############################################################################
# Create coordinates array
# ~~~~~~~~~~~~~~~~~~~~~~~~
# **创建坐标数组，用于请求结果**

coordinates = [[0.024, 0.03, 0.003]]
for i in range(1, 51):
    coord_copy = coordinates[0].copy()
    coord_copy[1] = coord_copy[0] + i * 0.001
    coordinates.append(coord_copy)

# 这段代码首先创建了一个包含一个列表的列表 ``coordinates``，该列表包含三个浮点数。
# 然后，代码进入一个从 1 到 50 的循环。在每次循环中，它都会复制 ``coordinates`` 的第一个元素（也就是那个包含三个浮点数的列表），
# 然后将复制的列表的第二个元素（索引为 1）设置为第一个元素（索引为 0）加上循环变量 i 乘以 0.001。然后，它将修改后的列表添加到 ``coordinates`` 的末尾。
# 这样， ``coordinates`` 最终将包含 51 个列表，每个列表都包含三个浮点数，其中第二个浮点数是递增的。


###############################################################################
# Create ``DpfPath`` object
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# **创建一个 ``DpfPath`` 对象**

path = post.create_path_on_coordinates(coordinates=coordinates)

###############################################################################
# Request result on path
# ~~~~~~~~~~~~~~~~~~~~~~
# **在此路径上请求结果**

stress = solution.stress(path=path)

###############################################################################
# Plot result
# -----------
# **绘制结果图**

stress_eqv = stress.von_mises
stress_eqv.plot_contour()
