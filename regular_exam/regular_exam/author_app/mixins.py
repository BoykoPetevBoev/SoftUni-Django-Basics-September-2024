from regular_exam.author_app.models import Author


class AuthorMixin:
    def get_author(self):
        return Author.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.get_author()
        return context
