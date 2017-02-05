<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AtCoder Checker</title>
    <!-- BootstrapのCSS読み込み -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- jQuery読み込み -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- BootstrapのJS読み込み -->
    <script src="js/bootstrap.min.js"></script>

  </head>
  <body>
  <div class="container">
    <h3>{{input_txt+"の結果"}}</h3>
    <ul class="nav nav-tabs">
     <li class="active"><a href="#tab1" data-toggle="tab">Grand</a></li>
     <li><a href="#tab2" data-toggle="tab">Regular</a></li>
     <li><a href="#tab3" data-toggle="tab">Beginner</a></li>
     <li><a href="#tab4" data-toggle="tab">Typical</a></li>
    </ul>

    <div class="tab-content">
     <div class="tab-pane active" id="tab1">
       <table class="table table-striped">
         <thead>
           <tr>
             <th>#</th>
             <th>A</th>
             <th>B</th>
             <th>C</th>
             <th>D</th>
             <th>E</th>
             <th>F</th>
           </tr>
         </thead>
         <tbody>
           %for k, v in sorted(scoreG.items()):
           <tr>
             <td>{{k}}</td>
             %for problem ,result in sorted(v.items()):
                 <!--print(k,problem, result)-->
             <td>{{result}}</td>
             % end
           </tr>
           % end
         </tbody>
       </table>
     </div>
     <div class="tab-pane" id="tab2">
       <table class="table table-striped">
         <thead>
           <tr>
             <th>#</th>
             <th>C</th>
             <th>D</th>
             <th>E</th>
             <th>F</th>
           </tr>
         </thead>
         <tbody>
           %for k, v in sorted(scoreR.items()):
           <tr>
             <td>{{k}}</td>
             %for problem ,result in sorted(v.items()):
             <td>{{result}}</td>
             % end
           </tr>
           % end
         </tbody>
       </table>
     </div>
     <div class="tab-pane" id="tab3">
       <table class="table table-striped">
         <thead>
           <tr>
             <th>#</th>
             <th>A</th>
             <th>B</th>
             <th>C</th>
             <th>D</th>
           </tr>
         </thead>
         <tbody>
           %for k, v in sorted(scoreB.items()):
           <tr>
             <td>{{k}}</td>
             %for problem ,result in sorted(v.items()):
               <td>{{result}}</td>
              % end
           </tr>
          % end
         </tbody>
       </table>
     </div>
     <div class="tab-pane" id="tab4">
       <table class="table table-striped">
         <thead>
           <tr>
             <th>#</th>
             <th>A</th>
             <th>B</th>
             <th>C</th>
           </tr>
         </thead>
         <tbody>
           %for k, v in sorted(scoreT.items()):
           <tr>
             <td>{{k}}</td>
             %for problem ,result in sorted(v.items()):
             <td>{{result}}</td>
             % end
           </tr>
           % end
         </tbody>
       </table>
     </div>
    </div>

    </div>

  </div>
</body>
</html>
