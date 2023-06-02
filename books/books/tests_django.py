from django.urls import reverse
from django.test import TestCase
from .models import Recipe


class RecipeListViewTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(
            title='Test Recipe',
            year=2023,
            description='Test Description'
        )
        Recipe.objects.create(
            title='Another Test Recipe',
            year=2022,
            description='Another Test Description'
        )

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')
        self.assertContains(response, 'Another Test Recipe')


class MainViewTestCase(TestCase):
    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Recipes for 2023')
        self.assertNotContains(response, 'Test Recipe')
        self.assertNotContains(response, 'Another Test Recipe')

        Recipe.objects.create(
            title='Test Recipe',
            year=2023,
            description='Test Description'
        )

        response = self.client.get(reverse('main'))
        self.assertContains(response, 'Test Recipe')


class RecipeDetailViewTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            year=2023,
            description='Test Description'
        )

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')
        self.assertContains(response, 'Test Description')


class RecipeDetailTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            year=2023,
            description='Test Description'
        )

    def test_recipe_detail(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')
        self.assertContains(response, 'Test Description')
        self.assertTemplateUsed(response, 'recipe_detail.html')