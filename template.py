template = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Title of the document</title>
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
    width: 200px;
    flex-wrap: nowrap;
  }}
  .stocks-graph {{
    flex-wrap: nowrap;
  }}  
</style>
</head>

<body>
{}
<div class="stocks-view">
  <div class="stocks-listing">
  {}
  </div>
  <div class="stocks-graph"
  <!-- TradingView Widget BEGIN -->
  <div class="tradingview-widget-container">
    <div id="tradingview_63a66"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/AAPL/" rel="noopener" target="_blank"><span class="blue-text">AAPL Chart</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.widget(
    {{
    "width": 980,
    "height": 610,
    "symbol": "AAPL",
    "interval": "D",
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
    </script>
  </div>
  <!-- TradingView Widget END -->
  </div>
</div>
</body>

</html>"""