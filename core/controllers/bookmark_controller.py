from core.controllers.common_controller import CommonController
from core.controllers.open_graph_controller import OpenGraphController
from core.models import Bookmark


class BookmarkController:

    class NotAccessException(Exception):
        pass

    def __init__(self, user):
        self.user = user

    def create_bookmark(self, url) -> Bookmark:
        # new_data = CommonController(Bookmark).update_data(data)
        site_info = OpenGraphController(url).open_graph_parse()
        bookmark = Bookmark.objects.get_or_create(created_by=self.user, title=str(site_info['title']),
                                                  description=site_info['description'], image=site_info['image'],
                                                  type_id=site_info['type_id'], ref=site_info['ref'])[0]

        return bookmark


    def destroy(self, pk):
        bookmark_list_id = list(Bookmark.objects.filter(created_by=self.user).values_list('id', flat=True))
        if pk in bookmark_list_id:
            Bookmark.objects.get(pk=pk).delete()
        else:
            raise self.NotAccessException('У вас нет прав для удаление этой закладки')