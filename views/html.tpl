<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AtCoder Checker</title>
    <!-- BootstrapのCSS読み込み -->
    <link href="/css/bootstrap.min.css" rel="stylesheet">
    <!-- jQuery読み込み -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- BootstrapのJS読み込み -->
    <script src="/js/bootstrap.min.js"></script>
  </head>
  <body>
    <div class="container">
    <div class="jumbotron">
      <h1>AtCoder Checker</h1>
      <p>AtCoderでの自分の進捗を確認することができるサイトです。<br/>
        AtCoderのUserIDを入力すると、自分の結果が表になって表示されます。一度でも正解したことがあれば、ACとなります。</p>
    </div>
    <form class="form-horizontal" action="/" method="post">
          <div class="form-group">

            <p for="input2" class="control-p">UserID</p>
            <div class="col-xs-4">
              <input type="text" name="input_txt"  class="form-control" id="input3" placeholder="UserID">
            </div>
          </div>

      <div class="form-group">
        <div class=" col-sm-10">
          <button type="submit" class="btn btn-primary">Check</button>
        </div>
      </div>
    </div>
  </form>

</body>
