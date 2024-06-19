from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin
from .models import Payment, Customer
from rest_framework import viewsets
from .serializers import ProductSerializer, PaymentSerializer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
import stripe
import uuid
stripe.api_key=settings.STRIPE_SECRET
print(settings.STRIPE_SECRET)

class CreateStripeLoad(
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin, 
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    
    
    def create(self, request, *args, **kwargs):
        data=JSONParser().parse(request)
     
        serializer=PaymentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
                ephemeral_key=""
                try:
                    
                    user=Payment.objects.filter(user=data["user"])
                    if not user:
                        customer = stripe.Customer.create(
                                email=data["user"],
                                name=data["user"],
                                description='Customer for' + data["user"],
                                payment_method='pm_card_visa'  # Optional
                            )
                        ephemeral_key = stripe.EphemeralKey.create(
                                    customer=customer.id,
                                    stripe_version="2020-08-27"
                                )
                        print(ephemeral_key)
                        Customer.objects.create(user=data["user"], customer_id=customer.id, ephemeral_key=ephemeral_key.id)
                    customerId=Customer.objects.get(user=data["user"])
                    payment=Payment.objects.create(user=data["user"],amount=data["amount"], customer_id=customerId)
                    intent = stripe.PaymentIntent.create(
                    amount=data["amount"],  # amount in cents
                    currency='usd',
                    customer=customerId.customer_id,
                    metadata={'integration_check': 'accept_a_payment'},
                    )
                    # creating stripe customer
                    
                    
                    return Response({"client_secret": intent["client_secret"],"key":customerId.ephemeral_key ,  **PaymentSerializer(payment).data,"customerId":customerId.customer_id, }, status=status.HTTP_200_OK)
                    
                except stripe.error.CardError as e:
                    body = e.json_body
                    err = body.get('error', {})
                    return Response({'status': 'error', 'message': err.get('message')}, status=status.HTTP_400_BAD_REQUEST)
                except stripe.error.RateLimitError as e:
                    return Response({'status': 'error', 'message': 'Rate limit error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except stripe.error.InvalidRequestError as e:
                    return Response({'status': 'error', 'message': 'Invalid request error'}, status=status.HTTP_400_BAD_REQUEST)
                except stripe.error.AuthenticationError as e:
                    return Response({'status': 'error', 'message': 'Authentication error'}, status=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)
                except stripe.error.APIConnectionError as e:
                    return Response({'status': 'error', 'message': 'Network error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except stripe.error.StripeError as e:
                    return Response({'status': 'error', 'message': 'Something went wrong. You were not charged. Please try again.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except Exception as e:
                    return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        
                        
         
        else:
            return Response({"status":"error","message":str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


    

    