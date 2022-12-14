from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    # number of items per page 
    page_size = 3 
    
    #www.example.com/?page=15, -> instead of 'page=15' now it will be 'p=15'
    page_query_param = 'p' 
    
    #www.example.com/?page=2&size=10 -> if default 'page_size=2' then it will now be overriden by 'page_size=10'
    page_size_query_param = 'size' 
    
    #www.example.com/?size=100 -> here 'size=100' would load 100 items per page, 
    #but because of 'max_page_size' only maximum of 10 items will be loaded
    max_page_size = 10
    
    #www.example.com/?page=last -> by default 'page=last' will load the 'LAST' page, but now it won't work 
    #'page=end' will load the 'LAST' page now.
    last_page_string = 'end'
    

class UserReviewListPagination(PageNumberPagination):
    # number of items per page 
    page_size = 3 
    
    #www.example.com/?page=15, -> instead of 'page=15' now it will be 'p=15'
    page_query_param = 'p' 
    
    #www.example.com/?page=2&size=10 -> if default 'page_size=2' then it will now be overriden by 'page_size=10'
    page_size_query_param = 'size' 
    
    #www.example.com/?size=100 -> here 'size=100' would load 100 items per page, 
    #but because of 'max_page_size' only maximum of 10 items will be loaded
    max_page_size = 10
    
    #www.example.com/?page=last -> by default 'page=last' will load the 'LAST' page, but now it won't work 
    #'page=end' will load the 'LAST' page now.
    last_page_string = 'end'
    
    
class UserReviewListLOPagination(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'lmt' #by deafult it's 'limit'  
    offset_query_param = 'offst' #by default it's 'offset'
    max_limit = 10 # by default nothing is set, any number will be taken
    

class UserReviewListCPagination(CursorPagination):
    page_size = 3 #no of item per page
    cursor_query_param = 'crsr' # by default it's 'cursor'
    ordering = 'created' # by default it's '-created' 