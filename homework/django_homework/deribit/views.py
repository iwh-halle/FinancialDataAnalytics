import requests
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime, timedelta

def chart_data(request):
    # Deribit API endpoint for getting trading view chart data
    url = "https://test.deribit.com/api/v2/public/get_tradingview_chart_data"

    # Calculate timestamps for the last two days
    end_timestamp = int(datetime.now().timestamp()) * 1000  # Current timestamp in milliseconds
    start_timestamp = int((datetime.now() - timedelta(days=2)).timestamp()) * 1000  # Two days ago

    # Parameters for the API call
    params = {
        'instrument_name': 'BTC-PERPETUAL',
        'resolution': '60',
        'start_timestamp': start_timestamp,
        'end_timestamp': end_timestamp
    }

    # Making the request
    response = requests.get(url, params=params)
    data = response.json()

    # Adjusting the timestamp format and filtering the necessary data
    if data and 'result' in data and 'ticks' in data['result']:
        ticks = data['result']['ticks']
        formatted_ticks = [datetime.fromtimestamp(ts / 1000).strftime('%d %H') for ts in ticks]
        open_prices = data['result']['open']
        result_data = list(zip(formatted_ticks, open_prices))
    else:
        result_data = []

    return JsonResponse({'data': result_data})


def chart_view(request):
    return render(request, 'chart.html')
