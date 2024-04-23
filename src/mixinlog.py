class MixinLog:

    def print_ex(self):
        print(repr(self))

    def __repr__(self):
        classname = self.__class__.__name__
        attrs = []
        for attribute, value in self.__dict__.items():
            attrs.append(f'{attribute}={value}')
        return (f"Был создан экземпляр класса {classname} с аттрибутами: "
                f"{', '.join(attrs)}")
