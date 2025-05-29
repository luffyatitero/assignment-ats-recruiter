from rest_framework import serializers
from candidates.models import Candidate



class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'age', 'email', 'phone', 'gender']
        read_only_fields = ['id']