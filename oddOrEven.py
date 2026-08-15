<!DOCTYPE html>
<html>
    <head><title>Oddy or eveny</title>
    </head>
    <body>
        <script>
          let oddOrEven = function (number) {
            if  (number % 2 == 0) {
                document.write("given number is even") 
                
            }
             else {
                document.write("given number is odd")
            }
          }
          let number = prompt("enter a number")
          oddOrEven(number)
        </script>
    </body>
</html>
