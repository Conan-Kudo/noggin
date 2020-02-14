from securitas.representation import Representation


class OTPToken(Representation):
    @property
    def uniqueid(self):
        return self._attr('ipatokenuniqueid')

    @property
    def description(self):
        return self._attr('description')

    @property
    def owner(self):
        return self._attrlist('ipatokenowner')

    @property
    def type(self):
        if 'type' in self.raw:
            return self.raw['type']
        return None
