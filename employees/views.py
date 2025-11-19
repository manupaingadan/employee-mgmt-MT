from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DynamicForm, EmployeeRecord
from .serializers import DynamicFormSerializer, EmployeeRecordSerializer
from rest_framework.permissions import IsAuthenticated

from django.db.utils import NotSupportedError
from rest_framework import status

class DynamicFormViewSet(viewsets.ModelViewSet):
    queryset = DynamicForm.objects.all().order_by('-created_at')
    serializer_class = DynamicFormSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class EmployeeRecordViewSet(viewsets.ModelViewSet):
    queryset = EmployeeRecord.objects.all().order_by('-created_at')
    serializer_class = EmployeeRecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['data']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def filter(self, request):
        key = request.query_params.get('key')
        value = request.query_params.get('value')
        if not key or value is None:
            return Response({"detail":"provide key and value query params"}, status=status.HTTP_400_BAD_REQUEST)

        partial = request.query_params.get('partial', '1')
        try:
            partial = bool(int(partial))
        except Exception:
            partial = True

        try:
            max_scan = int(request.query_params.get('max_scan', 2000))
            if max_scan <= 0:
                max_scan = 2000
        except Exception:
            max_scan = 2000

        qs = self.get_queryset()

        try:
            qs_filtered = qs.filter(data__contains={key: value})
            serializer = self.get_serializer(qs_filtered, many=True)
            return Response(serializer.data)  
        except NotSupportedError:
            pass
        except Exception:
            pass

        matches = []
        scanned = 0
        for obj in qs.iterator():
            scanned += 1
            if scanned > max_scan:
                break
            try:
                v = obj.data.get(key, None)
            except Exception:
                v = None
            if v is None:
                continue

            try:
                if partial:
                    if str(value).lower() in str(v).lower():
                        matches.append(obj)
                else:
                    if isinstance(v, (int, float)) and str(value).replace('.','',1).isdigit():
                        if float(v) == float(value):
                            matches.append(obj)
                    else:
                        if str(v) == str(value):
                            matches.append(obj)
            except Exception:
                continue

        serializer = self.get_serializer(matches, many=True)
        return Response(serializer.data)