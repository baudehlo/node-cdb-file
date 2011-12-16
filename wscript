srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')

def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.target = 'cdb-file'
  obj.source = 'cdb-file.cc cdb_find.c cdb_findnext.c cdb_hash.c cdb_init.c cdb_make.c cdb_make_add.c cdb_make_put.c cdb_seek.c cdb_seq.c cdb_unpack.c'
