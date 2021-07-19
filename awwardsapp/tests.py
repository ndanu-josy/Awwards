from django.test import TestCase
from .models import Profile,Project, Rating
from django.contrib.auth.models import User


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username = 'jos',email = 'jos@gmail.com')
        self.user.save()
        self.profile = Profile(user=self.user,  bio = 'tests',profile_picture = 'test.jpg',projects='020', contact_info='1111')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

class ProjectTest(TestCase):

    def setUp(self):
        self.project = Project(title ='project', image='image.jpg',description="my awwaaards project",link="http://www.awwaards.com")

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_projects()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.project.save_projects()
        projects = Project.objects.all()
        self.project.delete_projects()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

class ReviewTest(TestCase):
    def setUp(self):
        self.user = User(username='jos')
        self.user.save()
        self.project = Project(title ='project', image='image.jpg',description="my awwaaards project",link="http://www.awwaards.com")
        self.project.save_projects()
        self.new_review=Rating(design="6",usability="7",content="5",user=self.user,project=self.project)
        self.new_review.save_review()

    def tearDown(self):
        Rating.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Rating))

    def test_save_review(self):
        reviews = Rating.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_delete_review(self):
        self.new_review.save_review()
        self.new_review.delete_review()
        reviews = Rating.objects.all()
        self.assertTrue(len(reviews)==0)

