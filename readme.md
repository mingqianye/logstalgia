Docs:
  Logstalgia home page: https://code.google.com/p/logstalgia/
  SIC log format: https://sites.google.com/a/33across.com/project-sic/tech/log-syntax

How to run:
  cat data/FlumeData.1413158475731 | python transform.py | logstalgia -b 010513 --hide-response-code --paddle-position 0.5 --font-size 20 -g "sporcle.com,URI=sporcle.com,25" -g "breibart.com,URI=breitbart.com,25" -g "littlethings.com,URI=littlethings.com,25" -
