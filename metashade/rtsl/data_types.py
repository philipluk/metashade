# Copyright 2018 Pavlo Penenko
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

import numbers
import sys
import metashade.clike.data_types as clike
from metashade.clike.data_types import Float

class _RawVector(clike.ArithmeticType):
    _swizzle_str = 'xyzw'

    def __getattr__(self, name):
        is_valid_swizzle = False
        try:
            is_valid_swizzle = len(name) <= 4 and all(
                self.__class__._swizzle_str.index(ch) < self.__class__._dim
                    for ch in name
            )
        except ValueError:
            pass

        if is_valid_swizzle:
            dtype = self._get_related_type(len(name))
            return dtype('.'.join((self.get_ref(), name)))
        else:
            raise AttributeError

    def _check_dims(self, rhs):
        if rhs.__class__._dim != self.__class__._dim:
            raise ArithmeticError(
                'Operands must have the same dimensions.'
            )

    def _check_mul(self, matrix):
        if matrix.__class__._dims[0] != self.__class__._dim:
            raise ArithmeticError(
                'The number of rows in the matrix must be equal to the size of'
                ' the vector'
            )

    @classmethod
    def _is_compatible_tuple(cls, t):
        if type(t) is not tuple or len(t) != cls._dim:
            return False

        for element in t:
            if not (isinstance(element, numbers.Number) \
                or isinstance(element, cls._element_type)
            ):
                return False
        return True

    def _rhs_binary_operator(self, rhs, op : str):
        if self.__class__ != rhs.__class__:
            return NotImplemented

        self._check_dims(rhs)

        return self.__class__(
            self.__class__._emit_binary_operator(
                self, rhs, op
            )
        )

    @classmethod
    def _scalar_mul(cls, lhs, rhs):
        return cls(cls._emit_binary_operator(lhs, rhs, '*'))

    def __mul__(self, rhs):
        per_element_result = self._rhs_binary_operator(rhs, '*')
        if per_element_result != NotImplemented:
            return per_element_result

        if rhs.__class__ == self._element_type:
            return self.__class__._scalar_mul(self, rhs)
        else:
            return NotImplemented

    def __rmul__(self, lhs):
        if lhs.__class__ == self._element_type:
            return self.__class__._scalar_mul(lhs, self)
        else:
            return NotImplemented

    def dot(self, rhs):
        self._check_dims(rhs)
        return self.__class__._element_type(
            'dot({this}, {rhs})'.format(
                this = self.get_ref(), rhs = rhs.get_ref()
            )
        )

class Float1(_RawVector):
    _dim = 1

class Float2(_RawVector):
    _dim = 2

class Float3(_RawVector):
    _dim = 3

    def cross(self, rhs):
        if rhs.__class__ != self.__class__:
            raise ArithmeticError(
                'Cross product operands must have the same type (3D vector)'
            )
        return self.__class__(
            'cross({this}, {rhs})'.format(
                this = self.get_ref(), rhs = rhs.get_ref()
            )
        )

class Float4(_RawVector):
    _dim = 4

class _RawMatrix(clike.ArithmeticType):
    def _check_mul(self, vector):
        if self.__class__._dims[1] != vector.__class__._dim:
            raise ArithmeticError(
                'The number of columns in the matrix must be equal to the size'
                'of the vector'
            )

# Generate all concrete matrix types to avoid copy-and-paste
for rows in range(1, 5):
    for cols in range(1, 5):
        name = 'Float{rows}x{cols}'.format(rows = rows, cols = cols)
        globals()[name] = type(
            name,
            (_RawMatrix,),
            {'_dims' : (rows, cols)}
        )

def _get_tuple_type(element_type, dim : int, prefix : str):
    if dim == 1:
        return element_type

    if dim not in (2, 3, 4):
        raise RuntimeError('Unsupported vector width')

    if not issubclass(element_type, Float):
        raise RuntimeError(
            'Vectors of types other than 32-bit float are not implemented yet'
        )

    type_name = '{prefix}{dim}f'.format(prefix = prefix, dim = dim)
    return getattr(sys.modules[element_type.__module__], type_name)

def get_vector_type(element_type, dim : int):
    return _get_tuple_type(element_type, dim, 'Vector')

def get_point_type(element_type, dim : int):
    return _get_tuple_type(element_type, dim, 'Point')

class _VectorBase:
    @classmethod
    def _get_related_type(cls, dim):
        return get_vector_type(cls._element_type, dim)

class Vector2f(_VectorBase):
    pass

class Vector3f(_VectorBase):
    def as_vector4(self):
        vector4_type = self._get_related_type(4)
        return vector4_type(
            '{dtype}({this}, 0.0f)'.format(
                dtype = vector4_type.get_target_type_name(),
                this = self.get_ref()
            )
        )

class Vector4f(_VectorBase):
    def as_vector4(self):
        return self

class _PointBase:
    @classmethod
    def _get_related_type(cls, dim):
        return get_point_type(cls._element_type, dim)

class Point2f(_PointBase):
    pass

class Point3f(_PointBase):
    def as_vector4(self):
        vector4_type = get_vector_type(self.__class__._element_type, 4)
        return vector4_type(
            '{dtype}({this}, 1.0f)'.format(
                dtype = vector4_type.get_target_type_name(),
                this = self.get_ref()
            )
        )

class RgbF:
    pass

class RgbaF:
    pass
