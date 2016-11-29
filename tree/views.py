from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User ,Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import Family, Person
from .forms import UserForm

'''
content_type = ContentType.objects.get_for_model(Family, Person)
permission = Permission.objects.create(
    codename = 'can_publish',
    name = 'Can create',
    content_type = content_type
)
user = User.objects.get(username='greg')
group = Group.objects.get(name='ADD_group')
group.permissions.add(permission)
user.groups.add(group)
'''



#View of Home Page
class IndexView(generic.ListView):
    template_name = 'tree/index.html'
    context_object_name = 'all_families'

    def get_queryset(self):
        return Family.objects.all()

#View login Page

class LoginView(View):
    success_url = reverse_lazy('registration:login')

#View logout Page

class LogoutView(View):
    success_url = reverse_lazy('registration:login')

#View of Persons List
class PersonView(generic.ListView):
    template_name = 'tree/persons_list.html'
    context_object_name = 'all_persons'

    def get_queryset(self):
        return Person.objects.all()

#View of Family Details
class DetailView(generic.DetailView):
    model = Family
    template_name = 'tree/detail.html'
#View of Person Details
class DetailPersonView(generic.DetailView):
    model = Person
    template_name = 'tree/person_detail.html'


#View of Create Family form
class FamilyCreate(CreateView):
    model = Family
    fields = ['family_name', 'family_location', 'family_logo']
#View of Create Person form
class PersonCreate(CreateView):
    model = Person
    fields = ['family', 'first_name', 'second_name', 'person_photo', 'date_of_birth', 'person_descr', 'date_of_death', 'lives_in', 'is_married']

#View of Update Family form
class FamilyUpdate(UpdateView):
    model = Family
    fields = ['family_name', 'family_location', 'family_logo']
#View of Update Person form
class PersonUpdate(UpdateView):
    model = Person
    fields = ['family', 'first_name', 'second_name', 'person_photo', 'date_of_birth', 'person_descr', 'date_of_death', 'lives_in', 'is_married']


#View of Delete Family form
class FamilyDelete(DeleteView):
    model = Family
    success_url = reverse_lazy('tree:index')


#View of Delete Person form
class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('tree:persons')

#View for register User
class UserFormView(View):
    from_class = UserForm
    template_name = 'tree/registration_from.html'

    # distplay blank form
    def get(self, request):
        form = self.from_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.from_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #Cleaned (normalized) data

            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:


                if user.is_active:
                    login(request, user)
                    return redirect('tree:index')

        return render(request, self.template_name, {'form': form})