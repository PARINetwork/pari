from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from functional_tests.factory import *
from category.models import Category
from django.template import loader, Context
import shutil
import os


class Command(BaseCommand):
    help = 'Setup initial data for the application'

    def handle(self, *args, **options):
        sainath_bio = "P. Sainath is the founder-editor of the People's Archive of Rural India. He has been a rural reporter for decades and is the author of 'Everybody Loves a Good Drought'"
        namita_bio = "Namita Waikar is a writer, translator and the managing editor of PARI. She is a partner in a chemistry databases firm, and has worked as a biochemist and a software project manager"
        sainath = AuthorFactory(name="P.Sainath", slug="sainath", email="psainath@gmail.com", facebook_username="",
                                twitter_username="@PSainath_org", website="http://psainath.org/", bio=sainath_bio)
        namita = AuthorFactory(name="Namita Waikar", slug="namita", email="namita.waikar@gmail.com",
                               facebook_username="namita.waikar",
                               twitter_username="@NamitaWaikar", website="http://www.namitawaikar.com/", bio=namita_bio)

        self.create_categories()
        chennai = LocationFactory(name="Chennai", slug="chennai", district="Chennai", state="Tamil Nadu")
        mumbai = LocationFactory(name="Mumbai", slug="chennai", district="Mumbai", state="Maharashtra")

        self.copy_images()

        image1 = ImageFactory.create(photographers=(sainath,), locations=(chennai,), file="uploads/image1.jpg")
        image2 = ImageFactory.create(photographers=(sainath,), locations=(chennai,), file="uploads/image2.jpg")
        image3 = ImageFactory.create(photographers=(sainath, namita), locations=(chennai, mumbai),
                                     file="uploads/image3.jpg", title="loom")
        image4 = ImageFactory.create(photographers=(namita,), locations=(mumbai,), file="uploads/image4.jpg")
        image5 = ImageFactory.create(photographers=(namita,), locations=(mumbai,), file="uploads/image5.jpg")
        article_image1 = ImageFactory.create(photographers=(namita,), locations=(mumbai,), file="uploads/article1.jpg")
        article_image2 = ImageFactory.create(photographers=(namita,), locations=(mumbai,), file="uploads/article2.jpg")

        PageFactory.create(title="Header", path="00010007")
        PageFactory.create(title="Articles", path="00010005")
        PageFactory.create(title="Albums", path="00010006")

        category = Category.objects.get(slug="photozone")
        video_category = Category.objects.get(slug="videozone")
        get_tmpl = loader.get_template
        article1_content = get_tmpl("core/article1.txt").render()
        article2_content = get_tmpl("core/article2.txt").render()

        article1 = ArticleFactory.create(title="No longer a toy story", authors=(sainath,), categories=(category,),
                                         locations=(chennai,), featured_image=article_image1, depth=3, path="000100050020", content=article1_content)
        article1.save_revision().publish()
        article2 = ArticleFactory.create(title="The cows sons are praying in the fields", authors=(namita,), categories=(category,),
                                         locations=(mumbai,), featured_image=article_image2, depth=3, path="000100050021", content=article2_content)
        article2.save_revision().publish()
        video_article = ArticleFactory.create(title="video article", authors=(sainath, namita), categories=(video_category,),
                                         locations=(mumbai,), featured_image=image3, depth=3, path="000100050022")
        video_article.save_revision().publish()
        talking_album = TalkingAlbumSlideFactory.create(image=image4, page__depth=3, page__path="000100060020").page
        talking_album.save_revision().publish()
        photo_album = PhotoAlbumSlideFactory.create(image=image5, page__depth=3, page__path="000100060021").page
        photo_album.save_revision().publish()

        HomePageFactory.create(carousel_0=article1, carousel_1=article2, in_focus_page1=article1,
                               in_focus_page2=article2, video=video_article, talking_album=talking_album,
                               photo_album=photo_album, title='Home Page')
        GalleryHomePageFactory.create(photo_of_the_week=image1, video=video_article, talking_album=talking_album,
                               photo_album=photo_album, title='Gallery Home Page')

        GuidelinesPageFactory.create(titlle='Guidelines Page')

        # Create initial super user
        admin_user_present = User.objects.filter(username='admin').exists()
        if not admin_user_present:
            User.objects.create_superuser('admin', 'admin@development', 'admin')

        self.stdout.write('Data setup successfully')

    def copy_images(self):
        if not os.path.exists("media/uploads"):
            os.makedirs("media/uploads")

        shutil.copy2('core/management/commands/images/image1.jpg', 'media/uploads/image1.jpg')
        shutil.copy2('core/management/commands/images/image2.jpg', 'media/uploads/image2.jpg')
        shutil.copy2('core/management/commands/images/image3.jpg', 'media/uploads/image3.jpg')
        shutil.copy2('core/management/commands/images/image4.jpg', 'media/uploads/image4.jpg')
        shutil.copy2('core/management/commands/images/image5.jpg', 'media/uploads/image5.jpg')
        shutil.copy2('core/management/commands/images/article1.jpg', 'media/uploads/article1.jpg')
        shutil.copy2('core/management/commands/images/article2.jpg', 'media/uploads/article2.jpg')

    def create_categories(self):
        category_update_dict = {
            "things-we-do": {"name": "Things We Do", "description": "The world of rural labour"},
            "things-we-make": {"name": "Things We Make", "description": "Artisans, artists and craftspersons"},
            "farming-and-its-crisis": {"name": "Farming and its Crisis",
                                       "description": "The troubled world of agriculture"},
            "Little takes": {"name": "Little Takes", "description": "Small, impactful video clips"},
            "the-rural-in-the-urban": {"name": "The Rural in the Urban", "description": "Migrant workers across India"},
            "women": {"name": "Women", "description": "More than half the sky"},
            "adivasis": {"name": "Adivasis", "description": "The first dwellers"},
            "dalits": {"name": "Dalits", "description": "Struggles of the oppressed"},
            "we-are": {"name": "We Are", "description": "Communities and cultures"},
            "resource-conflicts": {"name": "Resource Conflicts", "description": "Jal, jungle, zameen"},
            "foot-soldiers-of-freedom": {"name": "Foot-Soldiers of Freedom",
                                         "description": "The last living freedom fighters"},
            "small-world": {"name": "Small World", "description": "A focus on children"},
            "musafir": {"name": "Musafir", "description": "Travellers' tales, everyday lives"},
            "getting-there": {"name": "Getting There", "description": "Zany rural transportation"},
            "the-wild": {"name": "The Wild", "description": "The world of nature"},
            "sports-games": {"name": "Rural Sports", "description": "Games people play"},
            "health": {"name": "Healthcare", "description": "The state of rural health"},
            "folklore": {"name": "Mosaic", "description": "Culture and folklore"},
            "environment": {"name": "Environment", "description": "People, livelihoods, habitats"},
            "tongues": {"name": "Tongues", "description": "The universe of our languages"},
            "visible-work-invisible-women": {"name": "Visible Work, Invisible Women",
                                             "description": "Women and work: a photo exhibition"},
            "one-offs": {"name": "One-Offs", "description": "Videos, photos, articles"},
            "headgear": {"name": "Things We Wear", "description": "Clothing, headgear, jewellery..."},
            "pari-for-schools": {"name": "PARI for Schools", "description": "Work done for PARI by students"},
            "videozone": {"name": "VideoZone", "description": "Stories told in moving pictures"},
            "audiozone": {"name": "AudioZone", "description": "You could listen all day"},
            "photozone": {"name": "PhotoZone", "description": "Collections of photographs"}
        }

        for slug, value in category_update_dict.iteritems():
            name = value["name"]
            description = value["description"]
            CategoryFactory(name=name, slug=slug, description=description)
