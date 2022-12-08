from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    # number of items per page 
    page_size = 3 
    
    #www.example.com/?page=15, -> instead of 'page=15' now it will be 'p=15'
    page_query_param = 'p' 
    
    #www.example.com/?page=2&size=10 -> if default 'page_size=2' then it will now be overriden by 'page_size=10'
    page_size_query_param = 'size' 
    

class UserReviewListPagination(PageNumberPagination):
    page_size = 3 
    page_query_param = 'p' 
    page_size_query_param = 'size' 