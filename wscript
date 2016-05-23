#!/usr/bin/env python
# encoding: utf-8

def options(opt):
	opt.load('compiler_c')

def configure(conf):
	conf.load('compiler_c flex bison')
        conf.env.LIB_CALC = ['m','fl']

def build(bld):
	tg = bld(
		features = 'c cprogram',
		source = 'rpcalc.y',
		target = 'rpcalc',
		use    = 'CALC')
        
	tc = bld(
		features = 'c cprogram',
		source = 'calc.l calc.y',
		target = 'calc',
		use    = 'CALC')
