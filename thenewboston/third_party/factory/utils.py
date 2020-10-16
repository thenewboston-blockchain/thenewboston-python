import factory


def build_json(factory_class, **kwargs):
    """
    Build json representation for object using factory.
    """

    return factory.build(
        dict,
        FACTORY_CLASS=factory_class,
        **kwargs,
    )
