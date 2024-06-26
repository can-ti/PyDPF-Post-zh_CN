.. _compatibility:

=============
Compatibility
=============

PyDPF-Post 支持 Windows 10 和 CentOS 7 及更高版本。更多信息，请参阅 `Ansys 平台支持 <https://www.ansys.com/solutions/solutions-by-role/it-professionals/platform-support>`_ 。

在容器化生态系统中使用 PyDPF-Post 可以支持其他平台，例如 `Docker <https://www.docker.com/>`_ 或 `Kubernetes <https://kubernetes.io/>`_ 。

由于在 PyDPF-Core 0.5.2 或更高版本中使用 PyDPF-Post 0.2.2 或更早版本可能会导致崩溃，您应该参考下表了解这两个库之间的兼容性。

.. list-table:: PyDPF compatibility
   :widths: 20 20 20
   :header-rows: 1

   * - DPF server version
     - ansys.dpf.core python module version
     - ansys.dpf.post python module version
   * - 7.0 (DPF Server 2024.1.pre0)
     - 0.9.0 or later
     - 0.5.0 or later
   * - 6.1 (DPF Server 2023.2.pre1)
     - 0.8.0 or later
     - 0.4.0 or later
   * - 6.0 (DPF Server 2023.2.pre0)
     - 0.7.0 or later
     - 0.3.0 or later
   * - 5.0 (Ansys 2023 R1)
     - 0.6.0 or later
     - 0.3.0 or later
   * - 4.0 (Ansys 2022 R2)
     - 0.5.0 or later
     - 0.3.0 or later
   * - 3.0 (Ansys 2022 R1)
     - 0.4.0 or later
     - 0.1.0 or later
   * - 2.0 (Ansys 2021 R2)
     - 0.3.0 or later
     - 0.1.0 or later
   * - 1.0 (Ansys 2021 R1)
     - 0.2.*
     - 0.1.0 or later
