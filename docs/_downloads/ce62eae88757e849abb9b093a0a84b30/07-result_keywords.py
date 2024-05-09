"""
.. _ref_result_keywords:

Result keywords
===============
**结果关键字**

此示例演示如何在从 ``Solution`` 对象调用 ``result`` 对象时使用关键字获得更精确的结果。
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

solution = post.load_solution(examples.multishells_rst)

###############################################################################
# Get keyword list
# ~~~~~~~~~~~~~~~~
# **获取关键词列表**

post.print_available_keywords()


###############################################################################
# Get ``Result`` objects
# ----------------------
# **获取 ``Result`` 对象**


###############################################################################
# Get displacement result using scoping
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **使用范围获取相应位移 ``Result`` 对象** 

###############################################################################
# 默认 ``location`` 是 ``nodal``。

displacement_result = solution.displacement(
    location=post.locations.nodal, node_scoping=[1, 2, 3]
)
displacement = displacement_result.vector

###############################################################################
# 这段代码首先调用 ``solution`` 对象的 ``displacement`` 方法，获取节点 1、2、3 的位移信息。参数 ``location=post.locations.nodal`` 表示获取节点的位移， ``node_scoping=[1, 2, 3]`` 表示只考虑节点 1、2、3。

# 然后，代码获取位移结果的向量部分，并将其存储在 ``displacement`` 中。

###############################################################################
# Get information on result
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# **获取位移结果信息**

# 首先调用 ``displacement`` 对象的 ``get_data_at_field`` 方法，获取第一个字段的位移数据。
displacement.get_data_at_field(0)

# 调用 ``solution`` 对象的 ``stress`` 方法，获取单元 1 的应力信息。参数 ``location=post.locations.elemental_nodal`` 表示获取单元节点的应力， ``element_scoping=[1]`` 表示只考虑单元 1。
stress_with_elem_scop_result = solution.stress(
    location=post.locations.elemental_nodal, element_scoping=[1]
)

# 接着，代码获取应力结果的张量部分，并将其存储在 ``stress_with_elem_scop`` 中。
stress_with_elem_scop = stress_with_elem_scop_result.tensor

# 最后，代码调用 ``stress_with_elem_scop`` 的 ``get_data_at_field`` 方法，获取第一个字段的应力数据。
stress_with_elem_scop.get_data_at_field(0)

###############################################################################
# Use named selection on result
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **在位移结果上使用命名选择**

# 这段代码首先调用 ``solution`` 对象的 ``stress`` 方法，获取名为 "SELECTION" 的命名选择的应力信息。参数 ``location=post.locations.elemental_nodal`` 表示获取单元节点的应力，``named_selection="SELECTION"`` 表示只考虑名为 "SELECTION" 的命名选择。
stress_on_ns_result = solution.stress(
    location=post.locations.elemental_nodal, named_selection="SELECTION"
)

# 然后，代码获取应力结果的张量部分，并将其存储在 ``stress_on_ns`` 中。
stress_on_ns = stress_on_ns_result.tensor

# 接着，代码获取 ``stress_on_ns`` 的字段数量。
stress_on_ns.num_fields

# 最后，代码获取 ``stress_on_ns`` 的第一个字段的长度。
len(stress_on_ns[0])

###############################################################################
# Get a subresult
# ~~~~~~~~~~~~~~~~~
# **获取子结果**

# 首先从 ``displacement_result`` 对象中获取 x 分量的位移，然后存储在 ``disp_x`` 中。
disp_x = displacement_result.x

# 然后从 ``stress_with_elem_scop_result`` 对象中获取 yz 分量的应力，然后存储在 ``stress_yz`` 中。
stress_yz = stress_with_elem_scop_result.yz

# 接着，代码从 ``stress_on_ns_result`` 对象中获取第三主应力，然后存储在 ``stress_principal_1`` 中。
stress_principal_1 = stress_on_ns_result.principal_3

# 最后，打印 stress_principal_1 的值。
stress_principal_1

###############################################################################
# Filter result
# ~~~~~~~~~~~~~~~
# **筛选结果**

###############################################################################
# 根据 time 、 time scoping 和 set 过滤结果。

# 首先打印 ``solution`` 对象的 ``time_freq_support`` 属性，这通常表示 ``solution`` 支持的时间或频率范围。
print(solution.time_freq_support)

# 代码调用 ``solution`` 对象的 ``stress`` 方法，获取时间为 1.0s 的应力信息。参数 ``time=1.0`` 表示获取时间为 1.0s 的应力。
stress_on_time_1s_result = solution.stress(time=1.0)
stress_on_time_1s = stress_on_time_1s_result.tensor

# 这段代码首先调用 ``solution`` 对象的 ``displacement`` 方法，获取集合 1 的位移信息。参数 ``set=1`` 表示获取集合 1 的位移。
# 代码获取位移结果的向量部分，并将其存储在 ``displacement_on_set_1`` 中。
displacement_on_set_1_result = solution.displacement(set=1)
displacement_on_set_1 = displacement_on_set_1_result.vector

# 代码调用 ``solution`` 对象的 ``elastic_strain`` 方法，获取时间为 1 和 3 的弹性应变信息。参数 ``time_scoping=[1, 3]`` 表示获取时间为 1 和 3 的弹性应变。
elastic_strain_with_time_scoping_result = solution.elastic_strain(time_scoping=[1, 3])
elastic_strain_with_time_scoping = elastic_strain_with_time_scoping_result.tensor
elastic_strain_with_time_scoping

###############################################################################
# Make grouping
# ~~~~~~~~~~~~~
# **进行分组**

# 这段代码首先调用 ``solution`` 对象的 ``displacement`` 方法，获取按单元形状分组的位移信息。参数 ``grouping=post.grouping.by_el_shape`` 表示按单元形状进行分组。
# 然后，代码获取位移结果的向量部分，并将其存储在 ``displacement_by_el_shape`` 中。
displacement_result = solution.displacement(grouping=post.grouping.by_el_shape)
displacement_by_el_shape = displacement_result.vector
displacement_by_el_shape

###############################################################################
# Filter MAPDL elements
# ~~~~~~~~~~~~~~~~~~~~~
# 筛选 MAPDL 单元

###############################################################################
# 筛选出类型为 solid 186 的单元 

stress_result = solution.stress(mapdl_grouping=186)
stress_on_solid_186 = stress_result.tensor
stress_on_solid_186

###############################################################################
# Manipulate result and change its definition
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# **操作结果并更改其定义**

print(stress_on_ns_result)
print(stress_on_ns_result.definition.location)

stress_on_ns_result.definition.location = post.locations.elemental
stress_on_ns_result.definition.time = 1.0
stress_on_ns_elemental = stress_on_ns_result.tensor
# 这段代码首先将 ``stress_on_ns_result`` 的定义中的位置信息设置为单元位置，将时间设置为 1.0。
# 然后，代码获取应力结果的张量部分，并将其存储在 ``stress_on_ns_elemental`` 中。


print(stress_on_ns_result)

###############################################################################
# Use miscellaneous results
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# **使用杂项结果**

###############################################################################
# 您可以在这里使用相同的关键字。对于复杂的结果，也可以使用关键字 ``phase`` ，它有一个浮点数值。(/mɪsə'leɪniəs/)

# 这段代码首先调用 ``solution`` 对象的 ``misc`` 属性中的 ``elemental_stress_ratio`` 方法，获取节点 1 和 32 在时间 1.0s 的单元应力比。参数 ``node_scoping=[1, 32]`` 表示只考虑节点 1 和 32，``time=1.0`` 表示获取时间为 1.0s 的应力比。
stress_ratio = solution.misc.elemental_stress_ratio(node_scoping=[1, 32], time=1.0)
print(stress_ratio)
