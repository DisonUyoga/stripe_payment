from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
import stripe

stripe.api_key=settings.STRIPE_SECRET
print(settings.STRIPE_SECRET)

class CreateStripeLoad(
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin, 
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    
    def create(self, request, *args, **kwargs):
        data=JSONParser().parse(request)
        print(data)
        serializer=ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):

            
                try:
                    starter_subscription = stripe.Product.create(
                    name=data["name"],
                    description=data["description"],)
               
                    if starter_subscription.id:
                    
                            starter_subscription_price = stripe.Price.create(
                            unit_amount=data["price"],
                            currency="usd",
                            recurring=None,
                            product=starter_subscription['id'],
                            )
                            print(starter_subscription_price)
                            if starter_subscription_price.id:
                                checkout_session=stripe.checkout.Session.create(
                                    line_items=[
                                        {
                                            'price': starter_subscription_price.id,
                                            'quantity': data["quantity"],
                                        },
                                    ],
                                    mode='payment',
                                    success_url="http://localhost" + '/?success=true',
                                    cancel_url="http://localhost" + '/?success=false',
                                )
                               
                        
                                return Response(checkout_session, status=status.HTTP_200_OK)
                            else:
                                return Response({"status":"error","message":"error establishing payment"})
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


    

    