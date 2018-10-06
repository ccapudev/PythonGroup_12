class Punto:
    def __init__(self, positiony, positionx):
        self.positiony = positiony
        self.positionx = positionx

    @property
    def position_str(self):
        return '{},{}'.format(
            self.positiony,
            self.positionx,
        )

    def __str__(self):
        return 'Punto({})'.format(
            self.position_str
        )

    def __repr__(self):
        return self.__str__()


class Circulo(Punto):

    def __init__(self, positiony, positionx, **kwargs):
        super(Circulo, self).__init__(positiony, positionx)
        self.radio = kwargs.get('radio')

    def __str__(self):
        return 'Circulo({}, diametro={})'.format(
            self.position_str,
            self.radio * 2
        )


punto = Punto(20, 10)
circulo = Circulo(20, 10, radio=5)

print([punto, circulo])



