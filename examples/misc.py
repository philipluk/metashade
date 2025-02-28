# This is just a helper file to test example code snippets for Markdown
# and presentations.

import math
from metashade.hlsl.sm6 import ps_6_0 as hlsl_ps

with open('misc.hlsl', 'w') as hlsl_file:
    sh = hlsl_ps.Generator(hlsl_file)

    with sh.function('foo', sh.Float)(
        N = sh.Vector3f, L = sh.Vector3f
    ):
        sh // 'Create a float variable with the value of pi'
        sh.x = sh.Float(math.pi)

        sh.rgba = sh.RgbaF(rgb = (0, 1, 0), a = 0)

        sh // 'Swizzling - the destination type is deduced'
        sh // "a-la `auto` in C++"
        sh.color = sh.rgba.rgb

        sh // 'Write masking'
        sh.color.r = 1

        sh // 'Intrinsics example'
        sh.N = sh.N.normalize()

        sh // 'Dot product == Python 3 matmul'
        sh // '(a.k.a. "walrus") operator'
        sh.NdotL = sh.N @ sh.L

        sh.xyz = sh.rgba.xyz    # Exception: `RgbaF` has no attribute `xyz`

        sh.return_(sh.NdotL)

        # TODO:
        # texture-sampler combination and sampling
        # Comments
        # build abstractions on top, e.g. glTF textures in my demo
