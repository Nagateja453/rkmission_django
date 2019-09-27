from django import forms
from krish.models import AddPost, Imageshow,Testinomials,Latestnews,AddPage, Donations
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
	def use_required_attribute(self, *args):
		return False


class AddPostForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AddPostForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs = {"class": "form-control test noshadow"}
		self.fields['Date_of_Birth'].widget.attrs.update({'placeholder': 'Enter Date_of_Birth (*)'})	
		self.fields['Place_Of_Birth'].widget.attrs.update({'placeholder': 'Enter Place_Of_Birth (*)'})
		self.fields['Parents'].widget.attrs.update({'placeholder': 'Enter Parents (*)'})
		self.fields['Wife'].widget.attrs.update({'placeholder': 'Enter Wife (*)'})
		self.fields['Religious_Views'].widget.attrs.update({'placeholder': 'Enter Religious_Views (*)'})
		self.fields['Place_Of_Death'].widget.attrs.update({'placeholder': 'Enter Place_Of_Death (*)'})
		self.fields['Philosopy'].widget.attrs.update({'placeholder': 'Enter Philosopy (*)'})
		self.fields['Memorial'].widget.attrs.update({'placeholder': 'Enter Memorial (*)'})
		self.fields['title'].widget.attrs.update({'placeholder': 'Enter title (*)'})
		self.fields['project_image1'].widget.attrs.update({'placeholder': 'project_image1 (*)'})
		self.fields['slug'].widget.attrs.update({'placeholder': 'slug (*)'})
		self.fields['excerpt'].widget.attrs.update({'placeholder': 'excerpt (*)'})
		self.fields['meta_description'].widget.attrs.update({'placeholder': 'meta_description (*)'})
		self.fields['keywords'].widget.attrs.update({'placeholder': 'keywords (*)'})
		self.fields['keywords'].widget.attrs.update({'placeholder': 'keywords (*)'})
		self.fields['Education'].widget.attrs.update({'placeholder': 'Enter education (*)'})
		self.fields['Spouse'].widget.attrs.update({'placeholder': 'Enter Spouse(*)'})
		self.fields['Guru'].widget.attrs.update({'placeholder': 'Enter Guru(*)'})
		self.fields['Death'].widget.attrs.update({'placeholder': 'Enter Death(*)'})
		
	content = forms.CharField(
		widget=TinyMCEWidget(
			attrs={'required': False, 'cols': 30, 'rows': 10}
		)
	)

	class Meta:
		model = AddPost
		fields = ['Date_of_Birth','Place_Of_Birth', 'Parents', 'Wife', 'Religious_Views', 'Philosopy','Place_Of_Death','Memorial','title','content','project_image1','slug','excerpt','meta_description','keywords','Education','Spouse','Guru','Death'] 


class ImageForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ImageForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs = {"class": "form-control test noshadow"}
		self.fields['title'].widget.attrs.update({'placeholder': 'Enter title (*)'})	
		self.fields['image_field_1'].widget.attrs.update({'placeholder': 'image1 (*)'})	
		self.fields['image_field_2'].widget.attrs.update({'placeholder': 'image1 (*)'})	
		self.fields['image_field_3'].widget.attrs.update({'placeholder': 'image1 (*)'})	
		self.fields['image_field_4'].widget.attrs.update({'placeholder': 'image1 (*)'})	
		self.fields['image_field_5'].widget.attrs.update({'placeholder': 'image1 (*)'})	
		self.fields['image_field_6'].widget.attrs.update({'placeholder': 'image1 (*)'})	
		self.fields["gallery"].choices = [("", "-- Select image (*)--"), ] + list(self.fields["gallery"].choices)[1:]


	class Meta:
		model =  Imageshow
		fields = ['title','image_field_1','image_field_2','image_field_3','image_field_4','image_field_5','image_field_6','gallery']


class TestForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TestForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs = {"class": "form-control test noshadow"}
		self.fields['name'].widget.attrs.update({'placeholder': 'name (*)'})	
		self.fields['title'].widget.attrs.update({'placeholder': 'title (*)'})	
		self.fields['description'].widget.attrs.update({'placeholder': 'description (*)'})	


	class Meta:
		model =  Testinomials
		fields = ['name','title','description']


class latnewsForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(latnewsForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs = {"class": "form-control test noshadow"}
		self.fields['title'].widget.attrs.update({'placeholder': 'title (*)'})	
		self.fields['description'].widget.attrs.update({'placeholder': 'description (*)'})	


	class Meta:
		model =  Latestnews
		fields = ['title','description']

class AddpageForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AddpageForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs = {"class": "form-control test noshadow"}
		self.fields['title'].widget.attrs.update({'placeholder': 'title (*)'})		
		self.fields['slug'].widget.attrs.update({'placeholder': 'slug (*)'})
		self.fields['excerpt'].widget.attrs.update({'placeholder': 'excerpt (*)'})
		self.fields['meta_description'].widget.attrs.update({'placeholder': 'meta_description (*)'})
		self.fields['project_image2'].widget.attrs.update({'placeholder': 'project_image (*)'})	
		self.fields['keywords'].widget.attrs.update({'placeholder': 'keywords (*)'})
		self.fields['ramakrishna'].choices = [("", "-- Select info (*)--"), ] + list(self.fields['ramakrishna'].choices)[1:]


	content = forms.CharField(
			widget=TinyMCEWidget(
				attrs={'required': False, 'cols': 30, 'rows': 10}
			)
		)
	
	class Meta:
		model =  AddPage
		fields = ['title','slug','excerpt','meta_description','keywords','project_image2','ramakrishna','content']
		

class DonationsForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(DonationsForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs = {"class": "form-control test noshadow"}
		self.fields['title'].widget.attrs.update({'placeholder': 'title (*)'})		
		self.fields['slug'].widget.attrs.update({'placeholder': 'slug (*)'})
		self.fields['excerpt'].widget.attrs.update({'placeholder': 'excerpt (*)'})
		self.fields['meta_description'].widget.attrs.update({'placeholder': 'meta_description (*)'})
		self.fields['project_image2'].widget.attrs.update({'placeholder': 'project_image (*)'})	
		self.fields['keywords'].widget.attrs.update({'placeholder': 'keywords (*)'})

	content = forms.CharField(
			widget=TinyMCEWidget(
				attrs={'required': False, 'cols': 30, 'rows': 10}
			)
		)
	
	class Meta:
		model =  Donations
		fields = ['title','slug','excerpt','meta_description','keywords','project_image2','content']
		
