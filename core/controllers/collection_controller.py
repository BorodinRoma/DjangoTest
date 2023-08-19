from django.contrib.auth.models import User

from core.models import Collection


class CollectionController:
    class NotExistException(Exception):
        pass

    def __init__(self, user: User):
        self.user = user

    def create_collection(self, data: dict):
        collection = Collection.objects.get_or_create(created_by=self.user, name=data['name'],
                                                      description=data['description'])[0]
        bookmarks_list_id = data['bookmarks']

        for bookmark_id in bookmarks_list_id:
            collection.bookmarks.add(bookmark_id)
            collection.save()

        return collection

    def add_bookmarks(self, data: dict):
        try:
            collection = Collection.objects.get(pk=data['collection_id'], created_by=self.user)
        except Collection.DoesNotExist:
            raise self.NotExistException('Такой коллекции не существует')
        bookmarks_list_id = data['bookmarks']

        for bookmark_id in bookmarks_list_id:
            collection.bookmarks.add(bookmark_id)
            collection.save()

        return collection

    def delete_bookmarks(self, data: dict):
        try:
            collection = Collection.objects.get(pk=data['collection_id'], created_by=self.user)
            bookmarks = list(collection.bookmarks.values_list('id', flat=True))


            for bookmark_id in data['bookmarks']:
                if bookmark_id in bookmarks:
                    collection.bookmarks.remove(bookmark_id)
                    collection.save()

        except Collection.DoesNotExist:
            raise self.NotExistException('Такой коллекции не существует')


