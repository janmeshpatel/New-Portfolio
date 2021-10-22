from django.contrib import admin
from myapp.models import Home
from myapp.models import Personal_Information
from myapp.models import Skill
from myapp.models import Interest
from myapp.models import Testimonials
from myapp.models import Profile
from myapp.models import Education
from myapp.models import Career
from myapp.models import Category
from myapp.models import Project
from myapp.models import Temp



# Register your models here.
admin.site.register(Home)
admin.site.register(Personal_Information)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Testimonials)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Career)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Temp)
