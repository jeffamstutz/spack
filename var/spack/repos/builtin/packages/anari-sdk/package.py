# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class AnariSdk(CMakePackage):
    """The ANARI-SDK implements the front end library + tools for using the
      ANARI 3D rendering engine interface API developed by Khronos."""

    homepage = "https://www.khronos.org/ANARI"
    url = "https://github.com/KhronosGroup/ANARI-SDK/archive/refs/tags/v0.10.0.zip"

    maintainers("jeffamstutz")

    license("Apache-2.0", checked_by="jeffamstutz")

    version("0.10.0", sha256="bf74a10150255bd2be9537585f027e1f077438d24a96652ad7cc31c544d7ec28")

    depends_on("python")

    def cmake_args(self):
        args = [
          self.define("BUILD_CTS", False),
          self.define("BUILD_EXAMPLES", False),
          self.define("BUILD_HELIDE_DEVICE", True),
          self.define("BUILD_REMOTE_DEVICE", False),
          self.define("BUILD_SCENES_LIB", True),
          self.define("BUILD_SHARED_LIBS", True),
          self.define("BUILD_TESTING", False),
          self.define("INSTALL_CODE_GEN_SCRIPTS", True),
          self.define("INSTALL_PYTHON_BINDINGS", True),
          self.define("INSTALL_VIEWER_LIBRARY", True)
        ]
        return args

