def all_field_names(model):
    """
    Return list of all field names for model
    """

    return [f.name for f in model._meta.get_fields()]


def common_field_names(a, b):
    """
    Return field names that are common between different models
    """

    field_names_a = standard_field_names(a)
    field_names_b = standard_field_names(b)
    return field_names_a.intersection(field_names_b)


def standard_field_names(model):
    """
    Return set of standard (excluding date, ID, and relational) field names for model
    """

    excluded = ['id', 'created_date', 'modified_date']
    return {f.name for f in model._meta.get_fields() if f.name not in excluded and not f.is_relation}
