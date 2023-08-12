from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Account, Category, Transaction
from .serializers import AccountSerializer, CategorySerializer, TransactionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(detail=True, methods=["get"])
    def balance(self, request, pk=None):
        account = self.get_object()
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if start_date and end_date:
            transactions = Transaction.objects.filter(
                user=account.user, date__range=[start_date, end_date]
            )

            incoming = transactions.filter(
                transaction_type=Transaction.INCOMING
            ).aggregate(sum=Coalesce(Sum("value"), 0))["sum"]
            outgoing = transactions.filter(
                transaction_type=Transaction.OUTGOING
            ).aggregate(sum=Coalesce(Sum("value"), 0))["sum"]

            balance = incoming - outgoing

            return Response({"balance": balance})

        return Response({"error": "Missing start_date and end_date query parameters."})


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=["get"])
    def spent_by_category(self, request):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if start_date and end_date:
            spent_by_category = (
                Transaction.objects.filter(
                    user=request.user,
                    date__range=[start_date, end_date],
                    transaction_type=Transaction.OUTGOING,
                )
                .values("category__name")
                .annotate(total_spent=Coalesce(Sum("value"), 0))
            )

            return Response(spent_by_category)

        return Response({"error": "Missing start_date and end_date query parameters."})
