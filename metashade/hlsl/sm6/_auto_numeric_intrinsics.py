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
	def EvaluateAttributeCentroid(self):
		return self.__class__( f'EvaluateAttributeCentroid({self})' )

	def QuadReadAcrossDiagonal(self):
		return self.__class__( f'QuadReadAcrossDiagonal({self})' )

	def QuadReadAcrossX(self):
		return self.__class__( f'QuadReadAcrossX({self})' )

	def QuadReadAcrossY(self):
		return self.__class__( f'QuadReadAcrossY({self})' )

	def WaveActiveMax(self):
		return self.__class__( f'WaveActiveMax({self})' )

	def WaveActiveMin(self):
		return self.__class__( f'WaveActiveMin({self})' )

	def WaveActiveProduct(self):
		return self.__class__( f'WaveActiveProduct({self})' )

	def WaveActiveSum(self):
		return self.__class__( f'WaveActiveSum({self})' )

	def WavePrefixProduct(self):
		return self.__class__( f'WavePrefixProduct({self})' )

	def WavePrefixSum(self):
		return self.__class__( f'WavePrefixSum({self})' )

	def abs(self):
		return self.__class__( f'abs({self})' )

	def clamp(self, min, max):
		return self.__class__( f'clamp({self}, {min}, {max})' )

	def mad(self, b, c):
		return self.__class__( f'mad({self}, {b}, {c})' )

	def max(self, b):
		return self.__class__( f'max({self}, {b})' )

	def min(self, b):
		return self.__class__( f'min({self}, {b})' )

