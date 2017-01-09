EXTRA_MODEL_FIELDS = (
    (
        "mezzanine.blog.models.BlogPost.excerpt",
        "TextField",
        ("Excerpt",),
        {"blank": True, "null": True}
    ),
    (
        "mezzanine.blog.models.BlogPost.image",
        "ImageField",
        ("Featured Image",),
        {'blank': True, 'null': True, 'upload_to': 'blog'}
    ),
)
