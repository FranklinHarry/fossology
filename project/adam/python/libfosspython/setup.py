from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext
setup(
  name = "PyrexDevelWrapper",
  ext_modules=[ 
    Extension("libfosspython", ["libfosspython.pyx"], extra_objects = ["./devel/libfossagent/libfossagent.o", "./devel/libfossdb/libfossdb.o", "./devel/libfossrepo/libfossrepo.o"], libraries = ["pq"], include_dirs = ["/usr/include/postgresql"])
    ],
  cmdclass = {'build_ext': build_ext}
)
