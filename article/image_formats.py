from wagtail.wagtailimages.formats import register_image_format, \
    unregister_image_format, Format


unregister_image_format("fullwidth")
register_image_format(Format('fullwidth', 'Full width', 'richtext-image full-width', 'max-1400x1120'))
register_image_format(Format('halfwidth', 'Half Width (512px)', 'richtext-image half-width', 'max-512x410'))
