import sys
from multiprocessing import cpu_count
from japronto import Application

def naked(request):
    return request.Response(b'Naked!')

app = Application()
app.router.add_route('/', naked, method='GET')
app.run(debug=False)    


if __name__ == '__main__':
    app.run(host=sys.argv[1], workers=cpu_count(), debug=False, port=int(sys.argv[2]))
    
