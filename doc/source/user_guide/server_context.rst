.. _user_guide_server_context:

==============
Server context
==============

在使用 Ansys 2023 R1 之后发布的 DPF 服务器时，将区分与 Ansys 许可证的两种交互方式：

- 当 **Premium** [ˈprimɪəm] DPF Server context 处于活动状态时，底层操作会检查是否存在有效的 Ansys 许可证，并允许在需要时签出该许可证。这意味着所有 DPF 功能都可用，但许可证可能会被签出。
- 当 **Entry** DPF Server context 处于活动状态时，底层操作会检查是否存在有效的 Ansys 许可证，但不允许签出任何许可证。这意味着需要签出许可证的操作不可用，并会引发错误。

默认情况下，使用 PyDPF-Post 启动 DPF 服务器时，**Premium** Server context 处于活动状态。要了解更多信息，请参阅 `PyDPF-Core 文档 <https://dpf.docs.pyansys.com/dev/user_guide/server_context.html>`_ 。

Change the default server context
---------------------------------

服务器的默认上下文是 **Premium** 。您可以使用 ``ANSYS_DPF_SERVER_CONTEXT`` 环境变量更改上下文。
有关详细信息，请参阅 `ServerContext class 文档 <https://dpf.docs.pyansys.com/dev/api/ansys.dpf.core.server_context.html>`_ 。您也可以使用此代码更改服务器上下文：

.. code-block:: python

    from ansys.dpf import post
    post.set_default_server_context(post.AvailableServerContexts.entry)


Release history
---------------

**Entry** 服务器上下文在服务器版本 6.0（Ansys 2023 R2）及更高版本中可用。

服务器版本早于 6.0（Ansys 2023 R1 及更早版本）时， **Premium** 是默认的服务器上下文，所有功能都可用，仅取决于其发布日期。