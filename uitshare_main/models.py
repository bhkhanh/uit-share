import uuid
from django.db import models
from django.urls import reverse
from uitshare_user.models import User as uit_share_user

# ============================================================
# ============================================================

# Generate filepath for thumbnail image in Category model
def generate_cover_img_filepath_for_category(instance, filename):
    file_extension = filename.split('.')[-1]
    # return /images/covers/cover_category__cong-nghe-phan-mem.jpeg
    return "images/covers/cover_category__{0}.{1}".format(instance.code_name, file_extension)


# Generate filepath for thumbnail image for Course model
def generate_cover_img_filepath_for_course(instance, filename):
    file_extension = filename.split('.')[-1]
    # return /images/covers/cover__nhap-mon-lap-trinh.jpeg
    return "images/covers/cover__{0}.{1}".format(instance.code_name, file_extension)

# Generate filepath for files
def generate_file_path(instance, filename):
    # return /courses/lap-trinh-ung-dung-web/Lecture/<file-name.pdf>
    return "courses/{0}/{1}/uit-share__{2}".format(instance.course_id.code_name, instance.file_type, filename)

# ============================================================
# ============================================================

# Category model
class Category(models.Model):
    id = models.UUIDField(verbose_name="Category ID", primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(verbose_name="Category Title", max_length=180, blank=False,)
    code_name = models.SlugField(verbose_name="Category Code-name", max_length=200, unique=True, blank=False,)
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True, editable=False,)
    date_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True,)
    by_user = models.ForeignKey(verbose_name="By User", to=uit_share_user, db_column="by_user", on_delete=models.SET_NULL, null=True, related_name="category_creations",)
    thumbnail_img = models.ImageField(verbose_name="Thumbnail Image", upload_to=generate_cover_img_filepath_for_category, max_length=255, default="images/covers/default-cover.jpg", blank=True,)
    
    # Returns the string representation of the object
    def __str__(self):
        return self.name.strip()
    
    # Absolute URL path for Category model
    def get_absolute_url(self):
        context_arguments = {
            "category_codename": self.code_name,
        }
        return reverse(viewname="category-detail-page", kwargs=context_arguments)   # Result: www.example.com/category/<category_codename>/
    
    class Meta:
        db_table = "uit_share_category"     # Table name in database
        verbose_name_plural = "Categories"  # Displaying this name in admin page
        ordering = ["name",]                # Ordered result when querying (ascending order based on Name field)


# ============================================================

# Course model
class Course(models.Model):
    id = models.UUIDField(verbose_name="Course ID", primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(verbose_name="Course Title", max_length=200, blank=False,)
    code_name = models.SlugField(verbose_name="Course Code-name", max_length=255, unique=True, blank=False,)
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True, editable=False,)
    date_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True,)
    category_id = models.ForeignKey(verbose_name="Category", to=Category, db_column="category_id", on_delete=models.SET_NULL, blank=False, null=True, related_name="courses",)
    by_user = models.ForeignKey(verbose_name="By User", to=uit_share_user, db_column="by_user", on_delete=models.SET_NULL, null=True, related_name="course_creations",)
    thumbnail_img = models.ImageField(verbose_name="Background Cover Image", upload_to=generate_cover_img_filepath_for_course, max_length=255, default="images/covers/default-cover.jpg", blank=True,)

    # Returns the string representation of the object
    def __str__(self):
        return self.name.strip()

    # Absolute URL path for Course model
    def get_absolute_url(self):
        context_arguments = {
            "course_codename": self.code_name,
        }
        return reverse(viewname="course-detail-page", kwargs=context_arguments) # Result: www.example.com/course/<course_codename>/

    def get_name_and_codename(val):
        return val

    class Meta:
        db_table = "uit_share_course"   # Table name in database
        verbose_name_plural = "Courses" # Displaying this name in admin page
        ordering = ["name",]            # Ordered result when querying (ascending order based on Name field)


# ============================================================

# File models
class File(models.Model):
    LAB = "Lab"
    LECTURE = "Lecture"
    EXAM = "Exam"
    EXERCISE = "Exercise"
    BOOK = "Book"
    OTHER = "Other"
    
    FileTypeChoices = [
        (LAB, "Labs"),
        (LECTURE, "Lectures"),
        (EXAM, "Exams"),
        (EXERCISE, "Exercises"),
        (BOOK, "Books"),
        (OTHER, "Others"),
    ]
    
    id = models.UUIDField(verbose_name="File ID", primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(verbose_name="File Title", max_length=255, blank=True,)
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True, editable=False,)
    date_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True,)
    course_id = models.ForeignKey(verbose_name="Course", to=Course, db_column="course_id", on_delete=models.CASCADE, blank=False, related_name="files",)
    uploaded_by = models.ForeignKey(verbose_name="Uploaded By", to=uit_share_user, db_column="uploaded_by", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="file_uploader",)
    file_uploaded = models.FileField(verbose_name="File/Document", upload_to=generate_file_path, max_length=255, blank=False,)
    file_type = models.CharField(verbose_name="File Type", max_length=10, choices=FileTypeChoices, default=OTHER,)

    # Returns the string representation of the object
    def __str__(self):
        return self.name.strip()

    class Meta:
        db_table = "uit_share_file"     # Table name in database
        verbose_name_plural = "Files"   # Displaying this name in admin page
        ordering = ["name",]            # Ordered result when querying (ascending order based on Name field)