from django.utils.text import slugify


def unique_slug_generator(model_instance, title, slug_field):
    '''Creates slug by reference to title. If title already
    exits, the primary key will be appended to the slug.

    Args:
        model_instance (object): An object that needs a slug
        title (string): Title of the object
        slug_field (string): Slug of object, if already exists.

    Returns:
        slug (string): A unique slug
    '''
    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1

        slug = f'{slug}-{object_pk}'

    return slug
