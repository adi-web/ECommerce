from Ecommerce_Store import settings

class Cart(object):
    def __init__(self,request):

        self.session=request.session
        cart=self.session.get('session_key')

        if 'session_key' not in request.session:
            cart=self.session['session_key']={}


        self.session=cart

