import sys
from multiprocessing import cpu_count
from japronto import Application

def home(request):
    return request.Response(json={'count': len(request.match_dict)})

app = Application()
app.router.add_route('/', home, method='POST')
app.run(debug=False)    


if __name__ == '__main__':
    app.run(host=sys.argv[1], workers=cpu_count(), debug=False, port=int(sys.argv[2]))
    
