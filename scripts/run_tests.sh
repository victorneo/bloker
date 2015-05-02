sudo docker build -t bloker_web .
sudo docker-compose run web py.test tests
OUT=$?
sudo docker rm bloker_web_run_1
return $OUT
