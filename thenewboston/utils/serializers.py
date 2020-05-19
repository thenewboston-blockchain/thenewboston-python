def all_field_names(model):
    """
    Return list of all field names for model
    """

    return [f.name for f in model._meta.get_fields()]
