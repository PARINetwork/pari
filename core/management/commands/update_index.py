from django.db import transaction
from wagtail.wagtailsearch.management.commands.update_index import Command


class Command(Command):
    def __init__(self):
        super(Command, self).__init__()
        self.chunk_size = 1000

    def add_arguments(self, parser):
        parser.add_argument(
            '--batch-size', action='store', dest='batch-size', default=None, type=int,
            help="Specify a batch size for indexing")
        super(Command, self).add_arguments(parser)

    def handle(self, **options):
        if options['batch-size']:
            self.chunk_size = options['batch-size']
        super(Command, self).handle(**options)

    # Atomic so the count of models doesnt change as it is iterated
    @transaction.atomic
    def queryset_chunks(self, qs):
        """
        Yield a queryset in chunks of at most ``chunk_size``. The chunk yielded
        will be a list, not a queryset. Iterating over the chunks is done in a
        transaction so that the order and count of items in the queryset
        remains stable.
        """
        chunk_size = self.chunk_size

        i = 0
        while True:
            items = list(qs[i * chunk_size:][:chunk_size])
            if not items:
                break
            yield items
            i += 1
