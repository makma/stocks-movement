template = """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Title of the document</title>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.3.0/milligram.min.css">
  <style>
    .tradingview-widget-container {{
      position: sticky;
      top: 20px;
    }}
    .stocks-view {{
      display: flex;
      flex-wrap: nowrap;
    }}
    .stocks-listing {{
      width: 650px;
      flex-wrap: nowrap;
      padding: 20px;
    }}
    .stocks-graph {{
      flex-wrap: nowrap;
      padding: 20px;
    }}
    .positive-movement {{
      color: green;
      font-weight: bold;
    }}
    .negative-movement {{
      color: red;
      font-weight: bold;
    }}
  </style>
</head>

<body>
{}
<div class="stocks-view">
  <div class="stocks-listing">
    <table>
      <thead>
        <tr>
          <th>Symbol</th>
          <th>April 1 2019</th>
          <th>Dec 2 2019</th>
          <th>Today</th>
          <th>Movement against 4/1/2019</th>
          <th>Movement against 12/2/2019</th>
        </tr>
      </thead>
      <tbody>
        {}
      </tbody>
    </table>

  </div>
  <div class="stocks-graph"
  <!-- TradingView Widget BEGIN -->
  <div class="tradingview-widget-container">
    <div id="tradingview_63a66"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/AAPL/" rel="noopener" target="_blank"><span class="blue-text">AAPL Chart</span></a> by TradingView</div>
  </div>
  <!-- TradingView Widget END -->
  </div>
</div>

<script type="text/javascript">
  function renderChart(symbol) {{
    new TradingView.widget(
    {{
      "width": 750,
      "height": 500,
      "symbol": symbol,
      "interval": "180",
      "timezone": "Etc/UTC",
      "theme": "light",
      "style": "1",
      "locale": "en",
      "toolbar_bg": "#f1f3f6",
      "enable_publishing": false,
      "allow_symbol_change": true,
      "container_id": "tradingview_63a66"
    }}
    );
  }}

  document.addEventListener('DOMContentLoaded', function(){{ 
    renderChart('BA');
  }}, false);
</script>
</body>

</html>"""