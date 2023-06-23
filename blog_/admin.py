from django.contrib import admin
from .models import Post
from django import forms

# Register your models here.


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def clean_first_name(self):
        if self.cleaned_data["title"] == "Spike":
            raise forms.ValidationError("No Vampires")

        return self.cleaned_data["title"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","created_at")

    fields = ("title", "body", "created_at", "image")
    form = PostAdminForm
    def title(self, obj):
        return obj.title
    def created_at(self, obj):
        return obj.created_at 
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["title"].label = "Tytuł:"
        form.base_fields["body"].label = "Treść:"
        form.base_fields["created_at"].label = "Czas i data :"
        form.base_fields["image"].label = "Tło postu :"
        return form    