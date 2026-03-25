import vpython as vp
import weakref as wf

def delete(obj: vp.standardAttributes):
    obj.visible = False
    # implement deletion from registers later
    del obj

# Python is garbage collected and this is not a real defer
# The delete activates once the ref count of the object is 0
# Not assignging the defer to a variable results in immediate deletion
class DeferredDelete:
    def __init__(self, obj: vp.standardAttributes):
        self.obj = obj
        self.finalizer = wf.finalize(self, delete, self.obj)

    @property
    def val(self) -> vp.standardAttributes:
        return self.obj
