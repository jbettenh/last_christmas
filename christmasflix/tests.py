from django.test import TestCase
from django.shortcuts import reverse

from .models import MovieList

class MovieListIndexViewTests(TestCase):
    def test_no_lists(self):
        response = self.client.get(reverse('christmasflix:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No movies are available")
        self.assertQuerysetEqual(response.context['movie_lists'],[])

    def test_one_movie_list(self):
        mylist1 = MovieList.objects.create(name="mylist1")
        response = self.client.get(reverse('christmasflix:index'))

        self.assertQuerysetEqual(response.context['movie_lists'], [mylist1])


    def test_two_movie_lists(self):
        mylist1 = MovieList.objects.create(name="mylist1")
        mylist2 = MovieList.objects.create(name="mylist2")
        response = self.client.get(reverse('christmasflix:index'))

        self.assertQuerysetEqual(response.context['movie_lists'], [mylist1, mylist2], ordered=False)


class DetailViewTest(TestCase):
    def test_list_uses_template(self):
        my_list = MovieList.objects.create()
        response = self.client.get(f'/christmasflix/{my_list.id}/')

        self.assertTemplateUsed(response, 'christmasflix/detail.html')
