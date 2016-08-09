#!/mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python
# USAGE:

# PREAMBLE:
import sys
import os

conf = sys.argv[1]
dcd_loc = sys.argv[2]
cpptraj_home = sys.argv[3]

# SUBROUTINES:

makedir = os.mkdir
changedir = os.chdir
terminal = os.system

def first_trun(conf, system, ncdf_loc):
        makedir('%s' %(system))
	changedir('%s' %(system))
	nf = open('trunc.in', 'w')
	nf.write('trajin %s ../../%s.prmtop\nautoimage\nsolvent :WAT\nclosest 5000 :1-257@CA oxygen outprefix truncated \nouttraj %s.dcd\nrun' %(dcd_loc, conf, system))
	nf.close()
	terminal("%s/cpptraj -p ../../%s.prmtop -i trunc.in > %s.cpptraj.log" %(cpptraj_home, conf, system))
	terminal("mv truncated.%s.prmtop ../../truncated.prmtop" %(conf))
	changedir('..')

def truncation(conf, system, ncdf_loc):
	makedir('%s' %(system))
	changedir('%s' %(system))
	nf = open('trunc.in', 'w')
	nf.write('trajin %s ../../%s.prmtop\nautoimage\nsolvent :WAT\nclosest 5000 :1-257@CA oxygen \nouttraj %s.dcd\nrun' %(dcd_loc, conf, system))
	nf.close()
	terminal("%s/cpptraj -p ../../%s.prmtop -i trunc.in > %s.cpptraj.log" %(cpptraj_home, conf, system))
	changedir('..')

# MAIN PROGRAM:

#truncation(conf,'min1', '../../min_heat_equil/%s.min1.ncdf' %(conf))
#truncation(conf,'min2', '../../min_heat_equil/%s.min2.ncdf' %(conf))
#first_trun(conf,'heat', '../../../../min_heat_equil/%s.heat.ncdf' %(conf))
#truncation(conf,'equil1', '../../../../min_heat_equil/%s.equil1.ncdf' %(conf))
#truncation(conf,'equil2', '../../../../min_heat_equil/%s.equil2.ncdf' %(conf))
#truncation(conf,'equil3', '../../../../min_heat_equil/%s.equil3.ncdf' %(conf))
truncation(conf,'equil4', '../../../../min_heat_equil/%s.equil4.ncdf' %(conf))
#truncation(conf,'equil5', '../../../../min_heat_equil/%s.equil5.ncdf' %(conf))

