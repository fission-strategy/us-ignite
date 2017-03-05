EXTRA_MODEL_FIELDS = (
    (
        "mezzanine.pages.models.RichTextPage.about_desc",
        "mezzanine.core.fields.RichTextField",
        ("About description",),
        {"blank": True, "null": True}
    ),
)

MIGRATION_MODULES = {
    "pages": "us_ignite.migration_modules.pages",
    "galleries": "us_ignite.migration_modules.galleries",
    "forms": "us_ignite.migration_modules.forms",
}
