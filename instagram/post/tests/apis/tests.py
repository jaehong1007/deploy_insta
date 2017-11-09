from pprint import pprint

from django.urls import reverse
from rest_framework.test import APIRequestFactory, APILiveServerTestCase
from post.apis import PostList


class PostListViewTest(APILiveServerTestCase):
    URL_API_POST_LIST_NAME = 'api-post'
    URL_API_POST_LIST = '/api/post/'

    def test_post_list_url(self):
        url = reverse(self.URL_API_POST_LIST_NAME)
        self.assertEqual(url, self.URL_API_POST_LIST)

    def test_post_list_url_resolve(self):
        url_name = resolve(self.URL_API_POST_LIST)
        self.assertEqual(url_name, self.URL_API_POST_LIST_NAME)

url = reverse('api-post')
factory = APIRequestFactory()
request = factory.get('/api/post/')

view = PostList.as_view()
response = view(request)

pprint(len(response.data))



