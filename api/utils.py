import utils.database_handler


def check_register_json(json):
    fields = {
        'name': str,
        'surname': str,
        'birthday': int,
        'gender': str,
        'password': str,
    }

    for field_name, field_type in fields.items():
        if field_name in json:
            if not isinstance(json[field_name], field_type):
                return False
        else:
            return False

    return True


def register_user(data):
    pass

