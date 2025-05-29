from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q, Value, IntegerField, Case, When
from django.db.models.functions import Lower

from candidates.models import Candidate
from candidates.serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """
    A viewset for creating, updating, and deleting candidates.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class CandidateSearchAPIView(APIView):
    """
    API endpoint for searching candidates by name with relevancy ranking.
    Relevancy = number of words in query found in candidate's name (case-insensitive).
    """
    def get(self, request):
        query = request.GET.get('q', '').strip()
        if not query:
            return Response([])
        
        # Deduplicate and clean words
        words = list(set([w for w in query.lower().split() if w]))

        if not words:
            return Response([])
        
        queryset = Candidate.objects.annotate(
            name_lower=Lower('name'),
            relevancy=sum([
                Case(
                    When(name_lower__icontains=word, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField()
                ) for word in words
            ])
        ).filter(relevancy__gt=0).order_by('-relevancy', 'name')
        
        serializer = CandidateSerializer(queryset, many=True)
        
        return Response(serializer.data)