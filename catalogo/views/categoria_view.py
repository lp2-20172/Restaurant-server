from ..models.categoria import Categoria
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class CategoriaSerializer(serializers.ModelSerializer):
    # campo_nuevo = serializers.SerializerMethodField()

    class Meta:
        model = Categoria
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    # def get_campo_nuevo(self, obj):
    #     # return "%s %s " % (obj.codigo, obj.nombre)
    #     return dict(
    #         nombre="dewdew"
    #         )


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(codigo__icontains=query),
                    Q(nombre__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
