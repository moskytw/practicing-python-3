# m

print('Access m:')

import m
m.f()

from m import f
f()

print()

# ma

print('Access ma:')

import p.ma
p.ma.fa()

from p import ma
ma.fa()

from p.ma import fa
fa()

print()

# mb

print('Access mb:')

import p.mb
p.mb.fa()

print()

# as

print('Use as:')

import m as _m
_m.f()

from m import f as _f
_f()
