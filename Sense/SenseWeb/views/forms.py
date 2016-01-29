from django import forms
from django.forms import inlineformset_factory
from SenseWeb.models import Movie, Quiz, QuizSet, Answer

class MovieForm(forms.ModelForm):
	def __init__(self, *args, ** kwargs):
		super(MovieForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			if field.widget.attrs.has_key('class'):
				field.widget.attrs['class'] += ' form-control'
			else:
				field.widget.attrs.update({'class':'form-control'})

	class Meta:
		model = Movie
		fields = ('__all__')
		widgets = {'title': forms.Textarea(attrs={'cols':200, 'rows':1}),
				   'description': forms.Textarea(attrs={'cols':200, 'rows': 4}),}


class QuizForm(forms.ModelForm):
	quiz_type = forms.ChoiceField(choices=Quiz.TYPE_CHOICES)

	def __init__(self, *args, ** kwargs):
		super(QuizForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			if field.widget.attrs.has_key('class'):
				field.widget.attrs['class'] += ' form-control'
			else:
				field.widget.attrs.update({'class':'form-control'})

	class Meta:
		model = Quiz
		fields = ('__all__')
		widgets = {'content': forms.Textarea(attrs={'cols':300, 'rows':2}),}

QuizSetFormSet = inlineformset_factory(Quiz, QuizSet, fields=('seq','content'), widgets={'content': forms.Textarea(attrs={'cols':200,'rows':2})})
QuizAnswerFormSet = inlineformset_factory(Quiz, Answer, fk_name='quiz', fields=('answer','follow_quiz'))

