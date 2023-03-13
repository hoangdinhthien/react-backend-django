import graphene
from graphene_django import DjangoObjectType

from customers.models import Customer

class CustomerTypes(DjangoObjectType):
    class Meta:
        model = Customer
        fields = "__all__"

class Query(graphene.ObjectType):     
    customers   =graphene.List(CustomerTypes)
    
    def resolve_customers(root, info):
        return Customer.objects.all()
    
schema = graphene.Schema(query=Query)
    
