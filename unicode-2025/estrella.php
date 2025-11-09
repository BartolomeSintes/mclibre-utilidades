
           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="75" viewBox="0 0 1180 512">
              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" stroke-width="20" stroke="red" />
              <text x="600" y="340" font-family="sans-serif" font-size="240" font-weight="bold" text-anchor="middle" fill="red">14</text>
           </svg>

           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="75" viewBox="0 0 1180 512">
              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" stroke-width="20" stroke="red" />
              <text x="600" y="340" font-family="sans-serif" font-size="220" font-weight="bold" text-anchor="middle" fill="red">New 15.1</text>
           </svg>
<?php
$puntosX = [22, 85, 53, 137, 141, 213, 260];
$puntosY = [254, 215, 135, 132, 48, 83, 20];
$n = 7;
print "           <svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" width=\"75\" viewBox=\"0 0 1180 512\" style=\"background-color: lightgray\">\n";
print "              <polygon points=\"";
for ($i = 0; $i < 7; $i++) {
   print "$puntosX[$i],$puntosY[$i] ";
}
// print "\n";

$ancho = $puntosX[6] - $puntosX[5];

for ($i = 0; $i < $n; $i++) {
   print $puntosX[6] + (2*$i + 1) * $ancho. "," . $puntosY[5] . " " . $puntosX[6] + (2*$i + 2) * $ancho. "," . $puntosY[6] . " ";
}
// print "\n";

$finalX = $puntosX[6] + 2*$i * $ancho;

for ($i = 0; $i < 5; $i++) {
   print $finalX + $puntosX[6] - $puntosX[5 - $i] . "," . $puntosY[5 - $i] . " ";
}
// print "\n";

for ($i = 0; $i < 7; $i++) {
   print $finalX + $puntosX[6] - $puntosX[$i] . "," . 2* $puntosY[0] - $puntosY[$i] . " ";
}
// print "\n";

for ($i = $n-1; $i > -1 ; $i--) {
   print $puntosX[6] + (2*$i + 1) * $ancho. "," . 2* $puntosY[0] - $puntosY[5] . " " . $puntosX[6] + (2*$i) * $ancho. "," . 2* $puntosY[0] - $puntosY[6] . " ";
}
// print "\n";

for ($i = 0; $i < 5; $i++) {
   print $puntosX[5 - $i] . "," . 2* $puntosY[0] - $puntosY[5 - $i] . " ";
}
print "\"\n";
print "                fill=\"none\" stroke-width=\"20\" stroke=\"red\" />\n";
print "              <text x=\"600\" y=\"340\" font-family=\"sans-serif\" font-size=\"240\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"red\">New 15.1</text>\n";
print "           </svg>\n";
