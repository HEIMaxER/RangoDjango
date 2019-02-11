# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.test import TestCase
from Rango.models import Category, Page
from django.core.urlresolvers import reverse
from django.utils.timezone import localdate
import datetime

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        cat = Category(name='test',views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    def test_slug_line_creation(self):

        cat = Category(name='Random Category String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')


class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):

        add_cat('test', 1, 1)
        add_cat('temp', 1, 1)
        add_cat('tmp', 1, 1)
        add_cat('tmp test temp', 1, 1)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")
        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)

class PageMethodTests(TestCase):

    def test_ensure_last_visit_is_in_the_past(self):
        c = Category(name='test')
        c.save()
        page = Page(category=c, last_visit=localdate()+datetime.timedelta(days=10))
        page.save()
        self.assertEqual(page.last_visit<=localdate(), True)

    def test_ensure_first_visit_is_in_the_past(self):
        c = Category(name='test')
        c.save()
        page = Page(category=c, first_visit=localdate()+datetime.timedelta(days=10))
        page.save()
        self.assertEqual(page.first_visit<=localdate(), True)

    def test_ensure_first_visit_is_before_last_visit(self):
        c = Category(name='test')
        c.save()
        page = Page(category=c, last_visit=localdate()-datetime.timedelta(days=10), first_visit=localdate())
        page.save()
        self.assertEqual(page.last_visit>=page.first_visit, True)
