now=`date '+%Y%m%d_%H%M%S'`
echo "now = ${now}"
logfile="./logs/current_python_packages${now}.log"
echo "logfile = ${logfile}"
# ./tests/chromedriver-linux64/chromedriver > ${logfile} &
./tests/chromedriver-win64/chromedriver.exe > ${logfile} 
pip install -r ./tests/requirements.txt >> ${logfile}
pip list >> ${logfile}

