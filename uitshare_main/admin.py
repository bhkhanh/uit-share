from django.contrib import admin
from .models import (
    Category,
    Course,
    File,
)
from .forms import (
    CategoryForm,
    CourseForm,
    FileForm,
)

# ============================================================
# ============================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ("id", "name", "code_name", "date_modified", "by_user", "thumbnail_img",)
    list_display_links = ("id", "name",)
    readonly_fields = ("id", "date_created", "date_modified", "by_user",)
    prepopulated_fields = {"code_name": ("name",)}
    ordering = ["-date_modified", "name",]
    
    def add_view(self, request, extra_context=None):
        self.fieldsets = (
            ("Category Information", {
                "fields": ("name", "code_name",),
            }),
            ("Cover Image", {
                "fields": ("thumbnail_img",),
            }),
        )
        return super(CategoryAdmin, self).add_view(request, extra_context)
    
    def change_view(self, request, object_id, extra_context=None):
        self.fieldsets = (
            ("Category Information", {
                "fields": ("name", "code_name",),
            }),
            ("Creation/Modification Information", {
                "fields": ("date_modified", "date_created", "by_user",)
            }),
            ("Cover Image", {
                "fields": ("thumbnail_img",),
            }),
        )
        return super(CategoryAdmin, self).change_view(request, object_id, extra_context)
    
    def save_model(self, request, obj, form, change):
        obj.by_user = request.user
        obj.save()

# ============================================================
# ============================================================

class AddViewFileInline(admin.TabularInline):
    model = File
    extra = 1
    fields = ["name", "file_uploaded", "file_type",]


class ChangeViewFileInline(admin.TabularInline):
    model = File
    extra = 0
    fields = ["name", "file_uploaded", "file_type", "uploaded_by", "date_modified",]
    readonly_fields = ["date_modified", "uploaded_by",]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = []
    form = CourseForm
    list_display = ("id", "name", "code_name", "date_modified", "category_id", "by_user", "thumbnail_img",)
    list_display_links = ("id", "name",)
    readonly_fields = ("id", "date_created", "date_modified", "by_user",)
    prepopulated_fields = {"code_name": ("name",)}
    ordering = ["-date_modified", "name",]
    
    def add_view(self, request, extra_context=None):
        self.fieldsets = (
            ("Course Information", {
                "fields": ("name", "code_name", "category_id",),
            }),
            ("Cover Image", {
                "fields": ("thumbnail_img",),
            }),
        )
        self.inlines = [AddViewFileInline,]
        return super(CourseAdmin, self).add_view(request, extra_context)
    
    def change_view(self, request, object_id, extra_context=None):
        self.fieldsets = (
            ("Course Information", {
                "fields": ("name", "code_name", "category_id",),
            }),
            ("Creation/Modification Information", {
                "fields": ("date_modified", "date_created", "by_user",),
            }),
            ("Cover Image", {
                "fields": ("thumbnail_img",),
            }),
        )
        self.inlines = [ChangeViewFileInline,]
        return super(CourseAdmin, self).change_view(request, object_id, extra_context)

    def save_model(self, request, obj, form, change):
        obj.by_user = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.uploaded_by = request.user
            instance.save()
        formset.save_m2m()

# ============================================================
# ============================================================

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    form = FileForm
    list_display = ("id", "name", "course_id", "file_uploaded", "uploaded_by", "date_modified",)
    list_display_links = ("id", "name",)
    readonly_fields = ("id", "date_created", "date_modified", "uploaded_by",)
    ordering = ["course_id", "uploaded_by", "name",]
    
    def add_view(self, request, extra_context=None):
        self.fieldsets = (
            ("File Information", {
                "fields": ("name", "course_id", "file_type", "file_uploaded",),
            }),
        )
        return super(FileAdmin, self).add_view(request, extra_context)
    
    def change_view(self, request, object_id, extra_context=None):
        self.fieldsets = (
            ("File Information", {
                "fields": ("name", "course_id", "file_type", "file_uploaded",),
            }),
            ("File Uploader", {
                "fields": ("uploaded_by",),
            }),
            ("Date & Time", {
                "fields": ("date_modified", "date_created",),
            }),
        )
        return super(FileAdmin, self).change_view(request, object_id, extra_context)
    
    def save_model(self, request, obj, form, change):
        obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)
