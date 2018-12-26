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

import metashade.hlsl.data_types
import metashade.clike.struct

class StageInterface(metashade.clike.struct.StructDef):
    pass

class VertexShaderIn(StageInterface):
    pass

class VertexShaderOut(StageInterface):
    def __init__(self, **kwargs):
        position_name = 'position'
        position_type = metashade.hlsl.data_types.Vector4f
        
        for name, data_type in kwargs.iteritems():
            if name == position_name or data_type == position_type:
                raise RuntimeError('Homogenous position output already defined')
        
        kwargs[position_name] = position_type 
        super(VertexShaderOut, self).__init__(**kwargs)

class PixelShaderIn(StageInterface):
    pass

class PixelShaderOut(StageInterface):
    pass