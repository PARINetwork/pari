from functional_tests.factory import ArticleFactory
from functional_tests.factory import CategoryFactory
from functional_tests.factory import PhotoAlbumSlideFactory
from functional_tests.factory import TalkingAlbumSlideFactory


class DataSetup():
    def create_article(self, title, author, category, location, image, show_modular_content=False,
                       modular_content=None):
        if modular_content is not None:
            return ArticleFactory.create(title=title, authors=(author,), categories=(category,),
                                         locations=(location,), featured_image=image,
                                         show_modular_content=show_modular_content, modular_content=modular_content
                                         )

        return ArticleFactory.create(title=title, authors=(author,), categories=(category,),
                                     locations=(location,), featured_image=image,
                                     show_modular_content=show_modular_content
                                     )

    def create_video_article(self, title, author, location, image):
        category = CategoryFactory.create(name="VideoZone", slug="videozone", order=16)
        return self.create_article(title, author, category, location, image)

    def create_talking_album(self, image):
        talking_slide = TalkingAlbumSlideFactory.create(image=image)
        return talking_slide.page

    def create_photo_album(self, image):
        photo_slide = PhotoAlbumSlideFactory.create(image=image)
        return photo_slide.page
