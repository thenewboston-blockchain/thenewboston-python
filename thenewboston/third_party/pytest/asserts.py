def assert_objects_vs_dicts(objects, dicts, sort=True, key='id'):
    """
    Compare list of django objects with serialized objects using their id's
    """

    objects_ids = [str(getattr(obj, key)) for obj in objects]
    dicts_ids = [str(obj.get(key)) for obj in dicts]

    if sort:
        assert sorted(objects_ids) == sorted(dicts_ids)
    else:
        assert objects_ids == dicts_ids
