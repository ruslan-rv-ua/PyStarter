class Example:
    def __getattr__(self, attr_name):
        print(f'Attribute `{attr_name}` not found')

obj = Example()
obj.undefined_attribute
# 