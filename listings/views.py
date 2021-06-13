from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from listings.choices import bedroom_choices,state_choices,price_choices
# Create your views here.

def index(request):
  listings = Listing.objects.all()
  paginator = Paginator(listings,6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)
  return render(request,'listings/listings.html',{'listings':paged_listings})

def listing(request,listing_id):
  listing = get_object_or_404(Listing,pk=listing_id)
  return render(request,'listings/listing.html',{'listing':listing})

def search(request):
  query_set = Listing.objects.order_by('-list_date')
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      query_set = query_set.filter(description__icontain=keywords)
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      query_set = query_set.filter(city__iexact=city)
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      query_set = query_set.filter(state__iexact=state)
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      query_set = query_set.filter(bedrooms__lte=bedrooms)
  if 'price' in request.GET:
    price = request.GET['price']
    if price == '1500000+':
      query_set = query_set.filter(price__gte=1500000)
    elif price:
      query_set = query_set.filter(price__lte=price)


  context = {
    'price_choices' : price_choices,
    'state_choices' : state_choices,
    'bedroom_choices' : bedroom_choices,
    'listings' : query_set,
    'values' : request.GET
  }
  return render(request,'listings/search.html',context)
