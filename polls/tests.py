import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

def create_question(text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        resp = self.client.get(reverse("polls:index"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "No polls are available.")
        self.assertQuerySetEqual(resp.context["latest_question_list"], [])

    def test_past_question(self):
        q = create_question("Past question.", days=-30)
        resp = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(resp.context["latest_question_list"], [q])

    def test_future_question(self):
        create_question("Future question.", days=30)
        resp = self.client.get(reverse("polls:index"))
        self.assertContains(resp, "No polls are available.")
        self.assertQuerySetEqual(resp.context["latest_question_list"], [])

    def test_future_and_past_questions(self):
        q = create_question("Past question.", days=-30)
        create_question("Future question.", days=30)
        resp = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(resp.context["latest_question_list"], [q])

    def test_two_past_questions(self):
        q1 = create_question("Past 1.", days=-30)
        q2 = create_question("Past 2.", days=-5)
        resp = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(resp.context["latest_question_list"], [q2, q1])

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        q = create_question("Future.", days=5)
        url = reverse("polls:detail", args=(q.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_past_question(self):
        q = create_question("Past.", days=-5)
        url = reverse("polls:detail", args=(q.id,))
        resp = self.client.get(url)
        self.assertContains(resp, q.question_text)