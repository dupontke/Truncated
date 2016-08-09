#!/mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python
# USAGE:

# PREAMBLE:
import sys
import os

conf = sys.argv[1]
prod_loc = sys.argv[2]
cpptraj_home = sys.argv[3]

# SUBROUTINES:

makedir = os.mkdir
changedir = os.chdir
terminal = os.system

def truncation(conf, system, ncdf_loc):
	makedir('%s' %(system))
	changedir('%s' %(system))
	nf = open('trunc.in', 'w')
	nf.write('trajin ../../%s/*.ncdf ../../%s.prmtop\nautoimage\nsolvent :WAT\nclosest 5000 :1-257@CA oxygen \nouttraj %s.dcd\nrun' %(prod_loc, conf, system))
	nf.close()
	terminal("%s/cpptraj -p ../../%s.prmtop -i trunc.in > %s.cpptraj.log" %(cpptraj_home, conf, system))
	changedir('..')

# MAIN PROGRAM:

truncation(conf, '%s' %(prod_loc), '../../%s/*.ncdf' %(prod_loc))
