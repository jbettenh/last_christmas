from django.test import TestCase
from django.shortcuts import reverse

from .models import MovieList
from christmasflix import omdbmovies


class MovieListIndexViewTests(TestCase):
    def test_no_lists(self):
        response = self.client.get(reverse('christmasflix:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No lists are available.")
        self.assertQuerysetEqual(response.context['movie_lists'], [])

    def test_one_movie_list(self):
        mylist1 = MovieList.objects.create(name="mylist1")
        response = self.client.get(reverse('christmasflix:index'))

        self.assertQuerysetEqual(response.context['movie_lists'], [mylist1])

    def test_two_movie_lists(self):
        mylist1 = MovieList.objects.create(name="mylist1")
        mylist2 = MovieList.objects.create(name="mylist2")
        response = self.client.get(reverse('christmasflix:index'))

        self.assertQuerysetEqual(response.context['movie_lists'], [mylist1, mylist2], ordered=False)


class IndexViewTest(TestCase):
    def test_index_uses_template(self):
        response = self.client.get(f'/christmasflix/')

        self.assertTemplateUsed(response, 'christmasflix/index.html')


class DetailViewTest(TestCase):
    def test_list_uses_template(self):
        my_list = MovieList.objects.create()
        response = self.client.get(f'/christmasflix/{my_list.id}/')

        self.assertTemplateUsed(response, 'christmasflix/movie_list.html')


class MovieViewTest(TestCase):
    def test_movies_uses_template(self):
        response = self.client.get(f'/christmasflix/movies/')

        self.assertTemplateUsed(response, 'christmasflix/movies.html')


class MovieResultsTest(TestCase):
    def test_no_movie_found(self):
        # asdasdfc
        omdbmovies.search_movie("Die Hard")
        self.assertRaises(KeyError)