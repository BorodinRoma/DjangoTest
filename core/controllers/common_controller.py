class CommonController:
    def __init__(self, model):
        self.model = model

    def clear_data(self, data: dict, secondary_fk: list):
        for fk in secondary_fk:
            if fk in data:
                data.pop(fk)

    def update_data(self, data: dict) -> dict:
        for field in self.model._meta.fields:
            field_type = field.get_internal_type()
            if field_type == 'ForeignKey' or field_type == 'OneToOneField':
                try:
                    data.update({field.name + '_id': data[field.name]})
                    data.pop(field.name)
                except KeyError:
                    pass
        return data