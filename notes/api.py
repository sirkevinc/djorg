from rest_framework import serializers, viewsets
from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):

  def create(self, validated_data):
      # import pdb; pdb.set_trace()
    user = self.context['request'].user

    note = Note.objects.create(user=user, **validated_data)
    return note

  class Meta:
    model = Note
    fields = ('title', 'content')

class NoteViewSet(viewsets.ModelViewSet):
  serializer_class = NoteSerializer
  queryset = Note.objects.all()

  def get_queryset(self):
    queryset = Note.objects.all()
    user = self.request.user.id

    if user:
      queryset = Note.objects.filter(user=user)
    else:
      queryset = Note.objects.none()
    return queryset
