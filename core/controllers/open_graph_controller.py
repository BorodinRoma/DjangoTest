import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from core.models import DictRefType


class OpenGraphController:

    def __init__(self, url: str):
        self.url = url

    def _get_page(self):
        """Scrapes a URL and returns the HTML source.

        Args:
            url (string): Fully qualified URL of a page.

        Returns:
            soup (string): HTML source of scraped page.
        """

        response = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(response,
                             'html.parser',
                             from_encoding=response.info().get_param('charset'))

        return soup

    def _get_og_title(self, soup):
        """Return the Open Graph title

        Args:
            soup: HTML from Beautiful Soup.

        Returns:
            value: Parsed content.
        """

        if soup.findAll("meta", property="og:title"):
            return soup.find("meta", property="og:title")["content"]
        else:
            return
        return

    def _get_og_locale(self, soup):
        """Return the Open Graph locale

        Args:
            soup: HTML from Beautiful Soup.

        Returns:
            value: Parsed content.
        """

        if soup.findAll("meta", property="og:locale"):
            return soup.find("meta", property="og:locale")["content"]
        else:
            return

        return

    def _get_og_description(self, soup):
        """Return the Open Graph description

        Args:
            soup: HTML from Beautiful Soup.

        Returns:
            value: Parsed content.
        """

        if soup.findAll("meta", property="og:description"):
            return soup.find("meta", property="og:description")["content"]
        else:
            return

        return

    def _get_og_site_name(self, soup):
        """Return the Open Graph site name

        Args:
            soup: HTML from Beautiful Soup.

        Returns:
            value: Parsed content.
        """

        if soup.findAll("meta", property="og:site_name"):
            return soup.find("meta", property="og:site_name")["content"]
        else:
            return

        return

    def _get_og_image(self, soup):
        """Return the Open Graph site name

        Args:
            soup: HTML from Beautiful Soup.

        Returns:
            value: Parsed content.
        """

        if soup.findAll("meta", property="og:image"):
            return soup.find("meta", property="og:image")["content"]
        else:
            return

        return

    def _get_og_property(self, soup):
        """Return the Open Graph site name

            Args:
                soup: HTML from Beautiful Soup.

            Returns:
                value: Parsed content.
            """

        if soup.findAll("meta", property="og:type"):
            return soup.find("meta", property="og:type")["content"]
        else:
            return
        return

    def _get_og_url(self, soup):
        """Return the Open Graph site name

        Args:
            soup: HTML from Beautiful Soup.

        Returns:
            value: Parsed content.
        """

        if soup.findAll("meta", property="og:url"):
            return soup.find("meta", property="og:url")["content"]
        else:
            return

        return


    def _ref_type_determine(self, type: str):

        if type == 'website':
            return 1
        elif type == 'book':
            return 2
        elif type == 'article':
            return 3
        elif type == 'music':
            return 4
        elif type == 'video':
            return 5

    def open_graph_parse(self) -> dict:

        soup = self._get_page()
        og_title = self._get_og_title(soup)
        og_description = self._get_og_description(soup)
        og_image = self._get_og_image(soup)
        #og_site_name = self._get_og_site_name(soup)
        og_type = self._get_og_property(soup)

        if og_type is None:
            og_type = 'website'
            og_type = 1
        else:
            og_type = self._ref_type_determine(og_type)

        site_info = {
            'ref': self.url,
            'title': og_title,
            'description': og_description[:200],
            'image': og_image,
            #'site_name': og_site_name,
            'type_id': og_type,
        }

        return site_info
