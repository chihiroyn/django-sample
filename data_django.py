from django_setup import django_setup

from django.utils import timezone

def main():
    from polls.models import Question

    new_question = Question(question_text="test", pub_date=timezone.now())
    new_question.save()

    for question in Question.objects.all():
        print(question.question_text)
        print(question.pub_date)
        print("\r")

    updated_question = Question.objects.filter(question_text="test").first()
    updated_question.question_text = "test2"
    updated_question.save()

    deleted_question = Question.objects.filter(question_text="test2")
    deleted_question.delete()


if __name__ == '__main__':
  django_setup()
  main()

