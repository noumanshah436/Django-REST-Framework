from blogs.models import BlogPost
from utility.models import Difficulty

# Create or get Difficulty instances
easy = Difficulty.objects.get(pk=1)
difficult = Difficulty.objects.get(pk=2)

BlogPost.objects.create(
    url='https://medium.com/@srplabs.in/tutorial-6-introduction-to-django-model-design-and-its-optional-keyword-arguments-77091cd9de24',
    title='Tutorial #6 – Introduction to Django Model Design and it\'s optional keyword arguments.',
    thumbnail='media/images/blogs/thumbnails/test1.jpeg',
    frontend_score=0,
    backend_score=20,
    setup_score=10,
    reactdj_score=230,
    read_time=4,
    difficulty=easy,
    publish_date='2019-03-25'
)

BlogPost.objects.create(
    url='https://blog.usejournal.com/tutorial-5-introduction-to-django-project-and-applications-and-understanding-directory-structure-7886d753f442',
    title='Tutorial #5– Introduction to Django Project and Applications and Understanding Directory Structure.',
    thumbnail='media/images/blogs/thumbnails/logo_VyPMj4B.png',
    frontend_score=0,
    backend_score=10,
    setup_score=10,
    reactdj_score=20,
    read_time=5,
    difficulty=difficult,
    publish_date='2019-03-22'
)

BlogPost.objects.create(
    url='https://medium.com/@srplabs.in/tutorial-4-live-project-discussion-and-front-end-setup-ba3bc0e0f1c',
    title='Tutorial #4 – Live Project Discussion and Front-End Setup',
    thumbnail='media/images/blogs/thumbnails/logo_iYMnWdW.png',
    frontend_score=20,
    backend_score=0,
    setup_score=10,
    reactdj_score=30,
    read_time=6,
    difficulty=easy,
    publish_date='2019-03-20'
)

# Verify creation
for post in BlogPost.objects.all():
    print(post)