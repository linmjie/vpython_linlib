import vpython as vp
from .axis import Axis

class vec3(vp.vector):
    @staticmethod
    def rand3() -> vec3:
        return vec3(vp.vector.random())

    @staticmethod
    def rand2() -> vec3:
        vec = vp.vector.random()
        vec.z = 0
        return vec3(vec)

    def display(self, *, origin: vp.vector | None = None,
                      color: vp.vector | None = None) -> vp.arrow:
        if origin is None:
            origin = Axis.ZERO
        if color is None:
            color = vp.color.red
        return vp.arrow(pos=origin, axis=self, color=color, shaftwidth=0.5, emissive=True)
