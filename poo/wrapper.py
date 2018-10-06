
class Wrapper(object):
    def __init__(self,wrapped_class,*args,**kwargs):
        self.props = kwargs.get('props')
        kwargs.pop('props', None)
        self.wrapped_class = wrapped_class(*args,**kwargs)

    def __getattr__(self, attr):
        orig_attr = self.wrapped_class.__getattribute__(attr)
        if orig_attr not in self.props and len(self.props) > 0:
            raise ValueError("la propiedad {} no existe".format(attr,))

        if callable(orig_attr):
            def hooked(*args, **kwargs):
                self.pre()
                result = orig_attr(*args, **kwargs)
                self.post()
                return result
            return hooked
        else:
            return orig_attr

    def pre(self):
        pass
        # print(">> pre")

    def post(self):
        pass
        # print("<< post")