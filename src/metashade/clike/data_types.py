# Copyright 2017 Pavlo Penenko
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

import metashade.base.data_types as base

class BaseType(base.BaseType):
    def _define(self, sh, identifier):
        self._bind(sh, identifier, allow_defaults=True)
        
        self._sh._write('{type_name} {identifier}{initializer};\n'.format(
            type_name = self.__class__.get_target_type_name(),
            identifier = self._name,
            initializer = '' if self._expression is None \
                else ' = {}'.format(self._expression) ))
        
    def _arg_define(self, sh, identifier):
        self._bind(sh, identifier, allow_defaults=False)
        
        self._sh._write('{type_name} {identifier}'.format(
            type_name = self.__class__.get_target_type_name(),
            identifier = self._name))
        
    def __setattr__(self, name, value):
        if name == '_':
            self._expression = value
            self._sh._write('{identifier} = {value};\n'.format(
                identifier = self._name,
                value = value.get_ref() if hasattr(value, 'get_ref') else value ))
        else:
            object.__setattr__(self, name, value)

    @classmethod
    def get_target_type_name(cls):
        return cls._target_name if hasattr(cls, '_target_name') \
            else cls.__name__

class AddMixIn(object):
    def __add__(self, rhs):
        return self.__class__('{this} + {rhs}'.format(
            this = self.get_ref(), rhs = rhs.get_ref() ))
        
class Float(BaseType, AddMixIn):
    pass