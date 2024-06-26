.. _user_guide_post_processing:

********************
Load the result file
********************

:class:`Simulation <ansys.dpf.post.simulation.Simulation>` 对象是 PyDPF-Post 的核心元素。该对象是浏览结果文件内容的入口。

**On Windows**

您可以通过以下方式加载结果文件：

.. code:: python

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> simulation = post.load_simulation('C:/Users/user/file.rst')


**On Linux**

您可以通过以下方式加载结果文件：
    
.. code:: python

    >>> simulation = post.load_simulation('/home/user/file.rst')


有关与 :class:`Simulation <ansys.dpf.post.simulation.Simulation>` 对象交互的更详细示例，请参阅 :ref:`ref_basics` 。
