import asyncio
from flask import Flask, request, render_template
import httpx
from time import perf_counter


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sync', methods=['GET', 'POST'])
def sync_view():
    if request.method == 'POST' and request.form['number'].isdigit():
        num = int(request.form['number'])
        t = perf_counter()

        res = [httpx.get(f'https://api.isevenapi.xyz/api/iseven/{i}/').json()['iseven']
               for i in range(num)]

        elapsed_time = round(perf_counter() - t, 2)
        return render_template('test.html', method='sync', res=res, elapsed_time=elapsed_time)
    return render_template('test.html', method='sync')


@app.route('/async', methods=['GET', 'POST'])
async def async_view():
    if request.method == 'POST' and request.form['number'].isdigit():
        num = int(request.form['number'])
        t = perf_counter()

        async with httpx.AsyncClient() as client:
            res = [i.json()['iseven'] for i in await asyncio.gather(
                *[client.get(f'https://api.isevenapi.xyz/api/iseven/{i}/') for i in range(num)]
            )]

        elapsed_time = round(perf_counter() - t, 2)
        return render_template('test.html', method='async', res=res, elapsed_time=elapsed_time)
    return render_template('test.html', method='async')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
