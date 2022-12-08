from rest_framework.pagination import PageNumberPagination

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