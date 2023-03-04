# Copyright 2023 Pavlo Penenko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ATTENTION! This file has been auto-generated by
# https://github.com/ppenenko/DirectXShaderCompiler/blob/metashade/issues/9/export_intrinsics/utils/metashade/export_intrinsics.py
 
class AnyLayoutMixin:
	def acos(self):
		return self.__class__( f'acos({self})' )

	def asin(self):
		return self.__class__( f'asin({self})' )

	def atan(self):
		return self.__class__( f'atan({self})' )

	def atan2(self, y):
		return self.__class__( f'atan2({self}, {y})' )

	def ceil(self):
		return self.__class__( f'ceil({self})' )

	def cos(self):
		return self.__class__( f'cos({self})' )

	def cosh(self):
		return self.__class__( f'cosh({self})' )

	def ddx(self):
		return self.__class__( f'ddx({self})' )

	def ddx_coarse(self):
		return self.__class__( f'ddx_coarse({self})' )

	def ddx_fine(self):
		return self.__class__( f'ddx_fine({self})' )

	def ddy(self):
		return self.__class__( f'ddy({self})' )

	def ddy_coarse(self):
		return self.__class__( f'ddy_coarse({self})' )

	def ddy_fine(self):
		return self.__class__( f'ddy_fine({self})' )

	def degrees(self):
		return self.__class__( f'degrees({self})' )

	def exp(self):
		return self.__class__( f'exp({self})' )

	def exp2(self):
		return self.__class__( f'exp2({self})' )

	def floor(self):
		return self.__class__( f'floor({self})' )

	def fmod(self, b):
		return self.__class__( f'fmod({self}, {b})' )

	def frac(self):
		return self.__class__( f'frac({self})' )

	def fwidth(self):
		return self.__class__( f'fwidth({self})' )

	def ldexp(self, exp):
		return self.__class__( f'ldexp({self}, {exp})' )

	def lerp(self, a, b):
		return self.__class__( f'lerp({a}, {b}, {self})' )

	def log(self):
		return self.__class__( f'log({self})' )

	def log10(self):
		return self.__class__( f'log10({self})' )

	def log2(self):
		return self.__class__( f'log2({self})' )

	def modf(self, ip):
		return self.__class__( f'modf({self}, {ip})' )

	def pow(self, y):
		return self.__class__( f'pow({self}, {y})' )

	def radians(self):
		return self.__class__( f'radians({self})' )

	def rcp(self):
		return self.__class__( f'rcp({self})' )

	def round(self):
		return self.__class__( f'round({self})' )

	def rsqrt(self):
		return self.__class__( f'rsqrt({self})' )

	def saturate(self):
		return self.__class__( f'saturate({self})' )

	def sin(self):
		return self.__class__( f'sin({self})' )

	def sinh(self):
		return self.__class__( f'sinh({self})' )

	def smoothstep(self, a, b):
		return self.__class__( f'smoothstep({a}, {b}, {self})' )

	def sqrt(self):
		return self.__class__( f'sqrt({self})' )

	def step(self, x):
		return self.__class__( f'step({self}, {x})' )

	def tan(self):
		return self.__class__( f'tan({self})' )

	def tanh(self):
		return self.__class__( f'tanh({self})' )

	def trunc(self):
		return self.__class__( f'trunc({self})' )

